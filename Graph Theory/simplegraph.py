#Simple implementation of an undirected graph using OOP

class Graph:
    
    graph = {"Vertices":[], "Edges":[]}

    def add_vertex(self, v):
        """
            Desc : This function enables you to add a new vertex to the graph
            Args : v (Integer or Str)
            Returns : None
        """

        if v not in self.graph["Vertices"]:
            self.graph["Vertices"].append(v)
        else:
            print(f"Vertex already in Graph at position { self.graph['Vertices'].index(v) }")

    def show_vertices(self):
        print(f"Vertices are : { ','.join(map(str, self.graph['Vertices'])) }")

    def add_edges(self, vertex, neighbor):
        """
            Desc : This function enables you to add edges to connect a vertext to another vertext or multiple
            Args: vertex and neighbor (int or str)
            Returns : None
        """

        assert (vertex in self.graph["Vertices"]) and (neighbor in self.graph["Vertices"]), "Vertex and Neighbor must be in Vertices, Check vertices using the show_vertices() method"

        #Since this is an undirected graph
        if [vertex, neighbor].sort() in list(map(sorted, self.graph["Edges"])):
            print(f"Edge {[vertex, neighbor]} already exists !")

        self.graph["Edges"].append([vertex, neighbor])

    def show_edges(self):
        print(f"Edges are {self.graph['Edges']}")


if __name__ == "__main__":
    g = Graph()
    g.add_vertex(5)
    g.add_vertex(6)
    g.add_vertex(8)
    g.add_vertex(5)
    g.show_vertices()

    g.add_edges(5, 8)
    g.show_edges()
    g.add_edges(1,5)


        
