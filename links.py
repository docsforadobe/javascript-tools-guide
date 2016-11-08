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

targetextension = [".rst"]

script_dir = os.path.dirname(__file__)
if script_dir is "":
    script_dir = "."

script, targetfile = sys.argv

# Replace with your source file
theFile = os.path.join(script_dir, targetfile)


def main():
    if os.path.isdir(theFile):
        for filename in os.listdir(theFile):
            extension = os.path.splitext(filename)[1]
            if extension in targetextension:
                print color.BOLD + color.RED + filename + color.END
                convert(os.path.join(theFile, filename))
                print "\n" * 5
    else:
        convert(theFile)


def convert(theFile):

    lines = ""
    with open(theFile) as originalFile:
        lines = originalFile.read()

    modifiedlines = checklines(lines, askEachTime=False)

    if not ask("Is this correct?"):
        modifiedlines = checklines(lines, askEachTime=True)

    filename = os.path.basename(theFile)
    # Split string at extension and get first element
    name = os.path.splitext(filename)[0]
    writefile(name, modifiedlines)

def checklines(lines, askEachTime):
    linkRegex = re.compile( r"(see (?:Chapter \d\d?, )?(\"(.+?)\.?\"(?: on page \d\d?\d?)?))", re.I|re.S)
    matches = linkRegex.findall(lines)
    print matches
    for match in matches:
        converted = convertmatch(match)
        print match[0],
        print color.GREEN + "    ->    "  + color.END,
        print color.BOLD + converted + color.END
        if not askEachTime or ask("Is this correct?"):
            lines = lines.replace(match[0], converted)
    return lines


def convertmatch(match):
    refname = match[2]
    ref = ":ref:`" + slugify(refname) + "`"
    refnamewithquotes = match[1]
    wholestring = match[0]
    period = "." if wholestring[-2:-1] == "." else ""
    return wholestring.replace(refnamewithquotes, ref) + period

def printAround(i, lines):
    for x in xrange(max(i-3, 0), min(i+4, len(lines))):
        string = lines[x]
        if lines[x-1].endswith("\n"):
            string = str(x) + "  " + lines[x]

        if x == i:
            string = color.WHITE + string[:-1]
            nextString = color.WHITE + lines[x+1]
            highlight = color.bPURPLE + " " + color.END
            string = string + highlight + nextString + color.END
        elif x == i + 1:
            continue
        else:
            string = color.GRAY + string + color.END

        sys.stdout.write(string)


def writefile(name, content):
    writingdir = "links/"
    if not os.path.exists(os.path.join(script_dir, writingdir)):
        os.makedirs(os.path.join(script_dir, writingdir))

    filename = name + ".rst"
    newfilepath = os.path.join(script_dir, writingdir, filename)
    newfile = open(newfilepath, 'w+')
    newfile.write(content)
    newfile.close()
    print "The modified contents has been written to " + newfilepath


class color:
    BLACK = '\033[30m'
    WHITE = '\033[37m'
    GRAY = '\033[39m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    bBlack = '\033[40m'
    bRED = '\033[41m'
    bGREEN = '\033[42m'
    bYELLOW = '\033[43m'
    bBLUE = '\033[44m'
    bPURPLE = '\033[45m'
    bCYAN = '\033[46m'
    bWHITE = '\033[47m'
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
