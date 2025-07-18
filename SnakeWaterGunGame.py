#Snake_Water_Gun Game
import streamlit as st
import random   

def play_game(user_choice):
    options = ['snake', 'water', 'gun']
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        st.write("Both are same!, Try Again")
    elif (user_choice == 'snake' and computer_choice == 'water') or (user_choice == 'water' and computer_choice == 'gun') or (user_choice == 'gun' and computer_choice == 'snake'):
        st.write("🎉 You Win!")
        st.balloons()
    else:
        st.write(f"Computer choice is {computer_choice}")
        st.write("Computer Wins!")

st.title("Welcome to Snake-Water-Gun Game!")
user_choice = st.selectbox("Choose your option:", ['snake', 'water', 'gun'])
if st.button("Play"):
    play_game(user_choice)