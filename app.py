import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# 1. إعدادات الصفحة (باسم فراس)
st.set_page_config(
    page_title="مُنظم فراس الأسطوري", 
    page_icon="👑", 
    layout="wide"
)

# 2. تصميم الـ CSS الملكي
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Tajawal:wght@500;800&display=swap');

    .stApp {
        background: radial-gradient(circle, #0d0d0d 0%, #1a1a1a 100%);
        color: #ffffff;
        font-family: 'Tajawal', sans-serif;
    }

    .main-title {
        font-family: 'Cairo', sans-serif;
        background: linear-gradient(to right, #D4AF37, #F9E2AF, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 55px;
        font-weight: 800;
        filter: drop-shadow(0px 5px 15px rgba(212, 175, 55, 0.4));
        margin-top: -30px;
    }

    .prayer-card {
        background: rgba(212, 175, 55, 0.05);
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        transition: 0.4s ease;
    }
    .prayer-card:hover {
        background: rgba(212, 175, 55, 0.1);
        border-color: #D4AF37;
        transform: translateY(-5px);
        box-shadow: 0px 10px 20px rgba(212, 175, 55, 0.2);
    }

    div.stButton > button {
        background: linear-gradient(45deg, #D4AF37, #8B6B13);
        color: white !important;
        border-radius: 30px;
        border: none;
        padding: 12px 30px;
        font-weight: bold;
        font-size: 18px;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        box-shadow: 0px 0px 20px #D4AF37;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الواجهة الرئيسية
st.markdown('<h1 class="main-title">FERAS SCHEDULER</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 18px; color: #C0C0C0; letter-spacing: 2px;">نظام إدارة الوقت الذكي - إصدار المسابقات</p>', unsafe_allow_html=True)

# 4. أوقات الصلاة
def get_prayer_times():
    url = "http://api.aladhan.com/v1/timingsByCity?city=Muscat&country=Oman&method=1"
    try:
        response = requests.get(url).json()
        return response['data']['timings']
    except:
        return None

timings = get_prayer_times()

if timings:
    st.markdown("<br>", unsafe_allow_html=True)
    cols = st.columns(5)
    prayers = {"Fajr": "الفجر", "Dhuhr": "الظهر", "Asr": "العصر
