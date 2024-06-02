import streamlit as st
import math
import matplotlib.pyplot as plt

# Fonction pour calculer les valeurs du modèle M/M/S
def mms_model(λ, μ, S):
    A = λ / μ  # Trafic offert

    # Probabilité que le système soit vide (P0)
    sum_terms = sum([(A**k) / math.factorial(k) for k in range(S)])
    P0 = 1 / (sum_terms + (A**S / (math.factorial(S) * (1 - A/S))))

    # Probabilité d'attente (Pa)
    Pa = (P0 * (A**S) / (math.factorial(S) * (S - A)))

    # Nombre moyen de clients dans le système (<N>)
    N = A + (Pa * A / (S - A))

    # Nombre moyen de clients en attente (<Na>)
    Na = Pa * A / (S - A)

    # Nombre moyen de clients en service (au guichet) (<Ns>)
    Ns = A

    # Temps moyen de séjour dans le système (τ)
    τ = 1 / μ * (1 + Pa / (S - A))

    # Temps moyen d'attente (τa)
    τa = Pa / (μ * (S - A))

    return P0, Pa, N, Na, Ns, τ, τa

# Interface utilisateur Streamlit
st.title("Modèle M/M/S")
st.write("Entrez les paramètres du système :")

λ = st.number_input("Fréquence moyenne d'arrivées (λ)", value=5.0)
μ = st.number_input("Temps moyen de service (1/μ)", value=1.0)
S = st.number_input("Nombre de postes de travail disponibles (S)", value=3, step=1, min_value=1)

if st.button("Calculer"):
    μ = 1 / μ  # Conversion du temps moyen de service en taux de service
    P0, Pa, N, Na, Ns, τ, τa = mms_model(λ, μ, S)
    
    st.write("### Résultats")
    st.write(f"Probabilité que le système soit vide (P0) : {P0:.4f}")
    st.write(f"Probabilité d'attente (Pa) : {Pa:.4f}")
    st.write(f"Nombre moyen de clients dans le système (<N>) : {N:.4f}")
    st.write(f"Nombre moyen de clients en attente (<Na>) : {Na:.4f}")
    st.write(f"Nombre moyen de clients en service (au guichet) (<Ns>) : {Ns:.4f}")
    st.write(f"Temps moyen de séjour dans le système (τ) : {τ:.4f}")
    st.write(f"Temps moyen d'attente (τa) : {τa:.4f}")

    # Création des graphiques
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Graphique pour les probabilités
    labels = ['P0', 'Pa']
    values = [P0, Pa]
    ax[0].bar(labels, values, color=['blue', 'orange'])
    ax[0].set_title('Probabilités')
    ax[0].set_ylim(0, 1)

    # Graphique pour les nombres moyens
    labels = ['<N>', '<Na>', '<Ns>']
    values = [N, Na, Ns]
    ax[1].bar(labels, values, color=['green', 'red', 'purple'])
    ax[1].set_title('Nombres Moyens')

    st.pyplot(fig)