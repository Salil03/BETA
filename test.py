import os
import easygui
import prettytable
import subprocess
import easygui
import time
import sys
from pathlib import Path


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


os.system('')
if(len(sys.argv) == 1):
    source_code = easygui.fileopenbox(msg="Open source code", title="Source Code",
                                      default="", multiple=False)
    if source_code is None:
        print("No input file selected!!")
        sys.exit(0)
else:
    source_code = sys.argv[1]


input_files = easygui.fileopenbox(
    msg="Open input files", title="Input", default="*.in",  multiple=True)
output_files = easygui.fileopenbox(
    msg="Open output files", title="Output", default="*.out",  multiple=True)
if len(input_files) != len(output_files) or output_files is None:
    print("Please enter same number of input and output files")
    sys.exit(0)
while True:
    print(bcolors.ENDC +
          u"\u001b[0m\u001b[7m Test Cases Checker \u001b[0m" + "\n")
    correct = 0
    x = prettytable.PrettyTable(["Test Case", "Judge Verdict", "Time Taken"])
    x.hrules = prettytable.ALL
    for i in range(len(input_files)):
        start = time.time()
        os.system("python \"" + source_code + "\" < \"" +
                  input_files[i] + "\" > myoutput.out")
        end = time.time()
        temp = subprocess.Popen(
            "FC /N /LB50 \"" + output_files[i] + "\" myoutput.out", stdout=subprocess.PIPE, shell=True)
        (out, err) = temp.communicate()
        if "no differences encountered" in out.decode("utf-8"):
            x.add_row([str(i+1), bcolors.OKGREEN + "AC" + bcolors.ENDC,
                       str(max(0, end - start - 0.125)) + " seconds"])
            correct += 1
        else:
            print(bcolors.UNDERLINE + "TEST " + str(i+1) +
                  " " + input_files[i] + ":" + bcolors.ENDC)
            print(bcolors.FAIL + "WA")
            print(out.decode("utf-8") + bcolors.ENDC)
            x.add_row([str(i+1), bcolors.FAIL + "WA" + bcolors.ENDC,
                       str(max(0, end - start - 0.125)) + " seconds"])
    print(x)
    os.remove("myoutput.out")
    print(bcolors.UNDERLINE + "Total Correct = " + str(correct) +
          "/" + str(len(input_files)) + bcolors.ENDC)
    if(str(input("Do you want to try again (Y/N): ")).lower() != "y"):
        break
