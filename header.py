# Use this to split a file based on headers
# Looks for reStructuredText headers, which looks like:
# ==============
# Example header
# ==============
# Creates files with the header contents as file name or "missing" if not found
# New files is placed in a folder called "split"

import re
import os
import sys
from slugify import slugify

script_dir = os.path.dirname(__file__)
if script_dir is "":
    script_dir = "."

script, targetfile = sys.argv


# Replace with your source file
theFile = os.path.join(script_dir, targetfile)

def main():

    headerFile = os.path.join(script_dir, "0 - Table Of Contents/index.rst")

    # open file
    headers = []

    with open(headerFile) as originalFile:
        headers = originalFile.readlines()

    headers = [x for x in headers if len(x.lstrip()) is not 0]
    mainheaders = [x for x in headers if len(x) is len(x.lstrip())]
    subheaders = [x.lstrip() for x in headers if len(x) is not len(x.lstrip())]

    lines = []
    with open(theFile) as originalFile:
        lines = originalFile.readlines()

    newfiles = [{"name": "index", "lines": []}]

    for i, line in enumerate(lines):
        converted = False
        if line in mainheaders:
            printAround(i, lines)
            if (ask("Convert to main header?")):
                newfiles.append({"name": slugify(line), "lines": []})
                mainheaders.remove(line)
                line = convertToHeader(line, "=")
                converted = True
        if not converted and line in subheaders:
            printAround(i, lines)
            if (ask("Convert to sub header?")):
                subheaders.remove(line)
                line = convertToHeader(line, "-")

        newfiles[-1]["lines"].append(line)

    for f in newfiles:
        writeFile(f["name"], "".join(f["lines"]))


def printAround(i, lines):
    for x in xrange(max(i-3, 0), i+4):
        string = str(x) + "  " + lines[x]
        if x == i:
            string = color.BOLD + color.BLUE + string + color.END
        sys.stdout.write(string)


def convertToHeader(line, headerString):
    label = ".. _" + slugify(line) + ":\n\n"
    h = headerString * (len(line) - 1) + "\n"
    return label + line + h


def writeFile(name, content):
    writingdir = "header/"
    if not os.path.exists(os.path.join(script_dir, writingdir)):
        os.makedirs(os.path.join(script_dir, writingdir))

    filename = name + ".rst"
    newfilepath = os.path.join(script_dir, writingdir, filename)
    newfile = open(newfilepath, 'w+')
    newfile.write(content)
    newfile.close()
    print "The modified contents has been written to " + newfilepath


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def ask(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    prompt = color.PURPLE + prompt + color.END

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


main()
