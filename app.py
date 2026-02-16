import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# 1. الإعدادات
st.set_page_config(page_title="منظم فراس", layout="wide")

# 2. تصميم ملكي (بأسطر قصيرة لتجنب القطع)
st.markdown("<style>", unsafe_allow_html=True)
st.markdown(".stApp { background-color: #0e1117; color: white; }", unsafe_allow_html=True)
st.markdown("h1 { color: #D4AF37 !important; text-align: center; }", unsafe_allow_html=True)
st.markdown(".p-box { background: rgba(212,175,55,0.1); padding: 10px; ", unsafe_allow_html=True)
st.markdown("border-radius: 10px; border: 1px solid #D4AF37; text-align: center; }", unsafe_allow_html=True)
st.markdown("</style>", unsafe_allow_html=True)

st.title("📅 FERAS SCHEDULER")
st.markdown("<p style='text-align:center;'>المبرمج: فراس حمد المعمري</p>", unsafe_allow_html=True)

# 3. جلب التوقيت العالمي (نظام 12 ساعة)
st.subheader("🌍 التوقيت العالمي")
city = st.text_input("اسم المدينة (بالإنجليزي):", "Muscat")

def get_times(c):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={c}&country=Oman&method=4"
    try:
        r = requests.get(url).json()
        return r['data']['timings'] if r['code']==200 else None
    except: return None

def to_12h(t):
    try: return datetime.strptime(t, "%H:%M").strftime("%I:%M %p")
    except: return t

tm = get_times(city)

if tm:
    st.write(f"📍 مدينة: {city}")
    cols =
