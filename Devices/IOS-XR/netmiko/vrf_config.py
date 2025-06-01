import sys
sys.path.append(r"d:\Practice\Practice\Devices")
from netmiko import ConnectHandler
from device_info import ios_xr_device


# Establish connection
net_connect = ConnectHandler(**ios_xr_device)

# Read VRF configuration from file
with open(r"d:\Practice\Practice\Devices\IOS-XR\netmiko\vrf_conf") as f:
    lines = f.read().splitlines()
print(lines)

# Send configuration to the device
vrf_config = net_connect.send_config_set(lines)
print("The following config was sent to the device:")
print(vrf_config)