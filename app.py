import streamlit as st
from streamlit_option_menu import option_menu
import pydeck as pdk
from modules import model_module
from modules import video_input_module
from modules import accident_report_module

# Enable wide mode for full-screen layout
st.set_page_config(layout="wide")

# Adding Button allowing to return to the Main site
home_url = "https://sites.google.com/berkeley.edu/ucberkely-caliber/mvp-demo"
if st.button("Return to Our Main Website"):
    st.write(f'<meta http-equiv="refresh" content="0; url={home_url}">', unsafe_allow_html=False)

# Initialize session state to track API key submission
if 'api_key_submitted' not in st.session_state:
    st.session_state['api_key_submitted'] = False
if 'api_keys' not in st.session_state:
    st.session_state['api_keys'] = {}


####################################################### Demon Playground Section
st.title("EmergEye Demo Playground")
# Custom CSS for borders
st.markdown("""
    <style>
    .module-container {
        border: 2px solid #f0f0f5;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        background-color: #fafafa;
    }
    .module-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Ensure session state is initialized for analysis and notification flag
if 'analysis_complete' not in st.session_state:
    st.session_state['analysis_complete'] = False

if 'notification_ready' not in st.session_state:
    st.session_state['notification_ready'] = False

# Create a container for the entire UI
with st.container(height=1010, border=True):
    
    # Create two columns: one for the left (video input and model) and one for the right (accident report)
    col_left, col_right = st.columns([2, 1])  # Adjust ratio as needed

    # Left Column: Video Input and Model Module
    with col_left:
        # Top section: Video Input Module
        with st.container(height=580, border=True):
            st.markdown('<div class="module-title">Live Stream Input</div>', unsafe_allow_html=True)            
            # Check if the API key has not been submitted yet
            if not st.session_state['api_key_submitted']:
                # Show the API key input and submit button
                nysdot_api_key = st.text_input("", type="password", placeholder="Submit NYSDoT API Key")
                if st.button("Submit API Keys"):
                    st.session_state['api_keys']['nysdot_api_key'] = nysdot_api_key
                    st.session_state['api_key_submitted'] = True  # Update session state
                    st.success("API Keys have been stored for this session.")            
            # Call the video input module
            video_input_module.display_video_input()
            st.markdown('</div>', unsafe_allow_html=True)


        # Bottom section: Model Module
        with st.container(height=380, border=True):
            # st.markdown('<div class="module-container">', unsafe_allow_html=True)
            st.markdown('<div class="module-title">Accident Detection (demo) </div>', unsafe_allow_html=True)
            model_module.display_model_analysis()  # Call the model analysis module
            st.markdown('</div>', unsafe_allow_html=True)

    # Right Column: Accident Report Module
    with col_right:
        with st.container(height=975, border=True):
            # st.markdown('<div class="module-container">', unsafe_allow_html=True)
            # st.markdown('<div class="module-title">Severe Accident Notification</div>', unsafe_allow_html=True)
            accident_report_module.display_accident_report()  # Call the accident report module
            st.markdown('</div>', unsafe_allow_html=True)
