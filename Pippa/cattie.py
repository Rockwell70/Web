#!/usr/bin/env python3
import os
from flask import Flask, render_template, Response

app = Flask(__name__)
app.secret_key = b"\x9f\x00\x1d.i\x80U\x8c\x9bPD]\xfbu\xe2\x8d\x12\x12\xc5\xef]h\xb0Z"
#app.secret_key = os.environ.get('SECRET_KEY').encode()

@app.route('/')
@app.route('/index')

def intro():
    image_one = "static/ftd-babyrabbit.jpg"
    image_two = "static/Kitten.jpg"
    return render_template('index.html', image_one=image_one, image_two = image_two)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9210))
    app.run(host="0.0.0.0", port=port, debug=False)
