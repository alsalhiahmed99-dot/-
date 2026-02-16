import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="منظم فراس المعمري العالمي", layout="wide")

# --- التصميم الملكي ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1 { color: #D4AF37 !important; text-align: center; font-family: 'Cairo', sans-serif; }
    .stButton>button { background: linear-gradient(to right, #D4AF37, #8B6B13); color: white !important; border-radius: 8px; border: none; width: 100%; font-weight: bold; }
    .prayer-box { background: rgba(212, 175, 55, 0.1); padding: 15px; border-radius: 12px; border: 1px solid #D4AF37; text-align: center; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📅 منظم الوقت العالمي - فراس حمد المعمري")

# --- الجزء الأول: نظام المواقع العالمي وتواقيت الصلاة ---
st.subheader("🌍 ضبط التوقيت العالمي (نظام 12 ساعة)")

# البحث عن أي مدينة في العالم
city_input = st.text_input("اكتب اسم المدينة بالإنجليزية (مثلاً: Muscat, London, Mecca):", value="Muscat")

def get_prayer_times(city):
    # رابط API يجلب التواقيت لأي مدينة في العالم بنظام 12 ساعة
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country=&method=4"
    try:
        response = requests.get(url).json()
        if response['code'] == 200:
            return response['data']['timings']
        else:
            return None
    except:
        return None

def convert_to_12h(time_str):
    # دالة لتحويل الوقت من 24 ساعة إلى 12 ساعة
    try:
        return datetime.strptime(time_str, "%H:%M").strftime("%I:%M %p")
    except:
        return time_str

timings = get_prayer_times(city_input)

if timings:
    st.info(f"📍 عرض تواقيت الصلاة لمدينة: {city_input}")
    cols = st.columns(5)
    prayers = {"Fajr": "الفجر", "Dhuhr": "الظهر", "Asr": "العصر", "Maghrib": "المغرب", "Isha": "العشاء"}
    for i, (key, val) in enumerate(prayers.items()):
        with cols[i]:
            time_12h = convert_to_12h(timings[key])
            st.markdown(f"""
                <div class="prayer-box">
                    <p style="color: #D4AF37; margin: 0; font-weight: bold;">{val}</p>
                    <h3 style="margin: 5px 0;">{time_12h}</h3>
                </div>
            """, unsafe_allow_html=True)
else:
    st.error("لم يتم العثور على المدينة. تأكد من كتابة الاسم بالإنجليزية بشكل
