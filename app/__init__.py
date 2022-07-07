import requests
from requests.auth import HTTPBasicAuth
from decouple import config


class JiraClient(object):
    def __init__(self):
        self.account = config('ACCOUNT')
        self.token = config('TOKEN')
        self.site_url = config('SITE_URL')
        self.api_version = config('API_VERSION')
        self.auth = HTTPBasicAuth(self.account, self.token)
        self.api_url = self.site_url + '/rest/api/' + self.api_version
        self.request_header = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get(self, endpoint, params=None, data=None):
        return requests.get(
            self.api_url + endpoint,
            headers=self.request_header,
            auth=self.auth,
            params=params,
            data=data
        )

    def post(self, endpoint, params=None, data=None):
        return requests.post(
            self.api_url + endpoint,
            headers=self.request_header,
            auth=self.auth,
            params=params,
            data=data
        )

    def put(self, endpoint, params=None, data=None):
        return requests.put(
            self.api_url + endpoint,
            headers=self.request_header,
            auth=self.auth,
            params=params,
            data=data
        )


client = JiraClient()
