import os
import platform
#platform ---> OS information
print(platform.system())  # os name
print(platform.release())  # os version
print(platform.machine())  # CPU type
print(platform.node())  # machine's network name
print(platform.python_version())


#os ---> directory opeartion
# print(os.getcwd())                # Current dir
# os.chdir("..")             # Change dir
# print(os.getcwd())                # Current dir
# os.mkdir("new-dir-saif")         # Make directory
# os.rmdir("new-dir-saif")         # Remove directory
# os.remove("TestFile2.bin")       # Delete file
# os.rename("b.txt", "TestFile3.txt")         # Rename file/dir
print(os.listdir("."))          # List contents

