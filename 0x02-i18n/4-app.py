#!/usr/bin/env python3
"""
simple app
"""

from flask import Flask, render_template
from flask_babel import Babel
from flask import request

app = Flask(__name__)


class Config(object):
    """Configuration class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale"""
    get_locale_param = request.args.get("locale")
    if get_locale_param and get_locale_param in app.config["LANGUAGES"]:
        return get_locale_param
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello_world():
    """return html page"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run
