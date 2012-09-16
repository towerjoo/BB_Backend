"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class APITest(TestCase):
    fixtures = ["all.json"]
    def setUp(self):
        self.c = Client()
        self.username = "zhutao1"
        self.access_token = ""
        self.host = "http://localhost:8000"

    def make_ret_as_dict(self, response):
        return eval(response.content)

    def login(self):
        url = self.host + reverse("account-login")
        response = self.c.post(url, {"username" : "zhutao1", "password" : "zhutao"})
        ret = self.make_ret_as_dict(response)
        self.access_token = ret.get("data").get('access_token')
        return response, ret

    def test_login(self):
        response, ret = self.login()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(ret.get("status"), "success")

    def get_endpoint_with_access_token(self, endpoint, detailId=""):
        endpoint = "%s%s%s?api_key=%s&username=%s&format=json" % (self.host, endpoint, detailId, \
                    self.access_token, self.username)
        return endpoint

    def test_get_user_profile(self):
        self.login()
        url = "/api/v1/account/"
        endpoint = self.get_endpoint_with_access_token(url, "1")
        print endpoint
        response = self.c.get(endpoint)
        print response
