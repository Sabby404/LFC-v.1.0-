import requests
import streamlit as st
from streamlit_lottie import st_lottie

#Page Configuration

st.set_page_config(
    page_title= "Lost and Found Catalogue",
    page_icon=":wave:")

st.title("Main Page")
st.sidebar.success("Select a page above.")

#=========================================================

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_searching = load_lottieurl("https://lottie.host/e5f1c8c9-3d82-4fbb-b132-7444c0021a04/d4ZzJwixSG.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Greetings :wave:")
    st.title("Lost and Found Catalogue")
    st.write(
        "This is the Lost and Found Catalogue is an easy way to find your lost belongings or submit items that you found to the office."
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What is the Lost and Found Catalogue (LFC)?")
        st.write("##")
        st.write(
            """
           Welcome to the online lost and found website!

            Here, we help lost items find their way back home. Whether you've lost something special or found a stray item, 
            this platform is designed to make reconnecting easy. You can browse through different categories or use our search tool to find specific items. 
            If you've found something, simply share details and upload a photo to help the owner identify it. And if you're looking for a lost item, 
            just fill out a quick form with its description. Let's work together to reunite lost treasures with their owners and bring back peace of mind.

            Join our community and let's make lost and found simple and effective!
            """
        )

    with right_column:
        st_lottie(lottie_searching, height=450, key="searching")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With The Developer!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.hechanovarenel@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()