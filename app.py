import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="منظم فراس الذكي", page_icon="📅", layout="centered")

# تنسيق CSS بسيط لتحسين المظهر
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("📅 منظم المهام وتواقيت الصلاة")
st.write(f"اليوم: {datetime.now().strftime('%Y-%m-%d')}")

# --- الجزء الأول: اختيار المدينة وتواقيت الصلاة ---
st.sidebar.header("📍 الإعدادات")
city = st.sidebar.selectbox("اختر مدينتك في عُمان:", 
                           ["Muscat", "Salalah", "Sohar", "Nizwa", "Sur", "Buraimi", "Ibra", "Khasab"])

def get_prayer_times(selected_city):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={selected_city}&country=Oman&method=1"
    try:
        response = requests.get(url).json()
        return response['data']['timings']
    except:
        return None

timings = get_prayer_times(city)

if timings:
    st.subheader(f"🕌 تواقيت الصلاة في {city}")
    cols = st.columns(5)
    prayers = {"Fajr": "الفجر", "Dhuhr": "الظهر", "Asr": "العصر", "Maghrib": "المغرب", "Isha": "العشاء"}
    for i, (key, val) in enumerate(prayers.items()):
        with cols[i]:
            st.metric(label=val, value=timings[key])

st.divider()

# --- الجزء الثاني: إدارة المهام ---
st.subheader("📝 جدول المهام اليومي")

if 'tasks' not in st.session_state:
