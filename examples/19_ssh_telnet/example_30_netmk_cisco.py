from pprint import pprint
import netmiko
import paramiko
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException


def send_show_command(ip, user, password, enable, command):
	print('Connection to', ip)
	try:
		with netmiko.ConnectHandler(
			device_type="cisco_ios", 
                        timeout=5, host=ip, 
                        username=user, password=password,
                        secret=enable) as ssh:
                        ssh.enable()
                        output = ssh.send_command(command)
                        return output
	except netmiko.ssh_exception.NetmikoTimeoutException:
		print('Was not able to connect to', ip, '\n')
	except netmiko.ssh_exception.NetMikoAuthenticationException as error:
		print(error)
	except ValueError as error:
		print(error)
	
if __name__ == "__main__":
	user = input("Username: ")
	passwd = getpass("Password: ")
	enable_p = getpass("Password: ")
	ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
	for ip in ip_list:
		out = send_show_command(ip, user, passwd, enable_p, "show ip int br")
		pprint(out, width=120)
