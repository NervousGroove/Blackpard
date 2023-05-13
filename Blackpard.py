import builtins
import os
import alert as alert
from tkinter import *
import logging
from tkinter import messagebox

root = Tk()
root.title("Blackpard Program")
root.geometry("300x200")

label = Label(root, text="Blackpard v1.0.2")
label.pack()

root.mainloop()


def vlu(name, value):
    builtins.__dict__[name] = value


currentMainFile = ""
with open("package.spike", "r") as f:
    for line in f:
        if "inf_Main" in line:
            currentMainFile = line.split('"')[1]
            break
vlu("currentMainFile", currentMainFile)

with open(currentMainFile, "r") as f:
    for line in f:
        if "action" in line:
            name = line.split()[1].split("(")[0]
            code = ""
            for line in f:
                if "}" in line:
                    break
                code += line
            exec(f"def {name}():\n{code}")

with open(currentMainFile, "r") as f:
    for line in f:
        if "sta" in line:
            name = line.split()[1].split("(")[1].split(",")[0].replace('"', '')
            value = line.split()[1].split("(")[1].split(",")[1].replace('"', '')
            exec(f"{name.upper()} = '{value}'")


def play_audio(audio_name):
    with open(currentMainFile, "r") as f:
        for line in f:
            if "BPDPlayAudio()" in line:
                audio_directory = ""
                audio_name_bpd = ""
                for line in f:
                    if "vlu(" in line:
                        if "audioDirectory" in line:
                            audio_directory = line.split('"')[3]
                        elif "audioName" in line:
                            audio_name_bpd = line.split('"')[3]
                    elif ")" in line:
                        break
                if audio_name_bpd == audio_name:
                    os.system(f"afplay {audio_directory}")
                    break


def stop_audio(audio_name):
    os.system(f"killall afplay -v {audio_name}")


def BPDMath():
    with open(currentMainFile, "r") as f:
        for line in f:
            if "BPDMath()" in line:
                operations = []
                for line in f:
                    if ")" in line:
                        operations.append(line)
                    elif "}" in line:
                        break
                results = []
                for operation in operations:
                    operation = operation.replace("math", "")
                    operation = operation.replace("(", "")
                    operation = operation.replace(")", "")
                    operation = operation.split(".")
                    if operation[0] == "add":
                        result = operation[1].split(" + ")
                        result = int(result[0]) + int(result[1])
                        results.append(f"{operation[1]} = {result}")
                    elif operation[0] == "split":
                        result = operation[1].split(" / ")
                        result = int(result[0]) / int(result[1])
                        results.append(f"{operation[1]} = {result}")
                    elif operation[0] == "sub":
                        result = operation[1].split(" - ")
                        result = int(result[0]) - int(result[1])
                        results.append(f"{operation[1]} = {result}")
                    elif operation[0] == "multi":
                        result = operation[1].split(" * ")
                        result = int(result[0]) * int(result[1])
                        results.append(f"{operation[1]} = {result}")
                alert_text = "Operations Results (Blackpard Technology):\n"
                for result in results:
                    alert_text += f"{result};\n"
                messagebox.showinfo("Alert", alert_text)


def execute_onstart_functions():
    with open("onstart.cfg", "r") as f:
        functions = f.read().split(",")
        for function in functions:
            exec(function.strip())


execute_onstart_functions()
