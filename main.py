from flask import Flask, request, Response, render_template, send_file
from email.message import EmailMessage
import smtplib
import json, os, signal
import subprocess

app = Flask(__name__)

# Define path to the text file containing valid credentials
VALID_CREDENTIALS_FILE = 'valid_credentials.txt'
ULB2_lyrics = 'static/blocked_audio.mp3'


#subprocess.run("ngrok tunnel --label edge=edghts_2dziYZnlfGRNEMcjxhL012llVpM http://localhost:5000", shell=True, check=True)
Access = "nul"
tempU = "a"
tempP = "b"
idk = "c"
recipient = "noel345@outlook.fr"
message = "Hello world!"


# Function to read valid credentials from the text file
def read_valid_credentials():
    with open(VALID_CREDENTIALS_FILE, 'r') as file:
        return [line.strip().split(',') for line in file]

# Define the list of valid credentials
VALID_CREDENTIALS = read_valid_credentials()

def is_web_browser_request():
    user_agent = request.headers.get('User-Agent')
    return user_agent and 'curl' not in user_agent.lower()

@app.route('/blocked')
def BLOCKEDONCEAGAIN():
    if is_web_browser_request():
        return render_template('ULB2.html')
    else:
        return "Blocked access."

@app.route('/', methods=['GET'])
def index():
    global tempU, tempP, Access
    auth = request.authorization
    if not auth or [auth.username, auth.password] not in VALID_CREDENTIALS:
        return authenticate()
    else:
        tempU = auth.username
        tempP = auth.password
        return WEBchoose()

def authenticate():
    return Response('Could not verify your credentials.', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

def WEBchoose():
    global Access
    if tempU == "noel":
        Access = "Director"
        return render_template("SiteDirector.html")
    elif tempU == "LMER" or tempU == "BlueShark": #security team+
        Access = "Security+"
        return render_template('LMER.html')
    elif tempU == "Jack Nyras": # security team
        Access = "Security"
        return render_template('employe.html')
    elif tempU == "GreyHate": # maintenance team+
        Access = "Maintenance+"
        return render_template('employe.html')        
    elif tempU != '':
        Access = "employee"
        return render_template('employe.html')
    else:
        return "Unknown user. Please log in with valid credentials."

@app.route('/test')
def test_page():
    global tempU, tempP
    auth = request.authorization
    if idk == "a":
        return "HACKER"
    elif not auth or [auth.username, auth.password] not in VALID_CREDENTIALS:
        return authenticate()
    else:
        tempU = auth.username
        tempP = auth.password
        return WEBchoose()

@app.route('/favicon.ico')
def favI():
    return send_file("favicon.ico")

@app.route('/apple-touch-icon.png')
def apple_touch_icon():
    return send_file("apple-touch-icon.png")

@app.route('/Unstable Reactor State.html')
def URS():
    global Access, tempU
    if Access == "Security+" or Access == "Director" or Access == "SpatialBaseSecurity" or Access == "ASES" or Access == "Maintenance+" or tempU == "jack Nyras":
        return render_template('Unstable Reactor State.html')
    elif Access == "employee":
        return render_template('ULB2.html')

@app.route('/button_clicked', methods=['POST'])
def heh():
    return render_template('ULB2.html')

@app.route('/Main.html')
def tsk():
    return render_template('MAIN.html')




@app.route('/shutdown', methods=['GET'])
def stopServer():
    global Access
    if Access == "Security+" or Access == "Director" or Access == "SpatialBaseSecurity" or Access == "ASES":
        os.kill(os.getpid(), signal.SIGINT)
        return jsonify({ "success": True, "message": "Server is shutting down..." })


def ASASEMAIL():
    global recipient, message
    sender = "ASAS-external-relay@outlook.fr"

    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = "Test Email"
    email.set_content(message)

    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(sender, "AIRplane78380")
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()














if __name__ == '__main__':
    app.run(debug=True)
