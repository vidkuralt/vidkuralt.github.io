import pandas as pd
import re
import os

# Read talk lists from Google sheet
df = pd.read_csv("https://docs.google.com/spreadsheets/d/1AI6fJIOr6IK48aTnMJ8KC6JUr3LmaIkf9XaEPO-Jh2A/export?format=csv&gid=2051672274")



for row, item in df.iterrows():
    clean_name = item.fullname.replace(" ", "-")
    clean_name = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_name)
    md_filename = (str(item.end) + "-" + clean_name + ".md").replace("--", "-")
    print(md_filename)

    ## YAML variables
    md = "---\ntitle: \""   + item.fullname + '"\n'
    md += 'begin: "' + str(item.begin) + '"\n'
    md += 'end: "' + str(item.end) + '"\n'
    md += 'level: "' + item.level + '"\n'
    if len(str(item.url)) > 3:
        md += 'persolink: "' + item.url + '"\n'
    if len(str(item.note)) > 3:
        md += 'note: "' + item.note + '"\n'
    md += "---\n"

    md_filename = os.path.basename(md_filename)
    with open("../_students/" + md_filename, 'w') as f:
        f.write(md)
