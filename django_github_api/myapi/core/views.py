from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated
from github import Github
import json
import myapi.core.Githubapicore as ghacore
from django.http import HttpResponse
import csv
import pandas as pd

class HelloView(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!, Hola Mundo, Ciao Mondo, Bonjour monde'}
        return Response(content)

class HelpView(APIView):

    def get(self, request):
        content = {'message': 'Help. Please do the next calls : hello, help, branches '}
        return Response(content)

class branchesView(APIView):

    def get(self, request):
        '''
        Recover data from GitHub, like :
        "[Branch(name=\"alfonsolzrg-add-instructions\"), Branch(name=\"alfonsolzrg-patch-1\"), Branch(name=\"master\")]"
        '''
        g = Github("USERNAME", "PASSWORD")
        url = "FlatDigital/fullstack-interview-test"
        repo = g.get_repo(url)
        list_braches = list(repo.get_branches())
        list_braches_names = []
        #print(list_braches)
        for element in list_braches:
            list_braches_names.append(element.name)
        print(list_braches_names)
        row_json = json.dumps(list_braches_names)
        #content = "Ohhh"
        content = row_json
        return Response(content) 

class branchesUrlView(APIView):

    def get(self, request):
        url = request.GET['url']
        g = Github("USERNAME", "PASSWORD")
        print(url)
        repo = g.get_repo(url)
        list_braches = list(repo.get_branches())
        list_braches_names = []
        for element in list_braches:
            list_braches_names.append(element.name)
        print(list_braches_names)
        row_json = json.dumps(list_braches_names)
        content = row_json
        return Response(content) 

class branchesPrView(APIView):

    def get(self, request):
        # get API response : 
        url = request.GET['url']
        g = Github("USERNAME", "PASSWORD")
        #git_Url = "FlatDigital/fullstack-interview-test" 
        g =  ghacore.GitHubInfoAdmin()
        g.extract_project_PRs(url) 
        file_csv = "PRs_dataset_2.csv"
        my_filtered_csv = pd.read_csv(file_csv, usecols=['contributor_email', 'contributor_type', 'pr_commits_count',
'pr_created_at', 'pr_html_url', 'pr_number', 'pr_state', 'pr_title', 
'pr_url'])
        #csv_pickle = my_filtered_csv.to_pickle(my_filtered_csv)
        row_json = my_filtered_csv.to_json(orient = "records")
        content = row_json
        return Response(content)      