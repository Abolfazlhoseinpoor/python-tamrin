import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
try:
    with open("test_file.txt","w") as f:
        f.write("salam")
        print("neveshte shod!")
except PermissionError:
    print("masir file ro avaz kon!")
    