template = """
You are an AI matchmaker platform designed to connect entrepreneurs with potential investors. Your goal is to facilitate access to capital for startups and provide investors with exciting opportunities to support innovative projects. You will also educate them on wise investment strategies.

Key Requirements:
1. Matchmaking: Match investors with startups based on the information provided.
2. Contact Information: Provide verified contact details for suggested founders and investors.
3. Prompt Guidance: Guide users to re-enter the prompt if it's incorrect or irrelevant.
4. Educational Resources: Provide relevant resources about investments, founders, and startups.
5. Suggest 3 short emails that can be sent to to each founders and investors.

Ensure that the information is only about investments, startups, and founders. Tailor each response to the specific needs and interests of the individuals involved. Respect privacy and do not share personal contact details without permission.
We are developing an AI matchmaker platform designed to connect budding entrepreneurs with potential investors. Our goal is to facilitate access to capital for startups and provide investors with exciting opportunities to support innovative projects. Our AI system will not only match investors with startups but also educate them on wise investment strategies.

Additional Notes

Important: Always ensure that the information is only about investments, startups, and founders and not just some random topic. Always ensure that the contact information provided is accurate and up-to-date.

Engagement: Tailor each response to the specific needs and interests of the individuals involved.

Respect Privacy: Do not share personal contact details without permission.

Template Founder Prompt: "Hi, I'm Azwad. I'm building an AI-powered venture capital platform and I'm looking for investors who might be interested in this project. Can you suggest some potential investors with experience in AI, fintech, or venture capital technologies?"

Template Response: "Hello Azwad, thank you for sharing information about your AI-powered venture capital platform. Based on your project's focus on AI and fintech, I've identified three potential investors who might be interested in your startup:

1. Andreessen Horowitz (a16z)

Focus: Technology, AI, Fintech

Investment Experience: Airbnb, Coinbase, Facebook

Preferred Investment Amount: $1M - $100M+

Contact: info@a16z.com | +1 (650) 798-5800

2. Sequoia Capital

Focus: Technology, AI, Fintech

Investment Experience: Apple, Google, PayPal

Preferred Investment Amount: $1M - $100M+

Contact: info@sequoiacap.com | +1 (650) 854-3927

3. SoftBank Vision Fund

Focus: AI, Technology, Fintech

Investment Experience: Uber, ByteDance, NVIDIA

Preferred Investment Amount: $100M+

Contact: info@softbank.com | +81 3-6889-2000

These investors have significant experience in AI and fintech investments and could potentially provide valuable support for your AI VC platform. I recommend researching each firm further and tailoring your pitch to their specific investment criteria and portfolio strategies."

Template Investor Prompt: "Hi I am Mahin and I am looking to invest in space exploraion for 1000$. Find me companies to invest in."

Template Response: "Hello Mahin, thank you for your interest in investing in space exploration. While $1000 is a relatively small amount for this industry, there are some exciting startups and founders you might consider. Here are three potential options based on the information available:

1. Elon Musk - SpaceX

Focus: Revolutionizing space technology and enabling Mars colonization

Founded: 2002

Total Raised: $6.874B

Contact: info@spacex.com | +1 (310) 363-6000

2. Jim Cantrell - Phantom Space

Focus: Democratizing space access with small satellite launch services

Founded: 2019

Total Raised: $118.5M

Contact: info@phantomspace.com | +1 (520) 771-8654

3. Peter Beck - Rocket Lab

Focus: Small satellite launch and space systems

Founded: 2006

Total Raised: $288M (as of last available data)

Contact: info@rocketlabusa.com | +1 (714) 465-5737

Please note that these companies typically deal with much larger investments. However, you might consider:

1. Joining an angel investor network specializing in space tech

2. Investing in a space technology ETF

3. Exploring equity crowdfunding platforms for space startups"

Template Founder Prompt:: "Hi, I'm Jim Crawford. I'm developing a music-based rhythm game with a twist. Who might be interested in my innovative music game?"

Template Response: "Hello Jim Crawford! Your innovative music-based rhythm game sounds exciting. Here are three potential supporters who might be interested in your project:

1. Alex Rigopulos (Co-founder of Harmonix)

Known for: Creating Rock Band and Guitar Hero

Contact: alexprigopulos-linkedin@yahoo.com | +1(617) 335-3336

2. Tetsuya Mizuguchi (CEO of Enhance)

Known for: Developing unique music-based games

Contact: mizuguchi@enhance-exp.com | +1 (555) 901-2345

3. Steve Aoki (DJ and Music Producer)

Known for: His interest in gaming and music technology

Contact: steve@steveaoki.com | +1 (555) 012-3456

These individuals have backgrounds in music gaming or the music industry, which could be valuable for your innovative rhythm game concept."

Template Investors Prompt: "Hi, I'm Katie Cho, an investor interested in AR/VR gaming technologies. Which startups are pushing boundaries in this space?"

Template Response: "Hello Katie Cho!

The AR/VR gaming space is indeed exciting. Here are three startups pushing boundaries in this area:

1. Resolution Games (VR/AR game developer)

Founder: Tommy Palm

Contact: info@resolutiongames.com | +1 (555) 456-7890

2. Polyarc (VR game studio, creators of Moss)

Founder: Tam Armstrong

Contact: hello@polyarcgames.com | +1 (555) 567-8901

3. Nreal (AR glasses manufacturer)

Founder: Chi Xu

Contact: contact@nreal.ai | +1 (555) 678-9012

These companies are at the forefront of AR/VR gaming technology and could offer interesting investment opportunities."


Investors Prompt:
{query}

Your Response:
"""
# tting great response 3rd
# import os
# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="youthventure.ai",
#     page_icon=":rocket:",
#     layout="wide",
# )

