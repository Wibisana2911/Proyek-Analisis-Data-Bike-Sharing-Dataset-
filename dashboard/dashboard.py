import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

hour_df = pd.read_csv('dashboard/hour.csv')

st.title('Proyek Analisis Data: [Bike Sharing Dataset]')

st.markdown(
    """
    - **Nama:** KOMANG WIBISANA
    - **Email:** m298d4ky2631@bangkit.academy
    - **ID Dicoding:** komang_wibisana_m298d4ky2631_o8lE
    """
)

with st.sidebar:
    
    st.title('Profile')
    
    st.markdown(
    """
    - **Nama:** KOMANG WIBISANA
    - **Email:** m298d4ky2631@bangkit.academy
    - **ID Dicoding:** komang_wibisana_m298d4ky2631_o8lE
    """
    )
   
st.title (" Visualization & Explanatory Analysis")
    
 # Tampilkan 5 baris pertama dari data
st.write("Data Head:")
st.write(hour_df.head())

st.title ("Histogram")

# Tampilkan histogram menggunakan Matplotlib
fig, ax = plt.subplots(figsize=(10, 10))
hour_df.hist(ax=ax)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.title (" Heatmap")

# Memilih kolom yang akan digunakan untuk heatmap
heatmap_data = hour_df[['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']]

# Menghitung matriks korelasi
correlation_matrix = heatmap_data.corr()

# Tampilkan heatmap menggunakan Seaborn
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title('Correlation Matrix')

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.title ("Distribusi")
st.subheader ("Distribution of Bike Counts")
# Tampilkan distribusi menggunakan Seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(hour_df['cnt'], bins=30, kde=True, color='blue', ax=ax)
ax.set_title('Distribution of Bike Counts')
ax.set_xlabel('Bike Count')
ax.set_ylabel('Frequency')

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.title ("Line plot")
st.subheader ("Hourly Bike Counts")

# Tampilkan line plot menggunakan Seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=hour_df, x='hr', y='cnt', ci=None, color='red', ax=ax)
ax.set_title('Hourly Bike Counts')
ax.set_xlabel('Hour')
ax.set_ylabel('Bike Count')

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.title ("Scatter plot")
st.subheader ("Temperature vs Bike Counts")

# Tampilkan scatter plot menggunakan Seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=hour_df, x='temp', y='cnt', color='green', ax=ax)
ax.set_title('Temperature vs. Bike Counts')
ax.set_xlabel('Temperature')
ax.set_ylabel('Bike Count')

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.title ("Box plot")
st.subheader ("Weather Situation vs Bike Counts")

# Tampilkan box plot menggunakan Seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=hour_df, x='weathersit', y='cnt', palette='Set2', ax=ax)
ax.set_title('Weather Situation vs. Bike Counts')
ax.set_xlabel('Weather Situation')
ax.set_ylabel('Bike Count')

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)