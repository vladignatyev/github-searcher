#!env/bin/python

import lib
import sys
import unicodecsv as csv
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE instead of presenting it on screen", metavar="FILE")
(options, args) = parser.parse_args()

f = None
if options.filename:
    f = open(options.filename, 'wb')
    print "Writing report to file: %s" % options.filename
    print "---"

username = raw_input('Username on GitHub [Enter to skip]:')
password = raw_input('Password on GitHub [Enter to skip]:')

keywords = raw_input('Enter keywords, divided with comma:').split(',')
language = raw_input('Enter language [Objective-C]:')
if not language:
    language = lib.OBJECTIVE_C

def format_repo_to_screen(repo):
    json = repo.to_json()
    return "Username: %s\n  %s [Fork:%s]\n  %s  %s\n  %s  %s  %s" % (json['owner'], 
        json['name'], json['fork'], json['description'], json['url'], 
        json['homepage'], json['followers'], json['forks'])

def generate_file_report(model, file):
    f.write('<html><table border="1">')
    fields = ["#", "owner", "owner_avatar", "owner_email", "owner_blog", "owner_location", 
    "name", "url", "homepage", "description", "followers", "forks"]

    f.write('<tr>')
    for field in fields:
        field_layout = field
        f.write(u'<td>%s</td>' % field_layout)
    f.write(u'</tr>')

    i = 0 
    for repo in model:
        i += 1
        f.write(u'<tr>')
        for field in fields:
            if field not in ['forks', 'followers', '#']:
                field_value = repo.get(field, '')
                if field_value is None:
                    value = ''
                else:
                    value = field_value.encode('utf-8')
            else:
                value = str(repo.get(field, ''))
            if field == '#':
                value = str(i)
                field_layout = i

            if field == 'owner_email':
                field_layout = u'<a href="mailto:%s">%s</a>' % (value, value)
            elif field == 'owner_blog' or field == 'url' or field == 'homepage':
                field_layout = u'<a href="%s">%s</a>' % (value, value)
            elif field == 'owner_avatar':
                field_layout = u'<img src="%s" width="128" />' % value
            else:
                field_layout = value

            f.write('<td>')
            f.write(field_layout)
            f.write('</td>')
        f.write(u'</tr>')
    f.write(u'</table></html>')
    f.close()

def generate_screen_report(model):
    for repo in model:
        print format_repo_to_screen(repo)

repos = lib.retrieve_repos_by_keyword(keywords, language, username, password)

repos_model = []

owners_emails_and_blogs = {}

print "Processing. Please wait..."
i = 0
for repo in repos:
    i += 1
    repos_model.append(repo)

if options.filename:
    generate_file_report(repos_model, f)
else:
    generate_screen_report(repos_model)

print "\nTotal records count: %s" % i
print "Thank you."