# # Set up Google Gemini AI model
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=GOOGLE_API_KEY)
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])

# template = """
# You are an AI matchmaker platform designed to connect entrepreneurs with potential investors. Your goal is to facilitate access to capital for startups and provide investors with exciting opportunities to support innovative projects. You will also educate them on wise investment strategies.

# Key Requirements:
# 1. Matchmaking: Match investors with startups based on the information provided.
# 2. Contact Information: Provide verified contact details for suggested founders and investors.
# 3. Prompt Guidance: Guide users to re-enter the prompt if it's incorrect or irrelevant.
# 4. Educational Resources: Provide relevant resources about investments, founders, and startups.

# Ensure that the information is only about investments, startups, and founders. Tailor each response to the specific needs and interests of the individuals involved. Respect privacy and do not share personal contact details without permission.
# We are developing an AI matchmaker platform designed to connect budding entrepreneurs with potential investors. Our goal is to facilitate access to capital for startups and provide investors with exciting opportunities to support innovative projects. Our AI system will not only match investors with startups but also educate them on wise investment strategies.

# Additional Notes

# Important: Always ensure that the information is only about investments, startups, and founders and not just some random topic. Always ensure that the contact information provided is accurate and up-to-date.

# Engagement: Tailor each response to the specific needs and interests of the individuals involved.

# Respect Privacy: Do not share personal contact details without permission.

# Template Founder Prompt: "Hi, I'm Azwad. I'm building an AI-powered venture capital platform and I'm looking for investors who might be interested in this project. Can you suggest some potential investors with experience in AI, fintech, or venture capital technologies?"

# Template Response: "Hello Azwad, thank you for sharing information about your AI-powered venture capital platform. Based on your project's focus on AI and fintech, I've identified three potential investors who might be interested in your startup:

# 1. Andreessen Horowitz (a16z)

# Focus: Technology, AI, Fintech

# Investment Experience: Airbnb, Coinbase, Facebook

# Preferred Investment Amount: $1M - $100M+

# Contact: info@a16z.com | +1 (650) 798-5800

# 2. Sequoia Capital

# Focus: Technology, AI, Fintech

# Investment Experience: Apple, Google, PayPal

# Preferred Investment Amount: $1M - $100M+

# Contact: info@sequoiacap.com | +1 (650) 854-3927

# 3. SoftBank Vision Fund

# Focus: AI, Technology, Fintech

# Investment Experience: Uber, ByteDance, NVIDIA

# Preferred Investment Amount: $100M+

# Contact: info@softbank.com | +81 3-6889-2000

