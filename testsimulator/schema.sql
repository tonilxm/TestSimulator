drop table if exists candidates;
create table candidates (
  candidate_id integer primary key autoincrement,
  name string not null,
  address string not null,
  email string not null,
  phone string not null,
  password string not null,
  picture_url string not null, /* system will create url for uploaded picture for user to download */
  resume_url string not null, /* system will create url for uploaded resume for user to download document */
  verification_code string not null, /* verification code is generated when user register and
                                        then system send it to user email address */
  test_id string, /* test id is generated once user is veirfied using email and then system will display it
                    on the screen page */
  verified string, /* verified is updated to 'Y' once user veriefy his registration from email sent by
                      system on user sucessfully register himself */
  created_on datetime, /* record creation/registration datetime */
  start_on datetime, /* datetime when user start the test */
  finished_on datetime /* datetime when user finished the test */
);
drop table if exists question;
create table question (
  question_id integer primary key autoincrement,
  level integer not null, /* level 1 = easy, level 2 = medium and level 3 = hard */
  content string not null, /* the actual question */
  multiple string, /* multiple question flag, 'Y' for multiple choice question and 'N' for essay */
  choices string /* if multiple = Y then choice will be contains pairs of choice and answer
                    A:choice1,B:choice2,C:choice3,..  */
);

drop table  if exists candidate_test;
create table candidate_test (
  candidate_id integer,
  test_id integer,
  question_id integer, /* foreign key to question table */
  multiple_asnwer string, /* example : A:choice */
  essay_answer string /* answer for essay type of question */
);