
from test import fetch_ip

answer = {}
asset_path = '/home/gslab/asset/test.txt'

event = []
ip_set = set()
list = []
with open('/var/log/remotehosts/remotelogs', 'r') as f:
    data = f.readlines()
    for line in data:
        list = line.split(" ")
        ip_set.add(list[4])
ip_list, asset = fetch_ip(asset_path)

while bool(ip_set):
    i = ip_set.pop()
    if i in ip_list:
        print("ip = ", i, "user=", asset[i])

with open('/var/log/remotehosts/remotelogs', 'r') as f:
    data = f.readlines()
    for line in data:
        list = line.split(" ")
        print("Event= ", list[6], "User =", asset[list[4]], "source IP =", list[4])
