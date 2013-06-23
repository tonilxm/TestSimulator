from testsimulator.constants import DEVELOPMENT_MODE, PRODUCTION_MODE


class baseconfig(object):
    NUM_OF_QUESTIONS = 10
    NUM_OF_LEV1_QUESTIONS = 5
    NUM_OF_LEV2_QUESTIONS = 3
    NUM_OF_LEV2_QUESTIONS = 2

class devconfig(baseconfig):
    MODE = DEVELOPMENT_MODE
    DATABASE = '/Users/toni/PycharmProjects/TestSimulator/db/test_simulator.db'
    DEBUG = True
    SECRET_KEY = 'please replace me'
    USERNAME = 'admin'
    PASSWORD = 'default'
    UPLOADED_PHOTOS_DEST = '/Users/toni/testsimulator/uploaded_pictures'
    UPLOADED_ATTACHMENTS_DEST = '/Users/toni/testsimulator/uploaded_resumes'

class prodconfig(baseconfig):
    MODE = PRODUCTION_MODE
    DATABASE = '/Users/toni/PycharmProjects/TestSimulator/db/test_simulator.db'
    DEBUG = False
    SECRET_KEY = 'please replace me'
    USERNAME = 'admin'
    PASSWORD = 'default'
    UPLOADED_PHOTOS_DEST = '/Users/toni/testsimulator/uploaded_pictures'
    UPLOADED_ATTACHMENTS_DEST = '/Users/toni/testsimulator/uploaded_resumes'
