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

    document = ' '.join(fIn.readlines())

    #document, errors = tidy_document(doc, options={'wrap': 100, 'vertical-space' : 'no'})


    document = document.replace('\r\n', '\n')

    matches = re.findall(r'\n+</pre>', document)

    print '!!', matches

    for match in set(matches):
        document = document.replace(match, '</pre>')


    document = document.split('\n')

    codeBlock = False
    #print document
    i = 0



    for line in document:
        if '<pre>' in line:
            codeBlock = True

        #fully de-indent all code
        if codeBlock:
            document[i] = line.lstrip()

        #add <comment> tags
        if codeBlock and ('#' in line) and (not '<comment>' in line):
            #print line

            document[i] = line.split("#")[0] + '<comment>#' + line.split("#")[1] + '</comment>'

        if '</pre>' in line:
            codeBlock = False

        i += 1


    fOut.write('\n'.join(document))

    fIn.close()
    fOut.close()
    try:
        os.remove(html+'~')
    except:
        print 'failed to delete:' + html+'~'