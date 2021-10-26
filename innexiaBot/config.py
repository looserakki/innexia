from innexiaBot.sample_config import Config

class Development(Config):
    OWNER_ID = 2007701745  # your telegram ID
    OWNER_USERNAME = "piroxpower"  # your telegram username
    TOKEN = "1728730929:AAHpuAEOph7_QVA3kswuU2xcjYMuSwhZmu8"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://oknsunpy:Gq78-oFzocoxGa_v_b628xb-5c8jZJOc@batyr.db.elephantsql.com/oknsunpy'  # sample db credentials
    MESSAGE_DUMP = '-1001504294786' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    DEV_USERS = "1669178360 1920106383 2007701745 1956381927 936481432 1756265729 1747260012 1753777248 1975644370"
    DONATION_LINK = "https://t.me/piroXpower"
    EVENT_LOGS = "-1001504294786"
    REDIS_URL = "redis-18987.c16.us-east-1-2.ec2.cloud.redislabs.com:18987"
    STRICT_GBAN = "True"
    BOT_ID = "1728730929"
    API_ID = "3546656"
    API_HASH = "48b79c54af688f05c350161bddea414c"
    SUPPORT_CHAT ="DECODESUPPORT"
    MONGO_DB_URI = "mongodb+srv://Evil:NRb0LXgSBdao6tHB@cluster0.phtr6.mongodb.net/EvilretryWrites=true&w=majority"
    SUDO_USERS = [1669178360, , 2007701745, 1956381927, 936481432, 1756265729, 1747260012, 1753777248, 1975644370]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
