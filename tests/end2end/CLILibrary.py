import platform
import subprocess
import os
from robot.api.logger import warn, info, debug, trace, console
from robot.libraries.BuiltIn import BuiltIn


class CLILibrary:

    def __init__(self) -> None:
        if platform.system() == "Windows":
            self.exe_name = "SecurityScannerSchadow.exe"
        else:
            self.exe_name = "SecurityScannerSchadow"
        self.exe_path = os.path.join(".", "dist", self.exe_name)


    def run_command(self, command):
        try:
            result = subprocess.run(command, check=True, text=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            info(result.stdout)
        except subprocess.CalledProcessError as e:
            warn(f"Command '{command}' failed with return code {e.returncode}")
            warn(f"Error output: {e.stderr}")
            raise RuntimeError(f"Command '{command}' failed to execute properly") from e

    def build_executable(self):
        if not os.path.exists(self.exe_path):
            info("build exe")
            cmd = 'pyinstaller --onefile --add-data "src;." --distpath ./dist --name SecurityScannerSchadow ./src/SecurityScanner.py'
            self.run_command(cmd)
        else:
            info("build already exists")


    def execute(self, args):
        # logdir
        self.log_dir = f"./logs/{BuiltIn().get_variable_value('${TEST NAME}')}".replace(" ", "_")
        if not os.path.exists(self.exe_path):
            os.mkdir(self.log_dir)
        cmd = f"{self.exe_path} "
        info("logdir " + self.log_dir)
        cmd += f"-l {self.log_dir} "
        cmd += args
        info(cmd)
        
        self.run_command(cmd)
