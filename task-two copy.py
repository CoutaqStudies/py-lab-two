import os
import hashlib


path = "./"
md5s = dict()
for key in os.listdir(path):
    with open(key, "rb") as f:
        md5s[key] = hashlib.md5(f.read()).hexdigest()

desired_keys = []
vals = some_dict.values()
for key, value in some_dict.items():
   if vals.count(value) > 1:
        desired_keys.append(key)

print(desired_keys)