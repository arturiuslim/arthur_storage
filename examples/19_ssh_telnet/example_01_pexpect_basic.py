#!/usr/bin/python3
from pprint import pprint
import pexpect

def send_show_command(ip, user, password, enable, command):
        with pexpect.spawn(f"ssh {user}@{ip}", timeout=10, encoding="utf-8") as ssh:
                    ssh.expect("Password")

                    ssh.sendline(password)
                    ssh.expect(">")
                    ssh.sendline("enable")
                    ssh.expect("Password")

                    ssh.sendline(enable)
                    ssh.expect("#")
                                                                            
                    ssh.sendline("terminal length 0")
                    ssh.expect("#")
                                                                                                    
                    ssh.sendline(command)
                    ssh.expect("#")
                    output = ssh.before
                    return output.replace("\r\n", "\n")

if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    for ip in ip_list:
        out = send_show_command(ip, "cisco", "cisco", "cisco", "show ip int br")
        pprint(out, width=120)
