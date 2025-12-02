from termcolor import colored
from hashlib import sha256
import requests
import socket
import json

def ip():
  ipify = requests.get("https://api.ipify.org/?format=json")
  use = ipify.json()["ip"]
  return use

socketz = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
amount = int(sha256("No".encode("utf-8")).hexdigest(), 16)
no = "No"*amount
port = 443
ip = ip()
socketz.sendto(no.encode("utf-8"), (ip, port))
print(colored("No", "white", attrs=["bold"]))
