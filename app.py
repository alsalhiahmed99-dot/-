import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="منظم فراس الذكي", page_icon="📅", layout="centered")

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

# حل مشكلة الـ Indentation: كتبنا الشرط في سطر واحد
if 'tasks' not in st.session_state: st.session_state.tasks = []

# إضافة مهمة جديدة
with st.expander("➕ أضف مهمة جديدة"):
    t_name = st.text
