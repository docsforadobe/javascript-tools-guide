# Use this to split a file based on headers
# Looks for reStructuredText headers, which looks like:
# ==============
# Example header
# ==============
# Creates files with the header contents as file name or "missing" if not found
# New files is placed in a folder called "split"

import re
import os
script_dir = os.path.dirname(__file__)

# Select file
theFile = script_dir+'/1 - Introduction/index.rst' # Replace with your source file

# open file
originalFile = open(theFile)
originalFileContent = originalFile.read()
originalFile.close()

# Split file
headerRegex = re.compile(r"(\n=+\n([^\n]+)\n=+)")

inserSplit = headerRegex.sub( r"=====split\1", originalFileContent)

splitFile = re.split("=====split", inserSplit)

# Create files
index = 1

if not os.path.exists(script_dir + '/split/'):
    os.makedirs(script_dir + '/split/')

for split in splitFile:
    # Write to new file
    if split is "":
        continue
    match = headerRegex.search(split)
    if match:
        fileName = str(index) + " - " + match.group(2)
    else:
        fileName = str(index) + " - missing"

    index += 1

    newFile = open(script_dir + '/split/' + fileName + '.rst', 'w+')
    newFile.write(split)
    newFile.close()
