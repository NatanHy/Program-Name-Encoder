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
    return base64.b64encode(bytes(s, "utf-8"))

def make_names(lines : list[str]) -> list[bytes] :
    names = list(map(get_encoded, lines))

    return names

def get_tags(length):
    d = {}
    for i in range(length):
        s = str(i)
        name = str(base64.b64encode(bytes("#" + s, "utf-8")))
        d[name] = s

    clear_dir("sorting")

    for name in d:
        open("sorting/" + str(name), "a").close()

    l = []

    for name in os.listdir("sorting"):
        l.append(d[name])

    clear_dir("sorting")

    # for elm in l:
    #     print(elm, str(base64.b64encode(bytes("#" + elm, "utf-8"))))

    return l

def read_code(filename):
    lines = []

    with open(filename, "r") as f:
        file_lines = list(f.readlines())

        tags = get_tags(len(file_lines))

        for i, line in enumerate(file_lines):
            lines.append(f"#{tags[i]}\n{line}".strip())

    return lines

def clear_dir(dir_name):
    for filename in os.listdir(dir_name):
        file_path = os.path.join(dir_name, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def make_files(names):
    clear_dir("names_test")

    for name in names:
        open("names_test/" + str(name)[2:-1], "a").close()

lines = read_code("code.txt")

for line in lines:
    print(line + " -> " + str(get_encoded(line)))

names = make_names(lines)

make_files(names)