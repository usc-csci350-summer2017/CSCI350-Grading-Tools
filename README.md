# CSCI350-Grading-Tools
## Hello there

Hello, if you are here because you are a member of the USC CSCI 350 teaching team (Professor, TA, CP), then you are at the right place! Here are the tools I have made to make grading easy.

If you are not a member of the CSCI 350 teaching team (student, or just someone else), then feel free to poke around. I'll just let you know right away that you won't find answers to anything here, so don't waste your time trying.

## Documents

In the *documents* directory, you will find the following files:

1. DesignDoc_Answers: These are the answers and grading guide for the designdoc questions. It is encrypted with a password, please ask a fewllow CP, TA, or the professor for the password.

2. Pintos Guide: This a guide for the students to help them with the projects. This is NOT an official guide, just something I wrote for fun.

3. Simple Guide to C: For students who have never written in C before, this is a good starting guide for students who are familiar with C++ but not C.

4. Sublime_Tutorial: Sublime is a great text editor for Pintos, especially with its file navigation right from the keyboard. I highly recommend this text editor, especially since it's already installed in the VM environment.

## Scripts

### Prerequisites

#### Submission Repo
You'll need to have scraped the student repositories before you use these scripts. Here are some musts for the scripts to work:

1. Place the submission repository one directory up (../).
2. You must name your repo directory as *submissions_proj\<i\>* replacing the *\<i\>* with the project number (eg. "*submissions_proj2*").
3. You must create a directory named "*DESIGNDOC*" in the submissions directory.
4. You must create a directory named "*GRADES*" in the submissions directory.

#### Student Repo

Each student's repo must be organized in a specific manner:

1. Each project must be named "*proj\<i\>*" in the root directory (eg. "proj2")
2. The designdoc must be named "DESIGNDOC" and placed under each respective project's main source directory. For example for project 2, the designdoc must be named "DESIGNDOC" and placed under "proj2/src/userprog/".

You'll also need to have a csv file ready with all the student's repo names. The format is simply the repo name (eg. pintos-ttrojan) on each line. Please make sure to include an empty line at the end of the file, otherwise the last line will be omitted from the script.

#### Python Packages

Make sure you have the relevant python packages installed:

```
$ sudo apt-get update
$ sudo apt-get install python-pip
$ pip install requests

```

### designdoc Script

The designdoc script simply copies every student's designdoc and places it under the DESIGNDOC driectory in the submissions repo with the student's username in the filename. It simply allows quick access to every student's designdoc.

To run the script, simply enter in the command line:

```
$ python designdoc_proj<i>.py <repos>.csv
```

Replacing \<i\> with the project number and the \<repos\> with the repo csv filename.

### make_grade Script

The make_grade script compiles and runs "make grade" on every student's repo, then copies the relevant number of tests passing information from the grade report generated to the GRADES directory in the submission repo.

To run the script, simply enter in the command line:

```
$ python make_grade_proj<i>.py <repos>.csv
```

Replacing \<i\> with the project number and the \<repos\> with the repo csv filename. Note that this script will run for a very long time as it needs to compile and run every pintos test for every studnet's submission. You might want to split the grading up into batches (hence the two csv files repos_all.csv for every student repo name and repos.csv for a subset), or running it on a dedicated machine overnight.

Every once in a while a student's submission will infinitely loop the grading script. Usually the pintos tests have a timeout that will fail the test automatically, but in some strange circumstances the script will still get stuck. If you suspect a student's submission is clogging up the script, simply remove the student from the csv and grade it manually.

## Closing Remarks

If you have any questions, feel free to contact me at stephen.sher.94@gmail.com. I'll try to help as much as I can. Have fun and happy grading!