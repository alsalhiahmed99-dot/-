import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="منظم فراس المعمري", layout="wide")

# 2. الواجهة الأسطورية (طريقة مختصرة عشان ما يظهر النص)
st.markdown("<style>h1{color:#D4AF37 !important; text-align:center;} .stMetric{color:#D4AF37 !important;}</style>", unsafe_allow_html=True)

# العنوان باسم فراس
st.markdown('# 📅 FERAS SCHEDULER')
st.markdown('<p style="text-align: center;">إبداع المبرمج: فراس حمد المعمري</p>', unsafe_allow_html=True)

# --- الجزء الأول: أوقات الصلاة ---
def get_prayer_times():
    url = "http://api.aladhan.com/v1/timingsByCity?city=Muscat&country=Oman&method=1"
    try:
        r = requests.get(url).json()
        return r['data']['timings']
    except:
        return None

timings = get_prayer_times()

if timings:
    st.subheader("🕌 تواقيت الصلاة اليوم - مسقط")
    cols = st.columns(5)
    p_names = {"Fajr":"الفجر", "Dhuhr":"الظهر", "Asr":"العصر", "Maghrib":"المغرب", "Isha":"العشاء"}
    for i, (k, v) in enumerate(p_names.items()):
        cols[i].metric(label=v, value=timings[k])

st.divider()

# --- الجزء الثاني: إضافة المهام ---
st.subheader("📝 إضافة المهام اليومية")

with st.form("task_form"):
    task_name = st.text_input("اسم المهمة")
    task_time = st.time_input("وقت البدء")
    priority = st.selectbox("الأهمية", ["عالية", "متوسطة", "منخفضة"])
    submit = st.form_submit_button("إضافة للجدول")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

if submit and task_name:
    st.session
