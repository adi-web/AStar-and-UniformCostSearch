from node import Node


class Grapth:
    def __init__(self):
        self.nodes={}
        self.neighbors={}

    def add_node(self,x,y):

        # position è un indice utilizzando come key nel dizionario
        position=(x,y)

        #controllo se il nodo esiste nel dizionario
        if position not in self.nodes:
            self.nodes[position]=Node(x,y)
            self.neighbors[position]={}
        else:
            print("nodo presente")

        return self.nodes[position]

    # funzione per inserire i neighbors
    def add_neighbors(self,from_x,from_y,to_x,to_y):

        from_position=(from_x,from_y)
        to_position=(to_x,to_y)

        self.neighbors[from_position][to_position]=self.add_node(to_x,to_y)
        self.neighbors[to_position][from_position]=self.nodes[from_position]


    def segment_intersection(self, p1, p2, p3, p4): # avremmo che p[0] rappresenta x e p[1] la y nel piano xy

        if p1 is p3 or p1 is p4 or p3 is p2 or p2 is p4 :
            return False

        d1= self.orentation(p1, p2, p3)
        d2 = self.orentation(p1, p2, p4)
        d3 = self.orentation(p3, p4, p1)
        d4 = self.orentation(p3, p4, p2)

        # l'idea che dobbiamo avere le orientazione opposte per dire che abbiamo intersezione
        if ((d1>0 and d2<0) or (d1<0 and d2>0)) and ((d3>0 and d4<0) or (d3<0 and d4>0)):
            #print("Interesezione")
            return True

        elif d1==0 and self.on_segment(p1,p2,p3):
            return True
        elif d2 == 0 and self.on_segment(p1, p2, p4):
            return True
        elif d3 == 0 and self.on_segment(p3, p4, p1):
            return True
        elif d1 == 4 and self.on_segment(p3, p4, p2):
            return True
        else:
            #print("no intersection")
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


    def vertex_straightline(self, start_vertex, end_vertex, polygon):

        self.add_node(start_vertex[0], start_vertex[1])
        intersection = False

        for index_pol in range(len(polygon)):

            #se trovo un intersezione interrompo la ricerca dell'intersezione
            if intersection is True:
                break

            for index_vertex_pol in range(len(polygon[index_pol])):

                # condizione che mi permette di trovare il vertice iniziale del poligono che sto esaminando
                if index_vertex_pol == len(polygon[index_pol])-1:
                    next_vertex_control=0

                else:next_vertex_control=index_vertex_pol+1

                #print(polygon[index_pol][index_vertex_pol])
                #print(" e")
                #print(polygon[index_pol][next_vertex_control])


                # polygon[index_pol][index_vertex_pol] e polygon[index_pol][next_vertex_control] formano un segmento
                # che dobbiamo verificare utilizzando segmnet_intersection se abbiamo un intersezione con il segmento formato da
                # start_vert ed exend_vertex
                if self.segment_intersection(start_vertex, end_vertex, polygon[index_pol][index_vertex_pol], polygon[index_pol][next_vertex_control]) is True:
                    intersection=True
                    break
                else:
                    #print("no intersection tra il segmento "+ start_vertex + " e "+ end_vertex+ " e il segmento :"+polygon[index_pol][index_vertex_pol] + " e "+polygon[index_pol][index_vertex_pol + 1] )
                    print("no intersection ")


        if intersection is False:
            #permette di inserire al nodo(star_vertex) un vicino che il nodo(end_vertex)
            self.add_neighbors(start_vertex[0],start_vertex[1], end_vertex[0], end_vertex[1])

    def orentation(self,p_first,p_second,p_third):

        #calcolo il risultato del prodotto vettoriale
        result=((p_second[0]-p_third[0])*(p_first[1]-p_third[1])-(p_first[0]-p_third[0])*(p_second[1]-p_third[1]))
        return result


    #funzione che controlla se siamo al bordo del segmento
    def on_segment(self,p1,p2,p3):
        if (min(p1[0],p2[0]) <= p3[0]<= max(p1[0],p2[0])) and (min(p1[1],p2[1]) <= p3[1]<= max(p1[1],p2[1])):
            return True
        else:
            return False



    def find_intersection(self, polygon, start_vertex, index_start_vertex):
        for index_pol in range(len(polygon)):

            if index_pol == index_start_vertex:
                continue
            for index_vertex in range(len(polygon[index_pol])):

                end_vertex = polygon[index_pol][index_vertex]

                # una volta avuto lo start e l'end si chiama la funzione vertex_straightline che permette di identificare se
                #possiamo collegare start e end con una linea retta senza intersezioni
                self.vertex_straightline(start_vertex, end_vertex, polygon)
