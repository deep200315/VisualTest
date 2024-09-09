from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import streamlit as st
import openai


# Function to generate test instructions
def generate_test_instructions(description, context_text):
    # Define multiple examples for multi-shot prompt
    examples = [
        {
            "description": "A login screen with fields for username and password, and a submit button.",
            "test_instructions": """
            **Description**: Test the login functionality of the application.
            **Pre-conditions**:
            1. The application must be deployed and running.
            2. User accounts must exist with valid credentials.

            **Testing Steps**:
            1. Open the login screen.
            2. Enter a valid username and password.
            3. Click the submit button.
            4. Verify that the user is redirected to the dashboard screen.
            5. Test by entering invalid credentials and ensure an error message is displayed.

            **Expected Result**:
            - With valid credentials, the user should successfully log in and be redirected to the dashboard.
            - With invalid credentials, an error message should be displayed.
            """
        },
        {
            "description": "A dashboard screen showing user statistics in a graph and table format.",
            "test_instructions": """
            **Description**: Test the dashboard data visualization.
            **Pre-conditions**:
            1. The user must be logged in.
            2. The application must have pre-loaded user statistics data.

            **Testing Steps**:
            1. Navigate to the dashboard screen.
            2. Verify that the graph shows the correct data points for user statistics.
            3. Ensure that the table data matches the graph's data.
            4. Test the sorting and filtering functionality of the table.

            **Expected Result**:
            - The graph should correctly reflect the user's statistics.
            - The table should display matching data and respond correctly to sorting/filtering actions.
            """
        }
    ]

    # Multi-shot prompt with examples and new image description
    template = """
    Below are examples of test instructions for digital product screenshots:

    Example 1:
    Screenshot description: "{example1_description}"
    Test Instructions: {example1_test_instructions}

    Example 2:
    Screenshot description: "{example2_description}"
    Test Instructions: {example2_test_instructions}

    Now, given the following screenshot description:
    "{image_description}"

    {context_text}

    Generate a detailed set of functional testing instructions only for QA, including:
    - **Description**: What the test case is about.
    - **Pre-conditions**: What needs to be set up or ensured before testing.
    - **Testing Steps**: Clear, step-by-step instructions on how to perform the test.
    - **Expected Result**: What should happen if the feature works correctly.
    Strictly follow the above structure and do not include # or * in the output. There should be only
    one Description and Pre-conditions for the whole description. step by step training steps are needed.
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=["example1_description", "example1_test_instructions", "example2_description", "example2_test_instructions", "image_description", "context_text"]
    )

    # Fill in the examples and input
    prompt_inputs = {
        "example1_description": examples[0]["description"],
        "example1_test_instructions": examples[0]["test_instructions"],
        "example2_description": examples[1]["description"],
        "example2_test_instructions": examples[1]["test_instructions"],
        "image_description": description,
        "context_text": context_text or "There is no additional context provided."
    }

    # Set up the LLM chain
    llm_chain = LLMChain(prompt=prompt, llm=ChatOpenAI(model="gpt-4", openai_api_key=st.secrets["OPEN_AI_API_KEY"]))

    # Generate the test instructions
    test_instructions = llm_chain.run(prompt_inputs)

    return test_instructions

# Function to generate a response from LLM for a given context
import openai

from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key=st.secrets["OPEN_AI_API_KEY"]  # Fetch API key from environment variable
)

def get_llm_answer(question: str, supporting_text: str) -> str:
    # Combine the supporting text (test instructions) and the question (context text)
    prompt = f"Supporting Information: {supporting_text}\n\nQuestion: {question}\nAnswer:"

    try:
        # Call the OpenAI API to get the response
       client = OpenAI(api_key=st.secrets["OPEN_AI_API_KEY"])
       response = client.chat.completions.create(
          model="gpt-4o-mini",
          messages=[
             {"role": "system", "content": "You are a helpful assistant in functional testing"},
             {"role": "user", "content": prompt}
       ],
           temperature=0
)
       response_dict = response.model_dump()    # <--- convert to dictionary
       answer = response_dict["choices"][0]["message"]["content"]  
       return answer

    except Exception as e:
        return f"Error occurred: {str(e)}"
