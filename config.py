# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("25131273"))
    API_HASH = os.environ.get("6b2715180a62e8c4fbcdde7d8b88787e")
    BOT_TOKEN = os.environ.get("7766243249:AAHdGrwbIQXuiNbq1cYY871jmAa80mDVaSc")
    LOGS_CHANNEL = int(os.environ.get("-1002357190696"))
    BOT_OWNER = int(os.environ.get("7831829394"))
    MONGODB_URL = os.environ.get("mongodb+srv://manu:<Sandeepa12>@cluster0.ez99o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    GOFILE_TOKEN = os.environ.get("dLfHTrZgAoogU0IGvP6asn0DsD9Yfv3l")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
