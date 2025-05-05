device_details = {"hostname": "sw1", "sw_version": 20.4, "alerts": False, "interfaces": ["Gi1", "Gi2", "Gi3"]}

if device_details["alerts"]:
    print("There are alerts on the device.")
else:
    print("No alerts on the device.")

# It will print the first interface if it is present, otherwise it will print the second interface.
if "Gi1" in device_details["interfaces"]:
    print("Interface Gi1 is present.")
elif "Gi2" in device_details["interfaces"]:
    print("Interface Gi2 is present.")

for interface in device_details["interfaces"]:
    print(interface)

while True:
    tests_availavle = input("Are there tests available? (yes/no): ").strip().lower()
    if tests_availavle == "yes":
        print("Tests are available.")
        break
    elif tests_availavle == "no":
        print("No tests available.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")