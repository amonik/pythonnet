import os

with open('ips') as f:
    read_data = f.readline()

for ip in read_data:
    print(ip)
    os.system("nmap -sS -v -v -Pn -g 88 {} | grep open".format(ip))
