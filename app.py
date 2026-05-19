import streamlit as st

st.set_page_config(page_title="Western Bills", page_icon="💰", layout="centered")

# Custom CSS for Modern Look
st.markdown("""
<style>
    .main {background: linear-gradient(135deg, #1a0033, #000033);}
    .stButton>button {background: #00ff88; color: black; border-radius: 12px; height: 50px; font-size: 18px;}
    .stTextInput>div>div>input {background: #ffffff15; color: white; border-radius: 12px;}
    h1 {color: white !important; font-size: 2.5rem;}
    .success {color: #00ff88;}
</style>
""", unsafe_allow_html=True)

st.title("💰 Western Bills")
st.markdown("<h3 style='color:#aaa; text-align:center;'>Fast Global Money Transfer</h3>", unsafe_allow_html=True)

# Navigation
page = st.sidebar.selectbox("Menu", ["🏠 Home", "📝 Register", "🔑 Login", "💰 Dashboard", "🔐 Admin"])

# ===================== HOME =====================
if page == "🏠 Home":
    st.image("https://source.unsplash.com/random/800x400/?money", use_column_width=True)
    st.subheader("Send • Withdraw • Secure")
    if st.button("💬 WhatsApp Support (Brazil)"):
        st.success("https://wa.me/5518981927601")

# ===================== REGISTER =====================
elif page == "📝 Register":
    st.subheader("Create New Account")
    with st.form("reg"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
        with col2:
            country = st.selectbox("Country", ["Brazil", "Nigeria", "United States", "Ghana", "Kenya"])
            phone = st.text_input("Phone Number")
        password = st.text_input("Create Password", type="password")
        if st.form_submit_button("Create Account"):
            # Registration logic (same as before)
            st.success("Account Created! Ask Admin to approve.")

# ===================== LOGIN =====================
elif page == "🔑 Login":
    st.subheader("Log in")
    st.markdown("Don't have an account? [Register](?page=Register)")
    
    email = st.text_input("Enter your email address")
    password = st.text_input("Enter password", type="password")
    
    if st.button("Continue", use_container_width=True):
        # Simple login logic
        if email == "admin@westernbills.com" and password == "admin123":
            st.session_state.current_user = email
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid credentials")

# Add other pages later...

st.caption("Western Bills Demo • WhatsApp: +55 18 98192-7601")