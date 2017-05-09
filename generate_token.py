import os
import requests
import json
import settings


class keystoneManager(object):
    @classmethod
    def fetch_token(cls):
        auth = {'auth': {'tenantName': 'admin',
                         'passwordCredentials': {'username': 'admin',
                                                 'password': '123456'}}}

        url = cls.format_url(service_url=settings.token_url)
        print "req: POST %s" % url
        response = requests.post(url=url, data=json.dumps(auth))
        content = json.loads(response.content)
        token = content['access']['token']['id']
        return token

    @classmethod
    def fetch_tenant_id(cls):
        auth = {'auth': {'tenantName': 'admin',
                         'passwordCredentials': {'username': 'admin',
                                                 'password': '123456'}}}

        url = cls.format_url(service_url=settings.token_url)
        response = requests.post(url=url, data=json.dumps(auth))
        content = json.loads(response.content)
        tenant_id = content['access']['token']['tenant']['id']
        return tenant_id

    @staticmethod
    def format_url(service_url=None):
        url = settings.protocol + "://" + settings.ip + ":" \
              + settings.keystone + service_url
        return url
