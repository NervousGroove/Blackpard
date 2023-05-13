![SpellSpike](https://img.shields.io/badge/Programming%20Language-SpellSpike-yellow)
![Wesley Y](https://img.shields.io/badge/Created%20by%20One%20Man-Started%20when%20I%20was%2014%20years%20old-blue)
![Not open source](https://img.shields.io/badge/A%20100%25%20Brazilian%20language-But%20with%20English%20grammar%20and%20syntax-white)

# <img src="https://raw.githubusercontent.com/NervousGroove/Blackpard/main/Blackpard_45px.png" alt="Galath" width="20"/> Blackpard
Blackpard is a high-level, cross-platform programming language developed to bring a new language concept to the market. Blackpard was developed to compete with modern high-level languages such as Python. In addition to being extremely powerful, broad and lightweight, Blackpard is extremely easy to read, code and interpret.

# ☕ Easy and Light
Programming doesn't have to be difficult. That's why Blackpard makes everything simple and better, creating a new language concept. Blackpard is modern, fast, light, safe and extremely easy, perfect for everything.

# 💸 Donate today! Help this project stay alive
You can help/support this project/repository and help SwankyNoob maintain this and all other amazing projects of our developer, with any amount of ETH! The existence of this project depends on you, donate today! No matter the amount, every donation helps a lot! OUR ADDRESS TO RECEIVE ETHEREUM (METAMASK):
```text
0x17352A0e682dAFa233C83f15C902C86Ba7EB5B65
```

#  ⚖️ License
SpellSpike is under the CC-NC-ND license. You must follow the standards of this license. Remember that this license is valid only for SpellSpike source code, you can feel free to distribute your programs created with SpellSpike, but you cannot distribute or copy the source code of the SpellSpike language.

# 🥤 Ideal for everything and everyone
Blackpard is broad, and can be used for everything, and by everyone. Blackpard's tight-knit and active community makes everything easy, and makes it easy for beginners.

# 📦 How to Install
To install Blackpard is easy. Just go to "https://shre.ink/blackpard-dl" and wait for the .ZIP download and delete all files except "Blackpard.py" and "package.spike". After that you must configure the "package.spike" file by defining the name and author of the app, and the most important: define the main file of your project. You must edit the "inf_Main" variable in the "package.spike" file and set its value to the name of the main (.bpd) file of your project. After that you can start editing. YOU DO NOT, AND FURTHERMORE, CANNOT EDIT THE "Blackpard.py" file, because editing this file will prevent you from distributing your app because of the CC-NC-ND 4.0 license, and your app may stop working. EDIT ONLY THE ".bpd" FILE(S) OF YOUR PROJECT AND THE "package.spike" FILE, YOU CANNOT EDIT/MODIFY THE BLACKPARD SOURCE CODE, READ THE LICENSE. 

# 🚀 Documentation

## ⚡ How to create variables
Unlike other known languages, in Blackpard you can define variables using only the keyword "vlu" (short for "value"). It is quite simple to create variables in our language, just use the keyword, then the variable name and then the value. Here is an example:
```python
vlu("HelloVar", "Hello World")
```
In this example, a variable called "HelloVar" was created with the value "Hello Word". Always, the first word in quotes means the name of the variable and the second word in quotes, means the value.

## ⚡ How to create functions
To create functions in Blackpard is quick and easy. You must use the keyword "action". For example:
```python
action Test() {
print("Hello")
}
```

## ⚡ Creating constant variables (Static)
In most languages, there are constant variables. They have a fixed value and do not change. But we find this name a bit meaningless and we don't think the name "constant" defines a variable that doesn't change its value, so we changed the name to "static". This is why in Blackpard constant variables are created with the keyword "sta" (short for "static"). Here is an example:
```python
sta("HelloVar", "Hello World")
```

## ⚡ Language Patterns
To make it easier and leave a striking syntax, which you will realize by the time you are part of the Blackpard language, our language has patterns. For example, all commands start with the keyword BDP (Short for Blackpard) and, the name of every command is referring to its own purpose.

## ⚡ Playing audios
To play audios in Blackpard you only need a little code, which takes the necessary information to play a certain audio. You should just call the function "BPDPlayAudio" and set the audio directory. For example:
```python
BPDPlayAudio()
vlu("audioDirectory", "audio.mp3")
vlu("audioName", "audioTest")
```

## ⚡ How to stop audios
In the previous topic you learned how to play audio, now let's do it the other way around. Notice that in the example code, you define the name of the audio, and this serves a purpose. With the name of the audio you can stop that specific audio, for example:
```python
BDPStopAudio()
vlu("stopThis", "audioTest")
```

## ⚡ Creating comments
You can create a code, and after days or months, come back to edit that code, or another common situation, you create a code for other people to edit together. To make it easier for you or others to understand your code, most languages provide comments. On the web (in social networks) we use the "@" to make quotes, so we thought that this character would make a lot more sense than the characters chosen to create comments in other languages. In Blackpard you can create comments using the "@" character. Here is an example:
```text
@ Hello World
```

## ⚡ Manipulating the GUI
You can add elements to your app, after all everything is made up of elements. You can add inputs, buttons, images, text and more!
Here is an example:
```python
@ A button
BPDCreateButton()
mybtn.prop(text = "Click Me", class = "test", event = "func", group = "main")
@ Creating an input
BPDCreateInput()
myinput.prop(text = "Type anything", class = "test", group = "main")
@ Creating Texts
BPDCreateText()
mytext.prop(text = "Hello World", class = "test", group = "main")
```

## ⚡ Editing Styles
Note that when creating elements, you can add the "class" property. This property binds a certain object as part of the style. For example, in the previous topic, the example shows a button with the "class" set to "test". For editing styles, Blackpard uses the "uilang" language, which is very similar to CSS.

## ⚡ Sending mail
In other languages, to send automated emails you need libraries, in Blackpard, this is a native tool. It's simple, just call the "BPDSendEmail" function and set the destination, subject and content. Here is an example:
```python
BPDSendEmail()
myemail.prop()
```

## ⚡ Setting the Window Title
To customize your window title is easy, follow the example:
```python
BPDSetWindowTitle()
vlu("windowTitle", "Test")
```

## ⚡ Manipulating Files
Manipulating files doesn't have to be difficult, so Blackpard simplifies this process. Here's an example:
```python
@ How to Open Files
BPDOpenFile()
vlu("fileDir", "Test.exe")
How to Read Files
BPDReadFile()
myfile.read(setContentTo = "myVar", fileDir = "main.txt")
```

## ⚡ Predefined Data
Predefined data is nothing more than privileged information about the user's hardware and software, such as: Date and Time, Hardware IDs (CPU and GPU), Average Connection Speed, and more. You can get this information easily, from variables that are updated every second, making data efficiently available, See:

## ⚡ Conditions
Conditions are everything. Your app revolves around conditions, they are simple but can help you a lot. In Blackpard, you can create the famous conditions, using "is" and "else". Here are some examples:
```python
is (fileDir = "test.exe") {
print("Is test.exe")
}

else {
print("is another")
}
```
You can also check if it is more or less, for example:
```python
is (num1 > 5) {
print("+ 5")
}

else {
print("- 5")
}
```
Or another example:
```python
is (num1 < 5) {
print("- 5")
}

else {
print("+ 5")
}
```

## ⚡ Math
Well fortunately (or unfortunately for many), math is everywhere, including programming. At Blackpard, everything is easy, including math. Here are examples:
```python
@ Addition
BPDMath()
add.math(5 + 5)
Division
BPDMath()
split.math(100 / 10)
@ Subtraction
sub.math(10 - 5)
@ Multiplication
multi.math(5 * 5)
```

## ⚡ Opening URLs
You can open URLs in the user's default browser. See:
```python
BPDOpenURL()
vlu("setURL", "https://myurl.com")
```

---> ALL RIGHTS RESERVED, SWANKYNOOB INC. | ESTABLISHED AND MANAGED BY Wesley YAN Soares Brehmer

[This repository/project/program and all others from SwankyNoob apply to the developer's terms.](https://github.com/NervousGroove/SwankyNoob/blob/main/TERMS)

<img src="https://raw.githubusercontent.com/NervousGroove/Blackpard/main/Blackpard_45px.png" alt="Galath" width="45"/>
