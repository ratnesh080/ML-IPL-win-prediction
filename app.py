import streamlit as st
import pickle
import pandas as pd
teams=['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))

st.title('IPL win Predictor')

col1,col2=st.columns(2)

with col1:
    batting_team=st.selectbox('select the batting team',sorted(teams))
with col2:
    bowling_team=st.selectbox('select the bowling team',sorted(teams))

selected_cities=st.selectbox('select the host cities',sorted(cities))

target=st.number_input('Target')

col3,col4,col5=st.columns(3)

with col3:
    score=st.number_input('score')
with col4:
    over=st.number_input('over completed')
with col5:
    wickets=st.number_input('wickets out')

if st.button('Predict probability'):
    run_left=target-score
    ball_left=120-(6*over)
    wickets=10-wickets
    crr=score/over
    rrr=(run_left*6)/ball_left

    input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_cities],
                       'runs_left':[run_left],'balls_left':[ball_left],'wickets':[wickets],'total_runs_x':[target],
                       'crr':[crr],'rrr':[rrr]})
    result=pipe.predict_proba(input_df )
    loss=result[0][0]
    win=result[0][1]
    st.header(batting_team+"-"+str(round(win*100))+"%")
    st.header(bowling_team + "-" + str(round(loss*100)) + "%")