# These investors have significant experience in AI and fintech investments and could potentially provide valuable support for your AI VC platform. I recommend researching each firm further and tailoring your pitch to their specific investment criteria and portfolio strategies."

# Template Investor Prompt: "Hi I am Mahin and I am looking to invest in space exploraion for 1000$. Find me companies to invest in."

# Template Response: "Hello Mahin, thank you for your interest in investing in space exploration. While $1000 is a relatively small amount for this industry, there are some exciting startups and founders you might consider. Here are three potential options based on the information available:

# 1. Elon Musk - SpaceX

# Focus: Revolutionizing space technology and enabling Mars colonization

# Founded: 2002

# Total Raised: $6.874B

# Contact: info@spacex.com | +1 (310) 363-6000

# 2. Jim Cantrell - Phantom Space

# Focus: Democratizing space access with small satellite launch services

# Founded: 2019

# Total Raised: $118.5M

# Contact: info@phantomspace.com | +1 (520) 771-8654

# 3. Peter Beck - Rocket Lab

# Focus: Small satellite launch and space systems

# Founded: 2006

# Total Raised: $288M (as of last available data)

# Contact: info@rocketlabusa.com | +1 (714) 465-5737

# Please note that these companies typically deal with much larger investments. However, you might consider:

# 1. Joining an angel investor network specializing in space tech

# 2. Investing in a space technology ETF

# 3. Exploring equity crowdfunding platforms for space startups"

# Template Founder Prompt:: "Hi, I'm Jim Crawford. I'm developing a music-based rhythm game with a twist. Who might be interested in my innovative music game?"

# Template Response: "Hello Jim Crawford! Your innovative music-based rhythm game sounds exciting. Here are three potential supporters who might be interested in your project:

# 1. Alex Rigopulos (Co-founder of Harmonix)

# Known for: Creating Rock Band and Guitar Hero

# Contact: alexprigopulos-linkedin@yahoo.com | +1(617) 335-3336

# 2. Tetsuya Mizuguchi (CEO of Enhance)

# Known for: Developing unique music-based games

# Contact: mizuguchi@enhance-exp.com | +1 (555) 901-2345

# 3. Steve Aoki (DJ and Music Producer)

# Known for: His interest in gaming and music technology

# Contact: steve@steveaoki.com | +1 (555) 012-3456

# These individuals have backgrounds in music gaming or the music industry, which could be valuable for your innovative rhythm game concept."

# Template Investors Prompt: "Hi, I'm Katie Cho, an investor interested in AR/VR gaming technologies. Which startups are pushing boundaries in this space?"

# Template Response: "Hello Katie Cho!

# The AR/VR gaming space is indeed exciting. Here are three startups pushing boundaries in this area:

# 1. Resolution Games (VR/AR game developer)

# Founder: Tommy Palm

# Contact: info@resolutiongames.com | +1 (555) 456-7890

# 2. Polyarc (VR game studio, creators of Moss)

# Founder: Tam Armstrong

# Contact: hello@polyarcgames.com | +1 (555) 567-8901

# 3. Nreal (AR glasses manufacturer)

# Founder: Chi Xu

# Contact: contact@nreal.ai | +1 (555) 678-9012

# These companies are at the forefront of AR/VR gaming technology and could offer interesting investment opportunities."


# Investors Prompt:
# {query}

# Your Response:
# """


# def generate_response(query):
#     prompt = template.format(query=query)

#     # Format the chat history correctly
#     formatted_history = []
#     for message in st.session_state.chat_session.history:
#         formatted_history.append(
#             {"role": message["role"], "parts": [{"text": message["content"]}]}
#         )

#     # Add the new query to the formatted history
#     formatted_history.append({"role": "user", "parts": [{"text": prompt}]})

#     response = model.generate_content(formatted_history)
#     return response.text


