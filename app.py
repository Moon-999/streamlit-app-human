# -*- coding: utf-8 -*-

#core pkgs
import streamlit as st
import streamlit.components.v1 as stc

#다른 파일불러오기
from eda_app import run_eda_app
from ml_app import run_ml_app

dec_temp ="""
### IRIS 예측 모델 개발
- IRIS 데이터를 활용하여 간단한 EDA 및 예측 모델을 구현한다. 
#### 데이터
    + https://www.kaggle.com/datasets/saurabh00007/iriscsv
"""

def main():
    

    #메뉴 만들기
    menu = ['Home', '탐색적 자료 분석', '머신러닝', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home':
        html_temp = """
        <style type="text/css">
        .tg  {border-collapse:collapse;border-spacing:0;}
        .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
        overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
        font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg .tg-0lax{text-align:left;vertical-align:top}
        </style>
        <table class="tg">
        <thead>
        <tr>
            <th class="tg-0lax">강의명</th>
            <th class="tg-0lax">(산대특)_공공데이터 활용 빅데이터 분석 및 시각화 전문가 과정 육성</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td class="tg-0lax">교과목명</td>
            <td class="tg-0lax">기초문법</td>
        </tr>
        <tr>
            <td class="tg-0lax">프로젝트 주제</td>
            <td class="tg-0lax">파이썬 Streamlit 라이브러리를 활용한 IRIS 데이터 머신러닝 대시보드 개발</td>
        </tr>
        <tr>
            <td class="tg-0lax">프로젝트 마감일</td>
            <td class="tg-0lax">2022년 12월 8일</td>
        </tr>
        <tr>
            <td class="tg-0lax">수강생명</td>
            <td class="tg-0lax">정문희</td>
        </tr>
        </tbody>
        </table>
        """
        html_temp1 = '''
        <div style="background-color:#3872fb;padding:10px;border-radius:10px">
	        <h1 style="color:white;text-align:center;">IRIS 머신러닝 모형</h1>
        </div>
        '''
        stc.html(html_temp1)
        st.subheader('Home')
        st.markdown(html_temp, unsafe_allow_html=True)

        st.markdown(dec_temp, unsafe_allow_html=True)
    elif choice == '탐색적 자료 분석':
        html_temp = '''
        <div style="background-color:#3872fb;padding:10px;border-radius:10px">
	        <h1 style="color:white;text-align:center;">탐색적 자료 분석</h1>
        </div>
        ''' 
        stc.html(html_temp)
        #st.subheader('탐색적 자료 분석')
        run_eda_app()
    elif choice == '머신러닝':
        html_temp = '''
        <div style="background-color:#3872fb;padding:10px;border-radius:10px">
	        <h1 style="color:white;text-align:center;">머신러닝</h1>
        </div>
        ''' 
        stc.html(html_temp)
        run_ml_app()
    elif choice == 'About':
        st.subheader('About')
        dec_temp2 ="""
        ### Github주소
        - https://github.com/Moon-999/streamlit-app-human 
        #### 시각화 Dashboard 
        + iris.csv파일을 이용하여 자료를 분석하고 다양한 형태의 그래프를 작성해봄.
        + 머신러닝 모델을 만들어 입력값에 따른 예상결과를 나타낼 수 있음.
        """
        st.markdown(dec_temp2)
    else:
        pass



if __name__=="__main__":
    main()