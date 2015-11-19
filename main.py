import re

f = open('data.txt')

# Retrieve latest import date
for line in f:
    tmp = re.search('latest', line)
    if tmp:
        latest_date = re.search('[0-9]{8}', line)
        print "tmp: %s" % (latest_date.group(0))
        break
    #print vars(tmp)


