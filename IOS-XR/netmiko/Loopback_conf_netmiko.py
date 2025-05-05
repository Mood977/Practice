import sys
sys.path.append(r"d:\Practice\Practice\IOS-XR")
from netmiko import ConnectHandler
from device_info import ios_xr_device


net_connect = ConnectHandler(**ios_xr_device)

loopback = {"int_name": "Loopback977",
            "description": "MSK Loopback sent using Netmiko",
            "ip": "20.20.20.2",
            "mask": "255.255.255.255" 
}

lp_config  = [
    "interface {}".format(loopback["int_name"]),
    "description {}".format(loopback["description"]),
    "ipv4 address {} {}".format(loopback["ip"], loopback["mask"]),
    "no shut",
    "root",
    "commit",
    "exit"
]

print(lp_config)

output = net_connect.send_config_set(lp_config)
print("The following config was send to the device:")
print(output)