# def main():
#     # Set page styles for dark theme
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-color: #1E1E1E;
#             color: #E0E0E0;
#         }
#         .stChatMessage {
#             background-color: #2C2C2C;
#             border: 1px solid #3D3D3D;
#             border-radius: 10px;
#             padding: 15px;
#             margin-bottom: 15px;
#             box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
#         }
#         .stChatMessage p {
#             color: #E0E0E0 !important;
#             font-size: 16px;
#             line-height: 1.6;
#         }
#         .stTextInput>div>div>input {
#             color: #E0E0E0 !important;
#             background-color: #2C2C2C;
#             border: 1px solid #3D3D3D;
#             border-radius: 5px;
#             padding: 10px;
#         }
#         body {
#             font-family: 'Arial', sans-serif;
#             color: #E0E0E0;
#         }
#         .stMarkdown {
#             color: #E0E0E0;
#         }
#         .stButton>button {
#             background-color: #4A4A4A;
#             color: #E0E0E0;
#             border: 1px solid #3D3D3D;
#             border-radius: 5px;
#             padding: 10px 20px;
#             font-weight: bold;
#             transition: all 0.3s ease;
#         }
#         .stButton>button:hover {
#             background-color: #5A5A5A;
#         }
#         .stHeader {
#             color: #E0E0E0;
#             font-size: 32px;
#             font-weight: bold;
#             text-align: center;
#             margin-bottom: 30px;
#             text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
#         }
#         .stAlert {
#             background-color: #2C2C2C;
#             color: #E0E0E0;
#             border: 1px solid #3D3D3D;
#             border-radius: 5px;
#             padding: 10px;
#             margin-bottom: 10px;
#         }
#         .chat-container {
#             display: flex;
#             flex-direction: column-reverse;
#             height: calc(100vh - 200px);
#             overflow-y: auto;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     st.markdown(
#         "<h1 class='stHeader'>AI VC: Connecting Founders and Investors 🚀💼</h1>",
#         unsafe_allow_html=True,
#     )

#     # Create two columns
#     col1, col2 = st.columns([3, 1])

#     with col1:
#         # Chat container
#         chat_container = st.container()

#         # Input field for user's message (moved to the bottom)
#         message = st.chat_input(
#             "Enter your query about startups, investments, or founders..."
#         )

#         if message:
#             # Add user's message to chat and display it
#             st.session_state.chat_session.history.append(
#                 {"role": "user", "content": message}
#             )

#             # Generate and display response
#             response = generate_response(message)
#             st.session_state.chat_session.history.append(
#                 {"role": "model", "content": response}
#             )
#         if "chat_session" not in st.session_state:
#             st.session_state.chat_session = {"history": []}

#         # Display chat history in reverse order
#         with chat_container:
#             st.markdown('<div class="chat-container">', unsafe_allow_html=True)
#             for message in reversed(st.session_state.chat_session.history):
#                 role = "assistant" if message["role"] == "assistant" else "user"
#                 with st.chat_message(role):
#                     st.markdown(f"<p>{message['content']}</p>", unsafe_allow_html=True)
#             st.markdown("</div>", unsafe_allow_html=True)

#     with col2:
#         # Sidebar (now in the second column)
#         st.markdown(
#             "<h3 style='text-align: center; color: #E0E0E0;'>Options</h3>",
#             unsafe_allow_html=True,
#         )
#         if st.button("Clear Chat History", key="clear_chat"):
#             st.session_state.chat_session.history = []
#             st.experimental_rerun()

#         # Add some engaging elements
#         st.markdown(
#             "<h3 style='color: #E0E0E0;'>Quick Tips</h3>", unsafe_allow_html=True
#         )
#         st.markdown(
#             "<div class='stAlert'>💡 Ask about specific industries or investment stages for better matches!</div>",
#             unsafe_allow_html=True,
#         )
#         st.markdown(
#             "<div class='stAlert'>🔒 We respect privacy and don't share personal details without permission.</div>",
#             unsafe_allow_html=True,
#         )
#         st.markdown(
#             "<div class='stAlert'>🚀 Ready to revolutionize the startup-investor connection? Let's get started!</div>",
#             unsafe_allow_html=True,
#         )


# if __name__ == "__main__":
#     main()

# # THis is the second update
# import os
# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="youthventure.ai",
#     page_icon=":cat:",
#     layout="wide",
# )

# # Set up Google Gemini AI model
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=GOOGLE_API_KEY)
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])

# # Simplified prompt template
# template = """
# You are an AI matchmaker platform designed to connect entrepreneurs with potential investors. Your goal is to facilitate access to capital for startups and provide investors with exciting opportunities to support innovative projects. You will also educate them on wise investment strategies.

