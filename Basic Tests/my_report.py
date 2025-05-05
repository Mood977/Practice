report_name = "Catalyst Center Managed Devices"
column_titels = ["Name", "Family", "Platform", "Mgt IP", "SW Version"]

print(f" *** MY REPORT: {report_name} ***")
print(column_titels)

devices = [
        {
            "hostname": "R1",
            "family": "Router",
            "platform": "C8200",
            "mgmt_ip": "10.10.10.1",
            "version": "17.9"
        },
        {
            "hostname": "R2",
            "family": "Router",
            "platform": "CSR",
            "mgmt_ip": "10.10.10.2",
            "version": "19.3"
        },
        {
            "hostname": "SW1",
            "family": "Switch",
            "platform": "C9KV",
            "mgmt_ip": "10.10.20.1",
            "version": "17.9"
        },
        {
            "hostname": "SW2",
            "family": "Switch",
            "platform": "C9KV",
            "mgmt_ip": "10.10.20.2",
            "version": "17.9"
        },
    ]

# Print certian devices.
print(f"  {devices[0]["hostname"]} ,   {devices[0]["family"]} ,   {devices[0]["platform"]} ,   {devices[0]["mgmt_ip"]} ,   {devices[0]["version"]}")
print(f"  {devices[1]["hostname"]} ,   {devices[1]["family"]} ,   {devices[1]["platform"]} ,   {devices[1]["mgmt_ip"]} ,   {devices[1]["version"]}")
print(f"  {devices[2]["hostname"]} ,   {devices[2]["family"]} ,   {devices[2]["platform"]} ,   {devices[2]["mgmt_ip"]} ,   {devices[2]["version"]}")

print("----------------------")

# Print all devices in the list dynamically.
for device in devices:
    print(f" {device["hostname"]} ,  {device["family"]} ,  {device["platform"]} ,  {device["mgmt_ip"]} ,  {device["version"]}")
