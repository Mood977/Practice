import sys
sys.path.append(r"d:\Practice\Practice\Devices")
from ncclient import manager
from device_info import ios_xe_device
from connect_functions import connect_ios_xe


with connect_ios_xe(ios_xe_device) as m:
    print("NETCONF Capabilities")
    print("===================================")
    for capability in m.server_capabilities:
        print(capability)
    print("===================================")

# Saving the output to a file
# output_file = r"d:\Practice\Practice\Devices\IOS-XE\NETCONF\netconf_capabilities_output.txt"

# with connect_ios_xe(ios_xe_device) as m:
#     with open(output_file, "w") as f:
#         f.write("NETCONF Capabilities\n")
#         f.write("===================================\n")
#         for capability in m.server_capabilities:
#             f.write(capability + "\n")
#         f.write("===================================\n")

# print(f"NETCONF capabilities have been written to {output_file}")