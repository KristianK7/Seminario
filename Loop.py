import numpy as np
import os
import subprocess
import random

def main():

    for i in range(25):
        print (i)
        python= "/bin/python3 "
        RutaInstance= "/home/seminario/Instance/main.py "
        azar = random.randint(1,4)
        tipo = 'uniforme '
        n = '100'
        if azar == 2: n = '120'
        if azar == 3: tipo = 'normal '
        if azar == 4: 
            n = '120'
            tipo = 'normal '

        comand= python+RutaInstance+"--t "+tipo+"--p "+n
        print(comand)
        out = subprocess.getoutput(comand)
        print (out)
        print ("\n")


if __name__ == '__main__':
    main()