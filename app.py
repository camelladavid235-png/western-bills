import streamlit as st

st.set_page_config(page_title="Western Bills", page_icon="💰", layout="centered")

# Modern Dark Theme
st.markdown("""
<style>
    .main {background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);}
    h1, h2, h3 {color: white !important;}
    .stButton>button {
        background: linear-gradient(90deg, #00ff88, #00cc6a);
        color: black;
        border-radius: 12px;
        height: 52px;
        font-size: 18px;
        font-weight: bold;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background: rgba(255,255,255,0.1);
        color: white;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.2);
    }
</style>
""", unsafe_allow_html=True)

st.title("💰 Western Bills")
st.markdown("**Fast • Secure • Global Money Transfer**")

page = st.sidebar.selectbox("Menu", ["🏠 Home", "📝 Register", "🔑 Login", "💰 Dashboard", "🔐 Admin"])

if page == "🏠 Home":
    st.success("Welcome to Western Bills")
    st.button("💬 WhatsApp Support (Brazil)", use_container_width=True)

elif page == "📝 Register":
    st.subheader("Create Account")
    with st.form("reg"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        country = st.selectbox("Country", ["Brazil", "Nigeria", "United States", "Ghana", "Kenya"])
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Create Account"):
            st.success("Account Created! Ask Admin to approve.")

elif page == "🔑 Login":
    st.subheader("Log in")
    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")
    if st.button("Continue", use_container_width=True):
        if email == "admin@westernbills.com" and password == "admin123":
            st.session_state.current_user = email
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid login")

elif page == "💰 Dashboard":
    if 'current_user' not in st.session_state:
        st.warning("Please login first")
    else:
        st.title("Welcome Back 👋")
        st.metric("Balance", "$5,250.00 USD")

elif page == "🔐 Admin":
    st.subheader("Admin Panel")
    if st.button("Login as Admin"):
        st.success("Admin Access Granted")
        st.write("Pending Users will appear here")

st.caption("Western Bills Demo • WhatsApp: +55 18 98192-7601")