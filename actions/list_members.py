import datetime

from github.GithubException import UnknownObjectException
from lib.base import BaseGithubAction
from lib.formatters import user_to_dict

__all__ = [
    'ListMembersAction'
]


class ListMembersAction(BaseGithubAction):
    def run(self, user,filter=None, role=None, limit=20):

        kwargs = {}
        if filter:
            kwargs['filter'] = filter
        if role:
            kwargs['role'] = role

        result = []
        try:
            org = self._client.get_organization(user)
            members = org.get_members(**kwargs)
            members = list(members)

            for index, member in enumerate(members):
                member = user_to_dict(user=member)
                result.append(member)
                if (index + 1) >= limit:
                    break

        except UnknownObjectException:
            print("Organization not found")

        return result
