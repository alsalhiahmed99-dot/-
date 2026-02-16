import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="مُنظم فراس الأسطوري", page_icon="👑", layout="wide")

# 2. تصميم الـ CSS الملكي - تأكد من نسخ هذا الجزء بالكامل
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
        font-size: 50px;
        font-weight: 800;
        filter: drop-shadow(0px 5px 15px rgba(212, 175, 55, 0.4));
    }
    .prayer-card {
        background: rgba(212, 175, 55, 0.05);
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
    }
    div.stButton > button {
        background: linear-gradient(45deg, #D4AF37, #8B6B13) !important;
        color: white !important;
        border-radius: 25px !important;
        width
