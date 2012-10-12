"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from common.test import APIBaseTest

class APITest(APIBaseTest):
    def test_shout_list(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/shout/")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_shout_detail(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/shout/", "1")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_shoutcomment_list(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/shoutcomment/")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_shoutcomment_detail(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/shoutcomment/", "1")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_shoutreport_list(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/shoutreport/")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_shoutreport_detail(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/shoutreport/", "1")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_shout_filter(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/shout/", filter="author__user__username=zhutao1")
        response = self.c.get(endpoint)
        self.pprint_result(response)

