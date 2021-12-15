from google.protobuf import message
import streamlit as st 

# 유저한테 입력하는 방법 
def main():
    name=st.text_input('이름을 입력하세요')
    st.title(name)

    name2=st.text_input('이름을 입력하세요',max_chars=5)
    st.title(name2)

    message= st.text_area('메세지를 입력하세요',height=3)
    st.text(message)
    #숫자 입력 
    number=st.number_input('숫자 입력하세요',1,100)
    st.text(number)
    # 실수 
    number2=st.number_input('숫자 입력하세요',0.0,20.0)
    st.text(number2)
   
   
   # 날짜 입력 
    my_data=st.date_input('약속 날짜 입력')
    st.write(my_data)
    # 프린트 문은 디버깅용이고,터미널에 출력된다.
    print(my_data)

    # 시간 받기 
    my_time=st.time_input('시간 선택')
    st.write(my_time)
    # 비밀번호 입력
    password = st.text_input('비밀번호 입력하세요',type='password',
    max_chars=12)
    st.write(password)
    # 색깔 입력 
    color=st.color_picker('색을 선택하세요')
    st.write(color)

if __name__=='__main__':
    main()