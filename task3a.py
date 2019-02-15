for line in fhand:
    line = line.rstrip()
    if not line.startswith('Internet'):
    continue
b = line.split(); c = (b[-3] + b[-1]); b = b[1]
    ips.append(b)
# Sort IP
for i in range(len(ips)):
    ips[i] = "%3s.%3s.%3s.%3s" % tuple(ips[i].split("."))
ips.sort()
for i in range(len(ips)):
    ips[i] = ips[i].replace(" ", "")
for ip in ips:
print ip (would also like 'c')
