

import glob, shutil, os

def main():
    for p_py in glob.glob('../articles/data_parsing/*examples*/*/*.py'):
        print p_py
        p_html = p_py.replace('.py', '.html')
        f_html = open(p_html, 'w')
        f_py = open(p_py, 'r')




        code = f_py.readlines()
        filename = os.path.basename(p_py)


        tagged_code = []
        codeBlock = False
        for line in code:



            if '#' in line:
                #replace line line
                line = line.split("#")[0] + '<comment>#' + line.split("#")[1].rstrip() + '</comment>\n'

            else:
                line, old_line = '', line
                str_open = False
                for char in old_line:

                    if str_open and char == open_char:
                        str_open = False
                        line += char
                        line += '</strings>'

                    elif not str_open and (char is '"' or char is "'"):
                        str_open = True
                        open_char = char
                        line += '<strings>'
                        line += char


                    else:
                        line += char




            tagged_code.append(line)

        code = ''.join(tagged_code)
        c_html = template % locals()


        f_html.writelines(c_html)

        f_html.close()
        f_py.close()





template = '''<html>
<link href="../../../../style.css" rel="stylesheet" type="text/css" >
<pre>
%(code)s
</pre>
</html>'''

main()