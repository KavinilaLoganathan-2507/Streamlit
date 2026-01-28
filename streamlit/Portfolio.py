import streamlit as st

# Page config
st.set_page_config(page_title="My Portfolio", page_icon="🌟")
st.image("images/Code_demo.jpg", caption="My Profile Photo", width=250)
# Sidebar
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

# Home
if menu == "Home":
    st.title("👩‍💻INNO_CORES")
    st.subheader("Aspiring Full Stack Developer and Enthusiast")
    st.write("Welcome to my Streamlit portfolio! Explore my projects and get in touch.")

# About
elif menu == "About":
    st.header("Viduna , Ranjith, Anish, Kavinila, Boomathi, Ashwin")
    st.write("""
    - Beginner Full Stack Developer 
    - Passionate about coding and technology
    - Eager to learn and grow in the tech industry
    """)

# Projects
elif menu == "Projects":
    st.header("🛠 Projects")
    st.write("🔹 Ergonomics analysis ")
    st.write("🔹 guessing game ")
    st.write("🔹 Class room engagement system ")

# Contact
elif menu == "Contact":
    st.header("📞 Contact Me")
    email = st.text_input("Enter your email")
    msg = st.text_area("Your message")

    if st.button("Send"):
        st.success("Message sent successfully ✅")