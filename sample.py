#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:set fileencoding=utf-8:

from flask import Flask

app = Flask("sample")

@app.route("/sample") #トップディレクトリ / は別に使うため
def index():

    return "<h1>Hello World</h1>"

if __name__ == "__main__":

    app.run(host="0.0.0.0",debug=True)
