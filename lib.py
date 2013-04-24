from github3 import GitHub, login

OBJECTIVE_C = 'Objective-C'

def retrieve_repos_by_keyword(keywords, language, username='', password=''):
    gh = None
    if username and password:
        gh = login(username, password=password)
    else:
        gh = GitHub()
    try:
        for keyword in keywords:
            for page in range(1, 11):
                repos = gh.search_repos(keyword, language=language, start_page=page)
                for repo in repos:
                    r = repo.to_json()
                    if r['language'] == language:
                        result = r
                        try:
                            user = gh.user(r['owner']).to_json()
                            result['owner_email'] = user.get('email', '')
                            result['owner_blog'] = user.get('blog', '')
                            result['owner_location'] = user.get('location', '')
                            result['owner_avatar'] = user.get('avatar_url', '')
                        except Exception as e:
                            pass
                        yield result
    except Exception as e:
        print e
        pass