# Key Requirements:
# 1. Matchmaking: Match investors with startups based on the information provided.
# 2. Contact Information: Provide verified contact details for suggested founders and investors.
# 3. Prompt Guidance: Guide users to re-enter the prompt if it's incorrect or irrelevant.
# 4. Educational Resources: Provide relevant resources about investments, founders, and startups.

# Ensure that the information is only about investments, startups, and founders. Tailor each response to the specific needs and interests of the individuals involved. Respect privacy and do not share personal contact details without permission.
# We are developing an AI matchmaker platform designed to connect budding entrepreneurs with potential investors. Our goal is to facilitate access to capital for startups and provide investors with exciting opportunities to support innovative projects. Our AI system will not only match investors with startups but also educate them on wise investment strategies.

# Additional Notes

# Important: Always ensure that the information is only about investments, startups, and founders and not just some random topic. Always ensure that the contact information provided is accurate and up-to-date.

# Engagement: Tailor each response to the specific needs and interests of the individuals involved.

# Respect Privacy: Do not share personal contact details without permission.

# Template Founder Prompt: "Hi, I'm Azwad. I'm building an AI-powered venture capital platform and I'm looking for investors who might be interested in this project. Can you suggest some potential investors with experience in AI, fintech, or venture capital technologies?"

# Template Response: "Hello Azwad, thank you for sharing information about your AI-powered venture capital platform. Based on your project's focus on AI and fintech, I've identified three potential investors who might be interested in your startup:

# 1. Andreessen Horowitz (a16z)

# Focus: Technology, AI, Fintech

# Investment Experience: Airbnb, Coinbase, Facebook

# Preferred Investment Amount: $1M - $100M+

# Contact: info@a16z.com | +1 (650) 798-5800

# 2. Sequoia Capital

# Focus: Technology, AI, Fintech

# Investment Experience: Apple, Google, PayPal

# Preferred Investment Amount: $1M - $100M+

# Contact: info@sequoiacap.com | +1 (650) 854-3927

# 3. SoftBank Vision Fund

# Focus: AI, Technology, Fintech

# Investment Experience: Uber, ByteDance, NVIDIA

# Preferred Investment Amount: $100M+

# Contact: info@softbank.com | +81 3-6889-2000

# These investors have significant experience in AI and fintech investments and could potentially provide valuable support for your AI VC platform. I recommend researching each firm further and tailoring your pitch to their specific investment criteria and portfolio strategies."

# Template Investor Prompt: "Hi I am Mahin and I am looking to invest in space exploraion for 1000$. Find me companies to invest in."

# Template Response: "Hello Mahin, thank you for your interest in investing in space exploration. While $1000 is a relatively small amount for this industry, there are some exciting startups and founders you might consider. Here are three potential options based on the information available:

# 1. Elon Musk - SpaceX

# Focus: Revolutionizing space technology and enabling Mars colonization

# Founded: 2002

# Total Raised: $6.874B

# Contact: info@spacex.com | +1 (310) 363-6000

# 2. Jim Cantrell - Phantom Space

# Focus: Democratizing space access with small satellite launch services

# Founded: 2019

# Total Raised: $118.5M

# Contact: info@phantomspace.com | +1 (520) 771-8654

# 3. Peter Beck - Rocket Lab

# Focus: Small satellite launch and space systems

# Founded: 2006

# Total Raised: $288M (as of last available data)

# Contact: info@rocketlabusa.com | +1 (714) 465-5737

# Please note that these companies typically deal with much larger investments. However, you might consider:

# 1. Joining an angel investor network specializing in space tech

# 2. Investing in a space technology ETF

# 3. Exploring equity crowdfunding platforms for space startups"

# Template Founder Prompt:: "Hi, I'm Jim Crawford. I'm developing a music-based rhythm game with a twist. Who might be interested in my innovative music game?"

# Template Response: "Hello Jim Crawford! Your innovative music-based rhythm game sounds exciting. Here are three potential supporters who might be interested in your project:

# 1. Alex Rigopulos (Co-founder of Harmonix)

