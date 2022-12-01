import streamlit as st
import utils
import pandas as pd 
#그래프 그릴때
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

def load_data(path):
    #csv 파일 가졍로 시
    df = pd.read_csv(path)
    return df

    #DB에서 가져올 경우

    #크롤링해서 가져올 경우

def run_eda_app():
    with st.expander('데이터셋 정보'):
        st.markdown(utils.attrib_info)

    #데이터셋 불러오기
    DATA_PATH = 'data/iris.csv'
    iris_df = load_data(DATA_PATH)

    #st.dataframe(iris_df)

    #서브메뉴 지정
    submenu = st.sidebar.selectbox("서브메뉴", ['기술통계량', '그래프'])
    if submenu == '기술통계량':
        st.subheader('기술통계량')
        st.write('모든 데이터')
        st.dataframe(iris_df.style.highlight_max(axis=0), width=1000, height=200)

        with st.expander('데이터 타입'):
            df2 = pd.DataFrame(iris_df.dtypes).transpose()
            df2.index = ['구분']
            st.dataframe(df2)

        with st.expander('기술 통계량'):
            st.dataframe(pd.DataFrame(iris_df.describe()).transpose())

        st.write('타겟분포')
        st.dataframe(iris_df['species'].value_counts())


    elif submenu == '그래프':
        st.subheader('그래프')

    
        # Tabs
        tab1, tab3, tab4 = st.tabs(['산점도', '히스토그램', '박스플롯'])
        with tab1:
            st.write('산점도 (Scatter plot)는 두 변수의 상관 관계를 직교 좌표계의 평면에 점으로 표현하는 그래프입니다.')
            with st.expander('산점도'):
            #plotly 그래프
                fig1 = px.scatter(iris_df, 
                                    x = 'sepal_width', 
                                    y = 'sepal_length',
                                    color = 'species',
                                    size = 'petal_width',
                                    hover_data = ['petal_length'],
                                    title = 'IRIS 산점도')
                st.plotly_chart(fig1)
            val_species = st.selectbox('종 선택', ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'))
            st.write('종 선택:', val_species)

            result = iris_df[iris_df['species'] == val_species]
            #st.dataframe(result)

            val_x = st.selectbox('x축 선택', ('sepal_width', 'petal_width'))
            val_y = st.selectbox('y축 선택', ('sepal_length', 'petal_length'))
            fig2 = px.scatter(result, x = val_x, y=val_y, size='petal_width')
            st.plotly_chart(fig2)

        with tab3:
            st.write('히스토그램 (Histogram)은 도수분포표를 그래프로 나타낸 것으로서, 가로축은 계급, 세로축은 도수 (횟수나 개수 등)를 나타냅니다.')
            sel1 = st.selectbox('컬럼 선택', ('sepal_width', 'petal_width', 'sepal_length', 'petal_length'))
            sel2 = st.selectbox('히스토그램 타입 선택', ('bar', 'step'))
            fig, ax = plt.subplots()
            ax.hist(iris_df[sel1], label='bins=10', histtype=sel2)
            ax.hist(iris_df[sel1], bins=30, label='bins=30', histtype=sel2)
            ax.set_title(sel1 + "-" + sel2)
            ax.legend()
            st.pyplot(fig)
        
        with tab4:
            st.write('박스 플롯은 "상자 수염 그림"(Box-and-Whisker Plot) "상자 그림" 등 다양한 이름으로 불린다.') 
            st.write('박스 플롯을 사용하는 이유는 많은 데이터를 눈으로 확인하기 어려울 때 그림을 이용해 데이터 집합의 범위와 중앙값을 빠르게 확인할 수 있는 목적으로 사용한다. 또한 통계적으로 이상치(outlier)가 있는지도 확인이 가능하다.')
            # seaborn 그래프
        
            val_x = st.selectbox('y축 선택', ('sepal_width', 'petal_width', 'sepal_length', 'petal_length'))
            fig, ax = plt.subplots()
            green_diamond = dict(markerfacecolor='g', marker='D')
            sns.boxplot(iris_df, x = 'species', y = val_x, hue="species", flierprops=green_diamond, ax = ax)
            st.pyplot(fig)



    else:
        pass