from ncclient import manager
from device_info import ios_xr_device
from connect_functions import connect_ios_xr


with connect_ios_xr(ios_xr_device) as m:
    print("NETCONF Capabilities")
    print("===================================")
    for capability in m.server_capabilities:
        print(capability)
    print("===================================")
