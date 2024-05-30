📖 Math Journal 📖
===================

The following provides a very lightweight way to keep a math journal. Within one keystroke you can start typing, and a file for that day will be automatically created. In another keystroke you can view a compiled version of your whole math journal. The philosophy behind this is that you should have a home to jot down thoughts instantly, and the tech behind it should enable you to do it without navigating directories, creating files, including them in a master file, etc. --- all of that is handled in the back end.
<p align="center">
<img width="550" alt="Screenshot 2024-04-06 at 1 37 16 PM" src="https://github.com/tbrazel/math-journal/assets/42276623/78029b2d-a242-40db-8b8e-479652787158">
</p>

# How to get set up:

1. Clone this repository or download the files into a directory. Remember the path to this directory!
2. Go into the master file `journal.tex` and look at line 12:
```
\def\startyear{2024}
```
Change this value to whatever year it currently is when you're starting the journal.

## Mac/Linux script setup

3. There are two shell scripts --- the first one is `edit-journal.sh`. This goes through and checks whether a file exists for today. If it does, it opens it in your favorite text editor. Open up this file and look at line three:
```
open -a MacVim $TARGETFILE
```
Replace "MacVim" with whatever application you use to type LaTeX (note --- you don't need this application to be able to compile LaTeX, that will be handled by the next shell script)

4. The other shell script is `view-journal.sh`. This compiles the `journal.tex` file and opens the pdf. The second line says
```
open -a Skim journal.pdf
```
and you can replace "Skim" with whatever your pdf viewer of choice is.


So in order to start typing, you want to run these shell scripts. You can do this usually by double-clicking on the shell script file and opening it in a terminal. You may have to change the permissions on the files to allow this.

## Windows script setup

3. There are two Powershell scripts --- the first one is `edit-journal.ps1`. 
This goes through and checks whether a file exists for today. If it does, it opens it in your favorite text editor. 
Open up this file and look at line one:
``` posh
Set-Alias -Name my-python -Value 'C:\Users\lucas\Miniconda3\python.exe'
```
Replace `C:\Users\lucas\Miniconda3\python.exe` with the location of your Python executable.
Also, on line two:
``` posh
Set-Alias -Name my-editor 'C:\Program Files (x86)\VSCodium\VSCodium-win32-x64-1.60.2\VSCodium.exe'
```
Replace `C:\Program Files (x86)\VSCodium\VSCodium-win32-x64-1.60.2\VSCodium.exe` with the location of the executable of the editor you use to type LaTeX (note --- you don't need this application to be able to compile LaTeX, that will be handled by the next shell script).

So in order to start typing, you want to run these shell scripts. 
You can do this usually by double-clicking on the shell script file and opening it in a terminal. 
You may have to change the permissions on the files to allow this.

# In one keystroke!

## Mac setup

If you set up [Keyboard Cowboy](https://github.com/zenangst/KeyboardCowboy) or a similar such program, you can set a key command to trigger the shell files!

<img width="485" alt="Screenshot 2024-04-06 at 1 10 59 PM" src="https://github.com/tbrazel/math-journal/assets/42276623/7ca2d0be-370d-4ca3-b456-009b03604bd4">

Replace `/path/to/directory` with the absolute path (from the root) to where you're keeping this files, and set a keyboard command you like. For instance I hit `ctrl-e` when doing anything on my computer, and it opens the tex file for today in the math journal and I can start editing. Doing `ctrl-v` runs the shell script `view-journal.sh` and I can view my journal.

## Windows setup

To set up a key command to trigger the shell files, you need to make a shortcut, move the shortcut to your desktop, set it to execute in powershell, and then set the keyboard command.
To do this in a Files window:

1. Right-click the shell script, click `Show more options`, then click `Create shortcut`
2. Click and drag the newly-created shortcut to your Desktop.
3. In your Desktop, right-click the shorcut, click `Show more options`, then click `Properties`.
4. In the `Target` box, before what is already in the box type `powershell.exe -file`
5. In the `Shortcut key` box, click and then enter your shortcut (for editing I use `CTRL-ALT-J` and for viewing `CTRL-ALT-V`).

![Windows shortcut instructions](windows_shortcut.gif)

# About the LaTeX

The master file is `journal.tex`. When you download it, there will be almost nothing in it, just enough to get the journal running. It loads the package `pgffor` in order to run the for loops to load files for each day, so make sure you have this installed.

# Castel

This project was inspired by [Gilles Castel's workflow](https://castel.dev/post/research-workflow/). His vision for wielding coding to improve the daily life of a mathematics student or research mathematician was amazing. His blog posts were friendly and easy to read, and invited a lot of us to enter the world of live-tex'ing and digitizing our workflow. Rest in peace ✝️
