import streamlit as st


def apply_styles():

    st.markdown(
        """
        <style>

        .block-container {
            max-width: 1450px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        </style>
        """,
        unsafe_allow_html=True
    )