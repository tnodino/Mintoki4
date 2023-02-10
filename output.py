import glob
import sys
fileList = glob.glob('input\input*.txt')
for filePath in fileList:
    idx = filePath.rfind('input')
    if idx == -1:
        continue
    infileName = filePath[idx:]
    outfileName = infileName.replace('in', 'out')
    sys.stdin = open(f'input\{infileName}', 'r')
    sys.stdout = open(f'output\{outfileName}', 'w')
    exec(open('main.py').read())
    sys.stdin.close()
    sys.stdout.close()
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__