from ncclient import manager
from device_info import ios_xr_device

with manager.connect(host=ios_xr_device["host"],
                    username=ios_xr_device["username"],
                    password=ios_xr_device["password"],
                    hostkey_verify=False) as m:
        
        print("NETCONF Capabilities")
        print("===================================")
        for capability in m.server_capabilities:
                print(capability)
        print("===================================")