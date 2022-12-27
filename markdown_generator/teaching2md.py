import pandas as pd
import re
import os

# Read talk lists from Google sheet
df = pd.read_csv("https://docs.google.com/spreadsheets/d/1AI6fJIOr6IK48aTnMJ8KC6JUr3LmaIkf9XaEPO-Jh2A/export?format=csv&gid=930478469")



for row, item in df.iterrows():
    clean_name = item.institution.replace(" ", "-")
    clean_name = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_name)
    md_filename = (str(item.year) + "-" + clean_name + ".md").replace("--", "-")
    print(md_filename)

    ## YAML variables
    md = "---\ntitle: \""   + item.title + '"\n'
    md += 'year: "' + str(item.year) + '"\n'
    md += 'program: "' + item.program + '"\n'
    md += 'institution: "' + item.institution + '"\n'
    md += 'location: "' + item.location + '"\n'
    if len(str(item.url)) > 3:
        md += 'courselink: "' + item.url + '"\n'
    md += "---\n"

    md_filename = os.path.basename(md_filename)
    with open("../_teaching/" + md_filename, 'w') as f:
        f.write(md)
