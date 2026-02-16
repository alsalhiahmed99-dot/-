import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="Ahmad AI | البرمج أحمد البدر",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. لمسة الفخامة بالـ CSS (التصميم الأسطوري)
st.markdown("""
    <style>
    /* استيراد خطوط عربية فخمة */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Tajawal:wght@500;800&display=swap');

    /* الخلفية العامة للتطبيق (تدرج ملكي غامق) */
    .stApp {
        background: radial-gradient(circle, #1a1a1d 0%, #000000 100%);
        color: #ffffff;
        font-family: 'Tajawal', sans-serif;
    }

    /* تصميم القائمة الجانبية (Sidebar) بأسلوب زجاجي */
    section[data-testid="stSidebar"] {
        background-color: rgba(20, 20, 20, 0.8) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(212, 175, 55, 0.2);
    }

    /* العنوان الرئيسي الأسطوري */
    .main-title {
        font-family: 'Cairo', sans-serif;
        background: linear-gradient(to right, #D4AF37, #F9E2AF, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 60px;
        font-weight: 800;
        filter: drop-shadow(0px 5px 15px rgba(212, 175, 55, 0.4));
        margin-top: -20px;
    }

    /* البطاقات التعريفية (Cards) */
    .feature-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(212, 175, 55, 0.1);
        text-align: center;
        transition: 0.4s;
    }
    
    .feature-card:hover {
        border: 1px solid #D4AF37;
        transform: translateY(-10px);
        box-shadow: 0px 10px 30px rgba(212, 175, 55, 0.2);
    }

    /* تصميم الأزرار الفخم */
    div.stButton > button {
        background: linear-gradient(45deg, #D4AF37, #b8860b);
        color: #000 !important;
        border-radius: 50px;
        border: none;
        padding: 15px 40px;
        font-weight: bold;
        font-size: 18px;
        transition: 0.5s;
        width: 100%;
    }
    
    div.stButton > button:hover {
        box-shadow: 0px 0px 25px #D4AF37;
        transform: scale(1.02);
        color: #fff !important;
    }

    /* تخصيص خانة الإدخال */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        color: white !important;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. محتوى الواجهة الرئيسي
st.markdown('<h1 class="main-title">AHMAD AI</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 20px; color: #C0C0C0;">الذكاء الاصطناعي بروح عمانية أصيلة 🇴🇲</p>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 4. قسم المميزات (موزع في أعمدة)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <h3 style="color: #D4AF37;">🤖 ذكاء فائق</h3>
            <p>برمجة متطورة تتعلم وتتفاعل معك بذكاء</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <h3 style="color: #D4AF37;">🎨 توليد صور</h3>
            <p>حول خيالك إلى واقع بدقة مذهلة</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <h3 style="color: #D4AF37;">🗣️ لهجة عمانية</h3>
            <p>أول نظام ذكاء يفهمك "من داخل وبترابها"</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><hr style='opacity: 0.1;'><br>", unsafe_allow_html=True)

# 5. منطقة التفاعل (الدردشة)
chat_container = st.container()
with chat_container:
    user_input = st.text_input("اسأل Ahmad AI أي شيء...", placeholder="مثلاً: كيف حالك اليوم؟")
    
    if st.button("إرسال الأمر"):
        if user_input:
            st.success(f"تم استقبال طلبك يا بطل! جاري معالجة: {user_input}")
        else:
            st.warning("اكتب شي أول عشان أبهرك!")

# 6. التذييل (Footer) - يثبت إنك المبرمج
st.sidebar.markdown(f"""
    <div style="text-align: center;">
        <h2 style="color: #D4AF37;">المبرمج</h2>
        <p style="font-weight: bold; font-size: 20px;">أحمد بن بدر السعدي</p>
        <p style="color: #888;">عمان - 2026</p>
    </div>
    <hr style="border-color: rgba(212, 175, 55, 0.2);">
""", unsafe_allow_html=True)

st.sidebar.info("هذا المشروع صُمم ليثبت أن الإبداع لا يعرف عمراً. فخامة، قوة، وذكاء.")
