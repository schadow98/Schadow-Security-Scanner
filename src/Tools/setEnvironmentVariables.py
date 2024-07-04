import platform
import dotenv

if platform.system() == "Windows":
    dotenv.load_dotenv(".env")