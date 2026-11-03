import streamlit as st

st.set_page_config(page_title="Facts-Only MF Assistant", page_icon="📈")

st.title("Facts-Only Mutual Fund Assistant")
st.caption(
    "Answers factual questions about selected SBI Mutual Fund schemes "
    "using official pages only."
)

st.info(
    "**Welcome to Facts-Only MF Assistant!**\n\n"
    "Ask factual questions about selected schemes "
    "(e.g., minimum SIP, exit load, lock-in period)."
)

# ---------------------------------------------------------------
# Example questions. Buttons write into session_state so the text
# box keeps the question after Streamlit reruns the script.
# ---------------------------------------------------------------
EXAMPLES = {
    "SBI ELSS Lock-in?": "What is the mandatory lock-in period for SBI Long Term Equity Fund?",
    "SBI Flexicap Min SIP?": "What is the minimum SIP amount for SBI Flexicap Fund?",
    "Download Capital Gains?": "How can I download my Capital Gains statement?",
}

if "query" not in st.session_state:
    st.session_state["query"] = ""


def set_query(text: str) -> None:
    st.session_state["query"] = text


st.write("**Example Questions:**")
cols = st.columns(len(EXAMPLES))
for col, (label, question) in zip(cols, EXAMPLES.items()):
    col.button(label, on_click=set_query, args=(question,))

st.text_input("Ask your question here:", key="query")

st.markdown(
    "<small style='color: gray;'>Facts-only. No investment advice.</small>",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------
# TODO (your part of the milestone): replace this function.
#
# It should:
#   1. Decide: is this a factual question, or advice/returns/PII?
#   2. If factual: retrieve the best chunk from your corpus and
#      write an answer of 3 sentences or fewer, with ONE source link
#      and "Last updated from sources: <date>".
#   3. If advice/returns: refuse politely with ONE educational link.
#   4. If the facts are not in your corpus: say so, don't guess.
#
# Return a dict: {"answer": str, "source": str, "updated": str}
# ---------------------------------------------------------------
def answer_question(query: str) -> dict:
    raise NotImplementedError("Retrieval and refusal logic not built yet.")


query = st.session_state["query"].strip()
if query:
    try:
        result = answer_question(query)
        st.write(result["answer"])
        st.markdown(f"**Source:** {result['source']}")
        st.caption(f"Last updated from sources: {result['updated']}")
    except NotImplementedError:
        st.warning("Answer logic is not built yet. The UI is ready.")

with st.sidebar:
    st.header("Disclaimer")
    try:
        with open("disclaimer.txt", "r", encoding="utf-8") as f:
            st.write(f.read())
    except FileNotFoundError:
        st.write("Facts-only. No investment advice.")
