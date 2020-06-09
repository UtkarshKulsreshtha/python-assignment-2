import re


def fetch_ip(filepath):
    with open(filepath, 'r') as f:
        answer = {}
        ip_set = set()
        for line in f:
            k, v = line.strip().split('=')
            answer[k.strip()] = v.strip()
            m = re.search('([0-9]{1,3}\.){3}[0-9]{1,3}', line)
            ip_set.add(m.group())
    return ip_set, answer


filepath = '/home/gslab/asset/test.txt'
fetch_ip(filepath)
