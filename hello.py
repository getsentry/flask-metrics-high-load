from flask import Flask

import sentry_sdk
from sentry_sdk import metrics

sentry_sdk.init(
    debug=True,
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    for i in range(100_000):
        metrics.count("test", 1.0)

    return "<p>Hello, World!</p>"
