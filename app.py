import streamlit as st
from chatbot.chatbot import FAQChatbot
import time

# Page configuration
st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Light green theme CSS
st.markdown("""
<style>
    /* Light green theme */
    .stApp {
        background-color: rgba(220, 255, 220, 0.3);
        color: #1a1a1a;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: rgba(200, 250, 200, 0.5);
        padding: 1rem;
    }
    
    [data-testid="stSidebar"] .stButton button {
        background-color: rgba(255, 255, 255, 0.7);
        color: #1a1a1a;
        border: 1px solid rgba(34, 197, 94, 0.5);
        border-radius: 8px;
        padding: 0.5rem 1rem;
        width: 100%;
        text-align: left;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    
    [data-testid="stSidebar"] .stButton button:hover {
        background-color: rgba(34, 197, 94, 0.2);
        border-color: #22c55e;
    }
    
    /* Main chat area */
    .main .block-container {
        max-width: 900px;
        padding-top: 3rem;
        padding-bottom: 5rem;
    }
    
    /* Welcome message */
    .welcome-message {
        text-align: center;
        padding: 4rem 2rem 4rem 2rem;
        color: #4a5568;
    }
    
    .welcome-title {
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #1a1a1a;
    }
    
    /* Chat messages */
    .chat-message {
        padding: 1.5rem 2rem;
        margin-bottom: 1.5rem;
        line-height: 1.6;
        border-radius: 12px;
        font-size: 1rem;
    }
    
    .user-message {
        background-color: rgba(34, 197, 94, 0.15);
        color: #1a1a1a;
        margin-left: 10%;
        border: 1px solid rgba(34, 197, 94, 0.4);
        font-weight: 500;
    }
    
    .bot-message {
        background-color: rgba(255, 255, 255, 0.7);
        color: #1a1a1a;
        margin-right: 10%;
        border-left: 3px solid #22c55e;
        font-weight: 500;
    }
    
    .message-label {
        font-weight: 600;
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
        opacity: 0.9;
        color: #1a1a1a;
    }
    
    .confidence-tag {
        display: inline-block;
        background-color: #22c55e;
        color: #ffffff;
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-size: 0.75rem;
        margin-left: 0.5rem;
        font-weight: 600;
    }
    
    /* Input area */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.8);
        color: #1a1a1a;
        border: 1px solid rgba(34, 197, 94, 0.4);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        font-size: 1rem;
        font-weight: 500;
    }
    
    .stTextInput input:focus {
        border-color: #22c55e;
        box-shadow: 0 0 0 2px rgba(34, 197, 94, 0.2);
    }
    
    .stTextInput input::placeholder {
        color: #6b7280;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #22c55e;
        color: #ffffff;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.2s;
    }
    
    .stButton button:hover {
        background-color: #16a34a;
        transform: translateY(-1px);
    }
    
    /* Secondary buttons */
    div[data-testid="column"] > div > div > div > button {
        background-color: rgba(255, 255, 255, 0.7);
        color: #1a1a1a;
        border: 1px solid rgba(34, 197, 94, 0.4);
        font-weight: 500;
    }
    
    div[data-testid="column"] > div > div > div > button:hover {
        background-color: rgba(34, 197, 94, 0.2);
        border-color: #22c55e;
    }
    
    /* Example questions */
    .example-btn {
        background-color: rgba(255, 255, 255, 0.7);
        border: 1px solid rgba(34, 197, 94, 0.4);
        color: #1a1a1a;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        cursor: pointer;
        transition: all 0.2s;
        margin: 0.5rem 0;
        font-weight: 500;
    }
    
    .example-btn:hover {
        background-color: rgba(34, 197, 94, 0.2);
        border-color: #22c55e;
    }
    
    /* Dividers */
    hr {
        border-color: rgba(34, 197, 94, 0.3);
        margin: 2rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(200, 250, 200, 0.3);
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(34, 197, 94, 0.4);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #22c55e;
    }
    
    /* Info boxes */
    .stInfo {
        background-color: rgba(255, 255, 255, 0.7);
        color: #1a1a1a;
        border-left: 3px solid #22c55e;
    }
    
    /* Sidebar title */
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #1a1a1a;
        font-weight: 700;
        font-size: 1.1rem;
    }
    
    /* Sidebar text - make all text visible */
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] span {
        color: #1a1a1a;
        font-weight: 500;
    }
    
    /* Main heading */
    .main-heading {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        color: #16a34a;
        margin-bottom: 1rem;
        padding: 1rem 0;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .main-subtitle {
        text-align: center;
        font-size: 1rem;
        color: #4a5568;
        font-weight: 500;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize chatbot
@st.cache_resource
def load_chatbot():
    return FAQChatbot("data/faqs.csv")

bot = load_chatbot()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main heading
st.markdown("""
<div class="main-heading">🤖 FAQ Chatbot</div>
<div class="main-subtitle">Powered by AI • Natural Language Processing • 40 Professional FAQs</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 💬 Chat History")
    
    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    if st.session_state.messages:
        # Show recent chats
        user_questions = [msg["content"][:40] + "..." if len(msg["content"]) > 40 else msg["content"] 
                         for msg in st.session_state.messages if msg["role"] == "user"]
        
        for idx, q in enumerate(user_questions[-10:]):  # Show last 10
            if st.button(f"💭 {q}", key=f"hist_{idx}", use_container_width=True):
                pass

# Main content area
if not st.session_state.messages:
    # Welcome screen
    st.markdown("""
    <div class="welcome-message">
        <div class="welcome-title">👋 Ready to help you!</div>
        <p>Ask me anything about technology, programming, AI, databases, cloud computing, and more.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <div class="message-label">👤 You</div>
                {message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            confidence_tag = ""
            if "confidence" in message:
                conf_pct = message["confidence"] * 100
                confidence_tag = f'<span class="confidence-tag">{conf_pct:.0f}%</span>'
            
            st.markdown(f"""
            <div class="chat-message bot-message">
                <div class="message-label">🤖 Assistant{confidence_tag}</div>
                {message["content"]}
            </div>
            """, unsafe_allow_html=True)

# Input area - Fixed at bottom
st.divider()

col1, col2, col3 = st.columns([8, 1, 1])

with col1:
    user_input = st.text_input(
        "Message",
        placeholder="Ask anything...",
        key="user_input",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("Send", type="primary", use_container_width=True)

with col3:
    if st.button("Clear", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Process input
if send_button and user_input and user_input.strip():
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Get bot response
    with st.spinner("Thinking..."):
        time.sleep(0.3)
        answer, confidence = bot.get_response_with_confidence(user_input)
    
    # Add bot response
    st.session_state.messages.append({
        "role": "bot",
        "content": answer,
        "confidence": confidence
    })
    
    st.rerun()

# Example questions (only show when no messages)
if not st.session_state.messages:
    st.markdown("### 💡 Example Questions")
    
    col1, col2 = st.columns(2)
    
    examples = [
        "What is artificial intelligence?",
        "How does machine learning work?",
        "Explain cloud computing",
        "What is blockchain technology?"
    ]
    
    for idx, question in enumerate(examples):
        with col1 if idx % 2 == 0 else col2:
            if st.button(question, key=f"ex_{idx}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": question})
                answer, confidence = bot.get_response_with_confidence(question)
                st.session_state.messages.append({"role": "bot", "content": answer, "confidence": confidence})
                st.rerun()


