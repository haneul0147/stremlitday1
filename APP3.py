<<<<<<< HEAD
import streamlit as st
import pandas as pd

def main():
    df=pd.read_csv('data/iris.csv')
    st.dataframe(df)
    species=df['species'].unique()
    st.text('아이리스 꽃은' + species+'으로 되어있다.')
    st.write(df.head())

if __name__=='__main__':
=======
import streamlit as st
import pandas as pd

def main():
    df=pd.read_csv('data/iris.csv')
    st.dataframe(df)
    species=df['species'].unique()
    st.text('아이리스 꽃은' + species+'으로 되어있다.')
    st.write(df.head())

if __name__=='__main__':
>>>>>>> ec64fbbfdfbc15644b38cc90f56e3d671e0181b7
    main()