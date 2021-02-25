import os

from modules.git import Git

g = Git(
    command="echo abcd",
    git_bin_loc="/usr/bin",
)
for i in g.run():
    print(i)

print(os.environ["PATH"])
