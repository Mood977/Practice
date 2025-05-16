import sys
sys.path.append(r"d:\Practice\Practice\Devices")
from ncclient import manager
from device_info import ios_xr_device
from connect_functions import connect_ios_xr


edit_tepmplate = open(r"d:\Practice\Practice\Devices\IOS-XR\NETCONF\config-temp-interfaces.xml").read()

netconf_payload = edit_tepmplate.format(int_name="Loopback999",
                                        int_desc="MSK Loopback Created using NETCONF",
                                        ip_address="20.20.20.30",
                                        prefix_length="32")


print("Conf Payload:")
print("====================================")
print(netconf_payload)

with connect_ios_xr(ios_xr_device) as m: 
    # Send NETCONF <edit-config>
    netconf_reply = m.edit_config(netconf_payload, target="candidate")
    m.commit()
    print(netconf_reply)
