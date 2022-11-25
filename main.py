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


parser = ap.ArgumentParser()
parser.add_argument('--t', type=str, default= 'uniforme', help='Tipo de distribucion')
parser.add_argument('--p', type=int, default=100, help='porcentaje de carga container')
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
    if args.t == 'uniforme':
        if args.p == 120:
            dimension_box, cantidad_box_type, n_tipes_box, n_box, v_carga, v_contenedor = U12.get_uni_prus()
        else:
            dimension_box, cantidad_box_type, n_tipes_box, n_box, v_carga, v_contenedor = U.get_uni()
    elif args.t == 'normal':
        if args.p == 120:
            dimension_box, cantidad_box_type, n_tipes_box, n_box, v_carga, v_contenedor = N12.get_norm_prus()
        else:
            dimension_box, cantidad_box_type, n_tipes_box, n_box, v_carga, v_contenedor = N.get_norm()

    print("tipos de cajas:")
    print(n_tipes_box)
    op = OBSG.get_optimo(alpha_op, beta_op, gamma_op,p_op)
    print("optimo paper es: "+op)

    
    #busqueda de el mejor p
    best = 0.0
    best_p = 0.0
    print("buscando mejor p: ")
    for i in range(p[0],p[1]):
        optimizacion = OBSG.get_optimo(alpha_op,beta_op,gamma_op,i/100)
        if float(optimizacion) > best:
            best = float(optimizacion)
            best_p = i/100
            print("nuevo best = "+str(best)+"% with p"+str(best_p))
 
    #busqueda de el mejor gamma
    best = 0.0
    best_gamma = 0.0
    print("buscando mejor gamma: ")
    for i in range(gamma[0],gamma[1]):
        optimizacion = OBSG.get_optimo(alpha_op,beta_op,i/10,best_p)
        if float(optimizacion) > best:
            best = float(optimizacion)
            best_gamma = i/10
            print("nuevo best = "+str(best)+"% with gamma"+str(best_gamma))
   
    #busqueda de el mejor beta
    best=0.0
    best_beta = 0.0
    print("buscando mejor beta: ")
    for i in range(beta[0],beta[1]):
        optimizacion = OBSG.get_optimo(alpha_op,i/10,best_gamma,best_p)
        if float(optimizacion) > best:
            best = float(optimizacion)
            best_beta = i/10
            print("nuevo best = "+str(best)+"% with beta"+str(best_beta))

    #busca el mejor alpha
    best = 0.0
    best_alpha = 0.0
    print("buscando mejor alpha: ")
    for i in range(alpha[0],alpha[1]):
        optimizacion = OBSG.get_optimo(i/10,best_beta,best_gamma,best_p)
        if float(optimizacion) > best:
            best = float(optimizacion)
            best_alpha = i/10
            print("nuevo best = "+str(best)+"% with alpha"+str(best_alpha))


    #Guardar 

        #-Numero de cajas -> n_box
    suma = 0
    for i in range(n_tipes_box):
        suma = suma + n_box[i]
    print("Numero de cajas = "+ str(suma))
        #-Cantidad de tipos de cajas-> n_tipes_box
    print('n_tipes_box = '+str(n_tipes_box))
        #-Volumen Total/Volumen Contenedor -> V_Carga/V_Contenedor
    relacion_volumen = v_carga /v_contenedor
    print('relacion = '+str(relacion_volumen)+' = '+str(v_carga)+'/'+str(v_contenedor))
        #-Media_l/l;h/h;w/w;
    media = []
    for i in range(3):
        aux_med=[]
        for j in range(n_tipes_box):
            for k in range(cantidad_box_type[j]):
                aux_med.append(dimension_box[j][i])

        media.append(np.mean(aux_med))
    print('media de [l,w,h] = ')
    print(media)
        #-Desviacion_l/l;h/h;w/w;
    desviacion = []
    for i in range(3):
        aux_desv=[]
        for j in range(n_tipes_box):
            for k in range(cantidad_box_type[j]):
                aux_desv.append(dimension_box[j][i])

        desviacion.append(np.std(aux_desv))
    print('desviacion de [l,w,h] = ')    
    print(desviacion)
        #-Media_volumen/volumen
    volumen = []
    for j in range(n_tipes_box):
        for k in range(cantidad_box_type[j]):
            aux_v= (dimension_box[j][0] * dimension_box[j][1])
            aux_v = aux_v * dimension_box[j][2]
            volumen.append(aux_v)
    desv_volumen = np.std(volumen)
    print('La desviacion volumen de cajas es: ')
    print(str(desv_volumen))
    media_volumen = np.mean(volumen)
    print('La desviacion volumen de cajas es: ')
    print(str(media_volumen))
    #-Desviacion_volumen/volumen


    #-Best_Alpha
    #-Best_beta
    #-Best_gamma
    #-Best_p



    archivo_instance = "Instance/out_BSG.txt";
    with open(archivo_instance, 'a') as file:
        file.write(str(args.p)+', '+str(optimizacion)+', ' + str(suma)+', '+str(n_tipes_box)+', '+str(relacion_volumen)+', '+str(media[0])+', '+str(media[1])+', '+str(media[2])+', '+str(desviacion[0])+', '+str(desviacion[1])+', '+str(desviacion[2])+', '+str(desv_volumen)+', '+str(media_volumen)+', '+str(best_alpha)+', '+str(best_beta)+', '+str(best_gamma)+', '+str(best_p)+', '+str(best)+"\n");



if __name__ == '__main__':
    main()