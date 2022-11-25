import random
import numpy as np

def get_uni_prus():
    n_casos=1
    caso=1

    #dimensiones de contenedor
    l=587
    w=233
    h=220

    n_tipos = [1,3,5,8,10,12,15,20,30,40,50,60,70,80,90,100]
    n =n_tipos[random.randint(0,15)]
    #numero de tipos de caja

    #dimesiones de las cajas (normalizada)
    alpha1 =30
    alpha2=25
    alpha3=20
    beta1=120
    beta2=100
    beta3=80

    #constante de estabilidad
    L=2

    #Semilla
    s=101

    #Volumen de contenedor
    tc = l*h*w;

    #limites de cajas
    low_bound= [alpha1, alpha2, alpha3];
    upper_bound= [beta1, beta2, beta3];

    #arreglo con dimensiones, cantidad y volumen de los tipos de cajas
    dimension_box = [];
    cantidad_box_type= [];
    volumen_box_type=[];

    orientacion_box=[];

    #Inicializa el volumen de carga de cajas
    volumen_cargo = 0;


    file = "Instance/instance.txt";

    #abre el archivo para guardarlo
    with open(file, 'w') as file:
        #guarda parametros base
        file.write(str(n_casos)+"\n");    
        file.write(str(caso)+" "+str(s)+"\n");
        file.write(str(l)+" "+str(w)+" "+str(h)+"\n");
        file.write(str(n)+"\n");

        i=0;

        for i in range(n):
            #inicializa las dimensiones de las cajas aleatoreamente dentro de los rangos
            r_j= [random.randint(alpha1,beta1),random.randint(alpha2,beta2),random.randint(alpha3,beta3)];
        
            aux_dim=[]

            #Defiene las dimensiones de las cajas asegurando que este en los rangos limites
            for j in range(3):
                aux_dim.append(low_bound[j]+(r_j[j]%(upper_bound[j]-low_bound[j]+1)));

            #Guarda el arreglo dentro de otro arreglo
            dimension_box.append(aux_dim)

            #print(dimension_box)
            #inicializa el tipo de caja
            cantidad_box_type.append(1);
            #guarda el volumen de la caja creada
            volumen_box_type.append(dimension_box[i][0]*dimension_box[i][1]*dimension_box[i][2])
            min_dim=99999
            #busca la dimension mas baja de la caja
            for j in range(3):
                if dimension_box[i][j] < min_dim:
                        min_dim=dimension_box[i][j];
            
            aux_orient=[]	
            #verifica si la orientacion es viable
            for j in range(3):
                if dimension_box[i][j]/min_dim < L:
                    aux_orient.append(1);
                else:
                    aux_orient.append(0);
                    
            orientacion_box.append(aux_orient)

            

        v_k = 0;
        flag = True;

        #[1,1,1,1,1]*[30,20,25,4,5]
        while flag:
            volumen_cargo = 0;
            #calcula el volumen de de carga
            for i in range(n):
                volumen_cargo +=cantidad_box_type[i]*volumen_box_type[i];

            aux=random.randint(0,n-1)
            v_k= volumen_box_type[aux];

            if tc*1.2 > volumen_cargo + v_k:
                cantidad_box_type[aux]+=1;
            else:
                break;


        #Guarda la instancia creada
        for i in range(n):
            file.write(str(i+1))
            
            for j in range(3):
                file.write(" "+str(dimension_box[i][j])+" "+str(orientacion_box[i][j]));
            file.write(" "+str(cantidad_box_type[i])+"\n");
       


    return (dimension_box, cantidad_box_type,n,cantidad_box_type,tc,volumen_cargo)
