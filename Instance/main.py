import argparse as ap
import random
import numpy as np
import os
import subprocess
import Generador_norm_120 as N12
import Out_BSG as OBSG
import Generador_norm as N
import Generador_uni as U
import Generador_uni_120 as U12
from datetime import datetime

now = datetime.now()

parser = ap.ArgumentParser()
parser.add_argument('--t', type=str, default= 'Uniforme', help='Tipo de distribucion')
parser.add_argument('--p', type=int, default=100, help='porcentaje de carga container')
parser.add_argument('--i', type=int, default=1, help='Iteracion')
parser.add_argument('--n', type=int, default= 1, help='Numero de proceso')
args = parser.parse_args()


def main():


    alpha_op = 4.0
    beta_op = 1.0
    gamma_op = 0.2
    p_op = 0.04


    alpha = [0,80]
    beta = [0,80]
    gamma = [0,20]
    p = [0,10]
    print(args.t+" "+str(args.p)+"%")
    if args.t == 'Uniforme':
        if args.p == 120:
            dimension_box, cantidad_box_type, n_tipes_box, n_box, v_contenedor, v_carga,l,h,w  = U12.get_uni_prus(str(args.n))
        else:
            dimension_box, cantidad_box_type, n_tipes_box, n_box, v_contenedor, v_carga,l,h,w = U.get_uni(str(args.n))
    elif args.t == 'Normal':
        if args.p == 120:
            dimension_box, cantidad_box_type, n_tipes_box, n_box, v_contenedor, v_carga,l,h,w = N12.get_norm_prus(str(args.n))
        else:
            dimension_box, cantidad_box_type, n_tipes_box, n_box, v_contenedor, v_carga,l,h,w = N.get_norm(str(args.n))

    print("tipos de cajas:")
    print(n_tipes_box)
    op = OBSG.get_optimo(alpha_op, beta_op, gamma_op,p_op)
    print("optimo paper es: "+op)
    if float(op) < 75:
        comand= "cp Instance/instance.txt Instance/Error/Error_"+str(args.i)+"_"+str(args.n)+".txt"
        out = subprocess.getoutput(comand)
        
        archivo_log= "Instance/LOG_BSG.txt";
        with open(archivo_log, 'a') as file:
            file.write(
                str(now)+', Error proceso '+str(args.n)+', iteracion'+str(args.i)+"\n");

        
        
    
    #busqueda de el mejor p
    best = 0.0
    best_p = 0.0
    print("buscando mejor p: ")
    for i in range(p[0],p[1]):
        optimizacion = OBSG.get_optimo(alpha_op,beta_op,gamma_op,i/100)
        if float(optimizacion) > best:
            best = float(optimizacion)
            best_p = i/100
            print("nuevo best = "+str(best)+"% with p = "+str(best_p))
 
    #busqueda de el mejor gamma
    best = 0.0
    best_gamma = 0.0
    print("buscando mejor gamma: ")
    for i in range(gamma[0],gamma[1]):
        optimizacion = OBSG.get_optimo(alpha_op,beta_op,i/10,best_p)
        if float(optimizacion) > best:
            best = float(optimizacion)
            best_gamma = i/10
            print("nuevo best = "+str(best)+"% with gamma = "+str(best_gamma))
   
    #busqueda de el mejor beta
    best=0.0
    best_beta = 0.0
    print("buscando mejor beta: ")
    for i in range(beta[0],beta[1]):
        optimizacion = OBSG.get_optimo(alpha_op,i/10,best_gamma,best_p)
        if float(optimizacion) > best:
            best = float(optimizacion)
            best_beta = i/10
            print("nuevo best = "+str(best)+"% with beta = "+str(best_beta))

    #busca el mejor alpha
    best = 0.0
    best_alpha = 0.0
    print("buscando mejor alpha: ")
    for i in range(alpha[0],alpha[1]):
        optimizacion = OBSG.get_optimo(i/10,best_beta,best_gamma,best_p)
        if float(optimizacion) > best:
            best = float(optimizacion)
            best_alpha = i/10
            print("nuevo best = "+str(best)+"% with alpha = "+str(best_alpha))
    print("Optimizacion de busqueda = "+str(best))

    extract(n_tipes_box, n_box, v_carga, v_contenedor,cantidad_box_type,dimension_box, optimizacion, best_alpha,best_beta,best_gamma,best_p, best,l,h,w)




