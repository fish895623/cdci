import os

from modules.git import Git

g = Git(command="echo abcd")
a1, b1, a2 = g.run()

print(a2)
loc = "/a"
os.environ["PATH"] = loc + ":" + os.environ["PATH"]

print(os.environ["PATH"])
