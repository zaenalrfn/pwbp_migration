import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HOST = str(os.environ.get("DB_HOST", "localhost"))
    DATABASE = str(os.environ.get("DB_DATABASE", "pwbp_week9"))
    USERNAME = str(os.environ.get("DB_USERNAME", "root"))
    PASSWORD = str(os.environ.get("DB_PASSWORD", ""))

    # Gunakan format string untuk lebih mudah dibaca
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
