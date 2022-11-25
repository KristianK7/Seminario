import os
import subprocess


def get_optimo(alpha,betha,gamma,p):
    RutaSolver= "./Metasolver/BSG_CLP "
    RutaInstance= "Instance/instance.txt "
    tiempo= 1
    instance= 1

    comand= RutaSolver+RutaInstance+"-i "+str(instance-1)+" -t "+str(tiempo)+" --alpha "+str(alpha)+" --beta "+str(betha)+" --gamma "+str(gamma)+" -p "+str(p)
    out = subprocess.getoutput(comand)

    out = out.splitlines()


    return (out[-1])