from lib.base import BaseGithubAction
import json
from st2client.client import Client
from st2client.models import KeyValuePair
from lib.formatters import filter_org

__all__ = [
    'AddOrgAction'
]

# Default Github API url
DEFAULT_API_URL = 'https://api.github.com'

class AddOrgAction(BaseGithubAction):
    def run(self, user, url, token, github_type, repositories, event_type_whitelist):

        client = Client()
        gitorgs = client.keys.get_by_name(name='git-orgs', decrypt=True)
        if gitorgs:
            dict=json.loads(gitorgs.value)
        else:
            dict={}
        
        user = user.strip()
        url = (url or '').strip()

        if len(url) == 0:
            url = DEFAULT_API_URL
            github_type = 'online'

        if repositories == None:
            repositories = []

        key = user + '|' + url
        org = dict.get(key)

        if org == None:
            org = {'user': user, 'url': url, 'token': token, 'type': github_type, 'repositories': repositories, 'event_type_whitelist': event_type_whitelist}
        else:
            if token != None:
                org['token'] = token
            org['repositories'] = list(set(org['repositories']).union(repositories))
            org['event_type_whitelist'] = list(set(org['event_type_whitelist']).union(event_type_whitelist))

        dict[key]=org
        gitorgs=json.dumps(dict)

        client.keys.update(KeyValuePair(name='git-orgs', value=gitorgs, secret=True))

        return list((key, filter_org(org)))
