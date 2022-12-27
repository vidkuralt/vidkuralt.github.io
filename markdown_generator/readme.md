Python utilities to create md files for individual publications, talks etc...

To update the site after you have added a publication, talk etc.., just type:
./runall

If you want to update only a specific page, you can run the scripts individually:
- Publications: update jp.bib and run
python bib2md

- Talks: update the list of talks on Google sheet and run
python talk2md

- Students: update the list of students on Google sheet and run
python students2md

- Teaching: update the list of students on Google sheet and run
python teaching2md

- Talk map: if you update a location in a talk or teaching, update the map with:
python talkmap.py
