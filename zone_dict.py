import os
import re
import json
import io
import pprint
from collections import OrderedDict

with open('zone_files/inmz.net.zonefile.txt') as f:
    zone_file = f.readlines()

inmz_zone_final = open('inmz.tf', 'w')

# empty objects for output
data = []
json_object = []

# this is a constant throughout terraform file
zone_id = "${aws_route53_zone.inmz.zone_id}"

for line in zone_file:
    stripped = re.sub(' +', ' ', line)
    words = stripped.split(' ')
    data.append(words)

for each_list in data:
    terrarecord = {
        "resource": {
            "aws_route53_record": {
                each_list[0]:
                    {
                        "zone_id": zone_id,
                        "name": each_list[0],
                        "type": each_list[2],
                        "ttl": each_list[1],
                        "records": [each_list[3].replace('\n', '')]
                    }
            }
        }
    }
    json_object.append(terrarecord)

for item in json_object:
    inmz_zone_final.write('%s' % json.dumps(json_object))

