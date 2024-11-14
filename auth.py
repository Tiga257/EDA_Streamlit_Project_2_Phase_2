import streamlit as st
from home import home_page

# Authentication function
def authenticate():
    """Handles the authentication process."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    # If not authenticated, show login form
    if not st.session_state.authenticated:
        login_form()
    else:
        show_authenticated_content()

# Login form function
def login_form():
    """Displays a simple login form."""
    st.title("Login")
    with st.form("login_form"):
        # Input fields for username and password
        username = st.text_input("Username", key="username_input")
        password = st.text_input("Password", type="password", key="password_input")

        # Submit button logic for login
        submitted = st.form_submit_button("Login")
        if submitted:
            if username == "admin" and password == "password":  # Check credentials
                st.session_state.authenticated = True
                st.success("Successfully logged in!")
            else:
                st.error("Invalid credentials")
            

# Show content after successful authentication
def show_authenticated_content():
  
    # Logout button that clears the session state
    if st.sidebar.button("Logout"):
        logout()

# Logout function
def logout():
    """Logs the user out and resets session state."""
    st.session_state.authenticated = False
    st.success("Logged out!")

# Main function
def main():
    """Main entry point for the Streamlit app."""
    authenticate()

# Run the main function
if __name__ == "__main__":
    main()
