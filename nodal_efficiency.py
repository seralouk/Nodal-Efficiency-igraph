from numpy import *
from igraph import *

def nodaleff(g):
    """
    This function returns the nodal efficiency of all nodes of a graph object.
    
    Input
    ------
    g: an iGraph graph object
    
    Output
    ne: nodal efficiency of all the nodes
    ------
    
    """
    g.es["weight"] = [1.0 / x for x in g.es["weight"]]
    sp = g.shortest_paths_dijkstra(weights=g.es["weight"])
    sp = asarray(sp)
    temp =1/sp
    fill_diagonal(temp,0)
    N=temp.shape[0]
    ne= ( 1.0 / (N-1)) * apply_along_axis(sum,0,temp)
    return ne

if __name__ =="__main__":
    
    g=Graph.Erdos_Renyi(100,0.7)
    g.es['weight'] = random.random(g.ecount())
    print("The number of nodes is:{}".format(g.vcount()))
    print("the nodal eff of each node is: {}".format(nodaleff(g)))
