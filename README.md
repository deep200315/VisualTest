
# VisualTest AI

VisualTestAI is a tool designed to automate the generation of testing instructions for digital products based on screenshots. By utilizing a multimodal large language model (LLM), this tool analyzes uploaded images and provides detailed, structured testing instructions. It helps streamline the testing process by describing the functionality and potential test cases for various features visible in the screenshots. It also helps with additional queries about the testing.


## Features

- Multimodal Analysis: Utilizes advanced multimodal LLMs (such as GPT-4o, or similar) to analyze and interpret visual data from screenshots.
- Image Analysis : Analyzes screenshots to identify and understand user interface elements, functionality, and visual features.
- Testing Instruction Generation: Generates comprehensive testing instructions with sections for Description, Pre-conditions, Testing Steps, and Expected Results.
- User Interaction: Built using Streamlit for an interactive and user-friendly experience.Allows users to upload multiple images and view generated testing instructions alongside each image.
- Additional Queries: Includes a floating text box for users to ask additional questions about the testing process.


## Installation

1.Clone the repository:

Open your terminal or command line and run the following command:
 

```ruby
 git clone https://github.com/deep200315/VisualTest.git
```

2.Navigate to the Project Directory:
 ```ruby
cd VisualTest
```

3.Set Up a Virtual Environment (Optional but Recommended):
 
  Create a virtual environment to manage dependencies:
  ```ruby
  python -m venv venv
```
Activate the virtual environment:
```ruby
venv\Scripts\activate
```
4.Install Dependencies:
```ruby
pip install -r requirements.txt
```
5.Set up Environment Variables:
Here we are using streamlit for frontend so:
Create a
 ```ruby
.streamlit/secrets.toml
``` 
file in the project root directory.
Add necessary variables such as api keys for accessing LLMs which is OpenAI LLM we are  using.

6.Run the application
As we are using streamlit:
```bash
streamlit run main.py
```
## Screenshots
Dashboard of the LLM Application:

![Screenshot 2024-09-09 140557.png](https://github.com/deep200315/VisualTest/blob/main/test_photos/Screenshot%202024-09-09%20140557.png)

After uploaded image is processed the "Describe test instructions" button appears:

![Screenshot 2024-09-09 151353.png](https://github.com/deep200315/VisualTest/blob/main/test_photos/Screenshot%202024-09-09%20151353.png)

After pressing the button test instructions will be generated:

![Screenshot 2024-09-09 144624.png](https://github.com/deep200315/VisualTest/blob/main/test_photos/Screenshot%202024-09-09%20144624.png)

Additional Context or queries can be typed in the text box and result is generated:

![Screenshot 2024-09-09 144706.png](https://github.com/deep200315/VisualTest/blob/main/test_photos/Screenshot%202024-09-09%20144706.png)

    
