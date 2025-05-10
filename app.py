import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")

st.title("🌱 Growth Mindset Challenge")
st.subheader("Empower yourself through learning, persistence, and self-belief.")

st.markdown("## What is a Growth Mindset?")
st.write(
    "A **growth mindset** is the belief that your abilities and intelligence "
    "can be developed through hard work, perseverance, and learning from mistakes. "
    "This concept, popularized by psychologist **Carol Dweck**, encourages us to see "
    "challenges as opportunities to grow rather than limitations."
)

st.markdown("## Why Adopt a Growth Mindset?")
reasons = [
    "🌟 Embrace Challenges — View obstacles as learning opportunities.",
    "✏️ Learn from Mistakes — Every error is a step toward improvement.",
    "💪 Persist Through Difficulties — Keep going even when it’s tough.",
    "🎯 Celebrate Effort — Value the process, not just the outcome.",
    "🔍 Keep an Open Mind — Stay curious and adapt based on new learnings."
]
for reason in reasons:
    st.markdown(f"- {reason}")

st.markdown("## How Can You Practice a Growth Mindset?")
practices = [
    "🎯 Set Learning Goals instead of only aiming for grades.",
    "🔁 Reflect on Your Learning regularly — both wins and setbacks.",
    "🗣️ Seek Feedback and use it constructively.",
    "😊 Stay Positive and believe in your potential to grow."
]
for practice in practices:
    st.markdown(f"- {practice}")

st.markdown("---")
st.markdown("## 💬 Share Your Commitment")

name = st.text_input("What's your name?")
commitment = st.text_area("Write one sentence about how *you* will adopt a growth mindset.")

if st.button("Submit"):
    if name and commitment:
        st.success(f"Thank you, {name}! 🌟 Your commitment has been recorded.")
        st.write(f"**Your Pledge:** _{commitment}_")
    else:
        st.warning("Please enter both your name and a commitment.")

st.markdown("---")
st.info("This app was built using [Streamlit](https://streamlit.io) and packaged with [uv](https://github.com/astral-sh/uv).")
