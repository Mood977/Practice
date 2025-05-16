import sys
sys.path.append(r"d:\Practice\Practice\Devices")
from ncclient import manager
from device_info import ios_xr_device
from connect_functions import connect_ios_xr
import xmltodict

netconf_filter = open(r"d:\Practice\Practice\Devices\IOS-XR\NETCONF\filter-ietf-interfaces.xml").read()


with connect_ios_xr(ios_xr_device) as m:  
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
    #print("  MAC Address: {}".format(intf_info["phys-address"]))
    #print("  Packets Input: {}".format(intf_info["statistics"]["in-unicast-pkts"]))
    #print("  Packets Output: {}".format(intf_info["statistics"]["out-unicast-pkts"]))
    print("====================================")

