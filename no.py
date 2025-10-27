from termcolor import colored
import requests
import socket
import json

def ip():
  ipify = requests.get("https://api.ipify.org/?format=json")
  use = ipify.json()["ip"]
  return use

socketz = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
no = "No"*32
port = 443
ip = ip()
socketz.sendto(no.encode("utf-8"), (ip, port))
print(colored("No", "white", attrs=["bold"]))
