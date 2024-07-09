import platform
import dotenv


# optional skript to load and set environment variables
# only needed for the synk api
if platform.system() == "Windows":
    dotenv.load_dotenv(".env")