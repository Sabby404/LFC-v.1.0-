import streamlit as st

st.title("Found")
st.sidebar.success("Select a page above.")

# ---- HEADER SECTION ----
with st.container():
    st.write(
            """

            This is the Found Items section of the Lost and Found Catalogue. In this page, you can look for any of your missing 
            belongings by browsing through the following list. The items on this list are submitted/surrendered to the office 
            by individuals who found it. 

            The surrendered items are kept and stored at the office storage room to ensure security.
            
            """
    )

#-----------------------------

