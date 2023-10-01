#!/usr/bin/python3
"""this is the api"""


if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    token = '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'
    head = {'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
            'Authorization': f"Bearer  {token}"}
    response = requests.get(url, headers=head)
    if response.status_code == 200:
        user_data = response.json()
        for i in range(len(user_data)):
            user_data[i]['commit']['author']['date'] =\
                user_data[i]['commit']['author']['date']\
                .replace('-', '')\
                .replace(':', '').replace('T', '').replace('Z', '')
        user_data =\
            sorted(user_data, key=lambda x: x['commit']['author']['date'])
        for i in range(10):
            dic = dict(user_data[i])
            print(dic['sha'] + ": " + dic['commit']['author']['name'])
    else:
        print("None")
