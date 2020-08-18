import datetime

from lib.base import BaseGithubAction
from lib.formatters import org_to_dict

__all__ = [
    'ListOrgsAction'
]


class ListOrgsAction(BaseGithubAction):
    def run(self, user, base_url, token, limit=20):
        if user == None:
            user = self._temp_client(token, base_url).get_user()
        else:
            if base_url == None:
                self._reset(user)
            else:
                self._reset(user+'|'+base_url)
                user = self._client.get_user(user)

        kwargs = {}

        orgs = user.get_orgs(**kwargs)
        orgs = list(orgs)

        result = []
        for index, org in enumerate(orgs):
            repo = org_to_dict(org=org)
            result.append(repo)

            if (index + 1) >= limit:
                break

        return result
