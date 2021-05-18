import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class TestViews(TestCase):
    """ Test module """

    def setUp(self):
        # initialize the APIClient app
        self.client = Client()
        self.branches_url = 'branches'
        self.branchesurl_url = 'branchesurl' 

    def test_branches(self):
        # get API response : 
        print("test: "+ self.branches_url)
        response = self.client.get(reverse(self.branches_url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_branches_url(self):
        # get API response : 
        print("test: "+ self.branchesurl_url)
        url_test = "FlatDigital/fullstack-interview-test"
        response = self.client.get(reverse(self.branchesurl_url), {'url': url_test})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hello(self):
        # get API response : 
        test_url = "hello"
        print("test: "+test_url)
        response = self.client.get(reverse(test_url))

    def test_help(self):
        # get API response : 
        test_url = "help"
        print("test: "+test_url)
        response = self.client.get(reverse(test_url))
