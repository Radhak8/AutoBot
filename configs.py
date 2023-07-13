from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", " "))
    API_HASH = getenv("API_HASH", " ")
    BOT_TOKEN = getenv("BOT_TOKEN", " ")
    FSUB = getenv("FSUB", " ")
    CHID = int(getenv("CHID", "  "))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Advika:advika@cluster0.tvgwdkv.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
