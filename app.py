import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="مُنظم فراس", layout="wide")

# 2. تصميم CSS مختصر بأسطر قصيرة
st.markdown("<style>", unsafe_allow_html=True)
st.markdown("body { background-color: #0d0d0d; color: white; }", unsafe_allow_html=True)
st.markdown(".main-title { text-align: center; color: #D4AF37; font-size: 40px; }", unsafe_allow_html=True)
st.markdown(".p-card { background: #1a1a1a; border: 1px solid #D4AF37; padding: 10px; border-radius: 10px; text-align: center; }", unsafe_allow_html=True)
st.markdown("</style>", unsafe_allow_html=True)

# 3. العناوين
st.markdown('<h1 class="main-title">FERAS SCHEDULER</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;">إبداع: فراس حمد المعمري</p>', unsafe_allow_html=True)

# 4. أوقات الصلاة
def get_p():
    try:
        url = "http://api.aladhan.com/v1/timingsByCity?city=Muscat&country=Oman&method=1"
        r = requests.get(url).json()
        return r['data']['timings']
    except: return None

t = get_p()
if t:
    st.write("---")
    c = st.columns(5)
    names = {"Fajr":"الفجر", "Dhuhr":"الظهر", "Asr":"العصر", "Maghrib":"المغرب", "Isha":"العشاء"}
    for i, (k, v) in enumerate(names.items()):
        # تم تقسيم السطر الطويل لأسطر قصيرة لتجنب الخطأ
        with c[i]:
            st.markdown(f'<div class="p-card">', unsafe_allow_html=True)
            st.markdown(f'<b style="color:#D4AF37">{v}</b>', unsafe_allow_html=True)
            st.markdown(f'<br>{t[k]}</div>', unsafe_allow_html=True)

st.write("---")

# 5. إدارة المهام
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

col1, col2 = st.columns(2)
with col1:
    n = st.text_input("المهمة:")
    p = st.selectbox("الأهمية:", ["عالية 🔥", "متوسطة ⚡", "عادية"])
with col2:
    tm = st.time_input("الوقت:")
    if st.button("إضافة للملف ✨"):
        if n:
            st.session_state.tasks.append({"الوقت": tm.strftime("%I:%M %p"), "المهمة": n, "الأهمية": p})
            st.rerun()

# 6. الجدول
if st.session_state.tasks:
    st.table(pd.DataFrame(st.session_state.tasks))
    if st
