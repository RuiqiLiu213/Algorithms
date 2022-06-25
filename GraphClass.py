import collections
import heapq

class Graph:
    '''
    self.graph_list:[[node1,node2,weight],[node1,node3,weight]...]
    self.graph_dict: {'node1': [(node2,weight), (node3,weight) ...],
                     'node2': [(node3,weight), (node4,weight),...],
                     ...}
    '''
    def __init__(self, _graph_list):
        if _graph_list == None:
            _graph_list = []
        self.graph_list = _graph_list
        self.graph_dict = collections.defaultdict(list)
        self.vertex = set()
        
        if self.graph_list:
            for (u,v,w) in self.graph_list:
                self.graph_dict[u].append((v, w))
                self.vertex.add(u)
                self.vertex.add(v)
                 
    def add_edge(self, node1, node2, weight=float('inf')):
        self.graph_list.append([node1,node2,weight])
        self.graph_dict[node1].append((node2, weight))
        self.vertex.add(u)
        self.vertex.add(v)
    
    def create_matrix(self):
        n = len(self.vertex)
        matrix = [[0]*n for i in range(n)]
        for (u,v,w) in self.graph_list:
            matrix [u][v] = w
        return matrix
        
    def print_adj_list(self):
        for key in self.graph_dict.keys():
            print("node", key, ": ", self.graph_dict[key])
        
            
            
    # ——————————————————————————————Algorithm—————————————————————————————————
    def Dijkstra(self, src):
        '''
        Time complexity: O(V^2) 
        
        Parameters
        src : String/Int
            indicating source node.

        Returns
        shortest_path: dic
        '''
        shortest_path = dict()
        edges = self.graph_dict
        if len(edges) < 2:
            return
        
        visited = set()
        h = [(0, src)]
        
        while (h):
            (w1 , n1) = heapq.heappop(h)
            if n1 in visited:
                continue
            visited.add(n1)
            shortest_path[n1] = w1
            
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(h, (w1 + w2 ,n2))
            
        return shortest_path
    
    
    def find_subtree(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_subtree(parent, parent[i])
            
    def kruskals_mst(self):
        '''
        Time complexity: O(V*log(V))

        '''
        # Resulting tree
        vertex_list = list(self.vertex)
        result = []
        
        # Iterator
        i = 0
        # Number of edges in MST
        e = 0
    
        # Sort edges by their weight
        self.graph_list = sorted(self.graph_list, key=lambda item: item[2])
        
        # Auxiliary arrays
        parent = []
        subtree_sizes = []
    
        # Initialize `parent` and `subtree_sizes` arrays
        for node in range(len(vertex_list)):
            parent.append(node)
            subtree_sizes.append(0)
    
        # Important property of MSTs
        # number of egdes in a MST is 
        # equal to (len(self.vertex) - 1)
        while e < (len(vertex_list) - 1):
            # Pick an edge with the minimal weight
            u, v, weight = self.graph_list[i]
            i = i + 1
            
            u_index = vertex_list.index(u)
            v_index = vertex_list.index(v)
            # find the index(place) of parent nodes
            x = self.find_subtree(parent, u_index)
            y = self.find_subtree(parent, v_index)
    
            if x != y:
                e = e + 1
                result.append([u, v, weight])
                # connect subtree
                parent[y] = x
        
        # Print the resulting MST
        for node1, node2, weight in result:
            print("%d - %d: %d" % (node1, node2, weight))
            
    def prims_mst(self):
        '''
        Time complexity: O(V^2)

        '''
        
        
# Create a graph G        
G = Graph([[0,1,6],[0,2,2],[2,1,1],[2,3,7],[1,3,1],[0,3,1]])

# Dijkstra
shortest_path = G.Dijkstra(0)
print(shortest_path)
G.kruskals_mst()
#G.prims_mst()