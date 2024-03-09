import base64
import os, shutil

MAX_NAME_LENGTH = 20

def add_tags(code):
    lines = code.split("\n")
    res = ""

    for i, line in enumerate(lines):
        res += f"#{i}\n"
        res += line + "\n"

    return res

def get_encoded(s : str) -> bytes:
    s = s.strip()
    return base64.b16encode(bytes(s, "utf-8"))

def make_names(lines : list[str]) -> list[bytes] :
    names = list(map(get_encoded, lines))

    return names[1:]

def get_padded_index(num, digits):
    padding = "0" * (digits - len(str(num)))

    return padding + str(num)

def read_code(filename):
    lines = []

    with open(filename, "r") as f:
        for i, line in enumerate(f.readlines()):
            lines.append(f"#{get_padded_index(i, 3)}\n{line}")

    return lines

def make_files(names):
    for filename in os.listdir("names_test"):
        file_path = os.path.join("names_test", filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    for name in names:
        print(str(name)[2:-1])
        open("names_test/" + str(name)[2:-1], "a").close()

lines = read_code("code.txt")

names = make_names(lines)

make_files(names)