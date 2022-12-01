import numpy as np
import os
import subprocess
import random

def main():
    for j in range(4):
        for i in range(25):
            print("Iteracion: "+str(i+1)+", "+str(j+1))
            python= "/bin/python3 "
            RutaInstance= "/home/seminario/Instance/main.py "
            azar = j+1
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