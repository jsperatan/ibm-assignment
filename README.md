# IBM Assignment - Development 
## Dependancies
- Python 3.12.5 (If running from host machine)
- Flask (If running from host machine)
## Web App Tasks Summary
1. Call https://jsonplaceholder.typicode.com/users to get list of users
2. Format response by including only relevant attributes (id, names, usernames, email and company_names)
3. Store formatted response into a list
   - Note: I opted for a list in this case since (I assume) all users id are generated and ordered during creation. This speeds up the runtime as specific user id can be directly referenced by the index instead of iterating thru the list.
4. Add handler for /users/all
5. Add handler for /users/<id>
   - As mentioned before, we do not need to do any searching as specific ids can be directly accessed from the list index (users id = index + 1)
## Running from Host Machine
1. Install Python 3.12.5
2. OPTIONAL: Activate virtual environment
3. Install required packages: pip install -r requirements.txt
4. Run application: py index.py
5. Access http://127.0.0.1:5656/users/all or http://127.0.0.1:5656/users/<id> from your web browser
  - Alternatively you can also use CURL: curl --location 'http://localhost:5656/users/all' or curl --location 'http://localhost:5656/users/<id>'
