import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="World Cities",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and welcome section
st.title("🌍 Welcome to World Cities")

st.markdown("""
    ## Explore the World's Cities

    Welcome to the World Cities application! This is your gateway to discovering 
    information about cities around the globe.

    ### About This App
    This multipage application provides various tools and resources to learn more 
    about cities worldwide, including demographics, geography, and more.

    ---
""")

# Main content area
col1, col2 = st.columns(2)

with col1:
    st.info("""
        ### 📍 Features
        - Explore city data
        - View statistics
        - Discover insights about world cities
    """)

with col2:
    st.success("""
        ### 🚀 Getting Started
        Click the button below to navigate to the main application
        and start exploring!
    """)

# Navigation button to app.py
st.markdown("---")
if st.button("🚀 Go to Cities Explorer", use_container_width=True, type="primary"):
    st.switch_page("pages/app.py")

st.markdown("""
    ---
    *Built with Streamlit | Explore the world, one city at a time*
""")
