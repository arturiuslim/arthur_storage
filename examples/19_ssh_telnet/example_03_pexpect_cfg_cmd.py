#!/usr/bin/python3
from pprint import pprint
import pexpect

def send_cfg_commands(ip, user, password, enable, commands):
    print(f"Trying to comnnect to {ip}")
    cmd_output = ""
    try:
        with pexpect.spawn(f"ssh {user}@{ip}", timeout=10, encoding="utf-8") as ssh:
            ssh.expect("[Pp]assword:")
            ssh.sendline(password)
            ssh.expect(">")
            ssh.sendline("enable")
            ssh.expect("[Pp]assword:")
            ssh.sendline(enable)
            ssh.expect("\S+#")
            prompt = "\(config\S*\)#" #R1(config)#

            if type(commands) == str:
                commands = ["conf t", commands, "end"]
            else:
                commands = ["conf t", *commands, "end"]


            
            for cmd in commands:
                ssh.sendline(cmd)
                ssh.expect([prompt, "#"])
                output = ssh.before + ssh.after
                output = output.replace("\r\n", "\n")
                if "%" in output:
                    raise ValueError(
                        f"Error during {cmd}"
                        f"{output}"
                    )
                cmd_output += output
        return cmd_output
    except pexpexćt.exeptions.TIMEOUT as error:
        print("Was not able to connect to {ip}")


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    commands = ["interface lo77", "ip address 10.1.1.1 255.255.255.255"]

    result = {}
    for ip in ip_list:
        try:
            out = send_cfg_commands(ip, "cisco", "cisco", "cisco", commands)
            print(out)
        except ValueError as error:
            print(error)
        
