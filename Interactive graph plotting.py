#Plot and show a graph based on user input
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
class Graph:
    def __init__(self,num_nodes):
        self.num_nodes=num_nodes
        self.adjacency_list=[[] for _ in range(num_nodes)]
    def vertex(self):
        self.adjacency_list.append([])
        self.num_nodes+=1
    def edge(self,node1,node2):
        if node1<self.num_nodes and node2<self.num_nodes:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)
        else:
            if node1>=self.num_nodes and node2>=self.num_nodes:
                print("{} & {} are invalid nodes".format(node1,node2))
            else:
                print("{} is an invalid node".format(max(node1,node2)))
    def adj(self):
        Matrix=np.zeros((self.num_nodes,self.num_nodes))
        for i in range(self.num_nodes):
            for j in self.adjacency_list[i]:
                Matrix[i][j]=1
        return Matrix
    def print(self):
        adjacency_matrix=self.adj()
        graph=nx.from_numpy_array(adjacency_matrix)
        nx.draw(graph,with_labels=True)
        plt.show()
    def connected(self):
        for j in range(self.num_nodes):
            for k in range(self.num_nodes):
                if k<j:
                    self.edge(j,k)
a=int(input("Enter no. of nodes\n"))
e=int(a*(a-1)/2)
g=Graph(a)
t=input("Is the graph connected? Answer 'y' for yes, 'n' for no\n")
if t.lower()=='y':
    g.connected()
elif t.lower()=='n':
    b=int(input("Enter no. of connected edges\n"))
    if b>e:
        b=int(input(f"Edges cannot be more than {e}. Enter a number smaller than or equal to {e}\n"))
    print(f"Vertices start from 0 to {a-1}\n")
    for _ in range(b):
        c=int(input("Enter 1st vertex\n"))
        d=int(input("Enter 2nd vertex\n"))
        print(f"Edge is ({c},{d})")
        g.edge(c,d)
print(g.adj())
g.print()
u=input("Would you like to add new vertices? Answer 'y' for yes, 'n' for no\n")
if u.lower()=='y':
    v=int(input("Enter no. of vertices to be added\n"))
    h=0
    for _ in range(v):
        g.vertex()
        o=a+1
        f=int(a*(a-1)/2)
        h=h+1
    w=int(input("No. of connected edges of new vertices\n"))
    x=int(h*a+h*(h-1)/2)
    if w>x:
        w=int(input(f"Invalid no. of edges. Enter edges less than or equal to {x}\n"))
    print(f"Vertices start from 0 to {o}\n")
    for _ in range(w):
        c=int(input("Enter 1st vertex\n"))
        d=int(input("Enter 2nd vertex\n"))
        print(f"Edge is ({c},{d})\n")
        g.edge(c,d)
    print(g.adj())
    g.print()