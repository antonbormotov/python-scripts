import re

f = open('data.txt')

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

for line in f:
    # Retrieve latest date for cc
    tmp = re.search('latest', line)
    if tmp:
        current_index = re.search('product_([a-z]{2})_([0-9]{8})', line)
        cc_latest[current_index.group(1)] = [current_index.group(2), '']
        #print "latest tmp: %s" % (cc_latest[current_index.group(1)])

    # Retrieve alias date for cc
    tmp = re.search('^product_[a-z]{2}\s', line)
    if tmp:
        current_index = re.search('^product_([a-z]{2})\s+product_[a-z]{2}_([0-9]{8})', line)
        cc_alias[current_index.group(1)] = [current_index.group(2), '']
        #print "alias tmp: %s" % (cc_alias[current_index.group(1)])

exit()

with open('data.txt', 'r') as f:
    for line in f:
        for key in cc_latest:
            tmp_regex = 'product_' + key + '_' + cc_latest[key] + '\s+[0-9]+\s[0-9]+(\s[0-9]+)'
            tmp = re.search(tmp_regex, line)
            #print "tmp_regex: %s" % (tmp_regex)
            if tmp:
                print "tmp: %s - %s" % (tmp.group(0), tmp.group(1))

