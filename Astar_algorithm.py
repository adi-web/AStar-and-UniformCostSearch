
import math


def distance(vertex, goal):
    dx = abs(goal[0] -vertex[0] )
    dy=abs(goal[1]- vertex[1])
    d=abs((dx*dx)+(dy*dy))
    return round(math.sqrt(d),2)


def AStar(vertex_start,vertex_goal,grapth):
    closedset=[]
    openset=[]
    came_from={}
    openset.append(grapth.nodes[vertex_start])
    grapth.nodes[vertex_start].setG(0)
    grapth.nodes[vertex_start].setH(distance(vertex_start, vertex_goal))
    f_score=grapth.nodes[vertex_start].getG()+grapth.nodes[vertex_start].getH()
    grapth.nodes[vertex_start].setF(f_score)


    while openset is not []:
       current=openset[0]
       if current.getVertex()==(vertex_goal):
           return "Funziona"

       closedset.append(current)
       openset.remove(current)

       for neighbor,node in grapth.neighbors[current.getVertex()].items():
            if node in closedset:
                continue

            tentative_score= current.getG() + distance(current.getVertex(), node.getVertex())
            print(tentative_score)
            if node not in openset or tentative_score < node.getG():
                came_from[node.getVertex()]=current
                node.setG(tentative_score)
                node.setF(node.getG()+distance(node.getVertex(),vertex_goal))
                if node not in openset:
                    openset.append(node)
                    openset.sort(key=lambda node:node.f)

    return False
