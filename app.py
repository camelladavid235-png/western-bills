import streamlit as st

st.set_page_config(page_title="Western Bills", page_icon="💰")

st.title("💰 Western Bills")

if st.button("🔄 Reset Everything"):
    st.session_state.clear()
    st.success("Reset done. Refresh page.")
    st.stop()

if 'users' not in st.session_state:
    st.session_state.users = {"admin@westernbills.com": {"name": "Admin", "status": "approved"}}

tab1, tab2 = st.tabs(["📝 Register", "🔐 Admin Panel"])

with tab1:
    st.subheader("Register New User")
    with st.form("reg"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        if st.form_submit_button("Create Account"):
            if email not in st.session_state.users:
                st.session_state.users[email] = {"name": name, "status": "pending"}
                st.success("✅ Account Created!")
                st.info("Switch to Admin Panel tab")
            else:
                st.error("Email already exists")

with tab2:
    st.subheader("Admin Panel")
    if st.button("Login as Admin"):
        st.session_state.admin_logged = True
    
    if st.session_state.get("admin_logged"):
        st.success("✅ Admin Access Granted")
        st.subheader("Pending Users")
        
        for email, data in st.session_state.users.items():
            if data.get("status") == "pending":
                st.write(f"**{data['name']}**")
                st.write(email)
                if st.button("✅ Approve", key=email):
                    st.session_state.users[email]["status"] = "approved"
                    st.success("Approved!")
                    st.rerun()
    else:
        st.info("Click 'Login as Admin'")

st.caption("WhatsApp Support: +55 18 98192-7601")