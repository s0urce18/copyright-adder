from datetime import datetime
today = datetime.today().strftime('%Y-%m-%d')
now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

file_name = input("Enter file name: ")
file = open(file_name, 'r')
file_lines = file.readlines()

try:
    copyright_file = open('COPYRIGHT.txt', "r")
except:
    copyright_file_name = input("Enter copyright file name: ")
    copyright_file = open(copyright_file_name)

text = copyright_file.read()
res = "\n" if text[-1] != '\n' else ""
i = 0
while i < len(text):
    if text[i] == "{":
        answ = input(text[i + 1: text[i:].find("}") + i] + ": ")
        if answ == "today":
            res += today
        elif answ == "now":
            res += now
        else:
            res += answ
        i = text[i:].find("}") + i + 1
    else:
        res += text[i]
        i += 1
res += "\n"

if text.split("\n")[0] + '\n' in file_lines and (text.split("\n")[-1] in file_lines or text.split("\n")[0] + '\n' in file_lines[file_lines.index(text.split("\n")[0] + '\n'):]):
    file = open(file_name, 'w')
    line = ""
    for i in range(0, file_lines.index(text.split("\n")[0] + '\n')):
        line = file_lines[i]
        file.write(line)
    if line[-1] == '\n' and res[-1] == '\n':
        res = res[1:]
    file.write(res)
    for i in range(file_lines.index(text.split("\n")[0] + '\n') + text.count("\n") + 1, len(file_lines)):
        file.write(file_lines[i])
else:
    file = open(file_name, 'a')
    file.write(res)

file.close()
copyright_file.close()