from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS extension
import random


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

ltr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
       'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
       'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(passwordlen, specialchar, numberlen):
    spchr = specialchar
    numlen = numberlen
    mypassword = ""
    pwdlen = passwordlen - (spchr + numlen)
    for _ in range(pwdlen):
        temp = random.choice(ltr)
        mypassword += temp
    for _ in range(spchr):
        temp1 = random.choice(sym)
        mypassword += temp1
    for _ in range(numlen):
        temp2 = random.choice(num)
        mypassword += temp2

    return mypassword

@app.route('/generate_password', methods=['GET', 'POST'])
def generate_password_api():
    if request.method == 'POST':
        data = request.get_json()
        password_len = data.get('password_len', 8)
        special_char_len = data.get('special_char_len', 1)
        number_len = data.get('number_len', 1)

        generated_password = generate_password(password_len, special_char_len, number_len)

        response = {'password': generated_password}
        return jsonify(response)
    else:
        return "Welcome to the password generator API! Send a POST request with the required parameters."

if __name__ == '__main__':
    app.run(debug=True)
