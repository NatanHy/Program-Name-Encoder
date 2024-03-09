import os
import base64

s = ""

for file in os.listdir("names_test"):
    decoded = bytes.decode(base64.b64decode(bytes(file, "utf-8")))
    s += decoded

exec(s)