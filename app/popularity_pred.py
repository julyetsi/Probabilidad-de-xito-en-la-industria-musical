import pickle
import os
import pandas as pd
import streamlit as st

# Cargar el modelo RandomForestRegressor desde el archivo .pkl
directorio_actual = os.getcwd()
#modelo_path = 'random_forest_model'

with open(os.path.join(directorio_actual, '..', 'Models', 'pkls', 'KNN','knn_model.pkl'), 'rb') as archivo_entrada:
    modelo = pickle.load(archivo_entrada)
 
def classify (num):
     song_name = st.text_input('Enter the song name:')
     if num > 0.8:
        st.success(f'The predicted success probability for "{song_name}" is {num:.2%}. ¡Esto definitivamente va a salir bien!')
     elif num > 0.5:
        st.success(f'The predicted success probability for "{song_name}" is {num:.2%}. ¡Tu canción tiene buenas posibilidades')
     else:
        st.success(f'The predicted success probability for "{song_name}" is {num:.2%}. Haz algunos ajustes a tu track y vuelve para intentarlo de nuevo.')
#song_name = st.text_input('Enter the song name:')
#funcion para clasificar el éxito
def main():
    st.title('Spotify Song Success Predictor')
    st.sidebar.header("Parámetros")
    # Widget para ingresar el nombre de la canción
    song_name = st.text_input('Enter the song name:')

    def user_input_parameters():
        danceability = st.slider('Danceability', 0.0, 1.0, 0.5)
        energy = st.slider('Energy', 0.0, 1.0, 0.5)
        valence = st.slider('Valence', 0.0, 1.0, 0.5)
        data= {'name' : song_name,
               "danceability" : danceability,
               "energy" : energy,
               "valence" : valence}
        
        features = pd.DataFrame(data, index = [0])
        return features
    
    df = user_input_parameters()
    
    option = ['Random Forest Model']
    model = st.sidebar.selectbox('Modelo',option)

    st.subheader( 'User Input Parameters')
    st.subheader(model)
    st.write(df)
    
    if st.button('Predecir'):
        if model == "Random Forest Model":
            st.success(classify(modelo.predict(df)))


