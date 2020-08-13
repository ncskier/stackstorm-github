import datetime

from lib.base import BaseGithubAction
from lib.formatters import organization_to_dict

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

        organizations = user.get_organizations(**kwargs)
        organizations = list(organizations)

        result = []
        for index, organization in enumerate(organizations):
            organization = organization_to_dict(organization=organization)
            result.append(organization)

            if (index + 1) >= limit:
                break

        return result
