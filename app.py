import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from template import template

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="youthventure.ai",
    page_icon=":rocket:",
    layout="wide",
)

# Set up Google Gemini AI model
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


def generate_response(query):
    prompt = template.format(query=query)

    # Format the chat history correctly
    formatted_history = []
    for message in st.session_state.chat_session.history:
        formatted_history.append(
            {"role": message["role"], "parts": [{"text": message["content"]}]}
        )

    # Add the new query to the formatted history
    formatted_history.append({"role": "user", "parts": [{"text": prompt}]})

    response = model.generate_content(formatted_history)
    return response.text


def main():
    # Set page styles for dark theme and fixed layout
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1E1E1E;
            color: #E0E0E0;
        }
        .chat-message {
            background-color: #2C2C2C;
            border: 1px solid #3D3D3D;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            margin-top: 30px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        .chat-message p {
            color: #E0E0E0 !important;
            font-size: 16px;
            line-height: 1.6;
        }
        .example-prompts {
            font-size: 14px;
            color: #B0B0B0;
            margin-bottom: 5px;
        }

        .example-prompts p {
            margin-bottom: 5px;
            margin-left: 15px;
            margin-right: 5px;
        }
        .stTextInput>div>div>input {
            color: #E0E0E0 !important;
            background-color: #2C2C2C;
            border: 1px solid #3D3D3D;
            border-radius: 5px;
            padding: 10px;
        }
        body {
            font-family: '__Space_Mono_12ac45', '__Space_Mono_Fallback_12ac45', 'Arial', sans-serif;
            color: #E0E0E0;
        }
        .stMarkdown {
            color: #E0E0E0;
        }
        .stButton>button {
            background-color: #4A4A4A;
            color: #E0E0E0;
            border: 1px solid #3D3D3D;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #5A5A5A;
        }
        .stHeader {
            color: #E0E0E0;
            font-size: 32px;
            font-weight: bold;
            text-align: center;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        }
        .chat-container {
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            
        }
        .input-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #1E1E1E;
            border-top: 1px solid #3D3D3D;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .fixed-header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background-color: #1E1E1E;
            z-index: 1000;
            padding-top: 50px;
            border-bottom: 1px solid #3D3D3D;
        }
        #input-wrapper {
            flex-grow: 1;
            margin-right: 10px;
        }
        .stButton>button {
            /*height: 100%;*/
            white-space: nowrap;
        }
        .css-zy9gvu {
            margin: 0;
            font-family: '__Space_Mono_12ac45', '__Space_Mono_Fallback_12ac45';
            font-weight: 400;
            font-size: 1rem;
            line-height: 1.75;
            margin-bottom: 0.35em;
            color: #D8D9DA;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Fixed header with title
    st.markdown(
        """
        <div class="fixed-header">
            <h1 class='stHeader'>AI VC: Connecting Founders and Investors</h1>
            <div class="example-prompts">
                <p>Example for Founder: "Hi, I'm Azwad. I'm building an AI VC platform and I'm looking for potential investors with experience in AI, fintech, or venture capital technologies?"</p>
                <p>Example for Investors: "Hi, I am Mahin and I am looking to invest in space exploration for $1000. Find me companies to invest in."</p>
            </div>
        </div>


        """,
        unsafe_allow_html=True,
    )

    # Add some padding to account for the fixed header
    # st.markdown("<div style='height: 140px;'></div>", unsafe_allow_html=True)

    # Chat container
    chat_container = st.container()

    # Display chat history in correct order
    with chat_container:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for message in st.session_state.chat_session.history:
            role = "assistant" if message["role"] == "model" else "user"
            with st.chat_message(role):
                st.markdown(
                    f"<div class='chat-message'><p>{message['content']}</p></div>",
                    unsafe_allow_html=True,
                )
        st.markdown("</div>", unsafe_allow_html=True)

    # Input field for user's message (fixed at the bottom)
    st.markdown(
        """
        <div class="input-container">
            <div id="input-wrapper" style="flex-grow: 1;"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    message = st.chat_input(
        "Enter your query about startups, investments, or founders...", key="chat_input"
    )

    if message:
        # Add user's message to chat and display it
        st.session_state.chat_session.history.append(
            {"role": "user", "content": message}
        )

        # Generate and display response
        response = generate_response(message)
        st.session_state.chat_session.history.append(
            {"role": "model", "content": response}
        )
        st.rerun()

    # JavaScript to move the input to the correct position
    st.markdown(
        """
        <script>
            function moveElements() {
                const inputWrapper = document.getElementById('input-wrapper');
                const chatInput = document.querySelector('.stChatInput');

                if (inputWrapper && chatInput) {
                    inputWrapper.appendChild(chatInput);
                }
            }

            // Run the function when the page loads and after a short delay
            document.addEventListener('DOMContentLoaded', moveElements);
            setTimeout(moveElements, 1000);
        </script>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
