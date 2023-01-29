import os

print(os.path.exists("files/data/AAPL.csv"))
print(os.path.exists("files/data/rtyrty.csv"))

print(os.path.abspath("files/data/AAPL.csv"))

print(os.path.sep)

base_dir = "files/data"
new_dir = "test1"
new_file = "sun.txt"

full_path = os.path.join(base_dir, new_dir, new_file)
print(full_path)

if not os.path.exists(os.path.dirname(full_path)):
    os.makedirs(os.path.dirname(full_path))

with open(full_path, 'w') as f:
    f.write("HELLO\n")

preffix, ext = os.path.splitext("files/data/AAPL.csv")
print(preffix, ext)

print(os.path.getsize("files/data/AAPL.csv"))