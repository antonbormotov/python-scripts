import re

f = open('data.txt')

cc = {
    'hk': '',
    'id': '',
    'my': '',
    'ph': '',
    'sg': '',
    'th': '',
    'vn': ''
    }

# Retrieve latest import date
for line in f:
    tmp = re.search('latest', line)
    if tmp:
        current_index = re.search('product_([a-z]{2})_([0-9]{8})', line)
        cc[current_index.group(1)] = current_index.group(2)
        print "tmp: %s" % (cc[current_index.group(1)])
