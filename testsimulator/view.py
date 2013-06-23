from flask.ext.uploads import UploadNotAllowed
from decorators import login_required
from testsimulator import app, uploaded_photos, uploaded_resumes, form
from testsimulator.form import SigninForm, LoginForm
from testsimulator.model import Candidate
from flask import render_template, url_for, session, flash, request, g, redirect
from sqlite3 import DatabaseError, DataError
import setting
from util import query_db

LOREM_IPSUM = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Typi non habent claritatem insitam; est usus legentis in iis qui facit eorum claritatem. Investigationes demonstraverunt lectores legere me lius quod ii legunt saepius. Claritas est etiam processus dynamicus, qui sequitur mutationem consuetudium lectorum. Mirum est notare quam littera gothica, quam nunc putamus parum claram, anteposuerit litterarum formas humanitatis per seacula quarta decima et quinta decima. Eodem modo typi, qui nunc nobis videntur parum clari, fiant sollemnes in futurum.'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        if valid_login(username, password):
            session['user_name'] = username
            return redirect(url_for('user_profile', username=username))
        else:
            flash(u'User name or password is incorrect.', 'error')
            return render_template('login.html')

    return render_template('login.html', form=form)


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    form = SigninForm(request.form)
    if request.method == 'POST':
        if form.validate() and valid_signin(form):
            c = Candidate({
                'name': form.name.data,
                'address': form.address.data,
                'email': form.email.data,
                'password': form.password.data,
                'phone': form.phone.data
            })

            # generate verification code for double authentication
            verification_code = generate_verification_code()
            c.verification_code = verification_code

            resume = request.files['resume']
            photo = request.files['photo']

            if save_new_candidate(c,  resume, photo):
                send_email(c.email, verification_code)
                return render_template('signin_success.html', email=c.email, photo_url=c.picture_url)
    return render_template('signin.html', form=form)


@login_required
@app.route('/profile/<username>')
def user_profile(username):
    profile = fetch_candidate(username)
    return render_template('candidate_profile.html', profile=profile)


@login_required
@app.route('/beforetest/<username>')
def before_test(username):
    profile = fetch_candidate(username)
    return render_template('welcome_test.html', profile=profile)


@login_required
@app.route('/test/<test_no>')
def test(test_no):
    choices_dict = None
    question_list = session.get('test_list', None)
    if question_list is None:
        question_list = generate_question_list()
        session['test_list'] = question_list
    current_question = question_list[test_no]
    if current_question['multiple'] == 'Y':
        choices = current_question['choices'].split(',')
        for choice in choices:
            key = choice.split[0]
            value = choice.split[1]
            choices_dict[key] = value

    return render_template('question.html', question_list=question_list,
                           current_question=current_question, choices_dict=choices_dict,
                           test_no=test_no, total=app.config('NUM_OF_QUESTIONS'))


@login_required
@app.route('/user_agreement')
def user_agreement():
    user_agreement_content = LOREM_IPSUM
    return render_template('user_agreement.html', user_agreement_content=user_agreement_content)


@login_required
@app.route('/submit_answer/<test_no>')
def submit_answer(test_no):
    pass


def generate_question_list():
    '''
    Generate dict of questions according to application config
    '''

    result = None
    questions_lvl1 = generate_question_dict(1)
    questions_lvl2 = generate_question_dict(2)
    questions_lvl3 = generate_question_dict(3)

    result = questions_lvl1
    for question in questions_lvl2:
        result[k] = v
    for k, v in questions_lvl3:
        result[k] = v

    return result


def generate_question_dict(level):
    '''
    fetch questions from question table that have level 'level'
    '''
    sql = 'select * from question where level=?'
    parameter = [level]
    cur = query_db(sql, parameter)
    return cur


def valid_login(username, password):
    password = encrypt(password)
    sql = 'select * from candidates where email = ? and password = ?'

    if app.config['MODE'] == setting.PRODUCTION_MODE:
        sql += ' and verified = 1'

    parameters = [username, password]
    cur = g.db.execute(sql, parameters)
    if cur:
        return True
    return False


def fetch_candidate(username):
    sql = 'select * from candidates where email = ?'
    parameter = [username]
    candidate = query_db(sql, parameter, one=True)
    return candidate


def save_new_candidate(candidate, resume, photo):
    try:
        photo = uploaded_photos.save(photo)
        photo_url = uploaded_photos.url(photo)
        candidate.picture_url = photo_url

        resume = uploaded_resumes.save(resume)
        resume_url = uploaded_resumes.url(resume)
        candidate.resume_url = resume_url
    except UploadNotAllowed:
        flash(u'Upload fail. Upload is not allowed by OS.')
        return False
    else:
        try:
            sql = 'insert into candidates(name, address, email, password, phone, ' \
                'picture_url, resume_url, verification_code) values (?, ?, ?, ?, ?, ?, ?, ?)'
            values = [candidate.name, candidate.address, candidate.email, candidate.password, candidate.phone,
                      candidate.picture_url, candidate.resume_url, candidate.verification_code]
            g.db.execute(sql, values)
            g.db.commit()
        except DatabaseError:
            flash(DatabaseError.message)
            return False
        except DataError:
            flash(DataError.message)
            return False
        else:
            return True


# TODO : create generate random unique verification for email verification
def generate_verification_code():
    return '123456789'


# TODO : write email process
def send_email(email_address, verification_code):
    pass


# TODO : write hashing using MD5 or SH1
def encrypt(str):
    return str


def valid_signin(form):
    valid = True
    if not form.name.data:
        flash(u'name is required', 'warning')
        valid = False
    if not form.email.data:
        flash(u'email is required', 'warning')
        valid = False
    if not form.password.data or not len(form.password.data) >= 6:
        flash(u'password is required and must at least 6 chars')
        valid = False
    if not form.phone.data:
        flash(u'phone is required')
        valid = False
    if not request.files['photo']:
        flash(u'please provide your passport size photo in jpg format.')
        valid = False
    if not request.files['resume']:
        flash(u'please provide your resume in doc format.')
        valid = False

    return valid

