from Dibujar import *

# >>>>>> CREACIÓN DE MAPA <<<<<<
#Solicitud de datos
columnas_estante=int(input('Cantidad de columnas por estantería: '))
estantes_f=int(input('Cantidad de Filas de estantería: '))
estantes_c=int(input('Cantidad de Columnas de estantería: '))
#Elaboración de matriz "MAPA"
mapa_filas = 2*estantes_f+4+(estantes_f-1)*2
mapa_columnas= estantes_c*columnas_estante+4+(estantes_c-1)*2
#Camino de ejemplo
camino=[[2,2],[3,1],[4,2],[5,3],[6,3]] 

mapa=Dibujar(50,mapa_columnas,mapa_filas,columnas_estante,estantes_f,estantes_c)
mapa.asignar_posiciones_casilleros()
mapa.dibujar_mapa()


mapa_full=Dibujar(50,mapa_columnas,mapa_filas,columnas_estante,estantes_f,estantes_c)
mapa_full.asignar_posiciones_casilleros()
mapa_full.definir_camino(camino)
mapa_full.dibujar_mapa_full()
mapa_full.ventana.mainloop()