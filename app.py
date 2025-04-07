from openai import OpenAI
import streamlit as st
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Configure the page and set the title
st.set_page_config(page_title="Multi-Model Chatbot", layout="wide")
st.title("GPT Chatbot")
# Initialize the OpenAI client with OpenRouter
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=st.secrets["OPENAI_API_KEY"])

# Define available models
models = [
    "deepseek/deepseek-chat-v3-0324:free",
    "google/gemma-3-27b-it:free",
    "featherless/qwerky-72b:free"
]

# Define job personas
jobs_dict = {
    "assistant": "You are a helpful assistant. Please answer the user's questions.",
    "developer": "You are a skilled software developer. Write and debug code effectively.",
    "data scientist": "You analyze data and build machine learning models.",
    "teacher": "You educate students and explain complex topics in simple terms.",
    "doctor": "You diagnose medical conditions and provide health advice.",
}

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for model and persona selection
with st.sidebar:
    st.header("Settings")
    selected_model = st.selectbox("Choose a model:", models)
    selected_persona = st.selectbox("Choose a persona:", list(jobs_dict.keys()))
    
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get user input
user_input = st.chat_input("Type your message here...")

# Process user input
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Display assistant thinking indicator
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        
        try:
            # Prepare messages for API call
            messages = [{"role": "system", "content": jobs_dict[selected_persona]}]
            # Add conversation history
            for msg in st.session_state.messages:
                messages.append({"role": msg["role"], "content": msg["content"]})
            
            # Call the API
            response = client.chat.completions.create(
                model=selected_model,
                messages=messages,
                temperature=0.7,
                stream=True
            )
            
            # Process streaming response
            full_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
            
            # Update with final response
            message_placeholder.markdown(full_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            message_placeholder.markdown(f"Error: {str(e)}")
            
# Add some helpful instructions at the bottom
st.markdown("---")
st.caption("Select a model and persona from the sidebar. Your conversation will be maintained until you clear it or refresh the page.")