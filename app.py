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
