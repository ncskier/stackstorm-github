import datetime

from lib.base import BaseGithubAction

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

        repos = user.get_orgs()
        repos = list(repos)

        return repos