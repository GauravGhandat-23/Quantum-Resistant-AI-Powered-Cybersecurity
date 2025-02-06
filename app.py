import streamlit as st
import requests
import json
import groq

# Initialize Groq API Client
client = groq.Groq(api_key="your_api_key")  # Replace with your actual API key

def call_groq_api(user_input):
    """Calls the Groq API to analyze cybersecurity threats."""
    try:
        # Define the conversation messages
        messages = [
            {"role": "system", "content": "You are an AI cybersecurity analyst."},
            {"role": "user", "content": user_input}
        ]

        # Make the API request
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.6,
            max_tokens=4096,
            top_p=0.95,
            stream=False  # Ensure we receive a single response
        )

        # Extract and return the AI response safely
        return completion.choices[0].message.content if completion.choices else "No response from AI."

    except Exception as e:
        return f"Error: {e}"

# Simulated Post-Quantum Encryption (Example: Lattice-based Encryption)
def pqc_encrypt(message):
    encrypted_message = "🔒" + "".join(chr(ord(char) + 3) for char in message) + "🔒"
    return encrypted_message

def pqc_decrypt(encrypted_message):
    decrypted_message = "".join(chr(ord(char) - 3) for char in encrypted_message.strip("🔒"))
    return decrypted_message

# Streamlit UI
st.title("Quantum-Resistant AI-Powered Cybersecurity")
st.subheader("Securing the Future with AI and Post-Quantum Encryption")

option = st.selectbox("Choose a security function:", ["AI Threat Detection", "Post-Quantum Encryption & Decryption"])

if option == "AI Threat Detection":
    user_input = st.text_area("Enter the cybersecurity incident or anomaly:")
    if st.button("Analyze with AI"):
        if user_input:
            result = call_groq_api(user_input)
            st.subheader("AI Threat Analysis")
            st.write(result)  # Directly display the result string
        else:
            st.warning("Please enter an incident description.")

elif option == "Post-Quantum Encryption & Decryption":
    pq_input = st.text_area("Enter text to encrypt:")
    if st.button("Encrypt"):
        if pq_input:
            encrypted = pqc_encrypt(pq_input)
            st.subheader("Encrypted Text")
            st.code(encrypted)
        else:
            st.warning("Please enter text to encrypt.")
    
    pq_decrypt_input = st.text_area("Enter encrypted text to decrypt:")
    if st.button("Decrypt"):
        if pq_decrypt_input:
            decrypted = pqc_decrypt(pq_decrypt_input)
            st.subheader("Decrypted Text")
            st.code(decrypted)
        else:
            st.warning("Please enter encrypted text to decrypt.")

st.success("Project successfully loaded! Secure your data now.")

