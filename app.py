import streamlit as st
import secret_santa
from io import StringIO
import pandas as pd

st.title('Secret Santa 🎅!!')

st.write('NOTE: File should be a txt file with each name in each line.')
uploaded_file = st.file_uploader("Choose a file.")
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    names = secret_santa.read_names(stringio)
    st.subheader('List of names in the input file: ')
    st.write(', '.join(names))

    secret_santa.shuffle_names(names)
    print(names)

    result = secret_santa.secret_santa_to_list(names)

    st.subheader('Output: ')
    st.write('NOTE: Download the file from below button')
    df = pd.DataFrame.from_dict(result)
    st.table(df)
    secret_santa.file_write_list(result)
    with open('result.txt') as f:
        st.download_button('Download Output File', f)