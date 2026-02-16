import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# إعدادات الصفحة
st.set_page_config(page_title="مُنظم جدول فراس حمد المعمري", layout="wide")

# --- تحسين الواجهة فقط (بدون تغيير الكود البرمجي) ---
st.markdown("""
    <style>
    /* خلفية التطبيق */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    /* العنوان الرئيسي */
    h1 {
        color: #D4AF37 !important;
        text-align: center;
        font-family: 'Cairo', sans-serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    /* الأزرار */
    .stButton>button {
        background: linear-gradient(to right, #D4AF37, #8B6B13);
        color: white !important;
        border: none;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 15px #D4AF37;
    }
    /* الجداول والمداخل */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        border-color: #D4AF37 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📅 منظم الجدول اليومي - فراس حمد المعمري")

# --- الجزء الأول: تواقيت الصلاة ---
def get_prayer_times():
    # مدينة مسقط كمثال
    url = "http://api.aladhan.com/v1/timingsByCity?city=Muscat&country=Oman&method=1"
    try:
        response = requests.get(url).json()
        return response['data']['timings']
    except:
        return None

timings = get_prayer_times()

if timings:
    st.subheader("🕌 تواقيت الصلاة اليوم في عُمان")
    cols = st.columns(5)
    prayers = {"Fajr": "الفجر", "Dhuhr": "الظهر", "Asr": "العصر", "Maghrib": "المغرب", "Isha": "العشاء"}
    for i, (key, val) in enumerate(prayers.items()):
        # عرض الوقت تحت المسمى بشكل أنيق
        cols[i].markdown(f"""
            <div style="background: rgba(212, 175, 55, 0.1); padding: 10px; border-radius: 10px; border: 1px solid #D4AF37; text-align: center;">
                <h4 style="color: #D4AF37; margin: 0;">{val}</h4>
                <h2 style="margin: 0;">{timings[key]}</h2>
            </div>
        """, unsafe_allow_html=True)

st.divider()

# --- الجزء الثاني: إضافة المهام ---
st.subheader("📝 أضف مهامك")

with st.form("task_form"):
    task_name = st.text_input("اسم المهمة")
    task_time = st.time_input("وقت البدء")
    priority = st.selectbox("الأهمية", ["عالية", "متوسطة", "منخفضة"])
    submit = st.form_submit_button("إضافة للجدول")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

if submit and task_name:
    st.session_state.tasks.append({
        "المهمة": task_name,
        "الوقت": task_time.strftime("%H:%M"),
        "الأهمية": priority
    })
    st.success("تمت إضافة المهمة!")

# --- الجزء الثالث: عرض الجدول المنظم ---
if st.session_state.tasks:
    st.subheader("📊 الجدول المنظم")
    df = pd.DataFrame(st.session_state.tasks)
    df = df.sort_values(by="الوقت")
    st.table(df)
