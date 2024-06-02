import streamlit as st
import numpy as np

def prim_algorithm(num_buildings, cost_matrix):
    # Initialize the MST and the list of selected nodes
    mst = []
    selected_nodes = [False] * num_buildings
    selected_nodes[0] = True
    total_cost = 0

    for _ in range(num_buildings - 1):
        min_cost = float('inf')
        a = b = -1

        for i in range(num_buildings):
            if selected_nodes[i]:
                for j in range(num_buildings):
                    if not selected_nodes[j] and cost_matrix[i][j]:
                        if min_cost > cost_matrix[i][j]:
                            min_cost = cost_matrix[i][j]
                            a, b = i, j

        mst.append((a, b, min_cost))
        total_cost += min_cost
        selected_nodes[b] = True

    return mst, total_cost

def main():
    st.title("Calcul de l'Arbre Couvrant Minimal")

    num_buildings = st.number_input("Entrez le nombre de bâtiments :", min_value=2, step=1, value=2)
    
    st.write(f"Nombre de bâtiments : {num_buildings}")

    cost_matrix = np.zeros((num_buildings, num_buildings))

    for i in range(num_buildings):
        for j in range(i + 1, num_buildings):
            cost = st.number_input(f"Coût pour connecter le bâtiment {i} au bâtiment {j} :", min_value=0)
            cost_matrix[i][j] = cost
            cost_matrix[j][i] = cost

    if st.button("Calculer l'arbre couvrant minimal"):
        mst, total_cost = prim_algorithm(num_buildings, cost_matrix)
        st.write(f"Coût total de l'arbre couvrant minimal : {total_cost}")
        st.write("Arêtes de l'arbre couvrant minimal (format: (bâtiment 1, bâtiment 2, coût)):")
        for edge in mst:
            st.write(edge)

if __name__ == "__main__":
    main()