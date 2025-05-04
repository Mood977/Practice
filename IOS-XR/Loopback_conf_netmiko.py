from netmiko import ConnectHandler

ios_xr_device = {
    "device_type": "cisco_xr",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": 22,
}

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