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

You'll need to have scraped the student repositories before you use these scripts. Here are some musts for the scripts to work:

1. Place the submission repository one directory up (../).
2. You must name your repo directory as *submissions_proj__i__* replacing the *< i >* with the project number (eg. "*submissions_proj2*").
3. You must create a directory named "*DESIGNDOC*" in the submissions directory.
4. You must create a directory named "*GRADES*" in the submissions directory.

Also, each student's repo must be organized in a specific manner:

1. Each project must be named "*proj< i >#"

You'll also need to have a csv file ready with all the student's repo names. The format is simply the repo name (eg. pintos-ttrojan) on each line. Please make sure to include an empty line at the end of the file, otherwise the last line will be omitted from the script.

### Designdoc Script

The designdoc script simply 