class Config(object):
    # Определяет, включен ли режим отладки
    # В случае если включен, flask будет показывать
    # подробную отладочную информацию. Если выключен -
    # - 500 ошибку без какой либо дополнительной информации.
    DEBUG = True
    # Включение защиты против "Cross-site Request Forgery (CSRF)"
    CSRF_ENABLED = True
    # Случайный ключ, которые будет исползоваться для подписи
    # данных, например cookies.
    SECRET_KEY = '12345'
    # URI используемая для подключения к базе данных
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True