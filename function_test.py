import time
import requests

def add(num1, num2):
    return num1 + num2

print(add(4, 8))

for number in range(1,3):
    print(number)
    time.sleep(1)

ip = requests.get("https://api.ipify.org").text
print(f"My public IP address is: {ip}")