import builtins
import os

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
