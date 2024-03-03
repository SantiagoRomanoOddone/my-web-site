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


# CV section
st.write('<div id="cv"></div>', unsafe_allow_html=True)  # Anchor for CV link
st.header("CV: Santiago Romano Oddone")
st.write("Machine Learning Engineer / Data Scientist")
st.write(
    """
    I'm a Machine Learning Engineer with a solid background in industrial engineering, currently pursuing a Master's in Management and Analytics.
    I specialize in developing AI models to predict scenarios and uncover meaningful patterns in data. With a focus on applying advanced analytics, I am poised to contribute innovative solutions to real-world business challenges.
    """
)
st.write("santiagoromano15@gmail.com +5493884840234")
st.write("Buenos Aires, Argentina")
st.write("[Kaggle Profile](www.kaggle.com/santiagoromanooddone)")
st.write("[LinkedIn Profile](linkedin.com/in/santiagoromanooddone)")
st.write("[GitHub Profile](github.com/SantiagoRomanoOddone)")
st.write("[Instagram Profile](instagram.com/santirom15)")

# Work Experience section
st.write("---")
st.header("Work Experience")

# Accenture
st.subheader("Machine Learning Engineer")
st.write("Accenture Argentina")
st.write("08/2023 - Present, Buenos Aires, Argentina")
st.write(
    """
    - Managing the implementation and optimization of worldwide demand and supply prediction models in production environments.
    - Collaborating effectively with data science teams to analyze monthly results and enhance the predictive capabilities of the models.
    """
)

st.subheader("Application Developer")
st.write("Accenture Argentina")
st.write("02/2022 - 07/2023, Buenos Aires, Argentina")
st.write(
    """
    - Building supervised and unsupervised Machine Learning models for client clustering and cluster prediction.
    - Developing and managing ETL packages, projects, and solutions for importing/exporting, loading, and processing data.
    - Developing and managing .NET CORE applications.
    """
)

# MuniraFoods
st.subheader("Business Analyst")
st.write("MuniraFoods")
st.write("03/2021 - 09/2021, Córdoba, Argentina")
st.write(
    """
    - Monitoring and analyzing operational processes by creating Key Performance Indicators (KPIs) for each product line.
    - Identifying and monitoring operational and compliance risks.
    - Applying continuous improvement techniques to production and logistics processes.
    """
)

# Education section
st.write("---")
st.header("Education")

st.subheader("Master in Management + Analytics")
st.write("Torcuato Di Tella University")
st.write("03/2023 - Present, Buenos Aires, Argentina")

st.subheader("Industrial Engineering")
st.write("National Technological University")
st.write("03/2015 - 12/2020, Córdoba, Argentina")
st.write("GPA: 8.35/10")

# Programming Languages section
st.write("---")
st.header("Programming Languages")
st.write("- Python")
st.write("- SQL")
st.write("- R")
st.write("- C#")
st.write("- GitHub")

# Certificates section
st.write("---")
st.header("Certificates")
st.write("- Deep Learning Specialization (12/2023), Provider: Deeplearning.ai")
st.write("- AWS Certified Cloud Practitioner (11/2023), Provider: AWS")
st.write("- Modern Natural Language Processing in Python (01/2023), Provider: Udemy")

# Professional Skills section
st.write("---")
st.header("Professional Skills")
st.write("- Problem-solving")
st.write("- Proactive")
st.write("- Analytical thinking")
st.write("- Continuous Learning")
st.write("- Effective communication")

# Languages section
st.write("---")
st.header("Languages")
st.write("- Spanish")
st.write("- English")

# Interests section
st.write("---")
st.header("Interests")
st.write("- Artificial Intelligence")
st.write("- Business Analytics")


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