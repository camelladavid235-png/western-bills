import streamlit as st

st.set_page_config(page_title="Western Bills", page_icon="💰", layout="centered")

st.title("💰 Western Bills")

# Reset Button
if st.button("🔄 Reset All Data"):
    st.session_state.clear()
    st.success("Reset done! Refresh page.")
    st.stop()

# Initialize
if 'users' not in st.session_state:
    st.session_state.users = {"admin@westernbills.com": {"full_name": "Admin", "status": "approved", "password": "admin123"}}

# Navigation
option = st.radio("Go to", ["Register", "Admin Panel"], horizontal=True)

if option == "Register":
    st.subheader("Create Account")
    with st.form("reg"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        country = st.selectbox("Country", ["Nigeria", "Brazil", "United States"])
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Create Account"):
            if email not in st.session_state.users:
                st.session_state.users[email] = {
                    "full_name": name, 
                    "country": country, 
                    "status": "pending", 
                    "password": password
                }
                st.success("✅ Account Created!")
                st.info("Now switch to Admin Panel and approve")
            else:
                st.error("Email already exists")

elif option == "Admin Panel":
    st.subheader("🔐 Admin Panel")
    
    if st.button("Login as Admin"):
        st.session_state.is_admin = True
    
    if st.session_state.get("is_admin"):
        st.success("✅ Admin Access Granted")
        st.subheader("Pending Users")
        
        pending = [ (e, d) for e, d in st.session_state.users.items() if d.get("status") == "pending" ]
        
        if pending:
            for email, data in pending:
                st.write(f"**{data['full_name']}** - {email}")
                if st.button(f"✅ Approve {data['full_name']}", key=email):
                    st.session_state.users[email]["status"] = "approved"
                    st.success(f"Approved {email}!")
                    st.rerun()
        else:
            st.info("No pending users. Register one first.")
    else:
        st.info("Click 'Login as Admin' above")

st.caption("WhatsApp Support: +55 18 98192-7601")