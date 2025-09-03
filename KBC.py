import streamlit as st

st.set_page_config(page_title="KBC Quiz", layout="centered")

st.title("🎙️ Kaun Banega Crorepati")
st.subheader("Welcome to the game!")

# Player name input
if 'name' not in st.session_state:
    st.session_state.name = ""

if st.session_state.name == "":
    name = st.text_input("Please enter your name to start:")
    if name:
        st.session_state.name = name
        st.success(f"Hello {name}, Welcome to KBC!")
        st.session_state.start_game = False
        st.session_state.current_q = 0
        st.session_state.total_won = 0
        st.session_state.game_over = False
else:
    st.info(f"👤 Player: {st.session_state.name}")

# Questions data (list of dictionaries)
questions = [
    {
        "q": "1. Which of the following is not a feature of Object-Oriented Programming?",
        "options": {"A": "Encapsulation", "B": "Inheritance", "C": "Polymorphism", "D": "Compilation"},
        "answer": "D",
        "money": 1000
    },
    {
        "q": "2. What is the time complexity of binary search in a sorted array?",
        "options": {"A": "O(n)", "B": "O(log n)", "C": "O(n log n)", "D": "O(1)"},
        "answer": "B",
        "money": 2000
    },
    {
        "q": "3. In a stack, which operation is not possible in O(1) time using arrays?",
        "options": {"A": "Push", "B": "Pop", "C": "Peek", "D": "Resize"},
        "answer": "D",
        "money": 3000
    },
    {
        "q": "4. What is the worst-case time complexity of linear search?",
        "options": {"A": "O(1)", "B": "O(log n)", "C": "O(n)", "D": "O(n^2)"},
        "answer": "C",
        "money": 4000
    },
    {
        "q": "5. Linear search can be performed on:",
        "options": {"A": "Sorted arrays only", "B": "Unsorted arrays only", "C": "Both sorted and unsorted arrays", "D": "Linked lists only"},
        "answer": "C",
        "money": 5000
    }
]

# Game Flow
if st.session_state.name and not st.session_state.get("start_game", False):
    if st.button("🎮 Start Game"):
        st.session_state.start_game = True
        st.session_state.current_q = 0
        st.session_state.total_won = 0
        st.session_state.game_over = False

# Game logic
if st.session_state.get("start_game") and not st.session_state.get("game_over"):
    q_idx = st.session_state.current_q
    if q_idx < len(questions):
        q = questions[q_idx]

        st.markdown(f"### Question for ₹{q['money']}")
        st.write(q["q"])

        selected = st.radio(
            "Choose your answer:",
            list(q["options"].keys()),
            format_func=lambda x: f"{x}. {q['options'][x]}",
            key=f"q_{q_idx}"
        )

        if st.button("✅ Submit Answer", key=f"submit_{q_idx}"):
            if selected == q["answer"]:
                st.success(f"🎉 Correct! You've won ₹{q['money']}")
                st.session_state.total_won += q["money"]
                st.session_state.current_q += 1
            else:
                st.error(f"❌ Wrong answer! Correct answer was {q['answer']}.")
                st.session_state.game_over = True
    else:
        st.success(f"🏆 Congratulations {st.session_state.name}, you won a total of ₹{st.session_state.total_won}!")
        st.session_state.game_over = True

# Show final result if game is over
if st.session_state.get("game_over"):
    st.info(f"Game Over! You won ₹{st.session_state.total_won}")
    if st.button("🔄 Play Again"):
        st.session_state.name = ""
        st.session_state.start_game = False
        st.session_state.current_q = 0
        st.session_state.total_won = 0
        st.session_state.game_over = False
