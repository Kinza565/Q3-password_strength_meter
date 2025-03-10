import streamlit as st
import re
import random
import string

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Upper and Lower Case Check
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one numeric digit (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    # Blacklist Common Passwords
    common_passwords = ["password", "123456", "qwerty", "password123", "letmein", "welcome"]
    if password.lower() in common_passwords:
        score = 1  # Auto-set to weak
        feedback = ["Your password is too common. Choose a more unique one."]
    
    # Determine Strength
    strength = "Weak" if score <= 2 else "Moderate" if score <= 3 else "Strong"
    
    return strength, feedback

# Function to generate strong password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, feedback = check_password_strength(password)
    st.write(f"**Password Strength:** {strength}")
    
    if feedback:
        st.subheader("Suggestions to Improve:")
        for tip in feedback:
            st.write(f"- {tip}")
    
    if strength == "Weak":
        st.subheader("Suggested Strong Password:")
        st.code(generate_strong_password(), language="plaintext")
