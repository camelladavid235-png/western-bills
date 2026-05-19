import streamlit as st

st.set_page_config(page_title="Western Bills", page_icon="💰")

st.title("💰 Western Bills")

if st.button("🔄 Reset Everything"):
    st.session_state.clear()
    st.success("Reset done - Refresh page")
    st.stop()

if 'users' not in st.session_state:
    st.session_state.users = {"admin@westernbills.com": {"name": "Admin", "status": "approved"}}

option = st.radio("Choose Page", ["Register New User", "Admin Panel"], horizontal=True)

if option == "Register New User":
    st.subheader("Register")
    with st.form("form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        if st.form_submit_button("Create Account"):
            if email not in st.session_state.users:
                st.session_state.users[email] = {"name": name, "status": "pending"}
                st.success("Account Created!")
                st.info("Go to Admin Panel now")
            else:
                st.error("Email exists")

elif option == "Admin Panel":
    st.subheader("Admin Panel")
    if st.button("Login as Admin"):
        st.session_state.admin = True
    
    if st.session_state.get("admin"):
        st.success("Admin Logged In")
        st.subheader("Pending Users")
        for e, d in st.session_state.users.items():
            if d.get("status") == "pending":
                st.write(f"**{d['name']}** - {e}")
                if st.button("Approve", key=e):
                    st.session_state.users[e]["status"] = "approved"
                    st.success("Approved!")
                    st.rerun()
    else:
        st.info("Click Login as Admin")

st.caption("WhatsApp: +55 18 98192-7601")