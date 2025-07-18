# Number Guessing Game
import streamlit as st
import random 

def Number_guess(guess):
    if guess :
        guess = int(guess)
        st.session_state.attempts += 1

        if guess < st.session_state.number :
            st.write("Too low! Try again 😊")
        elif guess > st.session_state.number :
            st.write("Too high! Try again 😊")
        else :
            st.write("🎉 Congratulations!")
            st.write(f"You guessed it in {st.session_state.attempts} attempts.")
            st.balloons()
            
# Streamlit app title and instructions
st.set_page_config(page_title="Number Guessing Game", page_icon=":game_die:", layout="wide")
st.title("Welcome to The Number Guessing Game 🎮")
st.subheader("Guess a number between 1 to 100")

if 'number' not in st.session_state :
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    
# Number_of_guess 
guess = st.text_input("Enter your guess : ")
Number_guess(guess)
        
# Reset the game        
if st.button("Reset Game") :
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.write("Game reset! Try again 😊")