import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Lost Items")
st.sidebar.success("Select a page above.")

# ---- HEADER SECTION ----
with st.container():
    st.write(
            """

            This is the Lost Items section of the Lost and Found Catalogue. In this page, you can look for any of your missing 
            belongings by simply providing sufficient description and a photo of the item. 
            
            """
    )

# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing lost entry data
existing_data = conn.read(worksheet="Lost_Entry", usecols=list(range(14)), ttl=5)
existing_data = existing_data.dropna(how="all")

st.dataframe(existing_data)