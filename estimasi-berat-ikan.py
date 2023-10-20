import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder

model = pickle.load(open('estimasi_ikan.sav', 'rb'))

st.title('Estimasi Berat Ikan Dalam gram')

Species = st.selectbox('Pilih Spesies', ['Perch', 'Bream', 'Roach', 'Pike', 'Smelt', 'Parkki', 'Whitefish'])
Length1 = st.number_input('Input Panjang vertikal dalam cm')
Length2 = st.number_input('Input Panjang diagonal dalam cm')
Length3 = st.number_input('Input Panjang silang dalam cm')
Height = st.number_input('Input Tinggi dalam cm')
Width = st.number_input('Input Lebar diagonal dalam cm')

label_encoder_spec = LabelEncoder()
label_encoder_spec.fit(['Perch', 'Bream', 'Roach', 'Pike', 'Smelt', 'Parkki', 'Whitefish'])
spec_encoded = label_encoder_spec.transform([Species])[0]

predict = ''

if st.button('Estimasi Berat Ikan'):
    predict = model.predict(
        [[spec_encoded,Length1,Length2,Length3,Height,Width]]
    )
    st.write ('Estimasi Berat Ikan Dalam gram : ', predict)
