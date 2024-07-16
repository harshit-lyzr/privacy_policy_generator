# Privacy Policy Generator using Lyzr Automata and OpenAI

This application generates a privacy policy for a company using Lyzr Automata and OpenAI's GPT-4 Turbo model.

## Overview

The Privacy Policy Generator leverages Lyzr Automata, a powerful tool for generating text-based outputs using AI models. It prompts users to input details such as company name, type, state of operation, and website to craft a customized privacy policy.

### Features

- **Input Requirements:** Users need to provide company-specific details like name, type, state of operation, and website.
- **Integration with OpenAI:** Uses the GPT-4 Turbo model from OpenAI for generating text outputs.
- **Privacy Policy Crafting:** Automates the process of drafting a privacy policy tailored to the provided company details.

## Setup

### Prerequisites

- Python 3.x
- Streamlit
- Lyzr Automata
- OpenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your/repository.git
   cd repository-folder

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
### Running the Application
1. Set up your OpenAI API key:

- Enter your API key in the provided text input on the sidebar.

2. Launch the application:
    ```bash
   streamlit run app.py
   
3. Access the application:

- Open your web browser and navigate to http://localhost:8501 (default Streamlit port).

### Usage
1. Input Details:

Enter the company name, type, state of operation, and website in the respective fields.
2. Generate Privacy Policy:

Click on the "Generate" button to initiate the privacy policy generation process.
3. View Output:

The generated privacy policy will be displayed below the input fields.
### Additional Notes
Ensure your OpenAI API key is kept secure and not shared publicly.
Customize the application's appearance or functionality as per your requirements by modifying the Streamlit code.