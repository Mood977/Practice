from prettytable import PrettyTable

def print_report(report_name, devices):
    """
    It prints a report of devices in a table format.
    """
    table = PrettyTable()
    table.field_names = ["Name", "Family", "Platform", "Mgmt IP", "SW Version"]
    for device in devices:
        table.add_row(
            [device["hostname"], 
             device["family"],
             device["platform"],
             device["mgmt_ip"],
             device["version"]])

    print(f" *** MY REPORT: {report_name} ***")
    print(table)

        
if __name__ == "__main__":
    report_name = "Network Devices"

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
    
    print_report(report_name, devices)