__author__ = 'JoesDesktop'


from tidylib import tidy_document


import fnmatch
import os , shutil, re

matches = []
for root, dirnames, filenames in os.walk(r'C:\Users\JoesDesktop\Dropbox\code\projects\jlittle576.github.io'):
  for filename in fnmatch.filter(filenames, '*parsing.htm?'):
      matches.append(os.path.join(root, filename))


for html in matches:

    shutil.move(html, html+'~')
    fIn = open(html+'~', 'rb')
    fOut = open(html, 'wb')

    doc = fIn.readlines()
    print doc

    i = 0
    codeBlock = False
    for line in doc:
        if '<pre>' in line:
            codeBlock = True

        #add <comment> tags
        if codeBlock and ('#' in line) and (not '<comment>' in line):
            #replace line line
            doc[i] = line.split("#")[0] + '<comment>#' + line.split("#")[1].rstrip() + '</comment>\n'

        if '</pre>' in line:
            codeBlock = False

        i += 1


    fOut.writelines(doc)

    fIn.close()
    fOut.close()
    try:
        os.remove(html+'~')
    except:
        print 'failed to delete:' + html+'~'