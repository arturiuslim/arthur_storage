from pprint import pprint
import netmiko
import paramiko
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
import yaml


def send_show_command(device_params, command):
        ip = device_params["ip"]
        print('Connection to', ip)
        try:
            with netmiko.ConnectHandler(**device_params) as ssh:
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
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        pprint(send_show_command(dev, "show ip int br"), width=120)
