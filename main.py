from Uniform_Cost_Search_algorithm import Uniform_Cost_Search
from graph import Grapth
from Astar_algorithm import AStar

if __name__ == '__main__':




    #Inserimento nuovi poligoni

   # quadrato1=[(2, 6), (2, 9), (5, 9), (5, 6)]
   # quadrato2=[(7, 2), (7, 5), (11, 5), (11, 2)]
   # quadrato3=[(5, 2), (5, 3), (6, 3), (6, 2)]
   # pol=[]
    #pol.append(quadrato1)
   # pol.append(quadrato2)
    #pol.append(quadrato3)

    triangolo=[(5,6),(5,11),(10,8)]
    polygon2=[(11,6),(13,9),(17,7),(16,3),(13,2)]
    pol=[]
    pol.append(triangolo)
    pol.append(polygon2)



    graph_create=Grapth()
    print(pol)

    for index_pol in range(len(pol)):
        for index_vertex_pol in range(len(pol[index_pol])):
            # start_vertex identifica il primo vertice che devo collegare con il vertice end_vertex
            start_vertex=pol[index_pol][index_vertex_pol]
            graph_create.add_node(start_vertex[0], start_vertex[1])


            #permette di salvare i neighbors dello stesso poligono identificato da index_pol
            if index_vertex_pol == len(pol[index_pol])-1:
                graph_create.add_neighbors(start_vertex[0], start_vertex[1], pol[index_pol][0][0],
                                           pol[index_pol][0][1])
            else:
                graph_create.add_neighbors(start_vertex[0], start_vertex[1], pol[index_pol][index_vertex_pol + 1][0],
                                           pol[index_pol][index_vertex_pol + 1][1])

            #funzione che permette di identificare con quali vertici end_vertex possiamo collegare lo start_vertex in linea retta
            graph_create.find_intersection(pol, start_vertex, index_pol)



    #add vertice start
    # graph_create.find_intersection(pol,start, -1)
    graph_create.find_intersection(pol,( 4,10.7), -1)
    pol.append([( 4,10.7)])

    #add vertice end
    #graph_create.find_intersection(pol,goal , -1)
    graph_create.find_intersection(pol, (18, 2), -1)

    graph_create.print_grapth()
    #AStar(( 4,10.7), (18, 2), graph_create)
    #Uniform_Cost_Search(( 4,10.7), (18, 2), graph_create)
