import streamlit as st

def main():
    st.title("Sélection de l'algorithme de graphe")

    # Options de la barre latérale
    option = st.sidebar.selectbox(
        "Choisissez l'algorithme à exécuter:",
        ("Prim", "Kruskal", "Dijkstra")
    )

    # Exécution du script en fonction de l'option sélectionnée
    if option == "Prim":
        st.write("Vous avez choisi l'algorithme de Prim.")
        # Importation et exécution du script prim.py
        import Prim
        Prim.main()
    elif option == "Kruskal":
        st.write("Vous avez choisi l'algorithme de Kruskal.")
        # Importation et exécution du script kruskal.py
        import kruskal
        kruskal.main()
    elif option == "Dijkstra":
        st.write("Vous avez choisi l'algorithme de Dijkstra.")
        # Importation et exécution du script dijkstra.py
        import dijkstra
        dijkstra.main()

if __name__ == "__main__":
    main()