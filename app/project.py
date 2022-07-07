import json
from pydantic import BaseModel
from app import client


class Project(BaseModel):
    id: str
    key: str
    name: str

    def change_permission(self, permission_scheme_id):
        data = {"id": permission_scheme_id}
        r = client.put('/project/{key}/permissionscheme'.format(key=self.key), data=json.dumps(data))
        return r

    @classmethod
    def find(cls, params=None):
        r = client.get('/project/search', params=params)
        if r.status_code == 200:
            return [cls(id=proj['id'], key=proj['key'], name=proj['name']) for proj in r.json()['values']]
