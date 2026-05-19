import streamlit as st

st.set_page_config(page_title="Western Bills", page_icon="💰", layout="centered")

if 'users' not in st.session_state:
    st.session_state.users = {
        "admin@westernbills.com": {
            "full_name": "System Admin", "country": "United States", "currency": "USD",
            "phone": "+1", "status": "approved", "balance": 8500000000.0, "password": "admin123"
        }
    }

page = st.sidebar.selectbox("Menu", ["🏠 Home", "📝 Register", "🔑 Login", "💰 Dashboard", "🔐 Admin Panel"])

# ===================== REGISTER =====================
if page == "📝 Register":
    st.title("Create Account")
    with st.form("register"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        country = st.selectbox("Country", ["Nigeria", "Brazil", "United States", "Ghana", "Kenya"])
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Create Account"):
            if email in st.session_state.users:
                st.error("Email already exists")
            else:
                st.session_state.users[email] = {
                    "full_name": name,
                    "country": country,
                    "currency": "NGN" if country == "Nigeria" else "BRL" if country == "Brazil" else "USD",
                    "phone": phone,
                    "status": "pending",
                    "balance": 5000.0,
                    "password": password
                }
                st.success("✅ Account Created Successfully!")
                st.info("Now go to Admin Panel and approve this account")
                st.rerun()

# ===================== ADMIN PANEL =====================
elif page == "🔐 Admin Panel":
    st.title("🔐 Admin Panel")
    
    if st.button("Login as Admin", type="primary"):
        st.session_state.is_admin = True
    
    if st.session_state.get("is_admin"):
        st.success("✅ Admin Access Granted")
        
        st.subheader("Pending Users")
        pending_count = 0
        for email, data in list(st.session_state.users.items()):
            if data.get("status") == "pending":
                pending_count += 1
                st.write(f"**{data['full_name']}**")
                st.write(f"Email: {email} | Country: {data['country']}")
                if st.button(f"✅ Approve {data['full_name']}", key=email):
                    st.session_state.users[email]["status"] = "approved"
                    st.success(f"✅ {email} Approved!")
                    st.rerun()
        
        if pending_count == 0:
            st.info("No pending users yet. Register a new user first.")

    else:
        st.info("Click 'Login as Admin' above")

st.caption("Western Bills Demo • WhatsApp: +55 18 98192-7601")