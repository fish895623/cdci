import os
from subprocess import PIPE, Popen


class Git:
    def __init__(
        self,
        command: str,
        git_bin_loc: str = "",
    ):
        """
        Arguments
            command: str
                list of command

            git_bin_loc: str
                git file location
        """
        self.command = command
        self.git_bin_loc = git_bin_loc
        if git_bin_loc == "":
            pass
        else:
            os.environ["PATH"] = git_bin_loc + ":" + os.environ["PATH"]
        pass

    def run(self):
        popen = Popen(
            self.command,
            stdout=PIPE,
            stderr=PIPE,
            shell=True,
        )
        (stdout, stderr) = popen.communicate()

        returncode = popen.returncode

        stdout = stdout.decode(encoding="utf-8")

        return stdout, stderr, returncode