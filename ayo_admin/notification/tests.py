"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from common.test import APIBaseTest

class APITest(APIBaseTest):
    def test_notification_list(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/shoutnotification/")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_notification_detail(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/shoutnotification/", "1")
        response = self.c.get(endpoint)
        self.pprint_result(response)

