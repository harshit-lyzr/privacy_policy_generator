import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
from lyzr_automata.tasks.task_literals import InputType, OutputType
import base64

st.set_page_config(
    page_title="Privacy Policy Generator",
    layout="wide",
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

api = st.sidebar.text_input("Enter Your OPENAI API KEY HERE", type="password")

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    .stApp  {
background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)), url("https://img.etimg.com/thumb/width-1600,height-900,imgsize-21086,resizemode-75,msid-102748711/news/how-to/how-to-safeguard-privacy-in-the-era-of-personalised-ads.jpg");
background-size: cover;
}
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Privacy Policy Generator")
st.markdown("## Welcome to the Privacy Policy Generator!")
st.markdown(
    "This App Harnesses power of Lyzr Automata to Generate Privacy Policy. You Need to input Your topic and it will craft mindmap")


if api:
    openai_model = OpenAIModel(
        api_key=api,
        parameters={
            "model": "gpt-4-turbo-preview",
            "temperature": 0.2,
            "max_tokens": 1500,
        },
    )
else:
    st.sidebar.error("Please Enter Your OPENAI API KEY")


def privacy_policy_generator(name, company_type, operation, website):
    policy_agent = Agent(
        prompt_persona=f"You are an Expert in Privacy policy crafting.",
        role="Privacy Policy Expert",
    )

    policy_task = Task(
        name="Privacy Policy",
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=openai_model,
        agent=policy_agent,
        log_output=True,
        instructions=f"""
        Draft a privacy policy for a {company_type} company called {name} that operates in the state of {operation}. 
        The company website is {website} .
        """,
    )

    output = LinearSyncPipeline(
        name="Privacy Policy Generation",
        completion_message="Privacy Policy Generated!",
        tasks=[
            policy_task
        ],
        ).run()
    return output[0]['task_output']


company_name = st.text_input("Enter Company Name")
company_type = st.text_input("Enter Company Type")
state_of_operation = st.text_input("Enter Company's State of Operation")
website = st.text_input("Enter Company Website")

if st.button("Generate"):
    solution = privacy_policy_generator(company_name,company_type,state_of_operation,website)
    st.markdown(solution)

