import requests
import socket
import urllib.request as urllib2
import json
import os
import sys

print("██╗   ██╗██████╗ ██╗         ██╗███╗   ██╗███████╗ ██████╗      ██████╗ ██████╗  █████╗ ██████╗ ███████╗██████╗ ")
print("██║   ██║██╔══██╗██║         ██║████╗  ██║██╔════╝██╔═══██╗    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
print("██║   ██║██████╔╝██║         ██║██╔██╗ ██║█████╗  ██║   ██║    ██║  ███╗██████╔╝███████║██████╔╝█████╗  ██████╔╝")
print("██║   ██║██╔══██╗██║         ██║██║╚██╗██║██╔══╝  ██║   ██║    ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══╝  ██╔══██╗")
print("╚██████╔╝██║  ██║███████╗    ██║██║ ╚████║██║     ╚██████╔╝    ╚██████╔╝██║  ██║██║  ██║██████╔╝███████╗██║  ██║")
print("╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")

url = input("What is the URL: ")
os.system("clear")
req = requests.get("https://"+url)
print(req.headers)
print("")

ip1 = socket.gethostbyname(url)
print("Ip Address of", url, "is: ", ip1)
print("")

while True:
  ip = ip1
  url = "http://ip-api.com/json/"
  response = urllib2.urlopen(url + ip)
  data = response.read()
  values = json.loads(data)

  print("Status: " + str(values['status']))
  print("Country: " + str(values['country']))
  print("Country Code: " + str(values['countryCode']))
  print("Region: " + str(values['region']))
  print("Region Name: " + str(values['regionName']))
  print("City: " + str(values['city']))
  print("Zip Code: " + str(values['zip']))
  print("Latitude: " + str(values['lat']))
  print("Longitude: " + str(values['lon']))
  print("Timezone: " + str(values['timezone']))
  print("Isp: " + str(values['isp']))
  print("Organization: " + str(values['org']))
  print("As: " + str(values['as']))
  break