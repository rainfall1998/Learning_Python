#!/usr/bin/env python3
import os

def txtReadlines(path_file,begin=1,end=0):
    file = open(path_file,'r')
    lines = file.readlines()
    file.close()

    if end<=0:
        end = len(lines) + end
    return lines[begin-1:end]

def removeN(lines_in,flag_remove = '\n'):
    ''' to remove the str for every line in a list of string
    Args:
    lines_in(list): the list to remove the str
    flag_remove(str): the str to remove
    Returns
    lines(list): the list  modifid
    '''
    lines = lines_in.copy()
    num_lines = len(lines)

    for i in range(0,num_lines):
        lines[i] = lines[i].replace(flag_remove,'')
    return lines

def writeMatchTxt(lines, path_write, type_file = 'w', num_match = 3):
    '''to write the match list of 1:3\n
    Args:
    lines(list):        the line list without '\\n' \n
    path_write(str):    the file path to write  \n
    type-file(str):     can choose w or w+, default is w    \n
    num_match(int):     1:num_match, means 1.jpg 2.jpg/3.jpg/.../(num_match+1).jpg  \n
    Returns:
    '''
    num_lines = len(lines)
    file = open(path_write,type_file)

    for i_lines in range(0,num_lines-num_match):
        for j in range(1,num_match+1):
            line_write = lines[i_lines] + ' ' + lines[i_lines+j] + '\n'
            file.write(line_write)
    
    for i_lines in range(num_lines-num_match,num_lines):
        for line in lines[i_lines+1:]:
            line_write = lines[i_lines] + ' ' + line + '\n'
            file.write(line_write)
    
    file.close()


if __name__ == '__main__':
    path_read = './data/txtRead.txt'
    path_write = './data/matchListTry.txt'

    lines = txtReadlines(path_read,2)
    lines = removeN(lines)
    writeMatchTxt(lines, path_write)