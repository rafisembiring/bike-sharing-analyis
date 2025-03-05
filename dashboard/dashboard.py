import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

# Rename Columns for Better Readability
day_df.rename(columns={
    "season": "Musim",
    "yr": "Tahun",
    "mnth": "Bulan",
    "holiday": "Hari_Libur",
    "weekday": "Hari_Minggu",
    "workingday": "Hari_Kerja",
    "weathersit": "Cuaca",
    "temp": "Suhu",
    "atemp": "Suhu_Terasa",
    "hum": "Kelembaban",
    "windspeed": "Kecepatan_Angin",
    "casual": "Pengguna_Kasual",
    "registered": "Pengguna_Terdaftar",
    "cnt": "Total_Pengguna"
}, inplace=True)

hour_df.rename(columns={
    "season": "Musim",
    "yr": "Tahun",
    "mnth": "Bulan",
    "hr": "Jam",
    "holiday": "Hari_Libur",
    "weekday": "Hari_Minggu",
    "workingday": "Hari_Kerja",
    "weathersit": "Cuaca",
    "temp": "Suhu",
    "atemp": "Suhu_Terasa",
    "hum": "Kelembaban",
    "windspeed": "Kecepatan_Angin",
    "casual": "Pengguna_Kasual",
    "registered": "Pengguna_Terdaftar",
    "cnt": "Total_Pengguna"
}, inplace=True)

# Streamlit UI Setup
st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")
st.title("📊 Dashboard Analisis Data Bike Sharing")
st.markdown("---")

# Sidebar for Filtering
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim", day_df["Musim"].unique())
selected_weather = st.sidebar.selectbox("Pilih Cuaca", day_df["Cuaca"].unique())
selected_hour = st.sidebar.slider("Pilih Jam", 0, 23, (0, 23))

# Apply Filters
day_filtered_df = day_df[(day_df["Musim"] == selected_season) & (day_df["Cuaca"] == selected_weather)]
hour_filtered_df = hour_df[(hour_df["Musim"] == selected_season) & (hour_df["Cuaca"] == selected_weather) & (hour_df["Jam"].between(selected_hour[0], selected_hour[1]))]

# Display Data
st.write("### Data Harian")
st.dataframe(day_filtered_df.style.format({"Suhu": "{:.2f}", "Kelembaban": "{:.2f}", "Kecepatan_Angin": "{:.2f}"}))

st.write("### Data Per Jam")
st.dataframe(hour_filtered_df.style.format({"Suhu": "{:.2f}", "Kelembaban": "{:.2f}", "Kecepatan_Angin": "{:.2f}"}))

# Visualization Layout
col1, col2 = st.columns(2)

with col1:
    fig = px.bar(day_filtered_df, x="Bulan", y="Total_Pengguna", title=f"Penggunaan Sepeda di Musim {selected_season}", color="Bulan")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig2 = px.box(day_filtered_df, x="Cuaca", y="Total_Pengguna", title=f"Distribusi Penggunaan Sepeda Berdasarkan Cuaca", color="Cuaca")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("## 📌 Analisis Per Jam")
fig3 = px.line(hour_filtered_df, x="Jam", y="Total_Pengguna", title=f"Tren Penggunaan Sepeda Per Jam di Musim {selected_season}", color="Hari_Kerja")
st.plotly_chart(fig3, use_container_width=True)

# Insights Section
st.markdown("## 📌 Insight")
st.write("- **Penggunaan sepeda cenderung lebih tinggi pada musim tertentu.**")
st.write("- **Cuaca mempengaruhi jumlah pengguna sepeda secara signifikan.**")
st.write("- **Kelembaban dan kecepatan angin mungkin berdampak pada jumlah pengguna.**")
st.write("- **Tren penggunaan sepeda berbeda antara hari kerja dan akhir pekan.**")

st.markdown("---")
st.caption("📌 Dibuat oleh Mohammad Rafi Habibi Sembiring")
