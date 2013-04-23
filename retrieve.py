import lib

keywords = raw_input('Enter keywords, divided with comma:').split(',')
language = raw_input('Enter language [Objective-C]:')
if not language:
    language = lib.OBJECTIVE_C

# {u'fork': False, 
# u'has_wiki': True, 
# u'private': False, 
# u'pushed': u'2012-02-28T15:44:29Z', 
# u'owner': u'gimenete', 
# u'size': 168, 
# u'score': 118.713745, 
# u'followers': 2418, 
# u'forks': 374, 
# u'homepage': u'http://iosboilerplate.com/', 
# u'username': u'gimenete', 
# u'description': u'iOS-app template with lots of common tasks solved', 
# u'has_downloads': True, 
# u'has_issues': True, 
# u'watchers': 2418, 
# u'name': u'iOS-boilerplate', 
# u'language': u'Objective-C', 
# u'created': u'2011-08-22T22:16:17Z', 
# u'url': u'https://github.com/gimenete/iOS-boilerplate', 
# u'type': u'repo', u'created_at': u'2011-08-22T22:16:17Z', 
# u'pushed_at': u'2012-02-28T15:44:29Z', 
# u'open_issues': 16}

def format_repo(repo):
    json = repo.to_json()
    return "Username: %s\n  %s [Fork:%s]\n  %s  %s\n  %s  %s  %s" % (json['owner'], 
        json['name'], json['fork'], json['description'], json['url'], 
        json['homepage'], json['followers'], json['forks'])

for repo in lib.retrieve_repos_by_keyword(keywords, language):
    print format_repo(repo)