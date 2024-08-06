from grapth import Grapth
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

    pol=[]
    pol.append(polygon1)
    pol.append(polygon2)
    pol.append(polygon3)



    a=Grapth()
    print(pol)

    for index in range(len(pol)):
        for valure_in_pol in range(len(pol[index])):
            # valure_in_pol sarebbe il start_vertex che dobbiamo vedere con
            # quali altri nodi può essere collegato direttamente
            start_vertex=pol[index][valure_in_pol]
            a.add_node(start_vertex[0], start_vertex[1])
            if valure_in_pol == len(pol[index])-1:
                a.add_neighbors(start_vertex[0], start_vertex[1], pol[index][0][0],
                                pol[index][0][1])
            else:
                a.add_neighbors(start_vertex[0], start_vertex[1], pol[index][valure_in_pol + 1][0],
                            pol[index][valure_in_pol + 1][1])

            a.find_intersection(pol,start_vertex,index)
           # for index2 in range(len(pol)):
                #if index2==index:
                    #continue
              #  for valure_in_pol2 in range(len(pol[index2])):
                    #qua troviamo l'end e vediamo se puo essere collegato direttamente
                   # end_vertex=pol[index2][valure_in_pol2]

                    #una volta avuto lo start e l'end si chiama la funzione vertex_straightline
                   # a.vertex_straightline(start_vertex,end_vertex,pol)

    a.find_intersection(pol,( 4,2), -1)
    pol.append([(4,2)])
    a.find_intersection(pol, (11, 7), -1)

    for i in range(len(pol)):
        for j in pol[i]:
           print(j)
            #a.vertex_straightline(i,pol,j)

    #a.vertex_straightline((2,6),(7,5),polygon3)
    AStar((4, 2), (11, 7), a)
    a.add_node(4,3)




    #a.print_grapth()
