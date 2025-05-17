import sys
sys.path.append(r"d:\Practice\Practice\Devices")
from ncclient import manager
from device_info import ios_xe_device
from connect_functions import connect_ios_xe


edit_template = open(r"d:\Practice\Practice\Devices\IOS-XE\NETCONF\config-temp-interfaces.xml").read()

netconf_payload = edit_template.format(int_name="Loopback1001",
                                        int_desc="MSK Loopback Created using NETCONF",
                                        ip_address="20.20.20.30",
                                        prefix_length="32")


print("Conf Payload:")
print("====================================")
print(netconf_payload)

with connect_ios_xe(ios_xe_device) as m: 
    # Send NETCONF <edit-config>
    netconf_reply = m.edit_config(netconf_payload, target="running")
    print(netconf_reply)
