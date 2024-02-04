from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import yaml
import netmiko
import paramiko
from itertools import repeat
import logging

logging.getLogger("netmiko").setLevel(logging.INFO)
logging.getLogger("paramiko").setLevel(logging.INFO)

logging.basicConfig(
    format = '%(asctime)s %(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO
)

def send_show(device, show):
    ip = device["ip"]
    logging.info(f"===>  Connection: {ip}")
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_command(show)
            logging.info(f"<===  Received:    {ip}")
            return output
    except netmiko.NetmikoTimeoutException as error:
        print(f"Was not able to connect to {device['host']}")
    except paramiko.ssh_exception.AuthenticationException:
        print(f"Authentication error on {device['host']}")

def collect_data(devices, command, mx_thr):
    ip_output_dict = {}
    with ThreadPoolExecutor(max_workers=mx_thr) as ex:
    #        result = ex.map(send_show, devices, ["show run | inc hostname"]*len(devices))
            result = ex.map(
                send_show, devices, repeat(command)
            )
            for dev, output in zip(devices,result):
                ip_output_dict[dev["ip"]] = output
            return ip_output_dict
if __name__ == "__main__":
    with open ("devices.yaml") as f:
        devices = yaml.safe_load(f)
        pprint(collect_data(devices, "show clock",2))

