# 测试flask实现可视化实时刷新
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

