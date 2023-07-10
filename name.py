import requests
import json

user_name = raw_input("Enter your GitHub username: ")
print user_name

github_token = raw_input("Enter your GitHub token: ")
print github_token

repo_name = raw_input("Enter your repo name: ")
print repo_name

repo_description = raw_input("Enter your repo description: ")
print repo_description

payload = {'name': repo_name, 'description': repo_description, 'auto_init': 'true'}
repo_request = requests.post('https://api.github.com/' + 'user/repos', auth=(user_name, github_token), data=json.dumps(payload))

if repo_request.status_code == 422:
    print "GitHub repo already exists. Try with another name."
elif repo_request.status_code == 201:
    print "GitHub repo has been created successfully."
elif repo_request.status_code == 401:
    print "You are an unauthorized user for this action."