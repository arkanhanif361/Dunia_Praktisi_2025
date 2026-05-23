import streamlit as st

st.set_page_config(
  page_title="Dunia_Praktisi_2025",
  page_icon="🧊",
  layout="centered",
  initial_sidebar_state="expanded",
)


st.title("📊 Dashboard")
st.header("Laporan Bulanan")
st.subheader("📈 Monthly Expenses")
st.caption("Made with ❤️ using Streamlit")
st.write("Hello, *World!* :sunglasses:")

title = st.text_input("Movie title", "Boboiboy")
st.write("The current movie title is", title)

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

st.button("Reset", type="primary")

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
