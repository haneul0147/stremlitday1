import streamlit as st
# 다른 파일에 있는 함수를 사용하기 위해서 Import 해왔다. 
from eda_app import run_eda_app 
from ml_app import run_ml_app
def main():
    st.title('파일 분리 앱')

    menu=['Home','EDA','ML','About']
    
    
    choice=st.sidebar.selectbox('메뉴',menu)
    if choice == 'Home':
        st.subheader('홈 화면 입니다')
    elif choice == 'EDA':
        run_eda_app()
    
    elif choice == 'ML':
        pass
    
    else:
        st.subheader('웹 소개 함수입니다.')

if __name__ == '__main__':
    main()