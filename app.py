import streamlit as st

st.set_page_config(page_title="Western Bills", page_icon="💰", layout="centered")

if st.sidebar.button("🔄 Reset App (Clear All Data)"):
    st.session_state.clear()
    st.success("App Reset Successfully! Refresh the page.")
    st.stop()

if 'users' not in st.session_state:
    st.session_state.users = {
        "admin@westernbills.com": {
            "full_name": "System Admin", "status": "approved", "password": "admin123"
        }
    }

page = st.sidebar.selectbox("Menu", ["🏠 Home", "📝 Register", "🔐 Admin Panel"])

if page == "📝 Register":
    st.title("Create Account")
    with st.form("reg"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        country = st.selectbox("Country", ["Nigeria", "Brazil", "United States"])
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Create Account"):
            if email in st.session_state.users:
                st.error("❌ Email already exists! Use a different email.")
            else:
                st.session_state.users[email] = {
                    "full_name": name,
                    "country": country,
                    "status": "pending",
                    "password": password
                }
                st.success("✅ Account Created Successfully!")
                st.info("Go to Admin Panel → Login as Admin → Approve this account")

elif page == "🔐 Admin Panel":
    st.title("🔐 Admin Panel")
    if st.button("Login as Admin"):
        st.session_state.is_admin = True
    
    if st.session_state.get("is_admin"):
        st.success("✅ Admin Access Granted")
        st.subheader("Pending Users")
        
        for email, data in st.session_state.users.items():
            if data.get("status") == "pending":
                st.write(f"**{data['full_name']}** - {email}")
                if st.button(f"Approve {email}", key=email):
                    st.session_state.users[email]["status"] = "approved"
                    st.success(f"{email} Approved!")
                    st.rerun()
    else:
        st.info("Click the button above to login as Admin")

st.caption("Western Bills Demo • WhatsApp: +55 18 98192-7601")