from flask import Flask, request, Response

app = Flask(__name__)



file_path = 'ASAS-CONNECTION-LOG-SUCCESS.txt'
 
with open(file_path, 'r') as file:
    NOELCONNECTED = file.read()

file_path = 'ASAS-CONNECTION-LOG.txt'
 
with open(file_path, 'r') as file:
    ASASCONNECTIONDENIED = file.read()



# Define username and password (replace with your own)
USERNAME = 'usernam'
PASSWORD = 'password'

@app.route('/', methods=['GET'])
def index():
        auth = request.authorization
        if auth.username == 'noel' and auth.password == 'Part':
            return NOELCONNECTED
        elif not auth or not check_auth(auth.username, auth.password):
            return ASASCONNECTIONDENIED
        else:
            return "Custom message for curl with correct credentials"
    # else:
    #     auth = request.authorization
    #     if not auth or not check_auth(auth.username, auth.password):
    #         return authenticate()
    #     else:
    #         return "Welcome to the website! You are logged in."

def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

def authenticate():
    return Response('Could not verify your credentials.', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

def is_curl_request():
    user_agent = request.headers.get('User-Agent')
    return user_agent and 'curl' in user_agent

if __name__ == '__main__':
    app.run(debug=True)
