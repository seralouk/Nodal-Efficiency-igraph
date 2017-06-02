from numpy import *
from igraph import *


g=Graph.Erdos_Renyi(100,0.7)
g.es['weight'] = random.random(g.ecount())
print("The number of nodes is:{}".format(g.vcount()))

def nodaleff(g):

    g.es["weight"] = [1.0 / x for x in g.es["weight"]]
    sp = g.shortest_paths_dijkstra(weights=g.es["weight"])
    sp = asarray(sp)
    temp =1/sp
    fill_diagonal(temp,0)
    N=temp.shape[0]
    ne= ( 1.0 / (N-1)) * apply_along_axis(sum,0,temp)
    return ne

if __name__ =="__main__":
    print("the nodal eff of each node is: {}".format(nodaleff(g)))