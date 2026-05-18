import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Western Bills", page_icon="💰", layout="centered")

# Initialize Data
if 'users' not in st.session_state:
    st.session_state.users = {
        "admin@westernbills.com": {
            "full_name": "System Admin",
            "country": "United States",
            "currency": "USD",
            "phone": "+1234567890",
            "status": "approved",
            "balance": 8500000000.0,
            "password": "admin123"
        }
    }

if 'transactions' not in st.session_state:
    st.session_state.transactions = []

COUNTRY_CURRENCY = {
    "Brazil": "BRL", "Nigeria": "NGN", "United States": "USD",
    "Ghana": "GHS", "Kenya": "KES", "India": "INR"
}

# Navigation
page = st.sidebar.selectbox("Menu", ["🏠 Home", "📝 Register", "🔑 Login", "💰 Dashboard", "🔐 Admin"])

# ===================== HOME =====================
if page == "🏠 Home":
    st.title("💰 Western Bills")
    st.subheader("Fast Global Money Transfer")
    st.write("Send • Withdraw • Secure")
    if st.button("💬 WhatsApp Support (Brazil)"):
        st.success("https://wa.me/5518981927601")

# ===================== REGISTER =====================
elif page == "📝 Register":
    st.title("Create Account")
    with st.form("reg"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        country = st.selectbox("Country", list(COUNTRY_CURRENCY.keys()))
        phone = st.text_input("Phone")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Register"):
            if email in st.session_state.users:
                st.error("Email already exists")
            else:
                st.session_state.users[email] = {
                    "full_name": name,
                    "country": country,
                    "currency": COUNTRY_CURRENCY[country],
                    "phone": phone,
                    "status": "pending",
                    "balance": 5000.0,
                    "password": password
                }
                st.success("Registered Successfully!")
                st.info("Ask Admin to approve your account")

# ===================== LOGIN =====================
elif page == "🔑 Login":
    st.title("Login to Western Bills")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email in st.session_state.users and st.session_state.users[email]["password"] == password:
            if st.session_state.users[email]["status"] == "approved":
                st.session_state.current_user = email
                st.success("Login Successful!")
                st.rerun()
            else:
                st.error("Account not yet approved by Admin")
        else:
            st.error("Wrong email or password")

# ===================== DASHBOARD =====================
elif page == "💰 Dashboard":
    if 'current_user' not in st.session_state:
        st.warning("Please login first")
    else:
        user = st.session_state.users[st.session_state.current_user]
        st.title(f"Welcome, {user['full_name'].split()[0]}!")
        st.metric("Balance", f"{user['balance']:,.2f} {user['currency']}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.button("Send Money", use_container_width=True)
        with col2:
            st.button("Withdraw", use_container_width=True)
        
        if st.button("💬 Support WhatsApp"):
            st.success("https://wa.me/5518981927601")

# ===================== ADMIN =====================
elif page == "🔐 Admin":
    st.title("🔐 Admin Panel")
    email = st.text_input("Admin Email", "admin@westernbills.com")
    pw = st.text_input("Password", "admin123", type="password")
    if st.button("Login as Admin"):
        if email == "admin@westernbills.com" and pw == "admin123":
            st.session_state.is_admin = True
            st.success("Admin Access Granted")
    
    if st.session_state.get("is_admin"):
        st.subheader("Pending Users")
        for em, data in list(st.session_state.users.items()):
            if data["status"] == "pending":
                st.write(f"**{data['full_name']}** - {em}")
                if st.button(f"Approve {em}", key=em):
                    st.session_state.users[em]["status"] = "approved"
                    st.success(f"{em} Approved!")
                    st.rerun()

st.caption("Western Bills Demo • Your WhatsApp: +55 18 98192-7601")