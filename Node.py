class Node():
    def __init__(self,x,y,parent_node):
        self.id = None
        self.G = 0
        self.H = 0
        self.x=x
        self.y=y
        self.parent=parent_node

    def in_close_list(self,node,close_list):
        for value in close_list:
            if node.id == value.id:
                return value
            else:
                return False

    def in_open_list(self,node,open_list):
        for value in open_list:
            if node.id == value.id:
                return value
            else:
                return False

    def dist_eucl(self,node,target_node):
        if target_node is None:
            return ( (node.parent.x-node.x)**2 + (node.parent.y-node.y)**2 ) **0.5
        else:
            return ( (target_node.x-node.x)**2 + (target_node.y-node.y)**2 ) **0.5

    def check_list(self,node,close_list,open_list,target_node):
        if node.id[0:5] == "Shelf":
            return False
        if self.in_close_list(node,close_list):
            return False
        
        node.G = node.parent.G + self.dist_eucl(node)
        node.H = self.dist_eucl(node,target_node)

        if (self.in_open_list(node,open_list)):
            return False
        else:
            return True

    def update_parent(self,old_parent,new_candidate):
        if old_parent.parent is not None:
            if (old_parent.parent.G>new_candidate.G):
                return True
            else:
                return False
        else:
            return True

    def min_F(self,open_list):
        print(open_list)
        minF = open_list[0]
        for node in open_list:
            if (node.G + node.H) <= (minF.G + minF.H):
                minF = node
        return minF

    def camino(self,current_node,target_node,close_list,open_list,mapa,mapa_columnas,mapa_filas):
        path_list = []
        open_list.append(current_node)
        while True:
            tmp = self.in_close_list(target_node,close_list)
            if tmp:
                path_list = [[tmp.x, tmp.y]]
                while tmp.parent:
                    tmp = tmp.parent
                    path_list.append([tmp.x, tmp.y])
                path_list.reverse()
                return path_list
            else:
                minF = self.min_F((open_list))
                print(minF)
                close_list.append(minF)
                open_list.remove(minF)
                for j in range(mapa_columnas):
                    for i in range(mapa_filas):
                        if mapa[i][j].x == minF.x:
                            if mapa[i][j].y == minF.y:
                                if (j>=mapa_columnas):
                                    if (i>=mapa_filas):
                                        if (self.update_parent(mapa[i-1][j-1],minF)):
                                            mapa[i-1][j-1].parent = minF
                                        if (self.update_parent(mapa[i][j-1],minF)):
                                            mapa[i][j-1].parent   = minF
                                        if (self.update_parent(mapa[i-1][j],minF)):
                                            mapa[i-1][j].parent   = minF
                                    else:
                                        if (self.update_parent(mapa[i-1][j],minF)):
                                            mapa[i-1][j].parent   = minF
                                        if (self.update_parent(mapa[i-1][j-1],minF)):                                        
                                            mapa[i-1][j-1].parent = minF
                                        if (self.update_parent(mapa[i][j-1],minF)):
                                            mapa[i][j-1].parent   = minF
                                        if (self.update_parent(mapa[i+1][j],minF)):
                                            mapa[i+1][j].parent   = minF
                                        if (self.update_parent(mapa[i+1][j-1],minF)):
                                            mapa[i+1][j-1].parent = minF                                      
                                if (j<=0) :
                                    if (i<=0):
                                        if (self.update_parent(mapa[i][j+1],minF)):
                                            mapa[i][j+1].parent   = minF
                                        if (self.update_parent(mapa[i+1][j],minF)):
                                            mapa[i+1][j].parent   = minF
                                        if (self.update_parent(mapa[i+1][j+1],minF)):
                                            mapa[i+1][j+1].parent = minF
                                    else:
                                        if (self.update_parent(mapa[i-1][j],minF)):
                                            mapa[i-1][j].parent   = minF
                                        if (self.update_parent(mapa[i-1][j+1],minF)):
                                            mapa[i-1][j+1].parent = minF
                                        if (self.update_parent(mapa[i][j+1],minF)):
                                            mapa[i][j+1].parent   = minF
                                        if (self.update_parent(mapa[i+1][j],minF)):
                                            mapa[i+1][j].parent   = minF
                                        if (self.update_parent(mapa[i+1][j+1],minF)):
                                            mapa[i+1][j+1].parent = minF
                                if  (j<mapa_columnas) and (j>0):
                                    if (i>0):
                                        if (i<mapa_filas):
                                            print(self)
                                            print(mapa[i+1][j])
                                            print(minF)
                                            if (self.update_parent(mapa[i+1][j],minF)):
                                                mapa[i+1][j].parent   = minF
                                            if (self.update_parent(mapa[i+1][j-1],minF)):
                                                mapa[i+1][j-1].parent = minF
                                            if (self.update_parent(mapa[i+1][j+1],minF)):
                                                mapa[i+1][j+1].parent = minF
                                            if (self.update_parent(mapa[i-1][j],minF)):
                                                mapa[i-1][j].parent   = minF
                                            if (self.update_parent(mapa[i-1][j-1],minF)):
                                                mapa[i-1][j-1].parent = minF
                                            if (self.update_parent(mapa[i-1][j+1],minF)):
                                                mapa[i-1][j+1].parent = minF
                                            if (self.update_parent(mapa[i][j-1],minF)):
                                                mapa[i][j-1].parent   = minF
                                            if (self.update_parent(mapa[i][j+1],minF)):
                                                mapa[i][j+1].parent   = minF
                                        else:
                                            if (self.update_parent(mapa[i-1][j],minF)):
                                                mapa[i-1][j].parent   = minF
                                            if (self.update_parent(mapa[i-1][j-1],minF)):
                                                mapa[i-1][j-1].parent = minF
                                            if (self.update_parent(mapa[i-1][j+1],minF)):
                                                mapa[i-1][j+1].parent = minF
                                            if (self.update_parent(mapa[i][j-1],minF)):
                                                mapa[i][j-1].parent   = minF
                                            if (self.update_parent(mapa[i][j+1],minF)):
                                                mapa[i][j+1].parent   = minF
                                    else:
                                            if (self.update_parent(mapa[i+1][j],minF)):
                                                mapa[i+1][j].parent   = minF
                                            if (self.update_parent(mapa[i+1][j-1],minF)):
                                                mapa[i+1][j-1].parent = minF
                                            if (self.update_parent(mapa[i+1][j+1],minF)):
                                                mapa[i+1][j+1].parent = minF
                                            if (self.update_parent(mapa[i][j-1],minF)):
                                                mapa[i][j-1].parent   = minF
                                            if (self.update_parent(mapa[i][j+1],minF)):
                                                mapa[i][j+1].parent   = minF
                for j in range(mapa_columnas):
                    for i in range(mapa_filas):
                        if  (mapa[i][j].parent==minF):
                            print("Mapa coordenadas: f y c")
                            print(i)
                            print(j)
                            if(self.check_list(mapa[i][j],close_list,open_list,target_node)):
                                open_list.append(mapa[i][j])
