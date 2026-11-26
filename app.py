
import streamlit as st
import random

# Initialize the game
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Game title
st.title("🎯 Number Guessing Game!")

st.write("I have selected a number between 1 and 100.")
st.write("Can you guess it?")

# Input
guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=100,
    step=1
)

# Submit button
if st.button("Submit Guess") and not st.session_state.game_over:

    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.warning("Too low! Try again.")

    elif guess > st.session_state.secret_number:
        st.warning("Too high! Try again.")

    else:
        st.success(
            f"Correct! You guessed the number in "
            f"{st.session_state.attempts} attempts."
        )
        st.session_state.game_over = True

# Display attempts
st.write(f"Attempts: {st.session_state.attempts}")

# Restart button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()
