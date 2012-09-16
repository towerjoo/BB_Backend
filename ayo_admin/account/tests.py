"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
import json

class APITest(TestCase):
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

    def test_login_succ(self):
        response, ret = self.login()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(ret.get("status"), "success")
        self.pprint_result(response)

    def test_login_fail(self):
        url = self.host + reverse("account-login")
        response = self.c.post(url, {"username" : "zhutao1", "password" : "zhutao2"})
        ret = self.make_ret_as_dict(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(ret.get("status"), "error")
        self.pprint_result(response)

    def test_register_succ(self):
        url = self.host + reverse("account-register")
        data = {
            "username" : "test1",
            "email" : "test1@gmail.com",
            "password" : "test1",
            "firstname" : "Test",
            "lastname" : "Test",
            "gender" : "male",
        }
        response = self.c.post(url, data)
        print response
        ret = self.make_ret_as_dict(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(ret.get("status"), "success")
        self.pprint_result(response)

    def test_register_fail(self):
        url = self.host + reverse("account-register")
        data = {
            "username" : "test1",
            "email" : "test1",
            "password" : "test1",
            "firstname" : "Test",
            "lastname" : "Test",
            "gender" : "male",
        }
        response = self.c.post(url, data)
        print response
        ret = self.make_ret_as_dict(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(ret.get("status"), "error")
        self.pprint_result(response)

    def get_endpoint_with_api_key(self, endpoint, detailId=""):
        endpoint = "%s%s%s?api_key=%s&username=%s&format=json" % (self.host, endpoint, detailId, \
                    self.api_key, self.username)
        return endpoint

    def test_facebook_connection_succ(self):
        url = self.host + reverse("account-facebook-connection")
        data = {
            "email" : "test1@gmail.com",
            "facebook_id" : "1509090335",
            "facebook_token" : "1509090335",
            "firstname" : "Test",
            "lastname" : "Test",
            "gender" : "male",
        }
        response = self.c.post(url, data)
        print response
        ret = self.make_ret_as_dict(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(ret.get("status"), "success")
        self.pprint_result(response)

    def test_facebook_connection_fail(self):
        url = self.host + reverse("account-facebook-connection")
        data = {
            "email" : "test1",
            "facebook_id" : "1509090335",
            "facebook_token" : "1509090335",
            "firstname" : "Test",
            "lastname" : "Test",
            "gender" : "male",
        }
        response = self.c.post(url, data)
        print response
        ret = self.make_ret_as_dict(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(ret.get("status"), "error")
        self.pprint_result(ret)


    ######## RESTful APIs testing

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


    def test_user_list(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/user/")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_user_detail(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/user/", "1")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_account_list(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/account/")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_account_detail(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/account/", "1")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_account_detail_put(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/account/", "1")
        data = {
            "gender" : "female"
        }
        response = self.c.put(endpoint, json.dumps(data), content_type='application/json')
        print response.content
        print response.status_code
        #self.pprint_result(response)


    def test_follow_relation_list(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/followrelation/", filter="follower_id=1")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_follow_relation_detail(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/followrelation/", "1")
        response = self.c.get(endpoint)
        self.pprint_result(response)


    def test_contact_group_list(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/contactgroup/")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_contact_group_detail(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/contactgroup/", "1")
        response = self.c.get(endpoint)
        self.pprint_result(response)

