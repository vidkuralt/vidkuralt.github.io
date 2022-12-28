import sys
import os
import getopt
from pybtex.database import parse_file
from time import strptime
import re
from pybtex.plugin import find_plugin
from pybtex.database import parse_string
APA = find_plugin('pybtex.style.formatting', 'unsrt')()
HTML = find_plugin('pybtex.backends', 'html')()

from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.formatting import toplevel

from pybtex.style.template import (
    field, first_of, href, join, optional, optional_field, sentence, tag,
    together, words, node, FieldIsMissing
)
from collections import Counter

date = words [optional_field('month'), field('year')]

@node
def apa_names(children, context, role, **kwargs):
    """
    Returns formatted names as an APA compliant reference list citation.
    """
    assert not children

    try:
        persons = context['entry'].persons[role]
    except KeyError:
        raise FieldIsMissing(role, context['entry'])

    style = context['style']

    if len(persons) > 7:
        persons = persons[:6] + persons[-1:]
        formatted_names = [style.format_name(
            person, style.abbreviate_names) for person in persons]
        return join(sep=', ', last_sep=', … ')[
            formatted_names].format_data(context)
    else:
        formatted_names = [style.format_name(
            person, style.abbreviate_names) for person in persons]
        return join(sep=', ', sep2=', & ', last_sep=', & ')[
            formatted_names].format_data(context)


class MyStyle(UnsrtStyle):
    def format_names(self, role, as_sentence=True):
        #formatted_names = names(role, sep=', ', sep2 = ' and ', last_sep=', and ')
        formatted_names = apa_names(role)
        if as_sentence:
            return sentence [formatted_names]
        else:
            return formatted_names

    def format_editor(self, e, as_sentence=True):
        editors = self.format_names('editor', as_sentence=False)
        if 'editor' not in e.persons:
            # when parsing the template, a FieldIsMissing exception
            # will be thrown anyway; no need to do anything now,
            # just return the template that will throw the exception
            return editors
        if len(e.persons['editor']) > 1:
            word = '(Eds)'
        else:
            word = '(Ed)'
        result = join(sep=' ') [editors, word]
        if as_sentence:
            return sentence [result]
        else:
            return result

    def get_techreport_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_title(e, 'title'),
            sentence [
                words[
                    first_of [
                        optional_field('type'),
                        'Technical Report',
                    ],
                    field('institution'),
                    optional_field('number'),
                ],
                optional_field('address'),
                date,
            ],
            sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

APA = MyStyle(abbreviate_names=True)

html_escape_table = {
    #"&": "&amp;",
    #'"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    #return text
    return "".join(html_escape_table.get(c,c) for c in text)


def main(argv):
    bibfile = 'jp.bib'
    outputdir = '../_publications/'
    opts, args = getopt.getopt(argv,"hb:o:",["bibfile=","outdir="])
    for opt, arg in opts:
        if opt == '-h':
            print ('bib2md.py -b <bibfile> -o <outputdir>')
            sys.exit()
        elif opt in ("-i", "--bibfile"):
            bibfile = arg
        elif opt in ("-o", "--outdir"):
            outputdir = arg
    print ('Bibtex file is ', bibfile)
    print ('Output dir is ', outputdir)

    # Parse the Bibtex file
    bibdata = parse_file(bibfile)

    # Prepare APA-style citations. For that, we remove doi/months/url/pdf first
    exclude_fields = ['url', 'doi', 'month', 'pdf']
    apabibdata = parse_string(bibdata.to_string('bibtex'), 'bibtex')
    for entry in apabibdata.entries.values():
        for ef in exclude_fields:
            if ef in entry.fields.__dict__['_dict']:
                del entry.fields.__dict__['_dict'][ef]
    formattedentries = APA.format_bibliography(apabibdata)
    i=0
    coaut = []
    # Loop through the individual entries
    for bib_id in bibdata.entries:

        # Reset default date
        pub_year = "1900"
        pub_month = "01"
        pub_day = "01"

        b = bibdata.entries[bib_id].fields

        try:
            pub_year = f'{b["year"]}'

            # todo: this hack for month and day needs some cleanup
            if "month" in b.keys():
                if (len(b["month"]) < 3):
                    pub_month = "0" + b["month"]
                    pub_month = pub_month[-2:]
                elif (b["month"] not in range(12)):
                    tmnth = strptime(b["month"][:3], '%b').tm_mon
                    pub_month = "{:02d}".format(tmnth)
                else:
                    pub_month = str(b["month"])
            if "day" in b.keys():
                pub_day = str(b["day"])
            pub_date = pub_year + "-" + pub_month + "-" + pub_day

            # Strip out {} as needed (some bibtex entries that maintain formatting)
            clean_title = b["title"].replace("{", "").replace("}", "").replace("\\", "").replace(" ", "-")

            url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
            url_slug = url_slug.replace("--","-")
            md_filename = (str(pub_date) + "-" + url_slug + ".md").replace("--","-")
            html_filename = (str(pub_date) + "-" + url_slug).replace("--","-")

            # Build citation
            citation = formattedentries.entries[i].text.render(HTML)
            i = i+1

            ## YAML variables
            md = "---\ntitle: \"" + html_escape(b["title"].replace("{", "").replace("}", "").replace("\\", "")) + '"\n'

            md += """collection: publications"""

            md += """\npermalink: /publications/""" + html_filename

            note = False

            md += "\ndate: " + str(pub_date)

            if "pdf" in b.keys():
                md += "\npdf: '../files/" + b["pdf"] + "'"

            if "doi" in b.keys():
                md += "\npaperurl: 'https://doi.org/" + b["doi"] + "'"
            elif "url" in b.keys():
                md += "\npaperurl: '" + b["url"] + "'"

            if "code" in b.keys():
                    md += "\ncode: '" + b["code"] + "'"

            md += "\ncitation: '" + html_escape(citation) + "'"

            md += "\n---"

            md_filename = os.path.basename(md_filename)

            with open(outputdir + md_filename, 'w') as f:
                f.write(md)
            print(f'SUCESSFULLY PARSED {bib_id}: \"', b["title"][:60], "..." * (len(b['title']) > 60), "\"")

            # Record co-authors
            for aut in bibdata.entries[bib_id].persons["author"]:
                coaut = coaut + [' '.join(aut.first_names + aut.middle_names + aut.last_names)]

        except KeyError as e:
                print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30],"..."*(len(b['title'])>30),"\"")
                continue

    countaut = Counter(coaut)
    with open("../_pages/coauthors.html", 'w') as f:
        f.write('---\nlayout: archive\ntitle: "Coauthors"\npermalink: /coauthors.html\nauthor_profile: true\n---\n')
        f.write("<p>Thank you to all my coauthors!</p>\n<ol>\n")
        for a in countaut.most_common():
            if a[0] not in ['Jean-Philippe Vert']:
                f.write("<li>"+a[0]+" ("+str(a[1])+")</li>\n")
        f.write("</ol>")



if __name__ == "__main__":
    main(sys.argv[1:])