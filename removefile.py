import os
if os.path.exists("alexo.txt"):
    os.remove("alexo.txt")
else:
    print("The file does not exist")
