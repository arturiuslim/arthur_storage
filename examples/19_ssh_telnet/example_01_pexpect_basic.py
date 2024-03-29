#!/usr/bin/python3
from pprint import pprint
import pexpect

def send_show_command(ip, user, password, enable, command):
    print(f"Trying connect to {ip}")
    cmd_output_dict = {}
    try:
        with pexpect.spawn(f"ssh {user}@{ip}", timeout=10, encoding="utf-8") as ssh:
            ssh.expect("Password")
       
            ssh.sendline(password)
            ssh.expect(">")
            ssh.sendline("enable")
            ssh.expect("Password")
            ssh.sendline(enable)
            ssh.expect("#")
                                                                            
            ssh.sendline("terminal length 0")
            ssh.expect("\S+#")
            prompt = ssh.after #R1#

            if type(command) == str:
                command  = [command]
            
            for cmd in command:
                ssh.sendline(cmd)
                ssh.expect("#")
                output = ssh.before + ssh.after
                output = output.replace("\r\n", "\n")
                cmd_output_dict[cmd] = output
        return cmd_output_dict
    except pexpect.exceptions.EOF as error:
        print(f"Connection timeout to {ip}")

if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    commands = ["show clock", "show run | in host"]
    result = {}
    for ip in ip_list:
        out = send_show_command(ip, "cisco", "cisco", "cisco", commands)
        result[ip] = out
    pprint(result, width=120)
