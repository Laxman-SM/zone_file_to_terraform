import os
import json
import re


with open('../zone_files/inmz.net.stripped.zonefile.txt') as f:
    zone_file = f.readlines()

# .tf file should be moved to dedicated tf dir
inmz_zone_final = open('../roles/route53/inmz.tf', 'w')

# empty objects for output
data = []
json_object = {'resource': {'aws_route53_record': None}}
terrarecord = {}

# this is a constant throughout terraform file
zone_id = "${aws_route53_zone.inmz.zone_id}"
url = '.inmz.net.'

# remove whitespace and create data list
for line in zone_file:
    stripped = re.sub(' +', ' ', line)
    words = stripped.split(' ')
    data.append(words)

# create our terraform file here
for each_list in data:
    terrarecord[each_list[0].replace('.', '')] = {
        "zone_id": zone_id,
        "name": each_list[0] + url, # not sure if I need to do this
        "type": each_list[2],
        "ttl": each_list[1],
        "records": [each_list[3].replace('\n', '')]
    }

json_object['resource']['aws_route53_record'] = terrarecord

# write to file
for item in json_object:
    inmz_zone_final.write('%s' % json.dumps(json_object))

inmz_zone_final.close()
f.close()
