from netmiko import ConnectHandler
from device_info import ios_xr_device

net_connect = ConnectHandler(**ios_xr_device)

with open(r"d:\Practice\Practice\IOS-XR\vrf_conf") as f:
    lines = f.read().splitlines()
print(lines)

vrf_config = net_connect.send_config_set(lines)
print("The following config was send to the device:")
print(vrf_config)