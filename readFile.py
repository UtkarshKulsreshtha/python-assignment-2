from test import fetch_ip

answer = {}
asset_path = '/home/gslab/asset/test.txt'

event = []
list = []
ip_set, asset = fetch_ip(asset_path)
with open('/var/log/remotehosts/remotelogs', 'r') as f:
    for line in f:
        list = line.split(" ")
        if list[4] in ip_set:
            print("Event= ", list[6], "User =", asset[list[4]], "source IP =", list[4])



