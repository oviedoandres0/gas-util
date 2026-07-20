import streamlit as st

st.title("Calculadora de Consumo de Combustible")

# Entradas del usuario
lt_100 = st.number_input("Consumo (L/100km):", value=11.8, step=0.1)
distance = st.number_input("Distancia recorrida (km):", value=195.5, step=0.1)

# Boton de calculo
if st.button("Calcular"):
    total_lt = (distance * lt_100) / 100
    gallons = total_lt / 3.785
    gallon_km = distance / gallons

    # Mostrar los resultados
    st.success(f"Resultados:")
    st.write(f"**Galones gastados:** {gallons:.2f} gal")
    st.write(f"**Rendimiento:** {gallon_km:.2f} km/gal")