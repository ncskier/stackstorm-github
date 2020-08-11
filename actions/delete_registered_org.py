from lib.base import BaseGithubAction
import json
from st2client.client import Client
from st2client.models import KeyValuePair
from lib.formatters import filter_org

__all__ = [
    'DeleteOrgAction'
]


class DeleteOrgAction(BaseGithubAction):
    def run(self, user, url):

        client = Client()
        gitorgs = client.keys.get_by_name(name='git-orgs', decrypt=True)
        if gitorgs:
            dict=json.loads(gitorgs.value)
        else:
            dict={}

        user = user.strip()
        url = url.strip()

        key = user + '|' + url

        if key in dict:
            org = dict[key]
            del dict[key]
            gitorgs=json.dumps(dict)

            client.keys.update(KeyValuePair(name='git-orgs', value=gitorgs, secret=True))

            return list((key, filter_org(org)))

        return False
