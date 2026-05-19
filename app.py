import streamlit as st

st.set_page_config(page_title="Western Bills", page_icon="💰", layout="centered")

st.title("💰 Western Bills")
st.subheader("Fast Global Money Transfer")

# Reset Button
if st.button("🔄 Reset All Data"):
    st.session_state.clear()
    st.success("✅ Reset Complete. Refresh the page.")
    st.stop()

# Initialize Data
if 'users' not in st.session_state:
    st.session_state.users = {
        "admin@westernbills.com": {"name": "System Admin", "status": "approved", "password": "admin123"}
    }

# Navigation
page = st.selectbox("Select Page", ["📝 Register", "🔐 Admin Panel"])

if page == "📝 Register":
    st.subheader("Create New Account")
    with st.form("register"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        country = st.selectbox("Country", ["Nigeria", "Brazil", "United States"])
        password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Create Account"):
            if email in st.session_state.users:
                st.error("❌ Email already exists")
            else:
                st.session_state.users[email] = {
                    "name": name,
                    "country": country,
                    "status": "pending",
                    "password": password
                }
                st.success("✅ Account Created Successfully!")
                st.info("Now go to Admin Panel → Login as Admin → Approve")

elif page == "🔐 Admin Panel":
    st.subheader("🔐 Admin Panel")
    
    if st.button("Login as Admin", type="primary"):
        st.session_state.is_admin = True
    
    if st.session_state.get("is_admin"):
        st.success("✅ Admin Access Granted")
        st.subheader("Pending Users")
        
        for email, data in st.session_state.users.items():
            if data.get("status") == "pending":
                st.write(f"**{data['name']}**")
                st.write(f"Email: {email}")
                if st.button(f"✅ Approve {data['name']}", key=email):
                    st.session_state.users[email]["status"] = "approved"
                    st.success(f"✅ {email} Approved!")
                    st.rerun()
    else:
        st.info("Click 'Login as Admin' above")

st.caption("WhatsApp Support: +55 18 98192-7601")