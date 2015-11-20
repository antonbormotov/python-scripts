#!/usr/bin/env python
import re
import subprocess

try:
    #output = subprocess.check_output(["./artisan es:list", ""], shell=True, stderr=subprocess.STDOUT)
    with open("data.txt", "r") as f:
        output_list = f.readlines()
    #output_list = []
    #i = 0
    #for line in output.splitlines():
    #    output_list.append(line.strip())
    #    print "%d %s" % (i, output_list[i])
    #    i += 1
except Exception as e:
    print "### Error: %s" % (str(e))

cc_latest = {
    'hk': [],
    'id': [],
    'my': [],
    'ph': [],
    'sg': [],
    'th': [],
    'vn': []
    }

cc_alias = {
    'hk': [],
    'id': [],
    'my': [],
    'ph': [],
    'sg': [],
    'th': [],
    'vn': []
    }

for line in output_list:
    # Retrieve latest date for cc
    tmp = re.search('latest', line)
    if tmp:
        current_index = re.search('product_([a-z]{2})_([0-9]{8})', line)
        cc_latest[current_index.group(1)].append(current_index.group(2))
        #print "latest tmp: %s" % (cc_latest[current_index.group(1)])

    # Retrieve alias date for cc
    tmp = re.search('^product_[a-z]{2}\s', line)
    if tmp:
        current_index = re.search('^product_([a-z]{2})\s+product_[a-z]{2}_([0-9]{8})', line)
        cc_alias[current_index.group(1)].append(current_index.group(2))
        #print "alias tmp: %s" % (cc_alias[current_index.group(1)])

for line in output_list:
    for key in cc_latest:
        tmp_regex = 'product_' + key + '_' + cc_latest[key][0] + '\s+[0-9]+\s[0-9]+\s+([0-9]+)'
        tmp = re.search(tmp_regex, line)
        if tmp:
            cc_latest[key].append(tmp.group(1))

    for key in cc_alias:
        tmp_regex = 'product_' + key + '_' + cc_alias[key][0] + '\s+[0-9]+\s[0-9]+\s+([0-9]+)'
        tmp = re.search(tmp_regex, line)
        #print "tmp_regex: %s" % (tmp_regex)
        if tmp:
            cc_alias[key].append(tmp.group(1))

sum_alias = 0
sum_latest = 0
for key in cc_alias:
    print "%s : Alias: %s Import: %s" % (key, cc_alias[key][1], cc_latest[key][1])
    sum_alias += int(cc_alias[key][1])
    sum_latest += int(cc_latest[key][1])

print ""
print "Total alias:  %10d " % (sum_alias)
print "Total latest: %10d " % (sum_latest)
print "Total diff: %10d " % (abs(sum_latest-sum_alias))
