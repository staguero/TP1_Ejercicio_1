import tkinter as tk
import numpy as np

class Dibujar():
    def __init__(self,lado,columna,fila,columnas_estante,estantes_f,estantes_c):
        self.lado=lado
        self.fila=fila
        self.columna=columna
        self.columnas_estante=columnas_estante
        self.estantes_f=estantes_f
        self.estantes_c=estantes_c
        self.casilleros=[]
        self.camino=[]
        
        self.ventana=tk.Tk()
        self.ventana.title("ÁREA DE TRABAJO")
        #self.ventana.iconbitmap("ico.ico")
        #Ventana con longitud requerida
        self.ventana.geometry(f"{str(lado*self.columna)}x{str(lado*self.fila)}")
        self.ventana.resizable(0,0) #evita que se agrande o minimice

        self.interfaz= tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both",expand=True)

    def asignar_posiciones_casilleros(self):
        fin_columnas=self.columna-(2+self.columnas_estante)
        m=np.linspace(2,fin_columnas,self.estantes_c)
        fin_filas=self.fila-(2+2)
        m2=np.linspace(2,fin_filas,self.estantes_f)
        for j in m:
            for i in m2:
                col=int(j)
                for k in range(self.columnas_estante): 
                    self.casilleros.append([int(i),col])
                    self.casilleros.append([int(i+1),col])
                    col+=1

    def definir_camino(self,camino):
        self.camino=camino
    
    def dibujar_mapa(self):
        for i in range(self.columna):
            for j in range(self.fila):
                    if [j,i] in self.casilleros:
                        self.interfaz.create_rectangle(i*self.lado,j*self.lado,(i+1)*self.lado,(j+1)*self.lado,fill="#2F4F4F")
                    else:
                        self.interfaz.create_rectangle(i*self.lado,j*self.lado,(i+1)*self.lado,(j+1)*self.lado,fill="#698B69")

    def dibujar_mapa_full(self):
        for i in range(self.columna):
            for j in range(self.fila):
                    if [j,i] in self.camino:
                        self.interfaz.create_rectangle(i*self.lado,j*self.lado,(i+1)*self.lado,(j+1)*self.lado,fill="#76EE00")
                    elif [j,i] in self.casilleros:
                        self.interfaz.create_rectangle(i*self.lado,j*self.lado,(i+1)*self.lado,(j+1)*self.lado,fill="#2F4F4F")
                    else:
                        self.interfaz.create_rectangle(i*self.lado,j*self.lado,(i+1)*self.lado,(j+1)*self.lado,fill="#698B69")