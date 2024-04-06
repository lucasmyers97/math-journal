Math Journal
================

The following provides a very lightweight way to keep a math journal. Within one keystroke you can start typing, and a file for that day will be automatically created. In another keystroke you can view a compiled version of your whole math journal. The philosophy behind this is that you should have a home to jot down thoughts instantly, and the tech behind it should enable you to do it without navigating directories, creating files, including them in a master file, etc. --- all of that is handled in the back end.

**How to get set up:**

* Clone this repository or download the files into a directory. Remember the path to this directory!
* Go into the master file `journal.tex` and look at line 12:
```
\def\startyear{2024}
```
Change this value to whatever year it currently is when you're starting the journal.
* There are two shell scripts --- the first one is `edit-journal.sh`. This goes through and checks whether a file exists for today. If it does, it opens it in your favorite text editor. Open up this file and look at line three:
```
open -a MacVim $TARGETFILE
```
Replace "MacVim" with whatever application you use to type LaTeX (note --- you don't need this application to be able to compile LaTeX, that will be handled by the next shell script)
* The other shell script is `view-journal.sh`. This compiles the `journal.tex` file and opens the pdf. The second line says
```
open -a Skim journal.pdf
```
and you can replace "Skim" with whatever your pdf viewer of choice is.


So in order to start typing, you want to run these shell scripts. You can do this usually by double-clicking on the shell script file and opening it in a terminal. You may have to change the permissions on the files to allow this.

**In one keystroke!**

If you set up [Keyboard Cowboy]() or a similar such program, you can set a key command to trigger the shell files!

figure goes here

Replace `/path/to/directory` with the absolute path (from the root) to where you're keeping this files, and set a keyboard command you like. For instance I hit `ctrl-e` when doing anything on my computer, and it opens the tex file for today in the math journal and I can start editing. Doing `ctrl-v` runs the shell script `view-journal.sh` and I can view my journal.


**About the LaTeX**

The master file is `journal.tex`. When you download it, there will be almost nothing in it, just enough to get the journal running. It loads the package `pgffor` in order to run the for loops to load files for each day, so make sure you have this installed.
