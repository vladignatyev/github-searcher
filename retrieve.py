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

keywords = raw_input('Enter keywords, divided with comma:').split(',')
language = raw_input('Enter language [Objective-C]:')

if not language:
    language = lib.OBJECTIVE_C

def format_repo_to_screen(repo):
    json = repo.to_json()
    return "Username: %s\n  %s [Fork:%s]\n  %s  %s\n  %s  %s  %s" % (json['owner'], 
        json['name'], json['fork'], json['description'], json['url'], 
        json['homepage'], json['followers'], json['forks'])

repos = lib.retrieve_repos_by_keyword(keywords, language)



if options.filename:
    writer = csv.writer(f, encoding='utf-8', delimiter='\t')
    print "Processing. Please wait..."
    writer.writerow(("#", "owner", "name", "fork", 
            "description", "url", "homepage", "followers", "forks",))
    i = 0
    for repo in repos:
        i += 1
        json = repo.to_json()
        writer.writerow((i, json["owner"], json["name"], '1' if json["fork"] else '0', 
            json["description"], json["url"], json["homepage"], json["followers"], json["forks"],))
    print "\nTotal records count: %s" % i
    print "Thank you."

else:
    for repo in repos:
        print format_repo_to_screen(repo)
