import streamlit as st
import random as rd

st.header("Random Number Generator")

# Random Number Generator
st.write("Click the button below to generate a random number between 1 and 100.")

if st.button("Generate Random Number"):
    st.success(f"Your random number is: {rd.randint(1, 100)}")

st.divider()

# Number Guessing Game
st.write("Click the button below to play the Number Guessing Game.")

# Initialize session state
if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "random_number" not in st.session_state:
    st.session_state.random_number = None

# Start Game
if st.button("Play Number Guessing Game"):
    st.session_state.random_number = rd.randint(1, 100)
    st.session_state.game_started = True

# Show game only after it starts
if st.session_state.game_started:
    guess = st.number_input(
        "Enter your guess (1-100)",
        min_value=1,
        max_value=100,
        step=1
    )

    if st.button("Submit Guess"):
        if guess < st.session_state.random_number:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.random_number:
            st.warning("Too high! Try again.")
        else:
            st.success(f"🎉 Congratulations! You guessed it! The number was {st.session_state.random_number}.")
            # Reset game
            st.session_state.game_started = False
            st.session_state.random_number = None