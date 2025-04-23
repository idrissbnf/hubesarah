import streamlit as st
import base64
from PIL import Image
import io
import time
import random

# Set page configuration
st.set_page_config(
    page_title="Do You Miss Me?",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Custom CSS to style the app like the original with mobile optimizations
st.markdown("""
<style>
    .main {
        background: #FFFFFF !important;
        padding: 10px;
        border-radius: 20px;
    }
    /* More specific button styling with !important flags */
    .stButton > button {
        border-radius: 50px !important;
        padding: 12px 0 !important;
        width: 100% !important;
        font-size: 1.1rem !important;
        margin: 5px auto !important;
        display: block !important;
        border: none !important;
    }
    .yes-btn > button {
        background-color: #e83e8c !important;
        color: white !important;
    }
    .no-btn > button {
        background-color: #6c757d !important;
        color: white !important;
    }
    .game-btn > button {
        background-color: #4CAF50 !important;
        color: white !important;
    }
    .back-btn > button {
        background-color: #6c757d !important;
        color: white !important;
    }
    .whatsapp-btn > button {
        background-color: #25D366 !important;
        color: white !important;
    }
    .camera-btn > button {
        background-color: #e83e8c !important;
        color: white !important;
    }
    /* Rest of your styles */
    .heart {
        font-size: 2.5rem;
        text-align: center;
        margin: 10px 0;
        animation: pulse 1.5s infinite;
    }
    .container {
        background-color: white !important;
        border-radius: 20px;
        padding: 20px 10px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        max-width: 100%;
        margin: 0 auto;
        text-align: center;
    }
    .question {
        font-size: 1.5rem;
        margin: 20px 0;
        color: #333 !important;
        text-align: center;
    }
    .game-card {
        background-color: #f8f9fa !important;
        border-radius: 15px;
        padding: 15px;
        margin: 15px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        color: #333 !important;
    }
    .game-title {
        color: #e83e8c !important;
        font-size: 1.4rem;
        margin-bottom: 10px;
        text-align: center;
    }
    .game-description {
        font-size: 1rem;
        margin-bottom: 15px;
        color: #495057 !important;
        text-align: center;
    }
    .game-question {
        font-size: 1.1rem;
        font-weight: bold;
        margin: 10px 0;
        color: #212529 !important;
        text-align: center;
    }
    .result-text {
        font-size: 1.3rem;
        text-align: center;
        margin: 10px 0;
        color: #212529 !important;
    }
    h1 {
        color: #e83e8c !important;
        text-align: center;
        font-size: 1.8rem;
    }
    img {
        max-width: 100%;
        height: auto;
        border-radius: 10px;
    }
    .whatsapp-link {
        display: inline-block;
        background-color: #25D366 !important;
        color: white !important;
        text-decoration: none;
        padding: 10px 20px;
        border-radius: 50px;
        margin: 10px auto;
        font-weight: bold;
    }
    .stTextArea textarea {
        border-radius: 15px;
        padding: 10px;
        color: #333 !important;
        background-color: #fff !important;
    }
    /* Override dark mode settings */
    [data-testid="stForm"] {
        background-color: #FFFFFF !important;
    }
    [data-testid="stVerticalBlock"] {
        background-color: #FFFFFF !important;
    }
    [data-testid="stHorizontalBlock"] {
        background-color: #FFFFFF !important;
    }
    [data-testid="element-container"] {
        background-color: #FFFFFF !important;
    }
    /* Ensure light mode is always used */
    body {
        background-color: #FFFFFF !important;
        color: #333333 !important;
    }
    .stApp {
        background-color: #FFFFFF !important;
    }
    /* Hide fullscreen button on mobile */
    @media (max-width: 768px) {
        button[title="View fullscreen"] {
            display: none;
        }
        .stButton > button {
            font-size: 1rem !important;
            padding: 10px 0 !important;
        }
    }
    /* Override any dark mode settings */
    [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF !important;
        color: #333333 !important;
    }
    [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    /* Force light text for dark backgrounds */
    button {
        color: white !important;
    }
    /* Improved dark mode override for text area */
    textarea {
        color: #333 !important;
        background-color: #fff !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if 'page' not in st.session_state:
    st.session_state.page = 'main'
    
if 'no_button_clicked' not in st.session_state:
    st.session_state.no_button_clicked = False
    
if 'wyr_current_question' not in st.session_state:
    st.session_state.wyr_current_question = 0
    
if 'quiz_current_question' not in st.session_state:
    st.session_state.quiz_current_question = 0
    
if 'wyr_result' not in st.session_state:
    st.session_state.wyr_result = None
    
if 'quiz_result' not in st.session_state:
    st.session_state.quiz_result = None
    
if 'camera_active' not in st.session_state:
    st.session_state.camera_active = False
    
if 'captured_image' not in st.session_state:
    st.session_state.captured_image = None

# Would You Rather Questions
would_you_rather_questions = [
    {
        "question": "Chnawoha nickname li kt tgoliya o ky3jbni bzzf?",
        "option1": "katkoti",
        "option2": "wldi",
        "response1": "Maknhemloch but for u katkotek ❤️",
        "response2": "mommyyyyyyyyyyyyy ❤️"
    },
    {
        "question": "chnahowa ahsn mra khrjna ?",
        "option1": "awl mra",
        "option2": "tani mra",
        "response1": " i think f chi hwayj but not the best",
        "response2": "i know it babe mn dak nhar o hnaa 9rab ❤️"
    },
    {
        "question": "Would you rather tfarji meaya fl barca o ntmchaw? ",
        "option1": "barcaaaa",
        "option2": "ntmchaww",
        "response1": "hhhhh zbi la mchiti meaya l9hwa",
        "response2": "haja bayna fen ma tkon chi dalma nbossek"
    }
]

# Love Quiz Questions
love_quiz_questions = [
    {
        "question": "What's my favorite color?",
        "options": ["Blue", "Red", "Purple", "Black"],
        "correctIndex": 3,
        "response": "You know me so well! Black is my favorite! 🖤"
    },
    {
        "question": "What's my idea of a perfect date?",
        "options": ["Beach picnic", "Movie night", "Hiking adventure", "Dancing"],
        "correctIndex": 2,
        "response": "Yes! A Hiking adventure with you is perfect! 🌄❤️"
    },
    {
        "question": "What makes me smile the most?",
        "options": ["Surprise gifts", "Your jokes", "Your smile", "Your messages"],
        "correctIndex": 2,
        "response": "Your smile always make my day brighter! 📱❤️"
    }
]

# Function for the "No" button behavior
def dodge_no_button():
    st.session_state.no_button_clicked = True
    time.sleep(1)  # Reduced to 1 second for better mobile experience
    st.session_state.page = 'result_yes'  # Automatically go to "Yes" result
    st.rerun()

# Function to handle Would You Rather game
def handle_wyr_option(option_num):
    current_q = st.session_state.wyr_current_question
    if option_num == 1:
        st.session_state.wyr_result = would_you_rather_questions[current_q]["response1"]
    else:
        st.session_state.wyr_result = would_you_rather_questions[current_q]["response2"]

# Function to handle next Would You Rather question
def next_wyr_question():
    st.session_state.wyr_current_question += 1
    st.session_state.wyr_result = None
    if st.session_state.wyr_current_question >= len(would_you_rather_questions):
        st.session_state.wyr_current_question = 0
        st.session_state.page = 'quiz_game'
    st.rerun()

# Function to handle Quiz options
def handle_quiz_option(option_index):
    current_q = st.session_state.quiz_current_question
    correct_index = love_quiz_questions[current_q]["correctIndex"]
    
    if option_index == correct_index:
        st.session_state.quiz_result = love_quiz_questions[current_q]["response"]
    else:
        st.session_state.quiz_result = "Try again! But I still love you! ❤️"

# Function to handle next Quiz question
def next_quiz_question():
    st.session_state.quiz_current_question += 1
    st.session_state.quiz_result = None
    if st.session_state.quiz_current_question >= len(love_quiz_questions):
        st.session_state.quiz_current_question = 0
        st.session_state.page = 'memory_game'
    st.rerun()

# Function to create WhatsApp link (direct method)
def create_whatsapp_link(message):
    # Replace with the actual phone number
    phone_number = "212621446429"  # Removed the '+' as it's automatically encoded
    encoded_message = message.replace(" ", "%20")
    return f"https://wa.me/{phone_number}?text={encoded_message}"

# Main App Logic
with st.container():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    
    # Main Page
    if st.session_state.page == 'main':
        st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)
        st.markdown('<h1>Hey hube Saraaah!</h1>', unsafe_allow_html=True)
        st.markdown('<div class="question">Do you miss me?</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="yes-btn">', unsafe_allow_html=True)
            if st.button("Yes"):
                st.session_state.page = 'result_yes'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="no-btn">', unsafe_allow_html=True)
            if st.button("No"):
                st.session_state.page = 'result_no'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
    
    # "Yes" Result Page
    elif st.session_state.page == 'result_yes':
        st.markdown('<div style="font-size: 1.6rem; margin-bottom: 10px;">I miss you too! ❤️</div>', unsafe_allow_html=True)
        
        # Display an embedded placeholder image instead of URL (more reliable)
        
        st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
        st.image("C:/Users/surface/Desktop/againhubesarah/image/WhatsApp Image 2025-04-22 at 15.51.00_0485fd70.jpg", caption="", width=250)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)
        st.markdown('<div>Can\'t wait to see you again!</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="game-btn">', unsafe_allow_html=True)
        if st.button("Let's Play a Game 🎮"):
            st.session_state.page = 'wyr_game'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    # "No" Result Page
    elif st.session_state.page == 'result_no':
        st.markdown('<div class="result-text">Really? Are you sure about that? 🥺</div>', unsafe_allow_html=True)
        
        # After 1 second, automatically go to "Yes" result
        if not st.session_state.no_button_clicked:
            dodge_no_button()
    
    # Would You Rather Game
    elif st.session_state.page == 'wyr_game':
        st.markdown('<h1>Love Games</h1>', unsafe_allow_html=True)
        st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)
        
        # Game card
        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.markdown('<div class="game-title">choose one babee</div>', unsafe_allow_html=True)
        st.markdown('<div class="game-description">Choose between two options. Let\'s see how well we know each other!</div>', unsafe_allow_html=True)
        
        current_q = st.session_state.wyr_current_question
        st.markdown(f'<div class="game-question">{would_you_rather_questions[current_q]["question"]}</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button(would_you_rather_questions[current_q]["option1"]):
                handle_wyr_option(1)
        with col2:
            if st.button(would_you_rather_questions[current_q]["option2"]):
                handle_wyr_option(2)
        
        # Show result if available
        if st.session_state.wyr_result:
            st.markdown(f'<div class="result-text">{st.session_state.wyr_result}</div>', unsafe_allow_html=True)
            st.markdown('<div class="game-btn">', unsafe_allow_html=True)
            if st.button("Next Question", key="wyr_next"):
                next_wyr_question()
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Back button
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("Back to Photo", key="wyr_back"):
            st.session_state.page = 'result_yes'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Quiz Game
    elif st.session_state.page == 'quiz_game':
        st.markdown('<h1>Love Games</h1>', unsafe_allow_html=True)
        st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)
        
        # Game card
        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.markdown('<div class="game-title">Love Quiz</div>', unsafe_allow_html=True)
        st.markdown('<div class="game-description">Test how well you know me!</div>', unsafe_allow_html=True)
        
        current_q = st.session_state.quiz_current_question
        st.markdown(f'<div class="game-question">{love_quiz_questions[current_q]["question"]}</div>', unsafe_allow_html=True)
        
        # Show options with better mobile styling
        for i, option in enumerate(love_quiz_questions[current_q]["options"]):
            if st.button(option, key=f"quiz_option_{i}"):
                handle_quiz_option(i)
        
        # Show result if available
        if st.session_state.quiz_result:
            st.markdown(f'<div class="result-text">{st.session_state.quiz_result}</div>', unsafe_allow_html=True)
            st.markdown('<div class="game-btn">', unsafe_allow_html=True)
            if st.button("Next Question", key="quiz_next"):
                next_quiz_question()
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Back button
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("Back to Photo", key="quiz_back"):
            st.session_state.page = 'result_yes'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Memory Game
    elif st.session_state.page == 'memory_game':
        st.markdown('<h1>Love Games</h1>', unsafe_allow_html=True)
        st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)
        
        # Game card
        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.markdown('<div class="game-title">Sweet Message</div>', unsafe_allow_html=True)
        st.markdown('<div class="game-description">Share a sweet memory or message</div>', unsafe_allow_html=True)
        st.markdown('<div class="game-question">What\'s a special moment you remember about us?</div>', unsafe_allow_html=True)
        
        memory_message = st.text_area("Write your sweet memory or message here...", height=120)
        
        # WhatsApp button - improved with direct link
        if memory_message.strip():
            message = f"Sweet message from Sarah: {memory_message}"
            whatsapp_link = create_whatsapp_link(message)
            
            st.markdown(f'<a href="{whatsapp_link}" class="whatsapp-link" target="_blank">Send to WhatsApp 💬</a>', unsafe_allow_html=True)
            
            # Add a button to move to the next page
            st.markdown('<div class="game-btn">', unsafe_allow_html=True)
            if st.button("Continue to Kiss Photo 📸", key="after_message"):
                st.session_state.page = 'kiss_game'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="whatsapp-btn">', unsafe_allow_html=True)
            if st.button("Preview Message", key="preview_msg"):
                st.warning("Please write a message before sending! ❤️")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Back button
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("Back to Photo", key="memory_back"):
            st.session_state.page = 'result_yes'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Kiss Picture Game - Simplified camera approach
    elif st.session_state.page == 'kiss_game':
        st.markdown('<h1>Love Games</h1>', unsafe_allow_html=True)
        st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)
        
        # Game card
        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.markdown('<div class="game-title">Send a Kiss Picture</div>', unsafe_allow_html=True)
        st.markdown('<div class="game-description">Take a kiss picture and send it to me babee ❤️</div>', unsafe_allow_html=True)
        
        if not st.session_state.camera_active and not st.session_state.captured_image:
            st.markdown('<div class="camera-btn">', unsafe_allow_html=True)
            if st.button("Take Selfie", key="take_selfie"):
                st.session_state.camera_active = True
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            
        elif st.session_state.camera_active:
            # Create a simple HTML/JS camera component without form
            camera_html = """
            <div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
                <video id="video" width="100%" style="border-radius: 10px;" autoplay playsinline></video>
                <button id="captureBtn" style="background-color: #e83e8c; color: white; border: none; border-radius: 50px; padding: 10px 20px; margin-top: 10px; cursor: pointer; font-size: 1rem;">
                    Capture Kiss Photo 💋
                </button>
                <canvas id="canvas" style="display: none;"></canvas>
                <img id="photo" style="display: none; width: 100%; margin-top: 10px; border-radius: 10px;">
                <p id="status" style="margin-top: 10px; color: #e83e8c;"></p>
            </div>
            
            <script>
                // Access the camera
                const video = document.getElementById('video');
                const canvas = document.getElementById('canvas');
                const photo = document.getElementById('photo');
                const captureBtn = document.getElementById('captureBtn');
                const statusText = document.getElementById('status');
                const constraints = { 
                    video: { 
                        facingMode: "user",
                        width: { ideal: 1280 },
                        height: { ideal: 720 }
                    } 
                };
                
                // Get access to the camera
                async function startCamera() {
                    try {
                        const stream = await navigator.mediaDevices.getUserMedia(constraints);
                        video.srcObject = stream;
                        statusText.textContent = "Camera ready!";
                    } catch (err) {
                        console.error("Error accessing camera: ", err);
                        statusText.textContent = "Could not access camera. Please make sure you've given permission.";
                    }
                }
                
                // Capture photo from camera
                captureBtn.addEventListener('click', function() {
                    // Draw the current video frame to the canvas
                    canvas.width = video.videoWidth;
                    canvas.height = video.videoHeight;
                    canvas.getContext('2d').drawImage(video, 0, 0);
                    
                    // Show the captured photo
                    photo.src = canvas.toDataURL('image/jpeg');
                    photo.style.display = 'block';
                    video.style.display = 'none';
                    captureBtn.textContent = 'Retake Photo';
                    captureBtn.onclick = retakePhoto;
                    
                    // Add download and share buttons
                    const actionsDiv = document.createElement('div');
                    actionsDiv.style.display = 'flex';
                    actionsDiv.style.justifyContent = 'space-between';
                    actionsDiv.style.marginTop = '10px';
                    
                    // Create download button
                    const downloadBtn = document.createElement('a');
                    downloadBtn.href = canvas.toDataURL('image/jpeg');
                    downloadBtn.download = 'kiss_photo.jpg';
                    downloadBtn.textContent = 'Download Photo';
                    downloadBtn.style.backgroundColor = '#6c757d';
                    downloadBtn.style.color = 'white';
                    downloadBtn.style.textDecoration = 'none';
                    downloadBtn.style.padding = '10px 20px';
                    downloadBtn.style.borderRadius = '50px';
                    downloadBtn.style.marginRight = '10px';
                    actionsDiv.appendChild(downloadBtn);
                    
                    // Create WhatsApp share button
                    const whatsappBtn = document.createElement('a');
                    const phoneNumber = "212621446429"; // Your WhatsApp number
                    whatsappBtn.href = `https://wa.me/${phoneNumber}?text=Sending%20you%20a%20kiss!%20%F0%9F%92%8B%E2%9D%A4%EF%B8%8F`;
                    whatsappBtn.target = "_blank";
                    whatsappBtn.textContent = 'Send to WhatsApp';
                    whatsappBtn.style.backgroundColor = '#25D366';
                    whatsappBtn.style.color = 'white';
                    whatsappBtn.style.textDecoration = 'none';
                    whatsappBtn.style.padding = '10px 20px';
                    whatsappBtn.style.borderRadius = '50px';
                    actionsDiv.appendChild(whatsappBtn);
                    
                    document.querySelector('div').appendChild(actionsDiv);
                    
                    // Add instruction text
                    const instructionText = document.createElement('p');
                    instructionText.textContent = "First download the photo, then open WhatsApp to share it";
                    instructionText.style.fontSize = '0.9rem';
                    instructionText.style.textAlign = 'center';
                    instructionText.style.marginTop = '10px';
                    instructionText.style.color = '#666';
                    document.querySelector('div').appendChild(instructionText);
                    
                    statusText.textContent = "Photo captured! Download and share it via WhatsApp.";
                    
                    // Stop the camera stream
                    const stream = video.srcObject;
                    const tracks = stream.getTracks();
                    tracks.forEach(track => track.stop());
                });
                
                function retakePhoto() {
                    // Hide photo and show video again
                    photo.style.display = 'none';
                    video.style.display = 'block';
                    
                    // Remove the action buttons
                    const actionsDiv = document.querySelector('div > div:last-child');
                    if (actionsDiv) actionsDiv.remove();
                    
                    // Remove instruction text
                    const instructionText = document.querySelector('div > p:last-child');
                    if (instructionText) instructionText.remove();
                    
                    // Reset capture button
                    captureBtn.textContent = 'Capture Kiss Photo 💋';
                    captureBtn.onclick = null;
                    
                    // Restart camera
                    startCamera();
                }
                
                // Start camera when component loads
                startCamera();
            </script>
            """
            
            # Display the camera component
            st.components.v1.html(camera_html, height=550)
            
            # Button to cancel camera
            st.markdown('<div class="back-btn">', unsafe_allow_html=True)
            if st.button("Cancel Camera", key="cancel_camera"):
                st.session_state.camera_active = False
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Back button
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("Back to Photo", key="kiss_back"):
            st.session_state.page = 'result_yes'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# Force light mode
st.markdown("""
<script>
    // Force light mode
    document.body.classList.remove('dark');
    document.body.classList.add('light');
    
    // Store preference in local storage
    localStorage.setItem('theme', 'light');
</script>
""", unsafe_allow_html=True)
