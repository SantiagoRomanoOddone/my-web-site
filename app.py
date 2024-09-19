import streamlit as st
from PIL import Image
import requests
import base64
from scr.info import * 

st.set_page_config(page_title="Main Page", page_icon="🏠", layout="wide",initial_sidebar_state="collapsed") 
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

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
    #st.sidebar.title("Navigation")
    #page = st.sidebar.radio("Go to", ["Home",  "Work Experience", "Education"])

    introduction()
    skill_tab()
    work_experience()
    education()
    # projects()
    footer()
    # elif page == "Work Experience":
    #     work_experience()
    #     footer()
    # elif page == "Education":
    #     education()
    #     footer()
    # elif page == "Projects":
    #     projects()
    #     footer()

def introduction():
    with st.container():
        st.title("Hi, I am Santiago Romano Oddone :wave:")
        st.markdown(info['about_me'])
    with st.container():
        st.markdown(
                    f'<img src="data:image/png;base64,{image_base64}" style="width:300px;margin:auto;display:block;">',
                    unsafe_allow_html=True
                )
    with st.container():
        left_column, middle_column ,right_column= st.columns([4,3,2])  # Adjust column widths

        with left_column:
            st.markdown(info['contact']['style'], unsafe_allow_html=True)
            st.markdown(info['contact']['data'], unsafe_allow_html=True)
        with right_column:
            #st.subheader("Profiles")  # Use subheader
            st.markdown(info['profiles']['style'], unsafe_allow_html=True)
            st.markdown(info['profiles']['data'], unsafe_allow_html=True)
    st.header("")
    # st.markdown("<hr style='border:2px solid white'>", unsafe_allow_html=True)
    


def skill_tab():
    st.subheader(info['skills']['title'],divider='rainbow') #,divider='rainbow'
    skill_col_size = 5
    rows,cols = len(info['skills']['data'])//skill_col_size, skill_col_size
    skills = iter(info['skills']['data'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
    st.markdown("<hr style='border:2px solid white'>", unsafe_allow_html=True)

def projects():
    st.title("Projects")
    st.write("Here are some of my projects.")
    st.write("---")

    # Display projects in a grid layout
    cols = st.columns(3)  # Create 3 columns for the grid layout

    for i, project in enumerate(info['projects']):
        with cols[i % 3]:  # Cycle through columns
            st.image(project["image"], use_column_width=True)
            st.subheader(project["title"])
            st.write(project["description"])
            st.markdown(f"[See the project]({project['link']})")

    st.markdown("<hr style='border:2px solid white'>", unsafe_allow_html=True)


def work_experience():
    st.title("Work Experience")
    st.write("---")

    # Scanntech
    with st.container():
        st.write("##")
        text_column, image_column = st.columns([2, 1])
        with text_column:
            st.subheader(info['work_experience']['scanntech']['title'])
            st.write(info['work_experience']['scanntech']['company'])
            st.write(info['work_experience']['scanntech']['duration'])
            st.write(info['work_experience']['scanntech']['description'])
        with image_column:
            st.image(scanntech.resize((300, 300)))

    st.write("---")

    # Accenture
    with st.container():
        st.write("##")
        text_column, image_column = st.columns([2, 1])
        with text_column:
            st.subheader(info['work_experience']['accenture']['title_ml'])
            st.write(info['work_experience']['accenture']['company_ml'])
            st.write(info['work_experience']['accenture']['duration_ml'])
            st.write(info['work_experience']['accenture']['description_ml'])
            st.subheader(info['work_experience']['accenture']['title_app'])
            st.write(info['work_experience']['accenture']['company_app'])
            st.write(info['work_experience']['accenture']['duration_app'])
            st.write(info['work_experience']['accenture']['description_app'])
        with image_column:
            st.image(accenture.resize((300, 200)))

    st.markdown("<hr style='border:2px solid white'>", unsafe_allow_html=True)

def education():
    st.title("Education")
    st.write("---")

    # Master in Management + Analytics
    with st.container():
        st.write("##")
        text_column, image_column = st.columns([2, 1])
        with text_column:
            st.subheader(info['education']['master']['title'])
            st.write(info['education']['master']['institution'])
            st.write(info['education']['master']['duration'])
        with image_column:
            st.image(utdt.resize((300, 300)), width=300)

    st.write("---")

    # National Technological University
    with st.container():
        st.write("##")
        text_column, image_column = st.columns([2, 1])
        with text_column:
            st.subheader(info['education']['bachelor']['title'])
            st.write(info['education']['bachelor']['institution'])
            st.write(info['education']['bachelor']['duration'])
            st.write(info['education']['bachelor']['gpa'])
        with image_column:
            st.image(utn.resize((300, 300)), width=300)


    st.markdown("<hr style='border:2px solid white'>", unsafe_allow_html=True)


def footer():
    # Add a footer
    st.header(info['footer']['header'])
    st.write("##")

    # Contact form
    contact_form = info['footer']['contact_form']
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.markdown(info['footer']['credits'], unsafe_allow_html=True)

    # Call the appropriate function based on the user's selection
    #pages[page]()

if __name__ == "__main__":
    home()