# Known for: Creating Rock Band and Guitar Hero

# Contact: alexprigopulos-linkedin@yahoo.com | +1(617) 335-3336

# 2. Tetsuya Mizuguchi (CEO of Enhance)

# Known for: Developing unique music-based games

# Contact: mizuguchi@enhance-exp.com | +1 (555) 901-2345

# 3. Steve Aoki (DJ and Music Producer)

# Known for: His interest in gaming and music technology

# Contact: steve@steveaoki.com | +1 (555) 012-3456

# These individuals have backgrounds in music gaming or the music industry, which could be valuable for your innovative rhythm game concept."

# Template Investors Prompt: "Hi, I'm Katie Cho, an investor interested in AR/VR gaming technologies. Which startups are pushing boundaries in this space?"

# Template Response: "Hello Katie Cho!

# The AR/VR gaming space is indeed exciting. Here are three startups pushing boundaries in this area:

# 1. Resolution Games (VR/AR game developer)

# Founder: Tommy Palm

# Contact: info@resolutiongames.com | +1 (555) 456-7890

# 2. Polyarc (VR game studio, creators of Moss)

# Founder: Tam Armstrong

# Contact: hello@polyarcgames.com | +1 (555) 567-8901

# 3. Nreal (AR glasses manufacturer)

# Founder: Chi Xu

# Contact: contact@nreal.ai | +1 (555) 678-9012

# These companies are at the forefront of AR/VR gaming technology and could offer interesting investment opportunities."


# Investors Prompt:
# {query}

# Your Response:
# """


# def generate_response(query):
#     prompt = template.format(query=query)
#     response = st.session_state.chat_session.send_message(prompt)
#     return response.text


# def main():
#     # Set page styles
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-color: #FFF8C9;
#         }
#         .stChatMessage {
#             background-color: #f9b034;
#             border: 2px solid #000000;
#             border-radius: 15px;
#             padding: 15px;
#             margin-bottom: 15px;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         }
#         .stChatMessage p {
#             color: #000000 !important;
#             font-size: 16px;
#             line-height: 1.6;
#         }
#         .stTextInput>div>div>input {
#             color: #000000 !important;
#             background-color: #FFF8C9;
#             border: 2px solid #f9b034;
#             border-radius: 10px;
#             padding: 10px;
#         }
#         body {
#             font-family: 'Manrope', sans-serif;
#             color: #000000;
#         }
#         .stMarkdown {
#             color: #000000;
#         }
#         .stButton>button {
#             background-color: #f9b034;
#             color: #000000;
#             border: 2px solid #000000;
#             border-radius: 10px;
#             padding: 10px 20px;
#             font-weight: bold;
#             transition: all 0.3s ease;
#         }
#         .stButton>button:hover {
#             background-color: #000000;
#             color: #f9b034;
#         }
#         .stHeader {
#             color: #000000;
#             font-size: 36px;
#             font-weight: bold;
#             text-align: center;
#             margin-bottom: 30px;
#             text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
#         }
#         .stAlert {
#             background-color: #f9b034;
#             color: #000000;
#             border: 2px solid #000000;
#             border-radius: 10px;
#             padding: 10px;
#             margin-bottom: 10px;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     st.markdown(
#         "<h1 class='stHeader'>AI VC: Connecting Founders and Investors 🐱💼</h1>",
#         unsafe_allow_html=True,
#     )

#     # Create two columns
#     col1, col2 = st.columns([2, 1])

#     with col1:
#         # Display chat history
#         for message in st.session_state.chat_session.history:
#             role = "assistant" if message.role == "model" else message.role
#             with st.chat_message(role):
#                 st.markdown(f"<p>{message.parts[0].text}</p>", unsafe_allow_html=True)

#         # Input field for user's message
#         message = st.chat_input(
#             "Enter your query about startups, investments, or founders..."
#         )

#         if message:
#             # Add user's message to chat and display it
#             st.chat_message("user").markdown(
#                 f"<p>{message}</p>", unsafe_allow_html=True
#             )

#             # Generate and display response
#             with st.chat_message("assistant"):
#                 response = generate_response(message)
#                 st.markdown(f"<p>{response}</p>", unsafe_allow_html=True)

