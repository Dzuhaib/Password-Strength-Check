import streamlit as st
import re

def check_password_strength(password):
    score = 0
    strength = "Weak"

    if len(password) >= 8:
        score += 1

    if re.search(f"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    
    if score == 1:
        strength = "Weak 🔴"
    if score == 2:
        strength = "Moderate 🟡"
    if score == 3:
        strength = "Strong 🟢"
    if score == 4:
        strength = "very strong 💪🔥"
    
    return strength, score

st.title("🔒 Password Strength Checker")

password = st.text_input("Enter a password:", type="password")

if password:
    strength, score = check_password_strength(password)
    st.subheader(f"Strength: {strength}")
    st.progress(score / 4)