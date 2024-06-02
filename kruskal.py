import streamlit as st
import pandas as pd

# Fonction pour trouver le parent d'un nœud
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# Fonction pour unir deux sous-ensembles
def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

# Fonction pour appliquer l'algorithme de Kruskal
def kruskal(n, edges):
    result = []  # Pour stocker le MST
    i, e = 0, 0  # Variables de compteur
    edges = sorted(edges, key=lambda item: item[2])  # Trier les arêtes par poids
    parent = []
    rank = []
    for node in range(n):
        parent.append(node)
        rank.append(0)
    while e < n - 1:
        u, v, w = edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)
    return result

# Titre de l'application
st.title("Optimisation du Réseau de Transport")

# Entrer le nombre d'entrepôts
num_entrepots = st.number_input("Entrez le nombre d'entrepôts", min_value=2, step=1)

# Entrer les distances entre les entrepôts
if num_entrepots:
    st.write(f"Entrez les distances entre les {num_entrepots} entrepôts:")
    edges = []
    for i in range(num_entrepots):
        for j in range(i + 1, num_entrepots):
            distance = st.number_input(f"Distance entre l'entrepôt {i} et l'entrepôt {j} (en km)", min_value=0.0, step=0.1)
            if distance:
                edges.append((i, j, distance))

    # Calculer le réseau optimal lorsque toutes les distances sont entrées
    if len(edges) == (num_entrepots * (num_entrepots - 1)) // 2:
        mst = kruskal(num_entrepots, edges)
        total_cost = sum([w for u, v, w in mst])
        st.subheader("Réseau optimal de transport :")
        for u, v, w in mst:
            st.write(f"Entrepôt {u} - Entrepôt {v} : {w} km")
        st.subheader(f"Coût total du réseau : {total_cost} km")

if __name__ == "__main__":
    main()