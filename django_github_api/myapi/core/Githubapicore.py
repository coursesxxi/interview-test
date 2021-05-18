# githubapicore
import os
from github import Github, RateLimitExceededException, BadCredentialsException, BadAttributeException, \
    GithubException, UnknownObjectException, BadUserAgentException
import pandas as pd
import requests
import time
from datetime import datetime


class GitHubInfoAdmin():
    #permission_classes = (IsAuthenticated,)

    def get_access_token():
        """
        Get your token in GitHub
        Define a OS Variable 
        {ACCESS_TOKEN_GITHUB, GitHub_token }
        """
        key = 'ACCESS_TOKEN_GITHUB'
        ACCESS_TOKEN = os.getenv(key)
        return ACCESS_TOKEN


    def extract_project_commits(self,project_full_name):
        """ extract_commits """

        df_commits = pd.DataFrame()
        while True:
            try:            
                access_token = GitHubInfoAdmin.get_access_token()
                
                g = Github(access_token, per_page=100, retry=20)
                repo = g.get_repo(project_full_name)
                start_time = datetime.strptime("2010-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')
                end_time = datetime.strptime("2021-12-31 00:00:00", '%Y-%m-%d %H:%M:%S')
                all_commits = repo.get_commits(author='s-t-e-v-e-n-k')
                
                counter = 0
                print(all_commits.totalCount)
                for commit in all_commits:
                    while True:
                        try:
                            counter += 1
                            print(f"Loop counter {counter}")
                            print(g.rate_limiting)
                            df_commits = df_commits.append({
                                'commit_sha': commit.sha,
                                'committer_username': commit.author.login if commit.author is not None else '',
                                'committer_name': commit.author.name if commit.author is not None else '',
                                'committer_email': commit.author.email if commit.author is not None else '',
                                'commit_date': commit.author.created_at if commit.author is not None else '',
                            }, ignore_index=True)
                        except RateLimitExceededException as e:
                            print(e.status)
                            print('Rate limit exceeded')
                            time.sleep(300)
                            continue
                        except BadCredentialsException as e:
                            print(e.status)
                            print('Bad credentials exception')
                            break
                        except UnknownObjectException as e:
                            print(e.status)
                            print('Unknown object exception')
                            break
                        except GithubException as e:
                            print(e.status)
                            print('General exception')
                            break
                        except requests.exceptions.ConnectionError as e:
                            print('Retries limit exceeded')
                            print(str(e))
                            time.sleep(10)
                            continue
                        except requests.exceptions.Timeout as e:
                            print(str(e))
                            print('Time out exception')
                            time.sleep(10)
                            continue
                        break
            except RateLimitExceededException as e:
                print(e.status)
                print('Rate limit exceeded')
                time.sleep(300)
                continue
            except BadCredentialsException as e:
                print(e.status)
                print('Bad credentials exception')
                break
            except UnknownObjectException as e:
                print(e.status)
                print('Unknown object exception')
                break
            except GithubException as e:
                print(e.status)
                print('General exception')
                break
            except requests.exceptions.ConnectionError as e:
                print('Retries limit exceeded')
                print(str(e))
                time.sleep(10)
                continue
            except requests.exceptions.Timeout as e:
                print(str(e))
                print('Time out exception')
                time.sleep(10)
                continue
            break
        df_commits.to_csv('commits_author_1.csv', sep=',', encoding='utf-8', index=True)
        print(df_commits)


    def extract_project_issues(self,project_full_name):
        """ extract_issues.py """
        df_issues = pd.DataFrame()
        while True:
            try:
                access_token = GitHubInfoAdmin.get_access_token()
                
                g = Github(access_token, per_page=100, retry=20)
                repo = g.get_repo(project_full_name)
                start_time = datetime.strptime("2020-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')
                end_time = datetime.strptime("2021-12-31 00:00:00", '%Y-%m-%d %H:%M:%S')
                all_issues = repo.get_issues(state='open', sort='created', direction='asc')
                counter = 0
                print(all_issues.totalCount)
                for issue in all_issues:
                    while True:
                        try:
                            counter += 1
                            print(f"Loop counter {counter}")
                            print(g.rate_limiting)
                            if issue.pull_request is not None:
                                break
                            issue_comments = []
                            for comment in issue.get_comments():
                                cmt = {
                                    'user': comment.user.name,
                                    'user_id': comment.user.id,
                                    'user_site_admin': comment.user.site_admin,
                                    'body': comment.body
                                }
                                issue_comments.append(cmt)
                                print(issue.id)
                                print(issue.pull_request)

                            df_issues = df_issues.append({
                                'issue_id': issue.id,
                                'issue_number': issue.number, # issue features
                                'issue_labels': [l.name for l in issue.labels],
                                'issue_title': issue.title,
                                'issue_body': issue.body,
                                'owner': issue.user.name if issue.user is not None else '', # Issue owner features
                                'owner_username': issue.user.login if issue.user is not None else '',
                                'followers': issue.user.followers,
                                'followings': issue.user.following,
                                'contributions': issue.user.contributions,
                                'stars': issue.user.get_starred().totalCount,
                                'issue_date': issue.created_at,
                                'issue_comments': issue_comments,
                                'issueORPR': issue.pull_request
                            }, ignore_index=True)
                        except RateLimitExceededException as e:
                            print(e.status)
                            print('Rate limit exceeded')
                            time.sleep(300)
                            continue
                        except BadCredentialsException as e:
                            print(e.status)
                            print('Bad credentials exception')
                            break
                        except UnknownObjectException as e:
                            print(e.status)
                            print('Unknown object exception')
                            break
                        except GithubException as e:
                            print(e.status)
                            print('General exception')
                            break
                        except requests.exceptions.ConnectionError as e:
                            print('Retries limit exceeded')
                            print(str(e))
                            time.sleep(10)
                            continue
                        except requests.exceptions.Timeout as e:
                            print(str(e))
                            print('Time out exception')
                            time.sleep(10)
                            continue
                        break
            except RateLimitExceededException as e:
                print(e.status)
                print('Rate limit exceeded')
                time.sleep(300)
                continue
            except BadCredentialsException as e:
                print(e.status)
                print('Bad credentials exception')
                break
            except UnknownObjectException as e:
                print(e.status)
                print('Unknown object exception')
                break
            except GithubException as e:
                print(e.status)
                print('General exception')
                break
            except requests.exceptions.ConnectionError as e:
                print('Retries limit exceeded')
                print(str(e))
                time.sleep(10)
                continue
            except requests.exceptions.Timeout as e:
                print(str(e))
                print('Time out exception')
                time.sleep(10)
                continue
            break
        df_issues.to_csv('open_issues_1.csv', sep=',', encoding='utf-8', index=True)
        print(df_issues)


    def extract_project_PRs(self,project_full_name):
        """ extract_PRs """

        df_PRs = pd.DataFrame()
        while True:
            try:
                access_token = GitHubInfoAdmin.get_access_token()

                g = Github(access_token, retry=10, timeout=15, per_page=100)
                print(f'Extracting data from {project_full_name} repo')
                repo = g.get_repo(project_full_name)
                PRs_list = repo.get_pulls(state='closed', sort='created', base='master')

                for pr in PRs_list:
                    try:
                        print(g.rate_limiting)
                        print(f'Extracting data from PR # {pr.number}')
                        # Review Comments on the Pull requests
                        review_comments = []
                        if pr.get_comments().totalCount>0:
                            for comment in pr.get_comments():
                                cmt = {
                                    'comment_id': comment.id,
                                    'comment_body': comment.body,
                                    'comment_created': comment.created_at,
                                    'commenter': comment.user.login,
                                    'type': comment.user.type
                                }
                                review_comments.append(cmt)
                        df_PRs = df_PRs.append({
                            'pr_id': pr.id, # PRs features
                            'pr_title': pr.title,
                            'pr_body': pr.body,
                            'pr_number': pr.number,
                            'pr_url': pr.url,
                            'pr_html_url': pr.html_url,
                            'pr_state': pr.state,
                            'additions': pr.additions,
                            'deletions': pr.deletions,
                            'pr_changed_files': pr.changed_files,
                            'pr_commits_count': pr.commits,
                            'pr_comments_count': pr.comments,
                            'pr_review_comments_count': pr.review_comments,
                            'pr_labels_count': len([l.name for l in pr.labels]),
                            'pr_assignees_count': len(pr.assignees),
                            'pr_labels': [l.name for l in pr.labels],
                            'pr_created_at': pr.created_at,
                            'pr_closed_at': pr.closed_at,
                            'pr_review_comments': review_comments,
                            'contributor': pr.user.name,  # Contributor's information
                            'contributor_id': pr.user.id,
                            'contributor_email': pr.user.email,
                            'contributor_type': pr.user.type,
                            'contributor_public_repos': pr.user.public_repos,
                            'contributor_private_repos': pr.user.owned_private_repos,
                            'contributor_followings': pr.user.following,
                            'contributor_followers': pr.user.followers,
                        }, ignore_index=True)
                    except RateLimitExceededException as e:
                        print(e.status)
                        print('Rate limit exceeded')
                        time.sleep(300)
                        continue
                    except BadCredentialsException as e:
                        print(e.status)
                        print('Bad credentials exception')
                        break
                    except UnknownObjectException as e:
                        print(e.status)
                        print('Unknown object exception')
                        break
                    except GithubException as e:
                        print(e.status)
                        print('General exception')
                        break
                    except requests.exceptions.ConnectionError as e:
                        print('Retries limit exceeded')
                        print(str(e))
                        time.sleep(10)
                        continue
                    except requests.exceptions.Timeout as e:
                        print(str(e))
                        print('Time out exception')
                        time.sleep(10)
                        continue

            except RateLimitExceededException as e:
                print(e.status)
                print('Rate limit exceeded')
                time.sleep(300)
                continue
            except BadCredentialsException as e:
                print(e.status)
                print('Bad credentials exception')
                break
            except UnknownObjectException as e:
                print(e.status)
                print('Unknown object exception')
                break
            except GithubException as e:
                print(e.status)
                print('General exception')
                break
            except requests.exceptions.ConnectionError as e:
                print('Retries limit exceeded')
                print(str(e))
                time.sleep(10)
                continue
            except requests.exceptions.Timeout as e:
                print(str(e))
                print('Time out exception')
                time.sleep(10)
                continue
            break
        df_PRs.to_csv('PRs_dataset_2.csv', sep=',', encoding='utf-8', index=True)
        print(df_PRs)
