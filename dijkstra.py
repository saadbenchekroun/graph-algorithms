import streamlit as st
import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

def main():
    st.title("Algorithme de Dijkstra - Trouver le chemin le plus court")

    st.sidebar.title("Entrer les données du graphe")

    num_nodes = st.sidebar.number_input("Nombre de nœuds", min_value=2, max_value=20, value=5, step=1)
    nodes = [st.sidebar.text_input(f"Nom du nœud {i+1}", f"N{i+1}") for i in range(num_nodes)]

    graph = Graph()
    for node in nodes:
        graph.add_node(node)

    num_edges = st.sidebar.number_input("Nombre d'arêtes", min_value=1, max_value=50, value=5, step=1)
    edges = []
    for i in range(num_edges):
        from_node = st.sidebar.selectbox(f"Arête {i+1} - Départ", nodes, key=f"from_node_{i}")
        to_node = st.sidebar.selectbox(f"Arête {i+1} - Arrivée", nodes, key=f"to_node_{i}")
        distance = st.sidebar.number_input(f"Arête {i+1} - Distance", min_value=1, value=1, key=f"distance_{i}")
        edges.append((from_node, to_node, distance))
        graph.add_edge(from_node, to_node, distance)

    start_node = st.sidebar.selectbox("Nœud de départ", nodes)
    
    if st.sidebar.button("Calculer le plus court chemin"):
        distances, path = dijkstra(graph, start_node)
        st.write("Distances depuis le nœud de départ:")
        st.write(distances)
        st.write("Arbre des chemins les plus courts:")
        st.write(path)

if __name__ == "__main__":
    main()