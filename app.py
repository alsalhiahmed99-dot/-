import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="منظم فراس المعمري", layout="wide")

# --- لوحة التحكم في الواجهة (مثل تخصيص جوجل) ---
st.sidebar.title("🎨 تخصيص الواجهة")
main_clr = st.sidebar.color_picker("اختر لونك المفضل (Theme Color):", "#D4AF37")
bg_type = st.sidebar.selectbox("نمط الخلفية:", ["داكن ملكي", "أسود فاحم", "رمادي احترافي"])

# تحديد كود الخلفية
if bg_type == "داكن ملكي": bg_val = "#0e1117"
elif bg_type == "أسود فاحم": bg_val = "#000000"
else: bg_val = "#262730"

# تطبيق التصميم الديناميكي
st.markdown(f"""
    <style>
    .stApp {{ background-color: {bg_val}; color: #ffffff; }}
    h1, h2, h3 {{ color: {main_clr} !important; text-align: center; }}
    .stButton>button {{ background: linear-gradient(to right, {main_clr}, #8B6B13); color: white !important; border-radius: 8px; border: none; font-weight: bold; width: 100%; }}
    .prayer-box {{ background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 12px; border: 1px solid {main_clr}; text-align: center; transition: 0.3s; }}
    .prayer-box:hover {{ transform: translateY(-5px); box-shadow: 0px 5px 15px {main_clr}; }}
    div[data-testid="stMetricValue"] {{ color: {main_clr} !important; }}
    </style>
    """, unsafe_allow_html=True)

st.title("📅 FERAS SCHEDULER")
st.markdown(f"<p style='text-align:center;'>تطوير المبرمج: فراس حمد المعمري</p>", unsafe_allow_html=True)

# --- الجزء الأول: تحديد الموقع وتواقيت الصلاة (نفس منطقك الأصلي) ---
st.subheader("🕌 تواقيت الصلاة الدقيقة")

location_options = {
    "مسقط": {"city": "Muscat", "country": "Oman"},
    "صحار": {"city": "Sohar", "country": "Oman"},
    "صلالة": {"city": "Salalah", "country": "Oman"},
    "نزوى": {"city": "Nizwa", "country": "Oman"},
    "البريمي": {"city": "Buraimi", "country": "Oman"},
    "عبري": {"city": "Ibri", "country": "Oman"},
    "الرستاق": {"city": "Rustaq", "country": "Oman"},
    "صور": {"city": "Sur", "country": "Oman"}
}

selected_loc = st.selectbox("📍 حدد موقعك:", list(location_options.keys()))

def get_prayer_times(city, country):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=4"
    try:
        response = requests.get(url).json()
        return response['data']['timings']
    except: return None

timings = get_prayer_times(location_options[selected_loc]["city"], location_options[selected_loc]["country"])

if timings:
    c1, c2, c3, c4, c5 = st.columns(5)
    prayers = {"Fajr": "الفجر", "Dhuhr": "الظهر", "Asr": "العصر", "Maghrib": "المغرب", "Isha": "العشاء"}
    for i, (key, val) in enumerate(prayers.items()):
        with [c1, c2, c3, c4, c5][i]:
            st.markdown(f"""
                <div class="prayer-box">
                    <p style="color: {main_clr}; margin: 0; font-weight: bold;">{val}</p>
                    <h2 style="margin: 5px 0;">{timings[key]}</h2>
                </div>
            """, unsafe_allow_html=True)

st.divider()

# --- الجزء الثاني: إضافة المهام (نفس منطقك الأصلي) ---
st.subheader("📝 جدول المهام اليومية")

with st.form("task_form"):
    task_name = st.text_input("اسم المهمة")
    task_time = st.time_input("وقت البدء")
    priority = st.selectbox("الأهمية", ["عالية 🔥", "متوسطة ⚡", "منخفضة ❄️"])
    submit = st.form_submit_button("إضافة المهمة للجدول ✨")

if 'tasks' not in st.session_state: st.session_state.tasks = []

if submit and task_name:
    st.session_state.tasks.append({
        "المهمة": task_name,
        "الوقت": task_time.strftime("%I:%M %p"),
        "الأهمية": priority
    })
    st.success(f"تمت الإضافة لجدول {selected_loc}!")

# --- الجزء الثالث: عرض الجدول ---
if st
