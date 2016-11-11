import os
import re
import json
import io
import pprint

with open('zone_files/inmz.net.zonefile.txt') as f:
    zone_file = f.readlines()

empty_file = open('inmz.tf', 'w')

data = []
json_object = []
zone_id = "${aws_route53_zone.inmz.zone_id}"

for line in zone_file:
    stripped = re.sub(' +', ' ', line)
    words = stripped.split(' ')
    data.append(words)
    #
    # if len(words) > 1:
    #     key = words[FIRST_ELEMENT]
    #     del words[FIRST_ELEMENT]
    #     dict[key] = words
    # elif len(words) == 1:
    #     dict[words[FIRST_ELEMENT]] = 'null'
#
# list = dict['drone']
#
# name = list[0]
# type = list[1]
# ttl = list[2]

# print(name, type, ttl)

for each_list in data:
    terrarecord = {
        "resource": {
            "aws_route_53_record": {
                each_list[0]:
                    {
                        "zone_id": zone_id,
                        "name": each_list[0],
                        "type": each_list[1],
                        "ttl": each_list[2],
                        "records": [each_list[3].replace('\n', '')]
                    }
            }
        }
    }
    json_object.append(terrarecord)

for item in json_object:
    empty_file.write('%s' % json_object)
