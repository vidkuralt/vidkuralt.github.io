

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks. 
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy

import glob
import getorg
from geopy import Nominatim

# Scrapes .md files in talks and teaching folders
g = glob.glob("../_talks/*.md") + glob.glob("../_teaching/*.md")

geocoder = Nominatim(user_agent="mypage")
location_dict = {}
location = ""
permalink = ""
title = ""

def safe_geocode(location, retries=3, delay=2):
	for attempt in range(retries):
		try:
			return geocoder.geocode(location, timeout=10)
		except (GeocoderTimedOut, GeocoderUnavailable) as e:
			print(f"Attempt {attempt+1} failed for '{location}': {e}")
			time.sleep(delay)
	print(f"Failed to geocode '{location}' after {retries} retries.")
	return None

for file in g:
    with open(file, 'r') as f:
        lines = f.read()
        if lines.find('location: "') > 1:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]
                            
        if location not in location_dict:
        	location_dict[location] = safe_geocode(location)
        	print(location, "\n", location_dict[location])

# print the output to ../talkmap
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="../talkmap", hashed_usernames=False)
