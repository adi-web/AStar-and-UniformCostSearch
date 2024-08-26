from Uniform_Cost_Search_algorithm import Uniform_Cost_Search
from graph import Grapth
from Astar_algorithm import AStar

if __name__ == '__main__':


    list_polgon=[]
    #quadrato1={1:[(2,6),(5,6)],2:[(2,6),(2,9)],3:[(2,9),(5,9)],4:[(5,9),(5,6)]}
    #print(quadrato1[1][0])

    # in questo caso dal vertice 2,6 si collega al 2,9 che di conseguenza si collega al 5,9 che si collega
    # a 5,6 però da ricordarsi che 5,6 di collega a 2,6
    polygon1=[(2,6),(2,9),(5,9),(5,6)]
    polygon2=[(7,2),(7,5),(11,5),(11,2)]
    polygon3=[(5,2),(5,3),(6,3),(6,2)]
    #polygon1=[(5,6),(5,11),(10,8)]
    #polygon2=[(11,6),(13,9),(17,7),(16,3),(13,2)]
    pol=[]
    pol.append(polygon1)
    pol.append(polygon2)
    pol.append(polygon3)



    a=Grapth()
    print(pol)

    for index_pol in range(len(pol)):
        for index_vertex_pol in range(len(pol[index_pol])):
            # start_vertex identifica il primo vertice che devo collegare con il vertice end_vertex
            start_vertex=pol[index_pol][index_vertex_pol]
            a.add_node(start_vertex[0], start_vertex[1])


            #permette di salvare i neighbors dello stesso poligono identificato da index_pol
            if index_vertex_pol == len(pol[index_pol])-1:
                a.add_neighbors(start_vertex[0], start_vertex[1], pol[index_pol][0][0],
                                pol[index_pol][0][1])
            else:
                a.add_neighbors(start_vertex[0], start_vertex[1], pol[index_pol][index_vertex_pol + 1][0],
                                pol[index_pol][index_vertex_pol + 1][1])

            #funzione che permette di identificare con quali vertici end_vertex possiamo collegare lo start_vertex in linea retta
            a.find_intersection(pol, start_vertex, index_pol)



   # a.find_intersection(pol,( 3,11), -1)
   # pol.append([( 3,11)])
    a.find_intersection(pol, (13,4), -1)

    for i in range(len(pol)):
        for j in pol[i]:
           print(j)
            #a.vertex_straightline(i,pol,j)

    #a.vertex_straightline((2,6),(7,5),polygon3)
    AStar( ( 2,9),(13, 4), a)
    Uniform_Cost_Search(( 2,9), (13, 4), a)
