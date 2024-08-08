
import math

def distance(vertex, goal):
    dx = abs(goal[0] -vertex[0] )
    dy=abs(goal[1]- vertex[1])
    d=abs((dx*dx)+(dy*dy))
    return round(math.sqrt(d),3)



def Uniform_Cost_Search(vertex_start, vertex_goal, graph):
    openset = []
    closedset = []
    openset.append(graph.nodes[vertex_start])
    graph.nodes[vertex_start].setG(0)
    came_from={}
    while openset is not []:
        current = openset[0]

        if current.getVertex() == (vertex_goal):
            print("Uniform cost")
            print(closedset.__len__())
            return print( reconstruct_path(came_from,current))

        print(current.getVertex())
        closedset.append(current)
        openset.remove(current)

        for node_current, node_neighbor in graph.neighbors[current.getVertex()].items():
            distance_node=current.getG()+distance(current.getVertex(), node_neighbor.getVertex())
            if node_neighbor not in openset and node_neighbor not in closedset:
                came_from[node_neighbor.getVertex()] = current
                node_neighbor.setG(distance_node)
                openset.append(node_neighbor)
            elif node_neighbor in openset and node_neighbor.getG()>distance_node:
                node_neighbor.setG(distance_node)
                came_from[node_neighbor.getVertex()] = current

            openset.sort(key=lambda node: node.g)


def reconstruct_path(came_from, current):
    total_path = [current.getVertex()]
    while current.getVertex() in came_from:
        current = came_from[current.getVertex()]
        total_path.append(current.getVertex())
    total_path.reverse()
    return total_path
