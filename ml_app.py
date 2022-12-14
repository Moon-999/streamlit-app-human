import streamlit as st
import joblib 
import os
import numpy as np
import utils

def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model

def run_ml_app():
    st.subheader("머신러닝")

    with st.expander('데이터셋 정보'):
        st.markdown(utils.attrib_info)

    #layout
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('입력값 조정')
        sepal_length = st.number_input('Sepal length')
        sepal_width = st.number_input('Sepal Width')
        petal_length = st.number_input('Petal Length')
        petal_width = st.number_input('Petal Width')

        sample = [sepal_length, sepal_width, petal_length, petal_width]
        st.write(sample)

    with col2:
        st.subheader('예측 결과 확인')
        #리스트를 2차원 배열로 만듦
        single_sample = np.array(sample).reshape(1,-1)
        #st.write(single_sample.shape)
        #st.write(single_sample)

        #모델 불러오기
        model = load_model('models/logistic_regression_model_iris_221122.pkl')
        #st.write(model.classes_)
        prediction = model.predict(single_sample)
        pred_prob = model.predict_proba(single_sample)
        #st.write(prediction)
        #st.write(pred_prob)
        if prediction == 0:
            st.write('Setosa 확률:', np.round(pred_prob[0][0]*100, 2),"%")
            st.write('Versicolor 확률:', np.round(pred_prob[0][1]*100, 2),"%")
            st.write('Virginica 확률:', np.round(pred_prob[0][2]*100, 2),"%")
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Irissetosa1.jpg/220px-Irissetosa1.jpg')
            st.success('Setosa 종')
        elif prediction == 1:
            st.write('Setosa 확률:', np.round(pred_prob[0][0]*100, 2),"%")
            st.write('Versicolor 확률:', np.round(pred_prob[0][1]*100, 2),"%")
            st.write('Virginica 확률:', np.round(pred_prob[0][2]*100, 2),"%")
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/220px-Blue_Flag%2C_Ottawa.jpg')
            st.success('Versicolor 종')
        elif prediction == 2:
            st.write('Setosa 확률:', np.round(pred_prob[0][0]*100, 2),"%")
            st.write('Versicolor 확률:', np.round(pred_prob[0][1]*100, 2),"%")
            st.write('Virginica 확률:', np.round(pred_prob[0][2]*100, 2),"%")
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/220px-Iris_virginica_2.jpg')
            st.success('Virginica 종')
        else:
            pass