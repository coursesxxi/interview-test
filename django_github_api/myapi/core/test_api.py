import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
import myapi.core.Githubapicore as ghacore

# Create your tests here.


class TestInfoGitHubApi(TestCase):
    """ Test module TestInfoGitHubApi """

    def test_extract_project_PRs(self):
        # get API response : 
        git_Url = "FlatDigital/fullstack-interview-test" 
        #git_Url = 'PyGithub/PyGithub'
        g =  ghacore.GitHubInfoAdmin()
        g.extract_project_PRs(git_Url) 

    def test_extract_project_commits(self):
        # get API response : 
        git_Url = "FlatDigital/fullstack-interview-test" 
        #git_Url = 'PyGithub/PyGithub'
        g =  ghacore.GitHubInfoAdmin()
        g.extract_project_commits(git_Url)

    def test_extract_project_issues(self):
        # get API response : 
        git_Url = "FlatDigital/fullstack-interview-test" 
        #git_Url = 'PyGithub/PyGithub'
        g =  ghacore.GitHubInfoAdmin()
        g.extract_project_issues(git_Url)
'''     
'''