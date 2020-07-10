import bcrypt
from flask import Flask, redirect, url_for, request
from flask import render_template
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from os import environ, getenv
from flask_wtf import FlaskForm
from wtforms.validators import required, ValidationError

from accountforms import UpdateAccountForm
from forms import PostsForm
from loginforms import LoginForm
from regforms import RegistrationForm
from flask_login import LoginManager, current_user, login_user, UserMixin, logout_user, login_required


app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')


class Posts(db.Model):
    userID = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    q1 = db.Column(db.String(10), primary_key=True, nullable=False)
    q2 = db.Column(db.String(10), nullable=False)
    q3 = db.Column(db.String(10), nullable=False)
    q4 = db.Column(db.String(10), nullable=False)
    q5 = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return ''.join(
            [
                'Answer1: ' + self.q1 + '\n'
                'Answer2: ' + self.q2 + '\n'
                'Answer3: ' + self.q3 + '\n'
                'Answer4: ' + self.q4 + '\n'
                'Answer5: ' + self.q5
            ]
        )


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return ''.join(
            [
                'UserID: ', str(self.id), '\r\n',
                'First_Name: ', self.first_name, '\n',
                'Last_Name: ', self.last_name, '\n',
                'Email: ', self.email,
            ]
        )


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect('home')
    return render_template('login.html', title='Login', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(email=form.email.data, password=hash_pw, first_name=form.first_name.data, last_name=form.last_name.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('riddles'))

    return render_template('registration.html', title='Register', form=form)


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)


@app.route('/riddles', methods=['GET', 'POST'])
@login_required
def riddles():
    form = PostsForm()
    if form.validate_on_submit():
        post_data = Posts(
            q1=form.q1.data,
            q2=form.q2.data,
            q3=form.q3.data,
            q4=form.q4.data,
            q5=form.q5.data
        )
        db.session.add(post_data)
        db.session.commit()
        return redirect(url_for('registration'))
    else:
        return render_template('riddles.html', title='Add a post', form=form)


@app.route('/create')
def create():
    db.create_all()
    post = Posts(q1='Paint', q2='Silence', q3='Shadow', q4="Match", q5='Short')
    post2 = Posts(q1='Blah', q2='Blah', q3='Blah', q4="Blah", q5='Blah')
    db.session.add(post)
    db.session.add(post2)
    db.session.commit()
    return "Added the table and populated it with some records"


@app.route('/delete')
def delete():
    db.drop_all()  # drops all the schemas
    # db.session.query(Posts).delete()  # deletes the contents of the table
    db.session.commit()
    return "everything is gone"


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


def validate_email(self, email):
    if email.data != current_user.email:
        user = Users.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError('Email already in use')


if __name__ == '__main__':
    app.run()
