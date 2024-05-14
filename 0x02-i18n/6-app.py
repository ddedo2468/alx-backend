#!/usr/bin/env python3
"""
simple app
"""

from flask import Flask, render_template, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get user"""
    try:
        return users.get(int(request.args.get("login_as")))
    except Exception:
        return None


@app.before_request
def before_request():
    """Before request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Get locale"""
    get_locale_param = request.args.get("locale")
    if get_locale_param and get_locale_param in app.config["LANGUAGES"]:
        return get_locale_param
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello_world():
    """return html page"""
    username = g.user.get("name") if g.user else None
    return render_template("5-index.html", username=username)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
