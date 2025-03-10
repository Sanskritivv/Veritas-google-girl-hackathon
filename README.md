# Veritas : on-the-go tax assistant 
## Summary
The proposed project is a tax assistant which operates as an agentic retrieval-augmented generation (RAG)
system that will help users with tax computations, receipt management, and invoice processing using optical
character recognition (OCR) . Users can communicate with the system through the chat interface, upload receipts
for them to extract OCR based data, set up reminders for tax payments that sync with Google Calendar, and prompt
users to perform tax related tasks. Structured data is stored in Airtable and intelligent tax related help is provided by
the system using a Large Language Model (LLM) [Google Gemini].

<br>

## Solution Approach

This project employs an integrated, agentic Retrieval-Augmented Generation (RAG) framework to streamline tax management through advanced AI and automation. The key features include:

- OCR Invoice Processing:
    The system utilizes an OCR reader to extract text from invoices and receipts. Extracted data is parsed and automatically saved into Airtable, ensuring that records are organized and easily accessible.

- Dual-Mode Tax Calculator:
    Users can benefit from a tax calculator that accepts both manually entered data and information derived from OCR. This dual approach allows for flexibility and accuracy, enabling users to validate and adjust the automatically extracted data as needed.

- Agentic RAG Framework:
    Operating as an agentic RAG system, the solution dynamically retrieves and processes relevant tax regulations, financial data, and contextual information. This ensures that the responses and recommendations are accurate, up-to-date, and tailored to user queries.

- Google Calendar Reminders:
    To promote timely tax compliance, the system integrates with Google Calendar. It automatically schedules reminders for upcoming tax deadlines and important dates, helping users manage their tax obligations effectively.

- Google Gemini LLM Integration:
    Google Gemini, a state-of-the-art Large Language Model, powers the system’s natural language processing capabilities. It interprets user queries, provides contextual tax advice, and enhances overall user interaction, 
    ensuring a seamless and intelligent support experience.

#### Blueprint

![image alt](https://github.com/Sanskritivv/Veritas-google-girl-hackathon/blob/main/images/blueprint.png?raw=true) 
  
<br>

## Results 

#### n8n format of AI agent 
![image alt](https://github.com/Sanskritivv/Veritas-google-girl-hackathon/blob/main/images/n8n.jpg?raw=true)

<br> 

#### ocr reader

![image alt](https://github.com/Sanskritivv/Veritas-google-girl-hackathon/blob/main/images/ocr.jpg?raw=true)

<br>

#### tax calculator 

![image alt](https://github.com/Sanskritivv/Veritas-google-girl-hackathon/blob/main/images/cal.jpg?raw=true)

<br>

#### tax calculator (manual)

![image alt](https://github.com/Sanskritivv/Veritas-google-girl-hackathon/blob/main/images/cal_manual.jpg?raw=true)

<br> 

## How to run on your system: 

#### Clone the Repository:
Open your terminal and run:
`` git clone <repository_url>``

#### Install Dependencies:
Navigate into the project directory and install the necessary dependencies mentioned in requirements.txt

#### Set Up Your Environment:
Configure your environment by setting the necessary environment variables. This may involve creating a .env file and adding your API keys and other configuration parameters.
and copy the n8n workflow [https://stella09.app.n8n.cloud/workflow/3l5OacJiuISTEI4Y] 

#### Obtain API Keys:
Ensure you have the required API keys for integrations (e.g., Google Calendar, Airtable, Google Gemini). Add these keys to your environment configuration.

#### Run the Streamlit App:
Once everything is configured, launch the Streamlit application with:
`` streamlit run app.py ``

<br> 

## Acknowledgments
I would like to express my gratitude to the open-source community and the developers behind the tools and libraries that made this individual project possible. 
Your dedication and innovation have been a constant source of inspiration throughout this endeavor.









