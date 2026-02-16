import streamlit as st
import pandas as pd
from datetime import datetime as dt
import requests

# 1. Page Config
st.set_page_config(page_title="Feras Task", layout="wide")

# 2. Style
st.markdown("<style>h1{color:#D4AF37;text-align:center;}</style>", unsafe_allow_html=True)

# 3. Title
st.title("📅 FERAS SCHEDULER")
st.write("---")

# 4. Prayer Times
city = st.text_input("City (EN):", "Muscat")

def get_t(c):
    u = f"http://api.aladhan.com/v1/timingsByCity?city={c}&country=Oman&method=4"
    try:
        r = requests.get(u).json()
        return r['data']['timings'] if r['code']==200 else None
    except: return None

res = get_t(city)

if res:
    # تقسيم الأعمدة بأسطر قصيرة جداً
    c1, c2, c3, c4, c5 = st.columns(5)
    p = {"Fajr":"الفجر","Dhuhr":"الظهر","Asr":"العصر","Maghrib":"المغرب","Isha":"العشاء"}
    # عرض كل وقت في عمود منفصل لتجنب الانقطاع
    c1.metric(p["Fajr"], dt.strptime(res["Fajr"],"%H:%M").strftime("%I:%M %p"))
    c2.metric(p["Dhuhr"], dt.strptime(res["Dhuhr"],"%H:%M").strftime("%I:%M %p"))
    c3.metric(p["Asr"], dt.strptime(res["Asr"],"%H:%M").strftime("%I:%M %p"))
    c4.metric(p["Maghrib"], dt.strptime(res["Maghrib"],"%H:%M").strftime("%I:%M %p"))
    c5.metric(p["Isha"], dt.strptime(res["Isha"],"%H:%M").strftime("%I:%M %p"))

st.write("---")

# 5. Tasks
if 'tk' not in st.session_state: st.session_state.tk = []

n = st.text_input("Task Name:")
tm = st.time_input("Time:")
if st.button("Add Task"):
    if n:
        st.session_state.tk.append({"Time":tm.strftime("%I:%M %p"),"Task":n})
        st.rerun()

# 6. View
if st.session_state.tk:
    st.table(pd.DataFrame(st.session_state.tk))
    if st.button("Clear"):
        st.session_state.tk = []
        st.rerun()

# 7. Sidebar
st.sidebar.header("المصمم")
st.sidebar.subheader("فراس حمد المعمري")
