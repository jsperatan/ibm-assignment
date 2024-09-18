# IBM Assignment - Development

## Dependancies

- Python 3.12.5 (If running from host machine)
- Flask (If running from host machine)
- Docker (If running from Docker)

## Web App Tasks Summary

1. Call https://jsonplaceholder.typicode.com/users to get list of users
2. Format response by including only relevant attributes (id, names, usernames, email and company_names)
3. Store formatted response into a list
   - Note: I opted for a list in this case since (I assume) all users id are generated and ordered during creation. This speeds up the runtime as specific user id can be directly referenced by the index instead of iterating thru the list.
4. Add handler for /users/all
5. Add handler for /users/<id>
   - As mentioned before, we do not need to do any searching as specific ids can be directly accessed from the list index (users id = index + 1)

## Running from Host Machine

1. Install Python
2. Clone and navigate to Git Repository
3. _OPTIONAL_: Activate virtual environment
4. Install required packages: `pip install -r requirements.txt`
5. Run application: `python3 index.py` or `py index.py`
6. Access http://127.0.0.1:5656/users/all or http://127.0.0.1:5656/users/<id> from your web browser - Alternatively you can also use cURL: `curl --location 'http://localhost:5656/users/all'` or `curl --location 'http://localhost:5656/users/<id>'`

## Build and Run using Docker

1. Install Docker
2. Clone and navigate to Git Repository
3. Build Docker image: `sudo docker build . -t ibm-assignment/web-app`
4. Run Docker container: `sudo docker run -p 127.0.0.1:5656:5656 -d ibm-assignment/web-app`
   - Assume that endpoint is only accessible from localhost. To expose the application to external networks, use: `sudo docker run -p 5656:5656 -d ibm-assignment/web-app`
5. Access endpoint via cURL: `curl --location 'http://localhost:5656/users/all'` or `curl --location 'http://localhost:5656/users/<id>'`

## Pull from Docker Hub
1. Install Docker
2. Pull Docker image: ```sudo docker pull projectquartz/ibm-assignment:latest```
3. Run Docker container: `sudo docker run -p 127.0.0.1:5656:5656 -d projectquartz/ibm-assignment:latest`
   - Assume that endpoint is only accessible from localhost. To expose the application to external networks, use: `sudo docker run -p 5656:5656 -d projectquartz/ibm-assignment:latest`
4. Access endpoint via cURL: `curl --location 'http://localhost:5656/users/all'` or `curl --location 'http://localhost:5656/users/<id>'`

