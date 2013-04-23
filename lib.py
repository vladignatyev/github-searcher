from github3 import GitHub

OBJECTIVE_C = 'Objective-C'

def retrieve_repos_by_keyword(keywords, language):
    gh = GitHub()
    try:
        for keyword in keywords:
            for page in range(1, 11):
                repos = gh.search_repos(keyword, language=language, start_page=page)
                for repo in repos:
                    if repo.to_json()['language'] == language:
                        yield repo
    except Exception:
        pass

