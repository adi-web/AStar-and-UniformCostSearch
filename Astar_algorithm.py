
import math


def distance(vertex, goal):
    dx = abs(goal[0] -vertex[0] )
    dy=abs(goal[1]- vertex[1])
    d=abs((dx*dx)+(dy*dy))
    return round(math.sqrt(d),3)


def AStar(vertex_start, vertex_goal, graph):
    # lista che contiene nodi esaminati
    closedset=[]
    #lista che contiene nodi da esplorare
    openset=[]
    #lista per ricostruire il path
    came_from={}
    openset.append(graph.nodes[vertex_start])
    graph.nodes[vertex_start].setG(0)
    graph.nodes[vertex_start].setH(distance(vertex_start, vertex_goal))
    f_score= graph.nodes[vertex_start].getG() + graph.nodes[vertex_start].getH()
    graph.nodes[vertex_start].setF(f_score)

    print("Nodi esaminati in A*")
    print(" ")
    while openset is not []:
       current=openset[0]
       if current.getVertex()==(vertex_goal):
           #reconstruct_path(came_from,current)

          print("astar nodi esaminti: ")
          print(closedset.__len__())
          return print( reconstruct_path(came_from,current))

       print(current.getVertex())
       closedset.append(current)
       openset.remove(current)


       for node_current,node_neighbor in graph.neighbors[current.getVertex()].items():

            if node_neighbor in closedset:
                continue

            tentative_score= current.getG() + distance(current.getVertex(), node_neighbor.getVertex())
            # print(tentative_score)
            if node_neighbor not in openset or tentative_score < node_neighbor.getG():
                came_from[node_neighbor.getVertex()]=current
                node_neighbor.setG(tentative_score)
                node_neighbor.setH(distance(node_neighbor.getVertex(),vertex_goal))
                node_neighbor.setF(node_neighbor.getG()+distance(node_neighbor.getVertex(),vertex_goal))
                if node_neighbor not in openset:
                    openset.append(node_neighbor)
                    openset.sort(key=lambda node:node.f)

    return False


def reconstruct_path(came_from, current):
    total_path = [current.getVertex()]
    while current.getVertex() in came_from:
        current = came_from[current.getVertex()]
        total_path.append(current.getVertex())
    total_path.reverse()
    return total_path
