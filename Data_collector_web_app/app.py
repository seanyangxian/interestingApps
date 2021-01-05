from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_result import send_email
from sqlalchemy.sql import func

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:YXql7440@localhost/video_platform_preference'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    age = db.Column(db.Integer)
    preference = db.Column(db.String(50))

    def __init__(self, email_, age_, preference_):
        self.email = email_
        self.age = age_
        self.preference = preference_


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/complete', methods=['POST'])
def complete():
    if request.method == 'POST':
        email = request.form['email_address']
        age = request.form['age_number']
        preferred_platform = request.form['video-platform']
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            user_data = Data(email, age, preferred_platform)
            db.session.add(user_data)
            db.session.commit()
            average_age = round(db.session.query(func.avg(Data.age)).scalar(), 1)
            total_users = db.session.query(Data).count()
            preference_percentage = round(db.session.query(Data).filter(Data.preference == preferred_platform).count() /
                                          total_users, 3)
            send_email(email, age, preferred_platform, average_age, preference_percentage, total_users)
            return render_template('success.html')
    return render_template('index.html', text="Oops, seems like this email already has data in our database, "
                                              "please submit survey result with other email. Thank you!")


if __name__ == '__main__':
    app.debug = True
    app.run()
