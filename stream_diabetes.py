import pickle
import streamlit as st

# membaca model 
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# judul web
st.title('Prediksi Diabetes')

# menginput dan menampilkan gambar
uploaded_file1 = st.file_uploader("Upload Gambar 1", type=["jpg", "png", "jpeg"])
uploaded_file2 = st.file_uploader("Upload Gambar 2", type=["jpg", "png", "jpeg"])

if uploaded_file1 is not None and uploaded_file2 is not None:
    col1, col2 = st.columns(2)
    with col1:
        st.image(uploaded_file1, caption='Gambar 1', width=150)
    with col2:
        st.image(uploaded_file2, caption='Gambar 2', width=150)
elif uploaded_file1 is not None:
    st.image(uploaded_file1, caption='Gambar 1', width=150)
elif uploaded_file2 is not None:
    st.image(uploaded_file2, caption='Gambar 2', width=150)
    
# membagi kolom
col1, col2 = st.columns(2)

with col1:
    L_MPA = st.text_input('L-MPA')

with col2:
    L_LPA = st.text_input('R-MPA')

with col1:
    L_MCA = st.text_input('L-MCA')

with col2:
    L_LCA = st.text_input('R-MCA')

with col1:
    R_MPA = st.text_input('L-LPA')

with col2:
    R_LPA = st.text_input('R-LPA')

with col1:
    R_MCA = st.text_input('L-LCA')

with col2:
    R_LCA = st.text_input('R-LCA')

# code untuk prediksi
diab_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[L_MPA, L_LPA, L_MCA, L_LCA, R_MPA, R_LPA, R_MCA, R_LCA]])
    if diab_prediction[0] == 1:
        diab_diagnosis = 'Pasien terkena diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena diabetes'

    st.success(diab_diagnosis)
