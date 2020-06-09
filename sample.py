line = 'Jun  8 20:54:38 127.0.0.1 gslab-Latitude-5480 systemd[1]: Stopping System Logging Service...'
list = line.split(" ")
ip_set = {'127.0.0.1'}
coll = []
dict = {}


def process(list, ip_set):
    if list[4] in ip_set:
        coll.append(list[6])
        dict[list[4]] = coll
    return dict
