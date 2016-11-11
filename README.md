# Take a zone file and convert it to Terraform file

Pretty basic. It takes a zone txt file* downloaded from Dyn Managed DNS,
loads it into a data structure and formats it into Terraform valid JSON.

The output isn't very user friendly so hopefully can clean this up.

Needs shell input functionality.

*zone file needs to be manually edited like in example folder
