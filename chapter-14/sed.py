'''Write a function called sed that takes as arguments a pattern string, a replacement
string, and two filenames; it should read the first file and write the contents into the second file
(creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.
If an error occurs while opening, reading, writing or closing files, your program should catch the
exception, print an error message, and exit. Solution: http: // thinkpython2. com/ code/ sed.
py .

'''
import sys

def sed(pattern, replace, source, dest):
    '''Read a source file and write the destination file.

    In each line, replace pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    '''
    try:
        fin = open(source, 'r')
        fout = open(dest, 'w')

        for line in fin:
            if line == pattern:
                line = line.replace(pattern, replace)
                fout.write(line)
        
        fin.close()
        fout.close()
    
    except:
        print('Something went wrong')

def main(name):
    pattern = 'tinxautrai'
    replace = 'tindeptrai'
    source = '/home/lark/Documents/my-think-python/file1.txt'
    dest = '/home/lark/Documents/my-think-python/file2' + '.replace'
    sed(pattern,replace,source,dest)

if __name__ == "__main__":
    main(*sys.argv)
