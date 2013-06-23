class Candidate():
    def __init__(self, kwargs):
        self._dict = kwargs

    # name attribute
    @property
    def name(self):
        return self._dict.get('name', None)

    @name.setter
    def name(self, name):
        self._dict['name'] = name

    @name.deleter
    def name(self):
        del self._dict['name']

    # address atrribute
    @property
    def address(self):
        return self._dict.get('address', None)

    @address.setter
    def address(self, address):
        self._dict['address'] = address

    @address.deleter
    def address(self):
        del self._dict['address']

    # email attribute
    @property
    def email(self):
        return self._dict.get('email', None)

    @email.setter
    def email(self, email):
        self._dict['email'] = email

    @email.deleter
    def email(self):
        del self._dict['email']

    # phone attribute
    @property
    def phone(self):
        return self._dict.get('phone', None)

    @phone.setter
    def phone(self, phone):
        self._dict['phone'] = phone

    @phone.deleter
    def phone(self):
        del self._dict['phone']

    # password attribute
    @property
    def password(self):
        return self._dict.get('password', None)

    @password.setter
    def password(self, password):
        self._dict['password'] = password

    @password.deleter
    def password(self):
        del self._dict['password']

    # picture_url attribute
    @property
    def picture_url(self):
        return self._dict.get('picture_url', None)

    @picture_url.setter
    def picture_url(self, picture_url):
        self._dict['picture_url'] = picture_url

    @picture_url.deleter
    def picture_url(self):
        del self._dict['picture_url']

    # resume_url attribute
    @property
    def resume_url(self):
        return self._dict.get('resume_url', None)

    @resume_url.setter
    def resume_url(self, resume_url):
        self._dict['resume_url'] = resume_url

    @resume_url.deleter
    def resume_url(self):
        del self._dict['resume_url']

    # verification_code attribute
    @property
    def verification_code(self):
        return self._dict.get('verification_code', None)

    @verification_code.setter
    def verification_code(self, verification_code):
        self._dict['verification_code'] = verification_code

    @verification_code.deleter
    def verification_code(self):
        del self._dict['verification_code']

    # verified attribute
    @property
    def verified(self):
        return self._dict.get('verified', None)

    @verified.setter
    def verified(self, verified):
        self._dict['verified'] = verified

    @verified.deleter
    def verified(self):
        del self._dict['verified']

    # tested_on attribute
    @property
    def tested_on(self):
        return self._dict.get('tested_on', None)

    @tested_on.setter
    def tested_on(self, tested_on):
        self._dict['tested_on'] = tested_on

    @tested_on.deleter
    def tested_on(self):
        del self._dict['tested_on']

    # finished_on attribute
    @property
    def finished_on(self):
        return self._dict.get('finished_on', None)

    @finished_on.setter
    def finished_on(self, finished_on):
        self._dict['finished_on'] = finished_on

    @finished_on.deleter
    def finished_on(self):
        del self._dict['finished_on']


class Question():
    def __init__(self, kwargs):
        self._dict = kwargs

    @property
    def question_id(self):
        return self._dict['question_id']

    @question_id.setter
    def question_id(self, value):
        self._dict['question_id'] = value

    @question_id.deleter
    def question_id(self):
        del self._dict['question_id']

    @property
    def level(self):
        return self._dict['level']

    @level.setter
    def level(self, value):
        self._dict['level'] = value

    @level.deleter
    def level(self):
        del self._dict['level']

    @property
    def multiple(self):
        return self._dict['multiple']

    @multiple.setter
    def multiple(self, value):
        self._dict['multiple'] = value

    @multiple.deleter
    def multiple(self):
        del self._dict['multiple']

    @property
    def essay(self):
        return self._dict['essay']

    @essay.setter
    def essay(self, value):
        self._dict['essay'] = value

    @essay.deleter
    def essay(self):
        del self._dict['essay']

    @property
    def content(self):
        return self._dict['content']

    @content.setter
    def content(self, value):
        self._dict['content'] = value

    @content.deleter
    def content(self):
        del self._dict['content']

    @property
    def choices(self):
        return self._dict['choices']

    @choices.setter
    def choices(self, value):
        self._dict['choices'] = value

    @choices.deleter
    def choices(self):
        del self._dict['choices']


class CandidateTest():
    def __init__(self, kwargs):
        self._dict = kwargs

    @property
    def candidate_id(self):
        return self._dict['question_id']

    @candidate_id.setter
    def candidate_id(self, value):
        self._dict['candidate_id'] = value

    @candidate_id.deleter
    def candidate_id(self):
        del self._dict['candidate_id']

    @property
    def test_id(self):
        return self._dict['test_id']

    @test_id.setter
    def test_id(self, value):
        self._dict['test_id'] = value

    @test_id.deleter
    def test_id(self):
        del self._dict['test_id']

    @property
    def question_id(self):
        return self._dict['question_id']

    @question_id.setter
    def question_id(self, value):
        self._dict['question_id'] = value

    @question_id.deleter
    def question_id(self):
        del self._dict['question_id']

    @property
    def multiple_answer(self):
        return self._dict['multiple_answer']

    @multiple_answer.setter
    def multiple_answer(self, value):
        self._dict['multiple_answer'] = value

    @multiple_answer.deleter
    def multiple_answer(self):
        del self._dict['multiple_answer']

    @property
    def essay_answer(self):
        return self._dict['essay_answer']

    @essay_answer.setter
    def essay_answer(self, value):
        self._dict['essay_answer'] = value

    @essay_answer.deleter
    def essay_answer(self):
        del self._dict['essay_answer']