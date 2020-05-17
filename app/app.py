from sql_module import DB_SESSION
from example_module import questionnaire
from settings import LINKS


if __name__ == '__main__':
    try:
        questionnaire(LINKS)
    except:
        pass
    finally:
        DB_SESSION.close()
        DB_SESSION.bind.dispose()
