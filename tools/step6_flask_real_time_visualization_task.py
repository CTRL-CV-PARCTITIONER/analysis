from flask import Flask, Response, json, render_template
from flask_sqlalchemy import SQLAlchemy
from configuration.config import _sqlParam
import sys
import os
sys.path.append(
    os.path.dirname(
         os.path.dirname(
             os.path.abspath(__file__)
         )
    )
)
from tools.step4_data_visualization_task import echarts

# create flask application object
app = Flask(__name__)

username = _sqlParam["username"]
password = _sqlParam["password"]
host = _sqlParam["host"]
port = _sqlParam["port"]
database = _sqlParam["database"]

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

# create db object
db = SQLAlchemy(app)

#TODO: create and connect user table
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    __tablename__= "user"


@app.route('/')
def query_user():
    users = User.query.all()    
    if users:
        user_data = []
        for user in users:
            user_data.append( (
                user.username,
                int(user.password)
            ) )
        echart = echarts(user_data, "templates/render.html")
        if not os.path.exists("templates"):
            os.makedirs("templates")
        echart.time_line()
        return render_template("render.html")
    else:
        return 'User not found'
        
    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")