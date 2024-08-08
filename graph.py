from node import Node


class Grapth:
    def __init__(self):
        self.nodes={}
        self.neighbors={}

    def add_node(self,x,y):
        position=(x,y)

        #utilizzo come indice in un dizionario position che sarebbe x e y del vertice del poligono
        #self.neighbors[position]="Funziona"
        #print(self.neighbors)
        # facendo cosi controllo se position esistente in nodes quindi controllo se la key c'è nel dizionario
        if position not in self.nodes:
            self.nodes[position]=Node(x,y)
            self.neighbors[position]={}
        else:
            print("nodo presente")

        return self.nodes[position]

    def add_neighbors(self,from_x,from_y,to_x,to_y):

        from_position=(from_x,from_y)
        to_position=(to_x,to_y)
        list_neighbors={}
        #list_neighbors=self.neighbors[from_position]
        #list_neighbors.append(Node(to_x, to_y))
        #self.neighbors[from_position]=list_neighbors
        self.neighbors[from_position][to_position]=self.add_node(to_x,to_y)
        self.neighbors[to_position][from_position]=self.nodes[from_position]


    def segmente_intersection(self,p1,p2,p3,p4): # avremmo che p[0] rappresenta x e p[1] la y nel piano xy

        if p1==7 and p2==2 and p3==4 and p4==2:
            print("df")
        if p1 is p3 or p1 is p4 or p3 is p2 or p2 is p4 :
            return False

        d1= self.orentation(p1, p2, p3)
        d2 = self.orentation(p1, p2, p4)
        d3 = self.orentation(p3, p4, p1)
        d4 = self.orentation(p3, p4, p2)

        # l'idea che dobbiamo avere le orientazione opposte per dire che abbiamo intersezione
        if ((d1>0 and d2<0) or (d1<0 and d2>0)) and ((d3>0 and d4<0) or (d3<0 and d4>0)):
            print("si")
            return True
        #elif (((d1 == 0 and d2 != 0) or (d2 == 0 and d1 != 0)) or ((d3 == 0 and d4 !=0 ) or (d4 == 0 and d3 !=0 ))) and (
           # self.on_segment(p1,p2,p3) or self.on_segment(p1,p2,p4) or self.on_segment(p3,p4,p1) or self.on_segment(p3,p4,p2)
        #):
           # print("si")
            #return True
        elif d1==0 and self.on_segment(p1,p2,p3): return True
        elif d2 == 0 and self.on_segment(p1, p2, p4):
            return True
        elif d3 == 0 and self.on_segment(p3, p4, p1):
            return True
        elif d1 == 4 and self.on_segment(p3, p4, p2):
            return True
        else:
           # self.add_neighbors(p1,p2,p3,p4)
            print("no intersection")
            return False


    def print_grapth(self):
        for key,node in self.nodes.items():
            print(node)
        # Iterating through the nested dictionary
        for position, neighbors_dict in self.neighbors.items():
            print(f"Position {position}:")
            for neighbor_position, node in neighbors_dict.items():
                pass
            print(f"  Neighbor position {neighbor_position}: {node}")



    #def vertex_straightline(self,start_vertex,end_vertex,polygon):
    #qua conviene passare lo start e il end e poi il polygon e andare a controllare se l'end puo
    #essere collegato direttamente
    #def vertex_straightline(self,number_pol,polygon,start_vertex):
        #print(len(polygon))
       # l=len(polygon)-1
        #self.add_node(start_vertex[0],start_vertex[1])

       # intersection=False
        #end_vertex=None
        #for i in range(len(polygon)):
           # if i==number_pol:
             #   continue
            #for end_vertex in polygon[i]:
                 #trovare qualche modo perche facendo cosi trovo start_vertex e con il secondo for trovo
                 # ogni vertex da controllare se può essere collegato direttamente con il primo vertex
                   #if polygon[i]>start_vertex[0]:
                        #continue
                  # end_vertex=j
                  # if self.segmente_intersection(start_vertex,end_vertex,polygon[i],polygon[i+1]) is True:
                       #intersection=True
                      # break


      #  if intersection is False:
           # self.add_neighbors(start_vertex[0],start_vertex[1], end_vertex[0], end_vertex[1])
           # self.nodes[(2,6)].setG(9)

    def vertex_straightline(self, start_vertex, end_vertex, polygon):

        self.add_node(start_vertex[0], start_vertex[1])
        intersection = False
        for index_pol in range(len(polygon)):

            if intersection is True:
                break

            #if index_pol==index:
                #self.add_neighbors(start_vertex[0], start_vertex[1], polygon[index_pol][1][0], polygon[index_pol][1][1])
                #self.add_neighbors(start_vertex[0], start_vertex[1], end_vertex[0], end_vertex[1])
                #continue

            for value_pol_control in range(len(polygon[index_pol])):
                if start_vertex[0]==5 and start_vertex[1]==2 and end_vertex[0]==7 and end_vertex[1]==2:
                    print("f")
                if value_pol_control == len(polygon[index_pol])-1:
                    next_vertex_control=0

                else:next_vertex_control=value_pol_control+1

                print(polygon[index_pol][value_pol_control])
                print(" e")
                print(polygon[index_pol][next_vertex_control])

                if self.segmente_intersection(start_vertex, end_vertex, polygon[index_pol][value_pol_control], polygon[index_pol][next_vertex_control]) is True:
                    intersection=True
                    break
                else:
                    #print("no intersection tra il segmento "+ start_vertex + " e "+ end_vertex+ " e il segmento :"+polygon[index_pol][value_pol_control] + " e "+polygon[index_pol][value_pol_control + 1] )
                    print("no intersection ")
        if intersection is False:
            self.add_neighbors(start_vertex[0],start_vertex[1], end_vertex[0], end_vertex[1])

    def orentation(self,p_first,p_second,p_third):

        #prodotto  vettoriale calcolo
        result=((p_second[0]-p_third[0])*(p_first[1]-p_third[1])-(p_first[0]-p_third[0])*(p_second[1]-p_third[1]))
        return result


    #funzione che controlla se siamo al bordo del segmento
    def on_segment(self,p1,p2,p3):
        if (min(p1[0],p2[0]) <= p3[0]<= max(p1[0],p2[0])) and (min(p1[1],p2[1]) <= p3[1]<= max(p1[1],p2[1])):
            return True
        else:
            return False


    def find_intersection(self,polygon,start_vertex,index):
        for index2 in range(len(polygon)):
            if index2 == index:
                continue
            for valure_in_pol2 in range(len(polygon[index2])):
                # qua troviamo l'end e vediamo se puo essere collegato direttamente
                end_vertex = polygon[index2][valure_in_pol2]
                # una volta avuto lo start e l'end si chiama la funzione vertex_straightline
                self.vertex_straightline(start_vertex, end_vertex, polygon)
