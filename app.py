import subprocess
import pandas as pd
import networkx as nx 


def install_required_libraries(libraries):
    for library in libraries:
        try:
            subprocess.run(["pip", "install", library])
            
        except Exception as e:
            raise Exception(f"Error al instalar la librería {library}: {e}")



class Sociograma:
    def __init__(self, archivo_csv):
        self.df = pd.read_excel(archivo_csv)
        self.G = nx.MultiDiGraph()
        self.G.add_nodes_from(self.df['personas'].tolist())
        self.G.add_edges_from(self.df[['personas', 'eleccion']].values.tolist())

    def mostrar(self):
        print(self.df)
   
    def ajustar_tamanio_nodos(self):
        tamanio_nodos = []
        for i in range(len(self.G)):
            # Calcula el tamaño del nodo en función de la nota
            tamanio_nodo = 1000 * self.df['nota'][i] / 10
            tamanio_nodos.append(tamanio_nodo)
        return tamanio_nodos

    def dibujar(self):
        #tamanio_nodos = self.ajustar_tamanio_nodos(self.df['parametro'])
        nx.draw(self.G, with_labels=True, arrowsize=20)
        #plt.show()





#Librerias 
#install_required_libraries(["networkx", "pandas"])

sociograma = Sociograma("alumnos_prueba.xlsx")
sociograma.dibujar()
