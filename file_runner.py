import os
import base64

s = ""

for file in os.listdir("names_test"):
    s += bytes.decode(base64.b16decode(bytes(file, "utf-8")))

print(s)

exec(s)