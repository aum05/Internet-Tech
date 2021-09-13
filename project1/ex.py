import random

host = []
ip = []
fl = []
with open('PROJI-DNSRS.txt', 'r') as file:
    for l in file:
        line = l.split(" ")
        #print(line)
        host.append(line[0])
        ip.append(line[1])
        fl.append(line[2].rstrip("\r\n"))

dns = {"hostName" : host, "IP": ip, "flag": fl}

with open('PROJI-HNS.txt', 'r') as f:
    read_file = f.readlines()

#n = random.randint(0,len(read_file)-1)
for line in read_file:
    string = line.rstrip("\r\n")
    print(string)

host_name = [name.lower() for name in dns["hostName"]]
#print(host_name)

if string.lower() in host_name:
    ind = host_name.index(string.lower())
    print(dns["hostName"][ind] + " " + dns["IP"][ind] + " " + dns["flag"][ind])
else:
    print("TSHostname - NS")

name = "localhost - NS".split(" - ")
print(name[0])