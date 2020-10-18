#!/usr/bin/python3

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}


for intf, vlan in trunk.items():
    print("interface FastEthernet" + intf)
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            comm = trunk[intf]
            str1 = ' '.join(comm)
            print(" {} {}".format(command, str1))
        else:
            print(" {}".format(command))

