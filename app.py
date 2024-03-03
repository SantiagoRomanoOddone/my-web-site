import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import requests


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# # ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
sales_forcasting = Image.open("images/sales-forcasting.png")
properati = Image.open("images/properati.png")

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
#with st.container():
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.subheader("Hi, I am Santiago Romano Oddone :wave:")
st.title("A Machine Learning Engineer and Data Scientist From Argentina")
st.write(
            "I am passionate about finding ways to use AI and Data Science to build solutions for industry and business challenges."
        )
st.write("[Learn More >](https://github.com/SantiagoRomanoOddone)")




# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")



# # ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
        """
        I am a Machine Learning Engineer with a solid background in industrial engineering, currently pursuing a Master's in Management and Analytics.
        I specialize in developing AI models to predict scenarios and uncover meaningful patterns in data. With a focus on applying advanced analytics, I am poised to contribute innovative solutions to real-world business challenges.
        """
    )
    with right_column:
         st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(sales_forcasting)
    with text_column:
        st.subheader("sales forcasting challenge")
        st.write(
            """
            complete
            """
        )
        st.markdown("[see the challenge..](https://github.com/SantiagoRomanoOddone/marketing-sales-analysis)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(properati)
    with text_column:
        st.subheader("contact prediction challenge")
        st.write(
            """
            complete
            """
        )
        st.markdown("[see the challenge...](https://github.com/SantiagoRomanoOddone/contact-prediction-challenge)")

# # ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/santiagoromano15@gmail.com" method="POST">
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