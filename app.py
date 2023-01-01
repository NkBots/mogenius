import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://Itz-zaid:ghp_147bkkabcdefgh@github.com/Itz-zaid/anywhere
os.system("git clone https://nkbots:token@github.com/nkbots/testre ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 main.py &")