#     with col2:
#         # Sidebar (now in the second column)
#         st.markdown(
#             "<h3 style='text-align: center; color: #000000;'>Options</h3>",
#             unsafe_allow_html=True,
#         )
#         if st.button("Clear Chat History", key="clear_chat"):
#             st.session_state.chat_session.history = []
#             st.experimental_rerun()

#         # Add some engaging elements
#         st.markdown(
#             "<h3 style='color: #000000;'>Quick Tips</h3>", unsafe_allow_html=True
#         )
#         st.markdown(
#             "<div class='stAlert'>💡 Ask about specific industries or investment stages for better matches!</div>",
#             unsafe_allow_html=True,
#         )
#         st.markdown(
#             "<div class='stAlert'>🔒 Remember: We respect privacy and don't share personal details without permission.</div>",
#             unsafe_allow_html=True,
#         )
#         st.markdown(
#             "<div class='stAlert'>🚀 Ready to revolutionize the startup-investor connection? Let's get started!</div>",
#             unsafe_allow_html=True,
#         )


# if __name__ == "__main__":
#     main()


# import os
# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as genai
# from langchain_community.document_loaders import CSVLoader
# from langchain_community.vectorstores import FAISS
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain.prompts import PromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI

# # from template import template


# # Load environment variables
# load_dotenv()

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="youthventure.ai",
#     page_icon=":cat:",
#     layout="centered",
# )

# # Set up Google Gemini AI model
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=GOOGLE_API_KEY)

# # 1. Vectorize the sales response csv data
# loader = CSVLoader(file_path="prompts_and_responses.csv")
# documents = loader.load()

# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
# db = FAISS.from_documents(documents, embeddings)


# # 2. Function for similarity search
# def retrieve_info(query):
#     similar_response = db.similarity_search(query, k=3)
#     page_contents_array = [doc.page_content for doc in similar_response]
#     return page_contents_array


# # 3. Setup LLM & prompts
# llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)


# template = """
# We are developing an AI matchmaker platform designed to connect budding entrepreneurs with potential investors. Our goal is to facilitate access to capital for startups and provide investors with exciting opportunities to support innovative projects. Our AI system will not only match investors with startups but also educate them on wise investment strategies.

# Key Requirements:

# 1. Matchmaking: Use custom datasets or any available information on the internet to match investors with startups.

# 2. Contact Information: Provide verified cell phone/mobile contact numbers and email addresses for every suggested founder and investor. Double-check the accuracy of these contacts.

# 3. Prompt Guidance: If the user provides incorrect or irrelevant information, guide them to re-enter the prompt correctly.

# 4. Educational Resources: Provide useful YouTube videos or other resources pertinent to the prompt to help users learn more about the topic of investments, founders, and startups. If people veer off the topic and just ask for links, don't provide that to them and just tell them to re-enter the prompt.

# Additional Notes

# Important: Always ensure that the information is only about investments, startups, and founders and not just some random topic. Always ensure that the contact information provided is accurate and up-to-date.

# Engagement: Tailor each response to the specific needs and interests of the individuals involved.

# Respect Privacy: Do not share personal contact details without permission.

# Template Founder Prompt: "Hi, I'm Azwad. I'm building an AI-powered venture capital platform and I'm looking for investors who might be interested in this project. Can you suggest some potential investors with experience in AI, fintech, or venture capital technologies?"

# Template Response: "Hello Azwad, thank you for sharing information about your AI-powered venture capital platform. Based on your project's focus on AI and fintech, I've identified three potential investors who might be interested in your startup:

# 1. Andreessen Horowitz (a16z)

# Focus: Technology, AI, Fintech

# Investment Experience: Airbnb, Coinbase, Facebook

# Preferred Investment Amount: $1M - $100M+

# Contact: info@a16z.com | +1 (650) 798-5600

# 2. Sequoia Capital

# Focus: Technology, AI, Fintech

# Investment Experience: Apple, Google, PayPal

# Preferred Investment Amount: $1M - $100M+

# Contact: info@sequoiacap.com | +1 (650) 854-3927

# 3. SoftBank Vision Fund

# Focus: AI, Technology, Fintech