def extract(n_tipes_box,n_box,v_carga, v_contenedor,cantidad_box_type,dimension_box, optimizacion, best_alpha,best_beta,best_gamma,best_p,best,l,h,w):

        #Guardar 

        #-Numero de cajas -> n_box
    suma = 0
    for i in range(n_tipes_box):
        suma = suma + n_box[i]
        #-Cantidad de tipos de cajas-> n_tipes_box
        #-Volumen Total/Volumen Contenedor -> V_Carga/V_Contenedor
    
    relacion_volumen = float("{:2f}".format(v_carga /v_contenedor))
        #-Media_l/l;h/h;w/w;
    
    media = []
    for i in range(3):
        aux_med=[]
        for j in range(n_tipes_box):
            for k in range(cantidad_box_type[j]):

                aux_med.append(dimension_box[j][i])

        media.append(float("{:2f}".format(np.mean(aux_med))))
        
        #-Desviacion_l/l;h/h;w/w;
    desviacion = []
    for i in range(3):
        aux_desv=[]
        for j in range(n_tipes_box):
            for k in range(cantidad_box_type[j]):
            
                aux_desv.append(dimension_box[j][i])

        desviacion.append(float("{:2f}".format(np.std(aux_desv))))
        #-Media_volumen/volumen
    volumen = []
    for j in range(n_tipes_box):
        for k in range(cantidad_box_type[j]):
            aux_v= (dimension_box[j][0] * dimension_box[j][1])
            aux_v = aux_v * dimension_box[j][2]
           
            volumen.append(float("{:2f}".format(aux_v)))
            
    desv_volumen = float("{:2f}".format(np.std(volumen)))
    media_volumen = float("{:2f}".format(np.mean(volumen)))
   #-Desviacion_volumen/volumen


    #-Best_Alpha
    #-Best_beta
    #-Best_gamma
    #-Best_p



    archivo_instance = "Instance/out_BSG"+str(args.n)+".txt";
    with open(archivo_instance, 'a') as file:
        file.write(
            str(optimizacion)+', ' + 
            str(suma)+', '+
            str(n_tipes_box)+', '+
            str(relacion_volumen)+', '+
            str(float("{:2f}".format(media[0]/l)))+', '+
            str(float("{:2f}".format(media[1]/w)))+', '+
            str(float("{:2f}".format(media[2]/h)))+', '+
            str(float("{:2f}".format(desviacion[0]/l)))+', '+
            str(float("{:2f}".format(desviacion[1]/w)))+', '+
            str(float("{:2f}".format(desviacion[2]/h)))+', '+
            str(float("{:2f}".format(desv_volumen/v_contenedor)))+', '+
            str(float("{:2f}".format(media_volumen/v_contenedor)))+', '+
            str(best_alpha)+', '+
            str(best_beta)+', '+
            str(best_gamma)+', '+
            str(best_p)+', '+
            str(best)+"\n");
    """
    - Optimizacion obtenida por el paper
    - Total de cajas
    - Numero de tipos de cajas
    - Relacion volumen Carga contenedor
    - Media del largo de las cajas/contenedor
    - Media del ancho de las cajas/contenedor
    - Media del alto de las cajas/contenedor
    - Descviacion del largo de las cajas
    - Descviacion del ancho de las cajas
    - Descviacion del alto de las cajas
    - Desviacion del volumen de las cajas
    - Media del volumen de las cajas
    - Mejor Alpha,Beta,Gamma,p
    - Optimizacion obtenido por la busqueda

    
    """



if __name__ == '__main__':
    main()