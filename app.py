import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="منظم فراس المعمري", layout="wide")

# 2. الواجهة الأسطورية (CSS فقط بدون تعديل الكود)
st.markdown("<style>", unsafe_allow_html=True)
st.markdown("body, .stApp { background-color: #0e1117; color: #ffffff; }", unsafe_allow_html=True)
st.markdown(".main-title { text-align: center; color: #D4AF37; font-size: 45px; font-weight: bold; text-shadow: 2px 2px 5px rgba(0,0,0,0.5); }", unsafe_allow_html=True)
st.markdown("div[data-testid='stMetricValue'] { color: #D4AF37 !important; }", unsafe_allow_html=True)
st.markdown(".stButton>button { background: linear-gradient(to right, #D4AF37, #8B6B13); color: white; border: none; border-radius: 10px; width: 100%; }", unsafe_allow_html=True)
st.markdown("</style>", unsafe_allow_html=True)

# العنوان الجديد الفخم
st.markdown('<h1 class="main-title">📅 FERAS SCHEDULER</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #C0C0C0;">إبداع المبرمج: فراس حمد المعمري</p>', unsafe_allow_html=True)

# --- الجزء الأول: تواقيت الصلاة (نفس كودك الأصلي) ---
def get_prayer_times():
    url = "http://api.aladhan.com/v1/timingsByCity?city=Muscat&country=Oman&method=1"
    try:
        response = requests.get(url).json()
        return response['data']['timings']
    except:
        return None

timings = get_prayer_times()

if timings:
    st.subheader("🕌 تواقيت الصلاة اليوم - مسقط")
    cols = st.columns(5)
    prayers = {"Fajr": "الفجر", "Dhuhr": "الظهر", "Asr": "العصر", "Maghrib": "المغرب", "Isha": "العشاء"}
    for i, (key, val) in enumerate(prayers.items()):
        cols[i].metric(label=val, value=timings[key])

st.divider()

# --- الجزء الثاني: إضافة المهام (نفس كودك الأصلي) ---
st.subheader("📝 إضافة المهام اليومية")

with st.form("task_form"):
    task_name = st.text_input("اسم المهمة")
    task_time = st.time_input("وقت البدء")
    priority = st.selectbox("الأهمية", ["عالية", "متوسطة", "منخفضة"])
    submit = st.form_submit_button("إضافة للجدول الأسطوري")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

if submit and task_name:
    st.session_state.tasks.append({
        "المهمة": task_name,
        "الوقت": task_time.strftime("%I:%M %p"),
        "الأهمية": priority
    })
    st.success("تمت إضافة المهمة بنجاح!")

# --- الجزء الثالث: عرض الجدول (نفس كودك الأصلي) ---
if st.session_state.tasks:
    st.subheader("📊 جدول فراس المنظم")
    df = pd.DataFrame(st.session_state.tasks)
    df = df.sort_values(by="الوقت")
    st.table(df)
    
    if st.button("تفريغ الجدول"):
        st.session_state.tasks = []
        st.rerun()
else:
    st.info("الجدول فارغ حالياً. ابدأ بإضافة مهامك يا فراس.")

# توقيع جانبي بسيط
st.sidebar.markdown("---")
st.sidebar.write("تصميم المبرمج: فراس حمد المعمري")
