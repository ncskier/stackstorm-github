import datetime

from lib.base import BaseGithubAction
from lib.formatters import org_to_dict

__all__ = [
    'ListOrganizationsAction'
]


class ListOrganizationsAction(BaseGithubAction):
    def run(self, user, base_url, since=None, limit=20):
        if base_url == None:
            self._reset(user)
        else:
            self._reset(user+'|'+base_url)
        user = self._client.get_user(user)

        kwargs = {}

        if since:
            kwargs['since'] = datetime.datetime.fromtimestamp(since)

        orgs = user.get_orgs()
        print(orgs)
        #print(orgs.get_page(0))
        #result = []
#        for org in orgs:
#            print(org)
#            result.append(org)
        #repos = list(repos)

 #       return result
        result = []
        for index, org in enumerate(orgs):
            org = org_to_dict(org=org)
            result.append(org)

            if (index + 1) >= limit:
                break

        return result
