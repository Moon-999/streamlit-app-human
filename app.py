# -*- coding: utf-8 -*-

#core pkgs
import streamlit as st

#data pkgs
import pandas as pd

#이미지 라이브러리
from PIL import Image

def main():
    """코드작성"""
    # 텍스트 Input
    fname = st.text_input('이름 입력')
    st.write(fname)

    #텍스트 Area
    message = st.text_area('입력해주세용!', height=100)
    st.write(message)

    # 숫자 입력
    number = st.number_input('숫자 입력')
    st.write(number)

    # 날짜
    myDate = st.date_input('날짜')
    st.write(myDate)

    #시간
    myTime = st.time_input('시간')
    st.write(myTime)

    #Color Picker
    color = st.color_picker('색상 선택')
    st.write(color)

if __name__=="__main__":
    main()