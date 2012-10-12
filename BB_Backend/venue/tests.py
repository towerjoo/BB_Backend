"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from common.test import APIBaseTest

class APITest(APIBaseTest):
    def test_venue_list(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/venue/")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_venue_detail(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/venue/", "1")
        response = self.c.get(endpoint)
        self.pprint_result(response)

    def test_venue_detail_put(self):
        self.login()
        endpoint = self.get_endpoint("/api/v1/venue/", "1")
        data = {
            "name" : "new name"
        }
        response = self.c.put(endpoint, json.dumps(data), content_type='application/json')
        print response.content
        print response.status_code
        #self.pprint_result(response)



