import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="منظم فراس المعمري", layout="wide")

# 2. تصميم فخم بأسطر قصيرة (عشان ما يقطع)
st.markdown("<style>", unsafe_allow_html=True)
st.markdown(".stApp { background-color: #0e1117; color: white; }", unsafe_allow_html=True)
st.markdown("h1 { color: #D4AF37 !important; text-align: center; }", unsafe_allow_html=True)
st.markdown(".p-card { background: rgba(212,175,55,0.1); padding: 15px; ", unsafe_allow_html=True)
st.markdown("border: 1px solid #D4AF37; border-radius: 12px; text-align: center; }", unsafe_allow_html=True)
st.markdown("</style>", unsafe_allow_html=True)

st.title("📅 FERAS SCHEDULER")
st.markdown("<p style='text-align:center;'>بإشراف المبرمج: فراس حمد المعمري</p>", unsafe_allow_html=True)

# 3. جلب مواقيت الصلاة (حسب توقيت مسقط - معتمد)
def get_oman_times():
    # استخدام إحداثيات مسقط لضمان مطابقة توقيت وزارة الأوقاف
    url = "http://api.aladhan.com/v1/timings?latitude=23.5859&longitude=58.4059&method=1"
    try:
        r = requests.get(url).json()
        return r['data']['timings']
    except: return None

def to_12h(t):
    return datetime.strptime(t, "%H:%M").strftime("%I:%M %p")

tm = get_oman_times()

if tm:
    st.subheader("🕌 مواقيت الصلاة (حسب توقيت السلطنة المعتمَد)")
    c1, c2, c3, c4, c5 = st.columns(5)
    p = {"Fajr":"الفجر", "Dhuhr":"الظهر", "Asr":"العصر", "Maghrib":"المغرب", "Isha":"العشاء"}
    
    # توزيع المواقيت بأسطر منفصلة لتجنب SyntaxError
    with c1: st.markdown(f'<div class="p-card"><b>{p["Fajr"]}</b><br>{to_12h(tm["Fajr"])}</div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="p-card"><b>{p["Dhuhr"]}</b><br>{to_12h(tm["Dhuhr"])}</div>', unsafe_allow_html=True)
    with c3: st.markdown(f'<div class="p-card"><b>{p["Asr"]}</b><br>{to_12h(tm["Asr"])}</div>', unsafe_allow_html=True)
    with c4: st.markdown(f'<div class="p-card"><b>{p["Maghrib"]}</b><br>{to_12h(tm["Maghrib"])}</div>', unsafe_allow_html=True)
    with c5: st.markdown(f'<div class="p-card"><b>{p["Isha"]}</b><br>{to_12h(tm["Isha"])}</div>', unsafe_allow_html=True)

st.divider()

# 4. نظام المهام
if 'list' not in st.session_state: st.session_state.list = []

col_a, col_
