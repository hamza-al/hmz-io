# HMZ-IO

## Description
A simple file system simulation implemented in python

## Goals
1. Learn how to implement a heirarchy style file system
2. No googling, challenge myself to learn and think without any reliance
3. Potentially create a tool that could help people with less technical skills learn to navigate a terminal based file navigation system
4. Create easy and understandable error messages

## How it works
HMZ-IO will operate by taking in standard commands into a REPL like simulation that mimicks the navigation and creation commands of a standard file system.


## Commands
### add 
Creates a new file with a given file name
- usage:
  - add \<filename>
  - User will be propted to add content to the file (can be left blank)
###  del
Deletes a file with a given file name
- usage:
  - del \<filename>
- errors:
  - file with that filename does not exist

### enter 
Changes current directory to a specified CHILD directory of the current directory
- usage:
  - enter \<dirname>
- errors:
  - directory with that name does not exist
### makedir 
Creates a new file with a given name
- usage:
  - makedir \<dirname>
- errors:
  - directory with that name exists
