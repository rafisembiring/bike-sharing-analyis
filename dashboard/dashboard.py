import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("submission/data/day.csv")
hour_df = pd.read_csv("submission/data/hour.csv")

# Title
st.title("Dashboard Analisis Data Bike Sharing")

# Sidebar
st.sidebar.header("Filter Data")
season_filter = st.sidebar.selectbox("Pilih Musim", day_df['season'].unique())
weather_filter = st.sidebar.selectbox("Pilih Cuaca", day_df['weathersit'].unique())

# Filter Data
day_filtered = day_df[(day_df['season'] == season_filter) & (day_df['weathersit'] == weather_filter)]

# Visualisasi 1: Pengaruh Musim terhadap Penyewaan Sepeda
st.subheader("Pengaruh Musim terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x=day_df['season'], y=day_df['cnt'], ax=ax)
st.pyplot(fig)

# Visualisasi 2: Pengaruh Cuaca terhadap Penyewaan Sepeda
st.subheader("Pengaruh Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x=day_df['weathersit'], y=day_df['cnt'], ax=ax)
st.pyplot(fig)

# Visualisasi 3: Penyewaan Sepeda berdasarkan Jam
st.subheader("Jumlah Penyewaan Sepeda berdasarkan Jam")
fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(x=hour_df['hr'], y=hour_df['cnt'], estimator='mean', ci=None, ax=ax)
st.pyplot(fig)

st.sidebar.write("Dashboard by [Nama Anda]")
