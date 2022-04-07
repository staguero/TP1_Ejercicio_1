class A_Star():
    def __init__(self,mapa,current_node,target_node):
        self.close_list=[]
        self.open_list=[]
        self.mapa = mapa
        self.current_node = current_node
        self.target_node = target_node
    
    def in_close_list(self,node):
        if node in self.close_list:
            return node
        else:
            return False
    
    def in_open_list(self,node):
        if node in self.open_list:
            return node
        else:
            return False

    def check_list(self,i,j):
        if self.mapa[i][j].id is not None:
            if self.mapa[i][j].id[0:5] == "Shelf":
                if self.mapa[i][j].id == self.target_node.id: 
                    self.close_list.append(self.mapa[i][j])
                return
        if self.in_close_list(self.mapa[i][j]):
            return
        
        self.mapa[i][j].G = self.mapa[i][j].parent.G + ( (self.mapa[i][j].parent.x-self.mapa[i][j].x)**2 + (self.mapa[i][j].parent.y-self.mapa[i][j].y)**2 ) **0.5
        self.mapa[i][j].H = ( (self.target_node.x-self.mapa[i][j].x)**2 + (self.target_node.y-self.mapa[i][j].y)**2 ) **0.5

        prev = self.in_open_list(self.mapa[i][j])
        if prev:
            if (self.mapa[i][j].G + self.mapa[i][j].H) < (prev.G + prev.H):
                self.open_list.remove(prev)
                self.open_list.append(self.mapa[i][j])
        else:
            self.open_list.append(self.mapa[i][j])

    def update_parent(self,old_parent,new_candidate):
        if old_parent.parent is not None:
            if (old_parent.parent.G>new_candidate.G):
                return True
            else:
                return False
        else:
            return True

    def min_F(self):
        minF = self.open_list[0]
        for node in self.open_list:
            if (node.G + node.H) <= (minF.G + minF.H):
                minF = node
        return minF
    
    def start_method(self,mapa_columnas,mapa_filas):
        path_list = []
        self.open_list.append(self.current_node)
        while True:
            tmp = self.in_close_list(self.target_node)
            if tmp:
                path_list = [[tmp.x, tmp.y]]
                while tmp.id is not self.current_node.id:
                    tmp = tmp.parent
                    path_list.append([tmp.x, tmp.y])

                path_list.reverse()
                return path_list
            else:
                minF = self.min_F()
                self.close_list.append(minF)
                self.open_list.remove(minF)
                for j in range(mapa_columnas):
                    for i in range(mapa_filas):
                        if self.mapa[i][j].x == minF.x:
                            if self.mapa[i][j].y == minF.y:
                                if (j>=mapa_columnas-1):
                                    if (i>=mapa_filas-1):
                                        if (self.update_parent(self.mapa[i-1][j-1],minF)):
                                            self.mapa[i-1][j-1].parent = minF
                                        if (self.update_parent(self.mapa[i][j-1],minF)):
                                            self.mapa[i][j-1].parent   = minF
                                        if (self.update_parent(self.mapa[i-1][j],minF)):
                                            self.mapa[i-1][j].parent   = minF
                                    else:
                                        if (self.update_parent(self.mapa[i-1][j],minF)):
                                            self.mapa[i-1][j].parent   = minF
                                        if (self.update_parent(self.mapa[i-1][j-1],minF)):                                        
                                            self.mapa[i-1][j-1].parent = minF
                                        if (self.update_parent(self.mapa[i][j-1],minF)):
                                            self.mapa[i][j-1].parent   = minF
                                        if (self.update_parent(self.mapa[i+1][j],minF)):
                                            self.mapa[i+1][j].parent   = minF
                                        if (self.update_parent(self.mapa[i+1][j-1],minF)):
                                            self.mapa[i+1][j-1].parent = minF                                      
                                if (j<=0) :
                                    if (i<=0):
                                        if (self.update_parent(self.mapa[i][j+1],minF)):
                                            self.mapa[i][j+1].parent   = minF
                                        if (self.update_parent(self.mapa[i+1][j],minF)):
                                            self.mapa[i+1][j].parent   = minF
                                        if (self.update_parent(self.mapa[i+1][j+1],minF)):
                                            self.mapa[i+1][j+1].parent = minF
                                    else:
                                        if (self.update_parent(self.mapa[i-1][j],minF)):
                                            self.mapa[i-1][j].parent   = minF
                                        if (self.update_parent(self.mapa[i-1][j+1],minF)):
                                            self.mapa[i-1][j+1].parent = minF
                                        if (self.update_parent(self.mapa[i][j+1],minF)):
                                            self.mapa[i][j+1].parent   = minF
                                        if (self.update_parent(self.mapa[i+1][j],minF)):
                                            self.mapa[i+1][j].parent   = minF
                                        if (self.update_parent(self.mapa[i+1][j+1],minF)):
                                            self.mapa[i+1][j+1].parent = minF
                                if  (j<mapa_columnas-1) and (j>0):
                                    if (i>0):
                                        if (i<mapa_filas-1):

                                            if (self.update_parent(self.mapa[i+1][j],minF)):
                                                self.mapa[i+1][j].parent   = minF
                                            if (self.update_parent(self.mapa[i+1][j-1],minF)):
                                                self.mapa[i+1][j-1].parent = minF
                                            if (self.update_parent(self.mapa[i+1][j+1],minF)):
                                                self.mapa[i+1][j+1].parent = minF
                                            if (self.update_parent(self.mapa[i-1][j],minF)):
                                                self.mapa[i-1][j].parent   = minF
                                            if (self.update_parent(self.mapa[i-1][j-1],minF)):
                                                self.mapa[i-1][j-1].parent = minF
                                            if (self.update_parent(self.mapa[i-1][j+1],minF)):
                                                self.mapa[i-1][j+1].parent = minF
                                            if (self.update_parent(self.mapa[i][j-1],minF)):
                                                self.mapa[i][j-1].parent   = minF
                                            if (self.update_parent(self.mapa[i][j+1],minF)):
                                                self.mapa[i][j+1].parent   = minF
                                        else:
                                            if (self.update_parent(self.mapa[i-1][j],minF)):
                                                self.mapa[i-1][j].parent   = minF
                                            if (self.update_parent(self.mapa[i-1][j-1],minF)):
                                                self.mapa[i-1][j-1].parent = minF
                                            if (self.update_parent(self.mapa[i-1][j+1],minF)):
                                                self.mapa[i-1][j+1].parent = minF
                                            if (self.update_parent(self.mapa[i][j-1],minF)):
                                                self.mapa[i][j-1].parent   = minF
                                            if (self.update_parent(self.mapa[i][j+1],minF)):
                                                self.mapa[i][j+1].parent   = minF
                                    else:
                                            if (self.update_parent(self.mapa[i+1][j],minF)):
                                                self.mapa[i+1][j].parent   = minF
                                            if (self.update_parent(self.mapa[i+1][j-1],minF)):
                                                self.mapa[i+1][j-1].parent = minF
                                            if (self.update_parent(self.mapa[i+1][j+1],minF)):
                                                self.mapa[i+1][j+1].parent = minF
                                            if (self.update_parent(self.mapa[i][j-1],minF)):
                                                self.mapa[i][j-1].parent   = minF
                                            if (self.update_parent(self.mapa[i][j+1],minF)):
                                                self.mapa[i][j+1].parent   = minF
                for j in range(mapa_columnas):
                    for i in range(mapa_filas):
                        if  (self.mapa[i][j].parent==minF):
                            self.check_list(i,j)
