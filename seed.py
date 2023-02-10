import glob
import sys
import generator
fileList = glob.glob('seed.txt')
if len(fileList) != 1:
    exit()
sys.stdin = open('seed.txt', 'r')
while True:
    try:
        inputSeed = int(input())
    except:
        break
    sys.stdout = open(f'input\input_{inputSeed}.txt', 'w')
    generator.mk_input(inputSeed)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
sys.stdin.close()
sys.stdin = sys.__stdin__