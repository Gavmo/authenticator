from flask import Flask, render_template, request, make_response, redirect
import bcrypt
import random
from string import ascii_letters

import csv
app = Flask(__name__)


def rand_string(char_len):
    return_str = ""
    for x in range(0, int(char_len)):
        return_str += ascii_letters[random.randrange(0, len(ascii_letters))]
    return return_str


@app.route("/", methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        with open(f"../data/creds.csv", 'r') as csv_file:
            csv_data = csv.reader(csv_file)
            for record in csv_data:
                if record[0] == request.form['user_name']:
                    if bcrypt.checkpw(request.form['passwd'].encode('utf-8'), record[1].encode('utf-8')):
                        pass
                        resp = make_response(redirect(request.base_url))
                        resp.set_cookie('SESSION', record[2])
                        # set header and do a redirect
                        return resp
        return request.form
    return render_template(f"login.html", )


