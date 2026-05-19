import streamlit as st

st.set_page_config(page_title="Western Bills", page_icon="💰", layout="centered")

st.title("💰 Western Bills")
st.subheader("Fast Global Money Transfer")

if st.button("🔄 Reset All Data"):
    st.session_state.clear()
    st.success("Reset Complete! Refresh the page.")
    st.stop()

# Initialize
if 'users' not in st.session_state:
    st.session_state.users = {
        "admin@westernbills.com": {"name": "System Admin", "status": "approved"}
    }

# Main Navigation
page = st.selectbox("Select Page", ["Register", "Admin Panel"])

if page == "Register":
    st.subheader("Create New Account")
    with st.form("register"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        if st.form_submit_button("Create Account"):
            if email in st.session_state.users:
                st.error("Email already exists")
            else:
                st.session_state.users[email] = {"name": name, "status": "pending"}
                st.success("✅ Account Created Successfully!")
                st.info("Now go to Admin Panel and approve")

elif page == "Admin Panel":
    st.subheader("🔐 Admin Panel")
    
    if st.button("Login as Admin"):
        st.session_state.admin = True
    
    if st.session_state.get("admin"):
        st.success("✅ Admin Logged In")
        st.subheader("Pending Users")
        
        for email, data in st.session_state.users.items():
            if data.get("status") == "pending":
                st.write(f"**{data['name']}**")
                st.write(email)
                if st.button("✅ Approve this user", key=email):
                    st.session_state.users[email]["status"] = "approved"
                    st.success(f"✅ {email} has been approved!")
                    st.rerun()
    else:
        st.info("Click the button above to login as Admin")

st.caption("WhatsApp Support: +55 18 98192-7601")