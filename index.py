from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False #ensure that attributes are not sorted

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

@app.route('/users/all', methods=['GET'])
def get_users():
    return jsonify(formatted_users)

@app.route('/users/<int:id>', methods=['GET'])
def get_users_by_id(id: int):
    if (id > 0 and id <= len(formatted_users)):
        return jsonify(formatted_users[id-1])
    return jsonify({"error": "User does not exist"}), 404

if __name__ == '__main__':
   app.run(port=5656)