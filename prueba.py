import streamlit as st
import time

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")
    
    st.button("Reset", type="primary")
    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)