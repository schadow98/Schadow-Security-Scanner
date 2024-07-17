import os
import sys


fileDir = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.abspath(os.path.join(fileDir, "..", ".."))
os.environ["PROJECT_PATH"] = PROJECT_PATH

print(sys.path)

SOURCE_PATH = os.path.join(
    PROJECT_PATH, "src"
)
sys.path.append(SOURCE_PATH)

TEST_PATH = os.path.join(
    PROJECT_PATH, "tests"
)
sys.path.append(TEST_PATH)