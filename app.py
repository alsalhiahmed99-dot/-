import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# إعدادات الصفحة
st.set_page_config(page_title="مُنظم جدول فراس", layout="wide")

st.title("📅 منظم الجدول اليومي - فراس")

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
        cols[i].metric(label=val, value=val) # تم تعديل العرض ليناسب ستريمليت
        cols[i].write(timings[key])

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
    
    if st.button("تفريغ الجدول"):
        st.session_state.tasks = []
        st.rerun()
else:
    st.info("الجدول فارغ حالياً. ابدأ بإضافة مهامك.")
