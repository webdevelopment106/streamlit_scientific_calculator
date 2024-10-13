import streamlit as st
import math

# Set page layout and title
st.set_page_config(page_title="Scientific Calculator", layout="centered")
st.title("🔢 Professional Scientific Calculator")

# Define button styles using HTML/CSS to enhance the UI
st.markdown(
    """
    <style>
    .button-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 20px;
        border-radius: 8px;
        height: 70px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True
)

# Calculator logic
def evaluate_expression(expression):
    try:
        # Evaluate mathematical expression securely
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        return result
    except Exception as e:
        return "Error"

# Initialize session state to store input and output
if "input" not in st.session_state:
    st.session_state.input = ""
if "output" not in st.session_state:
    st.session_state.output = ""

# Define button layout and functionality
def button_click(label):
    if label == "C":
        st.session_state.input = ""
        st.session_state.output = ""
    elif label == "=":
        st.session_state.output = str(evaluate_expression(st.session_state.input))
    else:
        st.session_state.input += label

# Display the calculator screen
st.text_input("Input", value=st.session_state.input, key="input_field", disabled=True)
st.text_input("Output", value=st.session_state.output, key="output_field", disabled=True)

# Define calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "(", ")", "C", "√",
    "sin", "cos", "tan", "log",
    "pi", "exp", "^", "%"
]

# Render buttons using Streamlit columns
st.markdown('<div class="button-container">', unsafe_allow_html=True)
for button in buttons:
    if st.button(button):
        if button == "√":
            button_click("math.sqrt(")
        elif button in {"sin", "cos", "tan", "log", "exp"}:
            button_click(f"math.{button}(")
        elif button == "pi":
            button_click("math.pi")
        elif button == "^":
            button_click("**")
        else:
            button_click(button)
st.markdown('</div>', unsafe_allow_html=True)
