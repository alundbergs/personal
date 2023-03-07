import requests
import streamlit as st
#from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


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
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_project_2.png")
img_lottie_animation = Image.open("images/yt_project_1.png")
img_profile = Image.open("images/arturs.png")

# ---- HEADER SECTION ----
with st.container():
    st.image(img_profile)

with st.container():
    st.subheader("Hi, I am Arturs")
    st.title("Automation Engineer")
    st.write(
        "I am passionate about finding ways to use Python to be more efficient and effective in business settings."
    )
    st.write("[Learn More >](https://alundbergs-new-product-streamlit-app-k8faur.streamlit.app/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """

            - I am looking for a way to leverage the power of Python in day-to-day work.
            - I am learning Data Analysis & Data Science to perform meaningful and impactful analyses.

            If this sounds interesting to you, be free to Contact me.
            """
        )
        st.write("[Email >](mailto:a.lundbergs@gmail.com)")
    with right_column:
        st.write("##")

    #     st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Your Streamlit Apps")
        st.write(
            """
            Learn how to use Files in Streamlit!
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To create Mobile Apps")
        st.write(
            """
            Want to add a mobile App to your Project?
            I'm going to show you how to create mobile app using a free service.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/a.lundbergs@gmail.com" method="POST">
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
