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
  <img src="img/installation_step1.png" width = 720/>
</p>

2. Next would be to download/clone this repository. Whichever option you take, make sure to note the directory of where you download/clone the repository to; this will come in handy later.

<p align="center">
  <img src="img/installation_step2.png" width = 720/>
</p>

3. Next we have to install pip. If you have Python 2 >=2.7.9 or Python 3 >=3.4 versions, pip should already be installed on your machine. To double check, you can always open a command line/terminal on your PC and type "pip". If you see "'pip' is not recognized as an internal or external command, operable program or batch file," then it's not installed. You can follow installation instructions from https://pip.pypa.io/en/stable/installing/

<p align="center">
  <img src="img/installation_step3.png" width = 720/>
</p>

4. Now that we have pip, it's time to install the dependent modules for the project. We have to open up a command line (terminal if on mac). The easiest way to do this is to go to the folder where we downloaded/cloned the project before. 
> For windows: Once in the root folder, simply type "CMD" in the address bar near the top of the window, and it should open a command line in the correct directory.

> For mac: Make sure the terminal icon is on your icon dock "bottom of screen". Next, simply drag the root folder onto that icon and your done.

<p align="center">
  <img src="img/installation_step4.png" width = 720/>
</p>

5. We are almost done! Next, simply type in the command: pip install -r requirements.txt . This will install all necessary dependencies for the project.

<p align="center">
  <img src="img/installation_step5.png" width = 720/>
</p>

6. Once that is done, we can finally run the script. Simply type in the command line: python main.py

<p align="center">
  <img src="img/installation_step6.png" width = 720/>
</p>

### That's it! You are now successfully using my version of the stronghold finder that directly reads from the clipboard so you don't have to type coordinates yourself during a run! :)

<p align="center">
  <img src="img/program.png" width = 720/>
</p>

# Usage
Using the program is extremely simple, follow these steps in-game:

#### For nether
Simply copy the coordinates (refer to handy shortcuts below) and that's it!

#### For stronghold.
1. Make sure you are in an open area with a lot of room. Throw the eye of ender.
2. Make sure the eye of ender is at the end of it's animation. It will fly toward a specific direction, then go straight up in the air a bit and float. This is what you are looking for.
3. Make sure you are looking directly at the eye. Then, copy the coordinates (refer to handy shortcuts below).
4. Go to the suggested 2nd throw coordinates. Repeat steps 1-3.
5. You should have the stronghold coordinates! Be careful though, the coordinates may not be 100% accurate as slight variations from user input could offput the calculations by a few blocks. Make sure to listen for silverfish and dig around a bit! A third eye may be thrown to make sure of the stronghold location.

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

### How accurate is the stronghold finder?
This stronghold finding algorithm is a rather reliable tool. The main issue here is user input variance. If you aren't looking directly at the eye, calculations could be off as it is crucial to get the proper angle. Out of many tests I have done (around 50 or so), the furthest I have been from a stronghold is about 10 blocks. Keep this in mind when using the tool!

### More to come in due time.