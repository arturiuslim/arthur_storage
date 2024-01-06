from pprint import pprint
import re 
import pexpect

def send_show_command(ip, user, password, enable, command):
    print(f"Connecting to {ip}")
    try:
        with pexpect.spawn(f"ssh {user}@{ip}", timeout=10, encoding="utf-8") as ssh:
            ssh.expect("[Pp]assword:")
            ssh.sendline(password)
            ssh.expect(">")
            ssh.sendline("enable")
            ssh.expect("Password:")
            ssh.sendline(enable)
            ssh.expect("\S+#")
            prompt = ssh.after

            ssh.sendline(command)
            output = ""
            while True:
                index = ssh.expect([prompt, "--More--", pexpect.TIMEOUT], timeout=1)
#                time.sleep(1)
                page = ssh.before
                page = re.sub(r" *\x08+ +\x08+", "\n", page)
                output += page
                if index == 0:
                    break
                elif index == 1:
                    ssh.send(" ")
                else:
                    print("Timeout")
                    break
            return output.replace("\r\n", "\n")
    except pexpect.exceptions.TIMEOUT as error:
        print(f"Was not able to connect to {ip}")

if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    out = send_show_command("192.168.100.1", "cisco", "cisco", "cisco", "sh run")
    pprint(out, width=120)
#    with open("r1_cfg_script.txt", "w") as f:
#        f.write(out)
