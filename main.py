import os
import json
import re

# Define file paths
zone_file_path = '../zone_files/inmz.net.stripped.zonefile.txt'
terraform_file_path = '../roles/route53/inmz.tf'

# Read the zone file
with open(zone_file_path) as f:
    zone_file = f.readlines()

# Prepare the Terraform output structure
zone_id = "${aws_route53_zone.inmz.zone_id}"
url_suffix = '.inmz.net.'
terra_records = {}

# Process the zone file
for line in zone_file:
    stripped_line = re.sub(' +', ' ', line.strip())
    words = stripped_line.split(' ')
    
    if len(words) >= 4:  # Ensure there are enough parts in the line
        record_name = words[0].replace('.', '')
        record_type = words[2]
        record_ttl = words[1]
        record_value = words[3].strip()  # Remove any trailing newline or spaces

        # Create a record entry
        if record_name not in terra_records:
            terra_records[record_name] = {
                "zone_id": zone_id,
                "name": record_name + url_suffix,
                "type": record_type,
                "ttl": record_ttl,
                "records": []
            }
        
        terra_records[record_name]["records"].append(record_value)

# Prepare the final JSON object
json_object = {
    'resource': {
        'aws_route53_record': terra_records
    }
}

# Write the Terraform configuration to a file
with open(terraform_file_path, 'w') as inmz_zone_final:
    json.dump(json_object, inmz_zone_final, indent=4)

print(f"Terraform configuration written to {terraform_file_path}")
