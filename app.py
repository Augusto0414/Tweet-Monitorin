import streamlit as st # web development
import numpy as np # np mean, np random
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop
import plotly.express as px # interactive charts

# read csv from a github repo
df = pd.read_csv("tweets.csv")


st.set_page_config(
    page_title = 'Real-Time Data Twitter Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Real-Time / Live Data Twitter Dashboard")

# top-level filters



# creating a single-element container.
placeholder = st.empty()

# dataframe filter


# near real-time / live feed simulation

for seconds in range(200):
    # while True:


    # creating KPIs
    number_seguidores = np.mean(df['seguidores'])

    number_seguidos = np.mean(df['seguidos'])


    number_tweet = np.mean(df['tweets'])

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(label="Seguidores 👨🏼‍💻", value=round(number_seguidores), delta=round(number_seguidores) - 10)
        kpi2.metric(label="seguidos 👨🏼", value=round(number_seguidos), delta=round(number_seguidos) - 10)
        kpi3.metric(label="Numero de Tweets 🔥", value=round(number_tweet), delta=round(number_tweet)-10)


        # create two columns for charts

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(data_frame=df, y='seguidores', x='seguidos')
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x='seguidores')
            st.write(fig2)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
    # placeholder.empty()



