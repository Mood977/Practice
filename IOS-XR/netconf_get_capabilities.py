from ncclient import manager
from device_info import ios_xr_device
from connect_functions import connect_ios_xr


with connect_ios_xr(ios_xr_device) as m:
    print("NETCONF Capabilities")
    print("===================================")
    for capability in m.server_capabilities:
        print(capability)
    print("===================================")

# Saving the output to a file
# output_file = r"d:\Practice\Practice\IOS-XR\netconf_capabilities_output.txt"

# with connect_ios_xr(ios_xr_device) as m:
#     with open(output_file, "w") as f:
#         f.write("NETCONF Capabilities\n")
#         f.write("===================================\n")
#         for capability in m.server_capabilities:
#             f.write(capability + "\n")
#         f.write("===================================\n")

# print(f"NETCONF capabilities have been written to {output_file}")