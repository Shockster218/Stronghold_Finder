# Table of Contents
1. [About](#About)
2. [Installation](#Installation)
3. [Usage](#Usage)
4. [FAQ](#FAQ)

# About
Slight modification of @AlanTheBenign's stronghold finder to read directly from the clipboard. Also reads nether coords. All cases are meant for speedrunning. Any questions or concerns about the algorithm of the stronghold finder should be directed toward https://github.com/AlantheBenign/Minecraft-Stronghold-Finder.

# Installation
1. Install the latest version of python at https://www.python.org/downloads/
> If you have the latest version of python, skip this step. It is recommended to have the latest version.

<p align="center">
  <img src="https://gyazo.com/47f08b324b40cdd114cde214f3a7682b.png"/>
</p>

2. Next would be to download/clone this repository. Whichever option you take, make sure to note the directory of where you download/clone the repository to; this will come in handy later.

<p align="center">
  <img src="https://gyazo.com/79b451ca2db9a2a70c61521b9def1325.png"/>
</p>

3. Next we have to install pip. If you have Python 2 >=2.7.9 or Python 3 >=3.4 versions, pip should already be installed on your machine. To double check, you can always open a command line/terminal on your PC and type "pip". If you see "'pip' is not recognized as an internal or external command, operable program or batch file," then it's not installed. You can follow installation instructions from https://pip.pypa.io/en/stable/installing/

<p align="center">
  <img src="https://gyazo.com/afc0aa08122b14a847c3b962bd274d84.png"/>
</p>

4. Now that we have pip, it's time to install the dependent modules for the project. We have to open up a command line (terminal if on mac). The easiest way to do this is to go to the folder where we downloaded/cloned the project before. 
> For windows: Once in the root folder, simply type "CMD" in the address bar near the top of the window, and it should open a command line in the correct directory.

> For mac: Make sure the terminal icon is on your icon dock "bottom of screen". Next, simply drag the root folder onto that icon and your done.

<p align="center">
  <img src="https://gyazo.com/fb4f97e7c13ddfd2b6b21f410df07f87.png"/>
</p>

5. We are almost done! Next, simply type in the command: pip install -r requirements.txt . This will install all necessary dependencies for the project.

<p align="center">
  <img src="https://gyazo.com/40a30295cc59494b5574225497fb5a6b.png"/>
</p>

6. Once that is done, we can finally run the script. Simply type in the command line: python main.py

<p align="center">
  <img src="https://gyazo.com/d2447518cec45eb69bc0b70bf3b33533.png"/>
</p>

### That's it! You are now successfully using my version of the stronghold finder that directly reads from the clipboard so you don't have to type coordinates yourself during a run! :)

<p align="center">
  <img src="https://gyazo.com/790176ba760e511b602ffd61f96edc74.png"/>
</p>

# Usage
Using the program is extremely simple. Simply have it running in the background (preferably on a second monitor) or anywhere in sight. When in-game, simply
hit the key combination F3 + C (in that order) to copy your cords to your clipboard. The program will then automatically detect what coords you are trying to save
(nether, first eye throw, second eye throw) and add them to the corresponding lines! Also, don't worry if you accidentally copied the wrong coords for whatever reason, there is a built in reset function in the program. Simply type "reset" into the command line or hit the tilde key "~" on your keyboard. Another handy feature of the program is to also detect when you are on a new run. This is on place so you don't have to reset the program everytime you start a new run. To close the program, simply type "exit" in the command line or close out of the console.

### Handy shortcuts
- F3 + C (in that order): Copy coordinates to clipboard for the program.
- Tilde Key "~" (next to 1 on keyboard): Reset the coordinates in the program.
- Typing "reset" in console: Reset the coordinates in the program.
- Type "exit" in console: Exits the program.

# FAQ 

### Why have an external program? Why not hook this directly into the client?
The reason this process is necessary is due to the guidelines and rules for speedrunning minecraft (found [here](https://docs.google.com/document/d/1A7NtP7LegD7SYjho54gQDSlJkYZlofndjw2COu00yMU/edit) ). You are not allowed to modify or tamper with the code of the client in any shape or form.

### Is this allowed for speedrunning?
Directly quoted from the speedrunning discord

> Q: Is a stronghold finder allowed?

>A: Yes, but no. Any stronghold/structure finder website that asks for seed input is not allowed. You are not allowed to use or see the seed of the world you’re in. However, stronghold calculators that take 2 angles as an input and locates the stronghold using math are allowed.

Since this program does not need nor ask for your seed, it is completely legal and follows speedrun guidelines.

### More to come in due time.