import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="مُنظم فراس المعمري", page_icon="👑", layout="wide")

# 2. تصميم CSS ملكي (ثابت ما يضيع)
css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700&family=Tajawal:wght@500&display=swap');
    .stApp {background: #0d0d0d; color: white; font-family: 'Tajawal', sans-serif;}
    .main-title {text-align: center; color: #D4AF37; font-family: 'Cairo'; font-size: 45px; text-shadow: 2px 2px 10px rgba(212,175,55,0.3);}
    .prayer-card {background: rgba(212, 175, 55, 0.1); border: 1px solid #D4AF37; border-radius: 10px; padding: 10px; text-align: center;}
    div.stButton > button {background: linear-gradient(45deg, #D4AF37, #8B6B13) !important; color: white !important; border-radius: 20px !important; width: 100% !important; font-weight: bold !important;}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# 3. العناوين
st.markdown('<h1 class="main-title">FERAS SCHEDULER</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #C0C0C0;">نظام إدارة الوقت الذكي - إبداع المبرمج فراس حمد المعمري</p>', unsafe_allow_html=True)

# 4. أوقات الصلاة
def get_p():
    try:
        r = requests.get("http://api.aladhan.com/v1/timingsByCity?city=Muscat&country=Oman&method=1").json()
        return r['data']['timings']
    except: return None

t = get_p()
if t:
    st.markdown("<br>", unsafe_allow_html=True)
    cols = st.columns(5)
    p_names = {"Fajr":"الفجر", "Dhuhr":"الظهر", "Asr":"العصر", "Maghrib":"المغرب", "Isha":"العشاء"}
    for i, (k, v) in enumerate(p_names.items()):
        cols[i].markdown(f'<div class="prayer
