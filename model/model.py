import networkx as nx

from UI.controller import Controller
from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.states = DAO.getStates()
        self.idMapS = {}
        for state in self.states:
            self.idMapS[state.id] = state

    def getShapes(self,anno):
        self.anno=anno
        return DAO.getShapes(anno)
    def buildGraph(self,shape):
        self.grafo.add_nodes_from(self.states)
        edges = DAO.getEdges(self.idMapS)
        for edge in edges:
            self.grafo.add_edge(edge[0],edge[1],weight=DAO.getWeight(edge[0].id,edge[1].id,self.anno,shape))
        print(len(self.grafo.edges))
        tupla = []
        for node in self.grafo.nodes:
            vicini = nx.neighbors(self.grafo,node)
            sum=0
            for v in vicini:
                sum+=self.grafo[node][v]["weight"]
            tupla.append((node,sum))
        return tupla
    def getDetails(self):
        return f"{len(self.grafo.nodes)} e {len(self.grafo.edges)} archi"
