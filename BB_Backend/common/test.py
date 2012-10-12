"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
import json

class APIBaseTest(TestCase):
    fixtures = ["all.json"]
    def setUp(self):
        self.c = Client()
        self.username = "zhutao1"
        self.api_key = ""
        self.host = "http://localhost:8000"

    def make_ret_as_dict(self, response):
        return eval(response.content)

    def pprint_result(self, resp):
        print json.dumps(json.loads(resp.content), indent=4)

    def login(self):
        url = self.host + reverse("account-login")
        response = self.c.post(url, {"username" : "zhutao1", "password" : "zhutao"})
        ret = self.make_ret_as_dict(response)
        self.api_key = ret.get("data").get('api_key')
        return response, ret


    def get_endpoint(self, endpoint, resourceId=None, filter=None):
        if resourceId:
            # detail
            return "%s%s%s?api_key=%s&username=%s&format=json" % (self.host, endpoint, resourceId, self.api_key, self.username)
        else:
            # list
            if filter is None:
                return "%s%s?api_key=%s&username=%s&format=json" % (self.host, endpoint, self.api_key, self.username)
            else:
                return "%s%s?api_key=%s&username=%s&format=json&%s" % (self.host, endpoint, self.api_key, self.username, filter)


