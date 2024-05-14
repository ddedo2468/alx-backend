#!/usr/bin/env python3
"""
simple app
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello_world():
    """return html page"""
    return render_template("0-index.html")
