from ncclient import manager


def connect_ios_xr(ios_xr_device):
    """Connect to IOS-XR device using NETCONF."""
    return manager.connect(
        host=ios_xr_device["host"],
        username=ios_xr_device["username"],
        password=ios_xr_device["password"],
        hostkey_verify=False
    )