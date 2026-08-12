import streamlit as st


def metric_card(title, value, description=""):

    st.metric(
        label=title,
        value=value,
        help=description
    )

    if description:
        st.caption(description)


def tool_badge(name):

    st.write(f"🔹 {name}")


def section_title(title, subtitle=None):

    st.subheader(title)

    if subtitle:
        st.caption(subtitle)