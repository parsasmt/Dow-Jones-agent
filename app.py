import streamlit as st
from datetime import datetime

from dashboard.styles import apply_styles
from dashboard.components import (
    metric_card,
    tool_badge,
    section_title
)

from agent.orchestrator import agent


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Dow Jones AI Agent",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)


apply_styles()


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


if "user_id" not in st.session_state:
    st.session_state.user_id = ""


if "last_tools" not in st.session_state:
    st.session_state.last_tools = []


if "last_success" not in st.session_state:
    st.session_state.last_success = None


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("📈 Dow Jones AI")

    st.caption(
        "Intelligent Market Analysis Agent"
    )

    st.divider()

    st.subheader("User")

    user_id = st.text_input(
        "User ID",
        value=st.session_state.user_id,
        placeholder="Enter your user ID"
    )

    st.session_state.user_id = user_id

    st.divider()

    st.subheader("Agent Components")

    tool_badge("RAG")
    tool_badge("Yahoo Finance")
    tool_badge("Tavily")
    tool_badge("FRED")
    tool_badge("GPT-OSS")

    st.divider()

    st.subheader("System")

    st.success("Agent Online")

    st.caption("Dow Jones AI Agent v1.0")


# ============================================================
# HEADER
# ============================================================

st.title("📈 Dow Jones AI Agent")

st.caption(
    "AI-powered analysis of the Dow Jones Industrial Average, "
    "financial markets, economic data and market news."
)


# ============================================================
# TOP METRICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    metric_card(
        "INDEX",
        "DJIA",
        "Dow Jones Industrial Average"
    )


with col2:

    metric_card(
        "AI MODEL",
        "GPT-OSS",
        "OpenRouter"
    )


with col3:

    metric_card(
        "KNOWLEDGE",
        "RAG",
        "Vector-based retrieval"
    )


with col4:

    if st.session_state.last_success is True:

        status = "SUCCESS"

    elif st.session_state.last_success is False:

        status = "ERROR"

    else:

        status = "ONLINE"


    metric_card(
        "STATUS",
        status,
        "Agent operational"
    )


st.divider()


# ============================================================
# MAIN LAYOUT
# ============================================================

left, right = st.columns(
    [2.2, 1]
)


# ============================================================
# CHAT AREA
# ============================================================

with left:

    section_title(
        "Ask the Dow Jones Agent",
        "Ask questions about the market, companies, economics or financial news."
    )


    # --------------------------------------------------------
    # DISPLAY CHAT HISTORY
    # --------------------------------------------------------

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )


    # --------------------------------------------------------
    # CHAT INPUT
    # --------------------------------------------------------

    question = st.chat_input(
        "Ask something about Dow Jones..."
    )


    if question:

        # ----------------------------------------------------
        # CHECK USER ID
        # ----------------------------------------------------

        if not user_id:

            st.warning(
                "Please enter a User ID in the sidebar first."
            )

            st.stop()


        # ----------------------------------------------------
        # DISPLAY USER MESSAGE IMMEDIATELY
        # ----------------------------------------------------

        with st.chat_message("user"):

            st.markdown(question)


        # ----------------------------------------------------
        # SAVE USER MESSAGE
        # ----------------------------------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )


        # ----------------------------------------------------
        # RUN AGENT
        # ----------------------------------------------------

        with st.chat_message("assistant"):

            with st.spinner(
                "Dow Jones Agent is thinking..."
            ):

                try:

                    response = agent.run(
                        user_id=user_id,
                        question=question
                    )


                    # --------------------------------------------
                    # FinalAnswer object
                    # --------------------------------------------

                    answer = response.answer

                    tools = response.tools_used

                    success = response.success


                    # --------------------------------------------
                    # Save agent information
                    # --------------------------------------------

                    st.session_state.last_tools = tools

                    st.session_state.last_success = success


                    # --------------------------------------------
                    # Display answer
                    # --------------------------------------------

                    st.markdown(answer)


                except Exception as e:

                    answer = (
                        "An error occurred while processing "
                        "your request.\n\n"
                        f"`{str(e)}`"
                    )


                    st.session_state.last_tools = []

                    st.session_state.last_success = False


                    st.error(answer)


        # ----------------------------------------------------
        # SAVE ASSISTANT MESSAGE
        # ----------------------------------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        # ----------------------------------------------------
        # REFRESH
        # ----------------------------------------------------

        st.rerun()


# ============================================================
# RIGHT PANEL
# ============================================================

with right:

    section_title(
        "Agent Activity"
    )


    # --------------------------------------------------------
    # PIPELINE
    # --------------------------------------------------------

    st.info(
        """
        **Agent Pipeline**

        🟢 User Question

        ↓

        🟢 Intent Detection

        ↓

        🟢 Tool Selection

        ↓

        🟢 Planning

        ↓

        🟢 Reasoning

        ↓

        🟢 Supervisor

        ↓

        🟢 Final Answer
        """
    )


    # --------------------------------------------------------
    # TOOLS USED
    # --------------------------------------------------------

    section_title(
        "Tools Used"
    )


    if st.session_state.last_tools:

        for tool in st.session_state.last_tools:

            st.write(
                f"🔹 {tool}"
            )

    else:

        st.caption(
            "No tools used yet."
        )


    # --------------------------------------------------------
    # SESSION
    # --------------------------------------------------------

    section_title(
        "Session"
    )


    if user_id:

        st.write(
            f"**User ID:** {user_id}"
        )

    else:

        st.write(
            "**User ID:** Not set"
        )


    st.write(
        f"**Messages:** "
        f"{len(st.session_state.messages)}"
    )


    st.write(
        "**Last activity:** "
        f"{datetime.now().strftime('%H:%M:%S')}"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Dow Jones AI Agent • "
    "RAG + Yahoo Finance + Tavily + FRED + GPT-OSS"
)