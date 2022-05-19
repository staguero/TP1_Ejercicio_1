import numpy as np
from pyparsing import line_start
from requests import delete
from Node import *
from A_Star import *
from Dibujar import *
import random
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # >>>>>> CREACIÓN DE MAPA <<<<<<
    #Solicitud de datos

    lista = []
    distancia_recorrida = []
    nodos_expandidos = []
    tiempo_empleado = []
    columnas_estante=2
    for k in range (1,50):
        estantes_c = k
        estantes_f = k

        #Elaboración de matriz "MAPA"
        mapa_filas = 2*estantes_f+4+(estantes_f-1)*2
        mapa_columnas= estantes_c*columnas_estante+4+(estantes_c-1)*2
        mapa_dimensiones= [mapa_filas,mapa_columnas]
        mapa=[]
        mapa = [[Node(i,j,None) for j in range(mapa_columnas)] for i in range(mapa_filas)]
        for j in range(mapa_columnas):
            for i in range(mapa_filas):
                mapa[i][j].setID("Empty")

        #Asignacion de estantes y su nombre
        fin_columnas=mapa_columnas-(2+columnas_estante)
        m=np.linspace(2,fin_columnas,estantes_c)
        fin_filas=mapa_filas-(2+2)
        m2=np.linspace(2,fin_filas,estantes_f)
        valor=1
        for j in m:
            for i in m2:
                col=int(j)
                for k in range(columnas_estante): 
                    mapa[int(i)][col].setID( "Shelf" + str(valor) )
                    mapa[int(i)+1][col].setID("Shelf" + str(valor+columnas_estante ) )
                    col+=1
                    valor+=1
                valor+=columnas_estante

        # >>>>>> TRANSPORTE <<<<<<
        # Introduccion de datos
        suma_distancia = 0
        suma_nodos = 0
        suma_tiempo = 0
        n_shelfs = columnas_estante*2*estantes_c*estantes_f
        for iteraciones in range(0,100):
            inicio = random.randint(1,n_shelfs)
            fin = random.randint(1,n_shelfs)
            while( inicio == fin):
                fin = random.randint(1,n_shelfs)

            for j in range(mapa_columnas):
                for i in range(mapa_filas):
                    if mapa[i][j].id is not None:
                        if mapa[i][j].id[5:]==str(inicio):
                            current_node = mapa[i][j]
                        if mapa[i][j].id[5:]==str(fin):
                            target_node = mapa[i][j]

            a_estrella=A_Star(mapa,current_node,target_node)
            a_estrella.start_method(mapa_columnas,mapa_filas)
            suma_distancia += a_estrella.distancia_recorrida 
            suma_nodos += a_estrella.nodos_expandidos
            suma_tiempo += a_estrella.tiempo_empleado

        distancia_recorrida.append(suma_distancia/100)
        nodos_expandidos.append(suma_nodos/100)
        tiempo_empleado.append(suma_tiempo/100)
        del a_estrella
    x=list(range(1, 50))
    fig, axs = plt.subplots(2, 3)
    axs[0, 0].plot(x, distancia_recorrida)
    axs[0, 0].set_title('Promedio de distancia recorrida')
    axs[0, 0].set_xlabel('Dimensiones NxN del almacen')
    axs[0, 1].plot(x, nodos_expandidos, 'tab:orange')
    axs[0, 1].set_title('Promedio de nodos expandidos')
    axs[0, 1].set_xlabel('Dimensiones NxN del almacen')
    axs[0, 2].plot(x, tiempo_empleado, 'tab:green')
    axs[0, 2].set_title('Promedio de tiempo en cada iteracion')
    axs[0, 2].set_xlabel('Dimensiones NxN del almacen')
    axs[0, 0].grid(axis='both', color='gray',linestyle = 'dashed')
    axs[0, 1].grid(axis='both', color='gray',linestyle = 'dashed')
    axs[0, 2].grid(axis='both', color='gray',linestyle = 'dashed')
    fig.tight_layout()
    fig.show()

input()

