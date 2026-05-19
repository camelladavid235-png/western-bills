import streamlit as st

st.set_page_config(page_title="Western Bills", page_icon="💰", layout="centered")

# Reset Button
if st.sidebar.button("🔄 Reset All Data"):
    st.session_state.clear()
    st.success("✅ All data cleared. Refresh the page.")
    st.stop()

# Initialize users
if 'users' not in st.session_state:
    st.session_state.users = {
        "admin@westernbills.com": {"full_name": "Admin", "status": "approved", "password": "admin123"}
    }

page = st.sidebar.selectbox("Go to", ["🏠 Home", "📝 Register", "🔐 Admin Panel"])

if page == "🏠 Home":
    st.title("💰 Western Bills")
    st.write("Fast Global Money Transfer")

elif page == "📝 Register":
    st.title("Create Account")
    with st.form("reg"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        country = st.selectbox("Country", ["Nigeria", "Brazil", "United States"])
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Create Account"):
            if email in st.session_state.users:
                st.error("Email already exists")
            else:
                st.session_state.users[email] = {
                    "full_name": name,
                    "country": country,
                    "status": "pending",
                    "password": password
                }
                st.success("✅ Account Created!")
                st.info("✅ Now go to Admin Panel and approve")

elif page == "🔐 Admin Panel":
    st.title("🔐 Admin Panel")
    
    if st.button("🔓 Login as Admin", type="primary"):
        st.session_state.is_admin = True
        st.rerun()
    
    if st.session_state.get("is_admin"):
        st.success("✅ Admin Access Granted")
        st.subheader("Pending Users")
        
        found = False
        for email, info in list(st.session_state.users.items()):
            if info.get("status") == "pending":
                found = True
                st.write(f"**{info['full_name']}**")
                st.write(f"Email: {email}")
                if st.button(f"✅ Approve {info['full_name']}", key=email):
                    st.session_state.users[email]["status"] = "approved"
                    st.success(f"{email} Approved!")
                    st.rerun()
        
        if not found:
            st.info("No pending users yet. Create one from Register page.")
    else:
        st.info("Click 'Login as Admin' above")

st.caption("Western Bills Demo • WhatsApp: +55 18 98192-7601")