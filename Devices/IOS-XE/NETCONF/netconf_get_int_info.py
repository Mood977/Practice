import sys
sys.path.append(r"d:\Practice\Practice\Devices")
from ncclient import manager
from device_info import ios_xe_device
from connect_functions import connect_ios_xe
import xmltodict

netconf_filter = open(r"d:\Practice\Practice\Devices\IOS-XE\NETCONF\get-ietf-interfaces.xml").read()


with connect_ios_xe(ios_xe_device) as m:  
    # Get Configuration and State Info for Interface
    netconf_reply = m.get(netconf_filter)
    print("NETCONF Reply:")
    print("===================================")
    print(netconf_reply)

    # Process the XML and store in useful dictionaries
    intf_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
    intf_config = intf_details["interfaces"]["interface"]

    print("====================================")
    print("Interface Details:")
    print("  Name: {}".format(intf_config["name"]))
    print("  Description: {}".format(intf_config["config"]["description"]))
    print("  Type: {}".format(intf_config["config"]["type"]["#text"]))
    print("  MAC Address: {}".format(intf_config["ethernet"]["config"]["mac-address"]))
    print("  Packets Input: {}".format(intf_config["state"]["counters"]["in-unicast-pkts"]))
    print("  Packets Output: {}".format(intf_config["state"]["counters"]["out-unicast-pkts"]))
    print("====================================")

