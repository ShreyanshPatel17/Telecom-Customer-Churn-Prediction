import streamlit as st
from streamlit_option_menu import option_menu

if "page" not in st.session_state:
    st.session_state.page = "main"

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Telecom Churn Prediction",
    layout="wide",
    page_icon="📊"
)

# ------------------ HIDE DEFAULT SIDEBAR ------------------
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# ------------------ GLOBAL STYLING ------------------
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}            

/* ===== SIDEBAR BASE ===== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a, #1e293b);
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* ===== APP TITLE ===== */
.sidebar-title {
    font-size: 22px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 15px;
    background: linear-gradient(90deg, #38f9d7, #43e97b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ===== OPTION MENU ITEMS ===== */
.nav-link {
    border-radius: 10px !important;
    transition: all 0.3s ease !important;
}

/* Hover effect */
.nav-link:hover {
    background: rgba(255,255,255,0.08) !important;
    transform: translateX(5px);
}

/* Active item */
button[aria-selected="true"] {
    background: linear-gradient(90deg, #ff512f, #dd2476) !important;
    color: white !important;
    font-weight: bold !important;
    box-shadow: 0 0 10px rgba(255, 81, 47, 0.6);
}

/* ===== DIVIDER ===== */
.sidebar-divider {
    height: 1px;
    background: rgba(255,255,255,0.1);
    margin: 20px 0;
}

/* ===== BOTTOM BUTTON ===== */
.sidebar-bottom {
    position: fixed;
    bottom: 20px;
    left: 15px;
    right: 15px;
}

/* Button style */
.sidebar-bottom button {
    width: 100%;
    border-radius: 12px !important;
    font-weight: bold !important;
    background: linear-gradient(90deg, #38f9d7, #43e97b) !important;
    color: black !important;
    transition: 0.3s;
}

/* Button hover */
.sidebar-bottom button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #43e97b, #38f9d7) !important;
}

/* ===== SCROLLBAR (optional premium touch) ===== */
::-webkit-scrollbar {
    width: 6px;
}
::-webkit-scrollbar-thumb {
    background: #38f9d7;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
with st.sidebar:

    # -------- TITLE --------
    st.markdown("<div class='sidebar-title'>📊 Churn Application</div>", unsafe_allow_html=True)

    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None,
        options=[
            "Churn Prediction",
            "Batch Prediction",
            "How Model Works",
            "About"
        ],
        icons=[
            "bar-chart",
            "cloud-upload",
            "question-circle",
            "info-circle"
        ],
        default_index=0,        
    )

    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # -------- BOTTOM BUTTON --------
    st.markdown('<div class="sidebar-bottom">', unsafe_allow_html=True)

    if st.button("👨‍💻 About Developer"):
        st.session_state.page = "about_dev"

    st.markdown('</div>', unsafe_allow_html=True)


# ------------------ ROUTING ------------------

# Priority: About Developer page
if st.session_state.page == "about_dev":
    from app_pages.about_developer import show_about_developer
    show_about_developer()

else:
    if selected == "Churn Prediction":
        from app_pages.churn_prediction import show_churn_prediction
        show_churn_prediction()

    elif selected == "Batch Prediction":
        from app_pages.batch_prediction import show_batch_prediction
        show_batch_prediction()

    elif selected == "How Model Works":
        from app_pages.model_workflow import show_model_workflow
        show_model_workflow()

    elif selected == "About":
        from app_pages.about import view_about
        view_about()

    
# ------------------ FOOTER ------------------
st.markdown("""
<hr style="border: 0.5px solid #444;">
<center style="color: gray;">Telecom Customer Churn Prediction • Built with Streamlit</center>
""", unsafe_allow_html=True)