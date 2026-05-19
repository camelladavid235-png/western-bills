import streamlit as st

st.set_page_config(page_title="Western Bills", page_icon="💰", layout="centered")

st.title("💰 Western Bills")
st.caption("Fast Global Money Transfer")

# Reset Button
if st.button("🔄 Reset All Data"):
    st.session_state.clear()
    st.success("App Reset! Please refresh the page.")
    st.stop()

# Initialize
if 'users' not in st.session_state:
    st.session_state.users = {
        "admin@westernbills.com": {"full_name": "Admin", "status": "approved", "password": "admin123"}
    }

tab1, tab2, tab3 = st.tabs(["📝 Register", "🔑 Login", "🔐 Admin Panel"])

with tab1:
    st.subheader("Create New Account")
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
                    "full_name": name, "country": country, "status": "pending", "password": password
                }
                st.success("✅ Account Created Successfully!")
                st.info("Go to Admin Panel tab to approve")

with tab2:
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email in st.session_state.users and st.session_state.users[email]["password"] == password:
            if st.session_state.users[email]["status"] == "approved":
                st.success(f"✅ Welcome {st.session_state.users[email]['full_name']}!")
                st.session_state.current_user = email
            else:
                st.error("Account not approved yet")
        else:
            st.error("Invalid login")

with tab3:
    st.subheader("🔐 Admin Panel")
    if st.button("Login as Admin"):
        st.session_state.is_admin = True
    
    if st.session_state.get("is_admin"):
        st.success("✅ Admin Access Granted")
        st.subheader("Pending Users")
        
        for email, data in list(st.session_state.users.items()):
            if data.get("status") == "pending":
                st.write(f"**{data['full_name']}** - {email}")
                if st.button(f"✅ Approve {data['full_name']}", key=email):
                    st.session_state.users[email]["status"] = "approved"
                    st.success(f"{email} Approved!")
                    st.rerun()
    else:
        st.info("Click 'Login as Admin' above")

st.caption("Western Bills Demo • WhatsApp: +55 18 98192-7601")