'''
Exercise 14.3. In a large collection of MP3 files, there may be more than one copy of the same song,
stored in different directories or with different file names. The goal of this exercise is to search for
duplicates.
1. Write a program that searches a directory and all of its subdirectories, recursively, and returns
a list of complete paths for all files with a given suffix (like .mp3 ). Hint: os.path provides
several useful functions for manipulating file and path names.
2. To recognize duplicates, you can use md5sum to compute a “checksum” for each files. If two
files have the same checksum, they probably have the same contents.
3. To double-check, you can use the Unix command diff .
'''
import os

def search_files(dirname='.'):
    ''' Find all the name of file in dirname and its subdirectories.

    dirname: string name of directory

    Return: string of files
    '''
    names = []
    for roots, dirs, filenames in os.walk(dirname):
        for filename in filenames:
            path = os.path.join(roots, filename)
            names.append(path)
    
    return names


def compute_checksum(filename):
    '''Computes the MD5 checksum of the content of file.

    filename: String
    '''
    return pipe('md5sum ' + filename)


def check_diff(name1, name2):
    '''Computes the different between the contents of two files.

    name1, name2: string filenames
    '''
    return pipe('diff %s %s' % (name1, name2))
                       
    
def pipe(cmd):
    '''Run a command in subprocess

    cmd:string Unix command

    Returns (res, stat), the output of the subprocess and the exit status.
    '''
    fp = os.popen(cmd)
    res = fp.read() 
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(names, suffix = '.py'):
    '''
    names: list, all files name have been found in search_files function.

    suffix: string, type file to match

    Returns: map from filename to checksum
    '''
    d = {}
    for name in names:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum, _ = res.split()
       
            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]
    
    return d


def check_pairs(names):
    '''Check whether any in list of files differs from the others.

    names: list, all file names have been found in search_file function
    '''
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1,name2)
                if res:
                    return False
    return True

         
def print_check_duplicate(d):
    '''Checks for duplicate files.
    
    Reports any files with the same chucksum and check
    whether they are, in fact, identical.
    Colton argues that such reactions arise from people's
    double standards towards software-produced

    d: map from checksum to list of files with that checksum
    '''
    for keys, names in d.items():
        if len(names) > 1:
            print('The following files have the same checksum')
            for name in names:
                print(name)
            if check_pairs(names):
                print('And they are identical')
            else:
                print('They are not identical')
    

if __name__ == "__main__":
    names = search_files('.')
    d = compute_checksums(names, '.py')
    print_check_duplicate(d)
             
