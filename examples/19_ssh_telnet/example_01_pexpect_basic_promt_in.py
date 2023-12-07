#!/usr/bin/python3
from pprint import pprint
from getpass  import getpass
import pexpect

def send_show_command(ip, user, password, enable, command):
    print(f"Trying connect to {ip}")
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

            ssh.sendline(command)
            ssh.expect("#")
            
            output = ssh.before
            return output.replace("\r\n", "\n")
    except pexpect.exceptions.EOF as error:
        print(f"Connection timeout to {ip}")

if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.12", "192.168.100.3"]
    user = input("Username: ")
    password = getpass()
    e_password = getpass("Enable password: ")
    for ip in ip_list:
        out = send_show_command(ip, user, password, e_password, "show ip int br")
        pprint(out, width=120)
