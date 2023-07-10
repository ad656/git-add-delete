#Author - Allan
#Date - 7/10/23
import requests
import json


def delete_github_repository(repo_owner, repo_name, access_token):
    #delete_url = "https://api.github.com/repos/{}/{repo_name}".format(repo_owner, repo_name)
    delete_url = "https://api.github.com/repos/{}/{}".format(repo_owner, repo_name)

    headers = {
        "Authorization": "Bearer {}".format(access_token),
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.delete(delete_url, headers=headers)

    if response.status_code == 204:
        print("Repository '{}/{}' has been deleted successfully.".format(repo_owner, repo_name))
    elif response.status_code == 404:
        print("Repository '{}/{}' does not exist.".format(repo_owner, repo_name))
    else:
        print("Failed to delete repository '{}/{}'.".format(repo_owner, repo_name))
        print("Response: {}".format(response.text))


repository_owner = raw_input("GitHub username: ")
repository_name = raw_input("Repository name: ")
access_token = raw_input("Access token: ")

delete_github_repository(repository_owner, repository_name, access_token)
