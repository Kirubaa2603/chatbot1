import streamlit as st

def main():
    st.set_page_config(page_title="Mindease Chatbot", layout="centered")
    
    st.title("🧠 Mindease Chatbot")
    
    # Initialize chat history if not already
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # User input
    user_input = st.text_input("Type your message:", key="user_input")
    
    if user_input:
        # Append user input to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Simple bot response (Modify this with actual chatbot logic)
        bot_response = f"You said: {user_input}"
        st.session_state.chat_history.append({"role": "bot", "content": bot_response})
        
        # Display bot response
        with st.chat_message("bot"):
            st.write(bot_response)
        
        # Clear input box
        st.session_state.user_input = ""
    
    # Button to clear chat history
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.experimental_rerun()

if __name__ == "__main__":
    main()
