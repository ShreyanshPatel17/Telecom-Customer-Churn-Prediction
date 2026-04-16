def show_about_developer():

    import streamlit as st
    import os

    # ------------------ TITLE ------------------
    # Centers the title using native markdown-style alignment
    st.markdown("<h1 style='text-align: center;'>👨‍💻 About Developer</h1>", unsafe_allow_html=True)

    # Adds space below using empty text or markdown
    st.write("") 
    st.write("")

    # ------------------ PROFILE + INTRO ------------------
    col1, col2 = st.columns([1, 2])

    with col1:
        # Profile Image
        image_path = "assets/profile photo.jpg"   # profile photo file name

        if os.path.exists(image_path):
            with st.container(horizontal_alignment="center"):
                st.image(image_path, width=200)
        else:
            st.warning("Profile image not found in assets folder")

        # Resume Download Button
        resume_path = "assets/Shreyansh Resume.pdf"   # resume file name

        if os.path.exists(resume_path):
            with st.container(horizontal_alignment="center"):
                with open(resume_path, "rb") as file:
                    st.download_button(
                        label="📄 Download Resume",
                        data=file,
                        file_name="Shreyansh_Patel_Resume.pdf",
                        mime="application/pdf"
                    )
        else:
            st.warning("Resume file not found in assets folder")

    with col2:
        st.markdown("""
        ### 👋 Hi, I'm **Shreyansh Patel**
        <div style="font-size:1.1rem;">
        Aspiring Data Scientist with a strong interest in <strong>Machine Learning</strong> and <strong>Artificial Intelligence</strong>, currently pursuing MCA.

        I have hands-on experience in data analysis, visualization, and predictive modeling. I enjoy building real-world applications that solve business problems using data-driven approaches.

        - 📍 **Location**: Gujarat, India  
        - 📧 **Email**: 17Shreyanshpatel@gmail.com  
        - 🔗 [LinkedIn](https://linkedin.com/in/shreyanshpatel17)  
        - 💻 [GitHub](https://github.com/shreyanshpatel17)
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ------------------ EDUCATION ------------------
    st.markdown("## 🎓 Education")

    st.markdown("""
    <div style="line-height:1.8; font-size:1.05rem;">

    <span style="font-weight:900; color:#ffffff; font-size:1.2rem;">
    🧑‍🎓 Master of Computer Applications (MCA)
    </span><br>
    <span style="color:#d1d5db;">
    &nbsp; &nbsp; &nbsp; &nbsp; Specialization in Artificial Intelligence & Data Science<br>
    &nbsp; &nbsp; &nbsp; &nbsp; D Y Patil International University, Pune
    </span>
    <br>
    <span style="font-weight:900; color:#ffffff; font-size:1.2rem;">
    🎓 Bachelor of Science (BSc) in Computer Science
    </span><br>
    <span style="color:#d1d5db; font-size:1.05rem;">
    &nbsp; &nbsp; &nbsp; &nbsp; SSR College of Arts, Commerce and Science<br>
    &nbsp; &nbsp; &nbsp; &nbsp; (Affiliated to Savitribai Phule Pune University)
    </span>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ------------------ SKILLS ------------------
    st.markdown("## 🧠 Skills")

    st.markdown("""
    <div style="font-size:1.1rem;">
    - <strong>Languages</strong>:&nbsp; Python, SQL<br>  
    - <strong>Libraries</strong>:&nbsp; Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn<br>
    - <strong>Tools</strong>:&nbsp; Power BI, Excel, MySQL, Jupyter Notebook, VS Code<br>
    - <strong>Core Areas</strong>:&nbsp; Data Science, Machine Learning, Data Analytics, Predictive Modeling, EDA, Data Visualization, Problem Solving  
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ------------------ WHY THIS PROJECT ------------------
    st.markdown("## 🎯 Why This Project?")

    st.markdown("""
    <div style="font-size:1.1rem;">
    This project was developed to understand customer behavior and apply machine learning techniques to solve real-world business challenges like customer churn.

    Customer retention is a major concern for telecom companies, and predicting churn in advance allows businesses to take proactive actions.

    Through this project, I aimed to:<br>
    - Apply end-to-end Machine Learning workflow<br>
    - Work with real-world datasets<br>
    - Build an interactive and user-friendly application<br>  
    - Deliver actionable insights for business decision-making
    
    This project also serves as a showcase of my skills and passion for data science, and I hope it can inspire others to explore the field further!
    </div> 
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ------------------ BACK BUTTON ------------------
    if st.button("⬅ Back to App"):
        st.session_state.page = "main"