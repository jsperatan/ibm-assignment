from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)

#get JSON data
url = "https://jsonplaceholder.typicode.com/users"

response = requests.request("GET", url)

users = json.loads(response.text)

#formatting list of users from request to desired output
formatted_users = []
for user in users: 
    user_details = {'id': user['id'],
                    'name': user['name'],
                    'email': user['email'],
                    'username': user['username'],
                    'company_name': user['company']['name']}
    formatted_users.append(user_details)

print(formatted_users)
