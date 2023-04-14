import numpy as np
import os
import subprocess
import random
import argparse as ap
from datetime import datetime

now = datetime.now()


parser = ap.ArgumentParser()
parser.add_argument('--n', type=str, default= '1', help='Numero de proceso')
parser.add_argument('--i', type=int, default= 10, help='Numero de iteraciones')
args = parser.parse_args()

def main():
    archivo_log= "Instance/LOG_BSG.txt";
    with open(archivo_log, 'a') as file:
        file.write(
            str(now)+', Inicio proceso '+args.n+"\n");
        print("Inicio proceso "+args.n)

    for j in range(4):
        for i in range(args.i):
            print(args.n)
            python= "/bin/python3 "
            RutaInstance= "Instance/main.py "
            azar = j+1
            tipo = 'Uniforme '
            porcentaje = '100'
            
            if azar == 2: porcentaje = '120'
            if azar == 3: tipo = 'Normal '
            if azar == 4: 
                porcentaje = '120'
                tipo = 'Normal '
            print("Iteracion: "+str(i+1)+", "+tipo+", "+porcentaje)


            comand= python+RutaInstance+"--t "+tipo+" --p "+porcentaje+" --i "+str(i+1)+" --n "+str(args.n)
            print(comand)
            out = subprocess.getoutput(comand)
            print (out)
            print ("\n")
    
    archivo_log= "Instance/LOG_BSG.txt";
    with open(archivo_log, 'a') as file:
        file.write(
            str(now)+', Inicio proceso '+args.n+"\n");




if __name__ == '__main__':
    main()