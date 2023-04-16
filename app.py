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
img_project_3 = Image.open("images/addon.png")
img_project_4 = Image.open("images/project_4.png")
img_project_5 = Image.open("images/project_5.png")
img_project_6 = Image.open("images/project_6.png")
img_project_7 = Image.open("images/project_7.png")
img_project_all = Image.open("images/projects_all.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.image(img_profile)

with st.container():
    st.subheader("Hi, I am Arturs")
    st.title("Automation Engineer")
    st.write(
        "I am passionate about finding ways to use Python to be more efficient and effective in business settings."
    )
    st.write("[Learn More >](https://lundbergsprd.streamlit.app/)")

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
        st.write("[Email](mailto:a.lundbergs@gmail.com)")
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
        st.subheader("Integrate Datasets in Your Streamlit Apps")
        st.write(
            """
            Learn how to load hundreds of datasets in a Streamlit app with PyDataset.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/bNaRdDWR-W4)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To create Mobile Apps")
        st.write(
            """
            Want to add a mobile App to your Project?
            Here is how to create mobile app using a free Framework.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/bMHK6NDVlCM)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project_3)
    with text_column:
        st.subheader("Static Ecommerce Website")
        st.write(
            """
            Ecommerce Website with integrated Stripe Payment Solution.
            """
        )
        st.markdown("[Project Link...](https://lundbergsprd.streamlit.app/)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project_4)
    with text_column:
        st.subheader("Full Stack Ecommerce App")
        st.write(
            """
            Full Stack Ecommerce App with user and product SQL DB, user Login System, automatic Google Signup and integrated Stripe Payment Solution.
            """
        )
        st.markdown("[Project Link...](https://y4ktyhwycn3jnxl5.anvil.app/RKD7O6X6DPKPBAOE7QDDEZBQ)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project_5)
    with text_column:
        st.subheader("Flask Taskmaster Web App")
        st.write(
            """
            Basic Flask Taskmaster Web App with Add, Delete and Update Functions.
            """
        )
        st.markdown("[Project Link...](https://flasktaskmaster.zirnis.repl.co/)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project_6)
    with text_column:
        st.subheader("Smart Factory Digital Twin")
        st.write(
            """
            Data driven Smart Factory Digital Twin Web App.
            """
        )
        st.markdown("[Project Link...](https://xlsdash.streamlit.app/)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project_7)
    with text_column:
        st.subheader("Business Automations")
        st.write(
            """
            Marketing Automation and Workflow creation.
            """
        )
        st.markdown("[Project Link...](https://student-27135688.hubspotpagebuilder.eu/landing)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project_all)
    with text_column:
        st.subheader("Other Projects")
        st.write(
            """
            Click on Links:
            """
        )
        st.markdown("[Consulting Website...](https://lundbergs.netlify.app/)")
        st.markdown("[Open Database Solution for Industry...](https://airtable.com/appPF6TVXYykEkRzb/tblAukmk0Kd1aM2tN/viwJfegfXH83WKZvX?blocks=hide)")
        st.markdown("[Plant Design Answer Assistant...](https://f5ctowkbfel5dues.anvil.app/A5DW2IMJQ6CXWQA62KBFCITB)")

        
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
