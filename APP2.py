import streamlit as st 

# main 함수만들기
def main():
    st.title('웹 대시보드 입니다')
    st.text('웹 대시보드 개발하기')
    name = '홍길동'
    st.text(' 제 이름은 {} 입니다'.format(name))
    st.header(' 이 영역은 헤더영역')
    st.subheader('이 곳은 서브영역')
    st.success('성공했을때의 메세지 영역')
    st.warning('경고 경고 조심하세요')
    st.info('정보를 보여주고 싶을때')
    st.error('문제가 발생했어요')
    st.help(range)
    st.help(sum)
if __name__=='__main__':
    main()