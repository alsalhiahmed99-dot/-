import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="منظم فراس المعمري", layout="wide")

# 2. القائمة الجانبية للإعدادات (تغيير الألوان والموقع)
st.sidebar.title("🎨 إعدادات المظهر")
main_color = st.sidebar.color_picker("اختر لون النظام اللامع:", "#D4AF37")
bg_choice = st.sidebar.selectbox("لون الخلفية:", ["داكن ملكي", "أسود فاحم", "رمادي احترافي"])

# تحويل اختيار الخلفية لكود لون
bg_color = "#0e1117" if bg_choice == "داكن ملكي" else "#000000" if bg_choice == "أسود فاحم" else "#262730"

# 3. واجهة المستخدم الديناميكية
st.markdown(f"""
    <style>
    .stApp {{ background-color: {bg_color}; color: #ffffff; }}
    h1, h2, h3 {{ color: {main_color} !important; text-align: center; }}
    .stButton>button {{ background: linear-gradient(to right, {main_color}, #8B6B13); color: white !important; border-radius: 8px; border: none; width: 100%; }}
    .prayer-box {{ background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 12px; border: 1px solid {main_color}; text-align: center; }}
    </style>
    """, unsafe_allow_html=True)

st.title("📅 FERAS SCHEDULER")
st.markdown(f"<p style='text-align:center;'>إبداع: فراس حمد المعمري</p>", unsafe_allow_html=True)

# 4. اختيار الولاية (كل مناطق عمان)
st.sidebar.write("---")
st.sidebar.title("📍 ضبط الموقع")
oman_regions = {
    "مسقط": "Muscat", "صحار": "Sohar", "صلالة": "Salalah", 
    "نزوى": "Nizwa", "البريمي": "Buraimi", "عبري": "Ibri",
    "صور": "Sur", "الرستاق": "Rustaq", "هيما": "Haima", 
    "خصب": "Khasab", "إبراء": "Ibra", "السويق": "Suwayq",
    "بهلاء": "Bahla", "بركاء": "Barka", "شنوص": "Shinas"
}
loc = st.sidebar.selectbox("اختر ولايتك لضبط الوقت:", list(oman_regions.keys()))

# 5. جلب التوقيت وتحويله لـ 12 ساعة
def get_p_times(city):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country=Oman&method=1"
    try:
        r = requests.get(url).json()
        return r['data']['timings']
    except: return None

def fmt_12h(t_str):
    return datetime.strptime(t_str, "%H:%M").strftime("%I:%M %p")

timings = get_p_times(oman_regions[loc])

if timings:
    st.subheader(f"🕌 تواقيت الصلاة في {loc}")
    c1, c2, c3, c4, c5 = st.columns(5)
    p_names = {"Fajr":"الفجر", "Dhuhr":"الظهر", "Asr":"العصر", "Maghrib":"المغرب", "Isha":"العشاء"}
    for i, (k, v) in enumerate(p_names.items()):
        with [c1, c2, c3, c4, c5][i]:
            st.markdown(f"""<div class="prayer-box"><p style="color:{main_color}; font-weight:bold;">{v}</p>
                <h3>{fmt_12h(timings[k])}</h3></div>""", unsafe_allow_html=True)

st.divider()

# 6. إدارة المهام (بدون تغيير المنطق)
if 'tasks' not in st.session_state: st.session_state.tasks = []

with st.form("task_form"):
    col_task, col_time = st.columns([2, 1])
    n = col_task.text_input("شو المهمة القادمة يا فراس؟")
    t = col_time.time_input("الوقت")
    p = st.selectbox("الأهمية", ["عالية جداً 🔥", "متوسطة ⚡", "عادية ❄️"])
    if st.form_submit_button("إضافة المهمة للجدول ✨"):
        if n:
            st.session_state.tasks.append({"المهمة": n, "الوقت": t.strftime("%I:%M %p"), "الأهمية": p})
            st.rerun()

# 7. عرض الجدول
if st.session_state.tasks:
    st.table(pd.DataFrame(st.session_state.tasks))
    if st.button("تفريغ الجدول"):
        st.session_state.tasks = []
        st.rerun()
else:
    st.info("الجدول فارغ، بانتظار إبداعات فراس المعمري.")

# توقيع ثابت
st.sidebar.write("---")
st.sidebar.write(f"المبرمج: فراس حمد المعمري")
