import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import requests
import base64



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # ---- LOAD ASSETS ----
# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
sales_forcasting = Image.open("images/sales-forcasting.png")
properati = Image.open("images/properati.png")
utdt = Image.open("images/UTDT.png")
utn = Image.open("images/UTN.png")
me_path = "images/RomanoOddoneSantiago.png"
accenture = Image.open('images/accenture.png')
scanntech = Image.open('images/scanntech.png')
munira = Image.open('images/munira.png')
me_image = Image.open(me_path)
# Convert the image to base64
with open(me_path, "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode("utf-8")
local_css("style/style.css")



def home():
    with st.container():
        introduction()
    st.write("---")
    with st.container():
        work_experience()
    st.write("---")
    with st.container():
        education()
    st.write("---")
    with st.container():
        projects()

    with st.container():
        footer()

def introduction():
    st.title("Welcome to my homepage!")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns([3, 1])  # Adjust column widths
        with left_column:
            st.title("Hi, I am Santiago Romano Oddone :wave:")
            st.markdown("""
            I'm a Machine Learning Engineer with a solid background in industrial engineering, currently pursuing a Master's in Management and Analytics. I specialize in developing AI models to predict scenarios and uncover meaningful patterns in data. With a focus on applying advanced analytics, I am poised to contribute innovative solutions to real-world business challenges.
            """)
        with right_column:
            st.markdown(
                f'<img src="data:image/png;base64,{image_base64}" style="width:300px;margin:auto;display:block;">',
                unsafe_allow_html=True
            )
    with st.container():
        st.write("---")
        left_column, right_column = st.columns([3, 1])  # Adjust column widths

        with left_column:
            st.subheader("Contact")  # Use subheader
            st.markdown(
            """
            - Email: santiagoromano15@gmail.com
            - Phone: +5493884840234
            - Location: Buenos Aires, Argentina
            """)
        with right_column:
            st.subheader("Profiles")  # Use subheader
            st.markdown("""
            - [LinkedIn](https://linkedin.com/in/santiagoromanooddone)
            - [GitHub](https://github.com/SantiagoRomanoOddone)
            - [Kaggle](https://kaggle.com/santiagoromanooddone)
            """)
    

    with st.container():
        st.write("---")
        left_column, right_column = st.columns([2, 1])  # Adjust column widths
        with left_column:
            st_lottie(lottie_coding, height=300, key="coding")
        with right_column:
            st.header("What I do")
            st.write("I am passionate about finding ways to use AI and Data Science to build solutions for industry and business challenges.")
            st.write("[Learn More >](https://github.com/SantiagoRomanoOddone)")

def projects():
    st.title("Projects")
    st.write("Here are some of my projects.")
    st.write("---")
    # st.header("My Projects")
    with st.container():
        st.write("##")
        text_column, image_column  = st.columns(2)
        #text_column, image_column = st.columns((1, 2))
        with text_column:
        
            st.subheader("Rossmann Store Sales")
            st.write(
                """
                Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, and more.

                In this Kaggle competition, Rossmann is challenging you to predict 6 weeks of daily sales for 1,115 stores located across Germany. Reliable sales forecasts enable store managers to create effective staff schedules that increase productivity and motivation. 
                """
            )
            st.markdown("[see the challenge..](https://github.com/SantiagoRomanoOddone/rossmann-store-sales)")
        with image_column:
            st.image(sales_forcasting.resize((300, 200)))
        
    with st.container():
        #text_column, image_column  = st.columns((1, 2))
        text_column, image_column  = st.columns(2)
        with text_column:
            st.subheader("contact prediction challenge")
            st.write(
                """
                I've participated in a competition hosted by Properatti, a prominent real estate portal across various countries. The challenge involved developing a predictive model to determine if property listings published during specific months in 2022 would receive a minimum of three contacts within the first 15 days of publication. 
                
                This project aims to enhance Properatti's services by providing valuable insights into listing performance, aiding in targeted marketing strategies, and facilitating improved communication with partner agencies.
                """
            )
            st.markdown("[see the challenge...](https://github.com/SantiagoRomanoOddone/contact-prediction-challenge)")
        with image_column:
            st.image(properati.resize((300, 200)))
    
def work_experience():
    st.title("Work Experience")

    # Scanntech
    with st.container():
        st.write("##")
        text_column, image_column  = st.columns(2)
        #text_column, image_column = st.columns((1, 2))
        with text_column:  
            st.subheader("Data Scientist")
            st.write("[Scanntech Uruguay](https://scanntech.com)")
            st.write("02/2024 - Present, Buenos Aires, Argentina")
            st.write("""
            - Developing and implementing advanced forecasting models in production environments for large corporations to accurately predict product demand throughout the supply chain, optimizing inventory management to prevent shortages and surplus goods.
            """)
        with image_column:
            st.image(scanntech.resize((300, 300)))

    st.write("---")
    # Accenture
    with st.container():
        st.write("##")
        text_column, image_column  = st.columns(2)
        #text_column, image_column = st.columns((1, 2))
        with text_column:
        
            st.subheader("Machine Learning Engineer")
            st.write("[Accenture Argentina](https://www.accenture.com/ar-es)")
            st.write("08/2023 - Present, Buenos Aires, Argentina")
            st.write("""
            - Managing the implementation and optimization of worldwide demand and supply prediction models in production environments.
            - Collaborating effectively with data science teams to analyze monthly results and enhance the predictive capabilities of the models.
            - Building supervised and unsupervised Machine Learning models for client clustering and cluster prediction.
            """)
            st.write("---")
            st.subheader("Application Developer")
            st.write("[Accenture Argentina](https://www.accenture.com/ar-es)")
            st.write("02/2022 - 07/2023, Buenos Aires, Argentina")
            st.write("""
            - Developing and managing ETL solutions for importing/exporting, loading, and processing data.
            - Developing and managing .NET CORE applications.
            """)
        with image_column:
            st.image(accenture.resize((300, 200)))
    
    st.write("---")
    # MuniraFoods
    with st.container():
        st.write("##")
        text_column, image_column  = st.columns(2)
        #text_column, image_column = st.columns((1, 2))
        with text_column:
        
            st.subheader("Business Analyst")
            st.write("[MuniraFoods](https://munirafoods.com)")
            st.write("03/2021 - 09/2021, Córdoba, Argentina")
            st.write("""
            - Monitoring and analyzing operational processes by creating Key Performance Indicators (KPIs) for each product line.
            - Identifying and monitoring operational and compliance risks.
            - Applying continuous improvement techniques to production and logistics processes.
            """)
        with image_column:
            st.image(munira.resize((300, 200)))

def education():
    st.title("Education")
    with st.container():
        text_column, image_column  = st.columns(2)
        with text_column:
            st.subheader("[Master in Management + Analytics](https://www.utdt.edu/listado_contenidos.php?id_item_menu=25098)")
            st.write("[Torcuato Di Tella University](https://www.utdt.edu)")
            st.write("03/2023 - Present, Buenos Aires, Argentina")
        with image_column:
            st.image(utdt.resize((300, 300)), width=300 )
    st.write("---")
    with st.container():
        text_column, image_column  = st.columns(2)
        with text_column:
            st.subheader("Industrial Engineering")
            st.write("[National Technological University](https://www.frc.utn.edu.ar)")
            st.write("03/2015 - 12/2020, Córdoba, Argentina")
            st.write("GPA: 8.35/10")
        with image_column:
            st.image(utn.resize((300, 300)), width=300)

def footer():
    # Add a footer
    st.markdown("---")
    st.markdown("Made with Streamlit by Santiago Romano Oddone")
    st.markdown("[LinkedIn](https://linkedin.com/in/santiagoromanooddone) | [GitHub](https://github.com/SantiagoRomanoOddone)")

    # # ---- CONTACT ----

    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

        # Documention: https://formsubmit.co/ !
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
# def certificates():
#     st.title("Certificates")
#     st.write("Here are my certificates.")
#     st.write("---")
#     #st.header("Certificates")
#     st.write("- Deep Learning Specialization (12/2023), Provider: Deeplearning.ai")
#     st.write("- AWS Certified Cloud Practitioner (11/2023), Provider: AWS")
#     st.write("- Modern Natural Language Processing in Python (01/2023), Provider: Udemy")

# Add a navigation bar


# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Home",  "Work Experience", "Education", "Projects"])
# # Use a dictionary to map page names to functions
# pages = {
#     "Home": introduction,
#     "Work Experience": work_experience,
#     "Education": education,
#     "Projects": projects
# }

# # Call the appropriate function based on the user's selection
# pages[page]()

if __name__ == "__main__":
    home()