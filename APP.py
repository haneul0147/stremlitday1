# 스트림릿 라이브러리를 사용하기 위한 임포트문 작성방법

# 사이트를 통해 다운했을 경우에는 임포트 를 안해도 된다.
# pip install streamlit 

# 위에 라이브러리를 설치했으므로,임포트만 하면 된다.
import streamlit as st 

# 웹 대시보드 개발 라이브러리 스트림릿은
# main 함수가 있어야 한다.

def main() :
    st.title('hello streamlit. 앱 데시보드 ')
    st.title('헬로우 안녕')
    
if __name__=='__main__':
    main()
