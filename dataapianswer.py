import requests
from flask import Flask, render_template
app = Flask(__name__)

apirequests = requests.get("https://reqres.in/api/users/2")
dataapi = apirequests.json()

@app.route('/')
def index():
    first_name = dataapi['data']['first_name']
    last_name = dataapi['data']['last_name']
    email = dataapi['data']['email']
    return render_template('test.html', first_name=first_name,last_name=last_name,email=email)

if __name__ == "__main__":
    app.run(debug=True)
