from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.8
    )

mode = input("Choose AI mode (e.g., happy, sad, strict, funny): ").lower().strip()

messages = [SystemMessage(content = f"""
                          You are a mood-based AI assistant.
                          Your current mode is: {mode}
                          You must strictly adapt your tone, style, and personality to this mode in every response.
                          """)]

print("\n----- Welcome to MoodBot -----")
print("Type '0' to exit\n")

while True :
    prompt = input("You : ")
    if prompt == "0" :
        break
    messages.append(HumanMessage(content = prompt))
    response = llm.invoke(messages)
    messages.append(AIMessage(content = response.content))
    print("Bot : ",response.content)


# streamlit version ->


# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# # ── Page config ──────────────────────────────────────────────────────────────
# st.set_page_config(page_title="MoodBot", page_icon="🎭", layout="centered")

# # ── Custom CSS ────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Mono:wght@300;400&display=swap');

# html, body, [class*="css"] {
#     font-family: 'DM Mono', monospace;
#     background-color: #0e0e0e;
#     color: #e8e8e0;
# }

# .stApp {
#     background-color: #0e0e0e;
# }

# h1 {
#     font-family: 'Syne', sans-serif !important;
#     font-weight: 800 !important;
#     font-size: 2.8rem !important;
#     letter-spacing: -1px;
#     color: #f0e040 !important;
#     margin-bottom: 0 !important;
# }

# .subtitle {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.78rem;
#     color: #666;
#     letter-spacing: 0.12em;
#     text-transform: uppercase;
#     margin-bottom: 2rem;
# }

# .mode-badge {
#     display: inline-block;
#     background: #f0e040;
#     color: #0e0e0e;
#     font-family: 'Syne', sans-serif;
#     font-weight: 700;
#     font-size: 0.85rem;
#     padding: 4px 14px;
#     border-radius: 2px;
#     letter-spacing: 0.08em;
#     text-transform: uppercase;
#     margin-bottom: 1.5rem;
# }

# .msg-user {
#     background: #1a1a1a;
#     border-left: 3px solid #f0e040;
#     padding: 12px 16px;
#     margin: 10px 0;
#     border-radius: 0 6px 6px 0;
#     font-size: 0.92rem;
# }

# .msg-bot {
#     background: #151515;
#     border-left: 3px solid #444;
#     padding: 12px 16px;
#     margin: 10px 0;
#     border-radius: 0 6px 6px 0;
#     font-size: 0.92rem;
#     color: #c8c8c0;
# }

# .msg-label {
#     font-size: 0.65rem;
#     letter-spacing: 0.14em;
#     text-transform: uppercase;
#     margin-bottom: 4px;
#     opacity: 0.5;
# }

# .stTextInput > div > div > input {
#     background-color: #1a1a1a !important;
#     border: 1px solid #2a2a2a !important;
#     border-radius: 4px !important;
#     color: #e8e8e0 !important;
#     font-family: 'DM Mono', monospace !important;
#     font-size: 0.9rem !important;
#     padding: 10px 14px !important;
# }

# .stTextInput > div > div > input:focus {
#     border-color: #f0e040 !important;
#     box-shadow: 0 0 0 1px #f0e04044 !important;
# }

# .stButton > button {
#     background: #f0e040 !important;
#     color: #0e0e0e !important;
#     font-family: 'Syne', sans-serif !important;
#     font-weight: 700 !important;
#     font-size: 0.85rem !important;
#     letter-spacing: 0.06em !important;
#     border: none !important;
#     border-radius: 3px !important;
#     padding: 8px 20px !important;
# }

# .stButton > button:hover {
#     opacity: 0.85 !important;
# }

# .stSelectbox > div > div {
#     background-color: #1a1a1a !important;
#     border: 1px solid #2a2a2a !important;
#     color: #e8e8e0 !important;
#     font-family: 'DM Mono', monospace !important;
#     border-radius: 4px !important;
# }

# hr {
#     border-color: #1e1e1e !important;
#     margin: 1.5rem 0 !important;
# }

# .chat-container {
#     max-height: 460px;
#     overflow-y: auto;
#     padding-right: 4px;
#     margin-bottom: 1rem;
# }

# #MainMenu, footer, header {visibility: hidden;}
# </style>
# """, unsafe_allow_html=True)

# # ── Session state init ────────────────────────────────────────────────────────
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "mode_set" not in st.session_state:
#     st.session_state.mode_set = False
# if "mode" not in st.session_state:
#     st.session_state.mode = ""

# # ── Header ────────────────────────────────────────────────────────────────────
# st.markdown("<h1>MoodBot 🎭</h1>", unsafe_allow_html=True)
# st.markdown('<p class="subtitle">mood-driven conversation engine</p>', unsafe_allow_html=True)

# # ── Mode selection screen ─────────────────────────────────────────────────────
# if not st.session_state.mode_set:
#     st.markdown("**Choose a mood to begin:**")

#     preset_modes = ["happy", "sad", "strict", "funny", "sarcastic", "poetic", "calm", "energetic"]
#     selected_preset = st.selectbox("Pick a preset mood", ["— select —"] + preset_modes)

#     st.markdown('<p class="subtitle">— or type your own —</p>', unsafe_allow_html=True)
#     custom_mode = st.text_input("Custom mood", placeholder="e.g. philosophical, pirate, sleepy…")

#     if st.button("Start Chat"):
#         mode = custom_mode.strip().lower() if custom_mode.strip() else (
#             selected_preset if selected_preset != "— select —" else ""
#         )
#         if not mode:
#             st.warning("Please choose or enter a mood first.")
#         else:
#             st.session_state.mode = mode
#             st.session_state.mode_set = True
#             st.session_state.messages = [
#                 SystemMessage(content=f"""
# You are a mood-based AI assistant.
# Your current mode is: {mode}
# You must strictly adapt your tone, style, and personality to this mode in every response.
# """)
#             ]
#             st.rerun()

# # ── Chat screen ───────────────────────────────────────────────────────────────
# else:
#     st.markdown(f'<div class="mode-badge">Mode: {st.session_state.mode}</div>', unsafe_allow_html=True)

#     chat_html = '<div class="chat-container">'
#     for role, text in st.session_state.chat_history:
#         if role == "You":
#             chat_html += f'<div class="msg-user"><div class="msg-label">You</div>{text}</div>'
#         else:
#             chat_html += f'<div class="msg-bot"><div class="msg-label">Bot</div>{text}</div>'
#     chat_html += '</div>'
#     st.markdown(chat_html, unsafe_allow_html=True)

#     col1, col2 = st.columns([5, 1])
#     with col1:
#         user_input = st.text_input(
#             "Your message",
#             key="user_input",
#             placeholder="Type something…",
#             label_visibility="collapsed"
#         )
#     with col2:
#         send = st.button("Send")

#     if send and user_input.strip():
#         prompt = user_input.strip()
#         st.session_state.messages.append(HumanMessage(content=prompt))

#         llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.8)
#         response = llm.invoke(st.session_state.messages)

#         st.session_state.messages.append(AIMessage(content=response.content))
#         st.session_state.chat_history.append(("You", prompt))
#         st.session_state.chat_history.append(("Bot", response.content))

#         st.rerun()

#     st.markdown("---")
#     if st.button("Reset / Change Mode"):
#         st.session_state.mode_set = False
#         st.session_state.mode = ""
#         st.session_state.messages = []
#         st.session_state.chat_history = []
#         st.rerun()