# Investment Experience: Uber, ByteDance, NVIDIA

# Preferred Investment Amount: $100M+

# Contact: info@softbank.com | +81 3-6889-2000

# These investors have significant experience in AI and fintech investments and could potentially provide valuable support for your AI VC platform. I recommend researching each firm further and tailoring your pitch to their specific investment criteria and portfolio strategies."

# Template Investor Prompt: "Hi I am Mahin and I am looking to invest in space exploraion for 1000$. Find me companies to invest in."

# Template Response: "Hello Mahin, thank you for your interest in investing in space exploration. While $1000 is a relatively small amount for this industry, there are some exciting startups and founders you might consider. Here are three potential options based on the information available:

# 1. Elon Musk - SpaceX

# Focus: Revolutionizing space technology and enabling Mars colonization

# Founded: 2002

# Total Raised: $6.874B

# Contact: info@spacex.com | +1 (310) 363-6000

# 2. Jim Cantrell - Phantom Space

# Focus: Democratizing space access with small satellite launch services

# Founded: 2019

# Total Raised: $118.5M

# Contact: info@phantomspace.com | +1 (520) 261-4350

# 3. Peter Beck - Rocket Lab

# Focus: Small satellite launch and space systems

# Founded: 2006

# Total Raised: $288M (as of last available data)

# Contact: info@rocketlabusa.com | +1 (714) 465-5737

# Please note that these companies typically deal with much larger investments. However, you might consider:

# 1. Joining an angel investor network specializing in space tech

# 2. Investing in a space technology ETF

# 3. Exploring equity crowdfunding platforms for space startups"

# Template Founder Prompt:: "Hi, I'm Jim Crawford. I'm developing a music-based rhythm game with a twist. Who might be interested in my innovative music game?"

# Template Response: "Hello Jim Crawford! Your innovative music-based rhythm game sounds exciting. Here are three potential supporters who might be interested in your project:

# 1. Alex Rigopulos (Co-founder of Harmonix)

# Known for: Creating Rock Band and Guitar Hero

# Contact: alex@harmonixmusic.com | +1 (555) 890-1234

# 2. Tetsuya Mizuguchi (CEO of Enhance)

# Known for: Developing unique music-based games

# Contact: mizuguchi@enhance-exp.com | +1 (555) 901-2345

# 3. Steve Aoki (DJ and Music Producer)

# Known for: His interest in gaming and music technology

# Contact: steve@steveaoki.com | +1 (555) 012-3456

# These individuals have backgrounds in music gaming or the music industry, which could be valuable for your innovative rhythm game concept."

# Template Investors Prompt: "Hi, I'm Katie Cho, an investor interested in AR/VR gaming technologies. Which startups are pushing boundaries in this space?"

# Template Response: "Hello Katie Cho!

# The AR/VR gaming space is indeed exciting. Here are three startups pushing boundaries in this area:

# 1. Resolution Games (VR/AR game developer)

# Founder: Tommy Palm

# Contact: info@resolutiongames.com | +1 (555) 456-7890

# 2. Polyarc (VR game studio, creators of Moss)

# Founder: Tam Armstrong

# Contact: hello@polyarcgames.com | +1 (555) 567-8901

# 3. Nreal (AR glasses manufacturer)

# Founder: Chi Xu

# Contact: contact@nreal.ai | +1 (555) 678-9012

# These companies are at the forefront of AR/VR gaming technology and could offer interesting investment opportunities."


# Template Prompt :
# {Prompt}

# Template Response:
# {Response}
# """

# prompt = PromptTemplate(input_variables=["Prompt", "Response"], template=template)


# # 4. Retrieval augmented generation
# def generate_response(message):
#     best_practice = retrieve_info(message)
#     chain = prompt | llm
#     response = chain.invoke({"Prompt": message, "Response": best_practice})
#     return response.content


# def main():
#     st.header("AI VC to match founders and investors :cat:")
#     message = st.text_area("Enter your prompt")

#     if message:
#         st.write("Getting you the matches...")
#         result = generate_response(message)
#         st.info(result)

#     # Button to clear input
#     if st.button("Clear input"):
#         st.experimental_rerun()


# if __name__ == "__main__":
#     main()
