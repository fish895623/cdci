from subprocess import PIPE, Popen


class git:
    def __init__(
        self,
        command: str,
        exec_loc: str,
    ):
        """
        command: str
            list of command
        exec_loc: str
            git file location
        """
        self.command = command
        pass

    def run(self):
        popen = Popen(
            self.command,
            stdout=PIPE,
            stderr=PIPE,
            shell=True,
        )
        (stdout, stderr) = popen.communicate()

        return stdout, stderr