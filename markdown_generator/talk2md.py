import pandas as pd
import re
import os

# Read talk lists from Google sheet
df = pd.read_csv("https://docs.google.com/spreadsheets/d/1AI6fJIOr6IK48aTnMJ8KC6JUr3LmaIkf9XaEPO-Jh2A/export?format=csv&gid=1887490935")

for row, item in df.iterrows():
    clean_title = item.Title.replace(" ", "-")
    clean_title = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
    md_filename = (item.Date + "-" + clean_title + ".md").replace("--", "-")
    print(md_filename)

    ## YAML variables
    md = "---\ntitle: \""   + item.Title + '"\n'
    md += 'venue: "' + item.Venue + '"\n'
    md += 'location: "' + item.Location + '"\n'
    md += 'date: "' + item.Date + '"\n'
    if len(str(item.Venue_link)) > 3:
        md += 'venue_link: "' + item.Venue_link + '"\n'
    if len(str(item.Slides)) > 3:
        md += 'slides: "' + item.Slides + '"\n'
    if len(str(item.Video)) > 3:
        md += 'video: "' + item.Video + '"\n'
    md += "---\n"

    md_filename = os.path.basename(md_filename)
    with open("../_talks/" + md_filename, 'w') as f:
        f.write(md)
