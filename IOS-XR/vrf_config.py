from netmiko import ConnectHandler

ios_xr_device = {
    "device_type": "cisco_xr",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": 22,
}

net_connect = ConnectHandler(**ios_xr_device)

with open(r"d:\Practice\Practice\IOS-XR\vrf_conf") as f:
    lines = f.read().splitlines()
print(lines)

vrf_config = net_connect.send_config_set(lines)
print("The following config was send to the device:")
print(vrf_config)

