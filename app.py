import bcrypt
from flask import Flask, redirect, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_wtf import FlaskForm
from forms import PostsForm


app = Flask(__name__)


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

db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(email=form.email.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('riddles'))

    return render_template('registration.html', title='Register', form=form)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/riddles', methods=['GET', 'POST'])
def riddles():
    form = PostsForm()
    if form.validate_on_submit():
        post_data = Posts(
            q1=form.q1.data,
            q2=form.q2.data,
            q3=form.q3.data,
            q4=form.q4.data,
            q5=form.q5.data,
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
    #db.session.query(Posts).delete()  # deletes the contents of the table
    db.session.commit()
    return "everything is gone"


if __name__ == '__main__':
    app.run()