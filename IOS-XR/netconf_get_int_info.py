from ncclient import manager
from device_info import ios_xr_device
import xmltodict

netconf_filter = open(r"d:\Practice\Practice\IOS-XR\filter-ietf-interfaces.xml").read()

with manager.connect(host=ios_xr_device["host"],
                    username=ios_xr_device["username"],
                    password=ios_xr_device["password"],
                    hostkey_verify=False) as m:
    
    # Get Configuration and State Info for Interface
    netconf_reply = m.get(netconf_filter)
    #print("NETCONF Reply:")
    #print("===================================")
    #print(netconf_reply)


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

