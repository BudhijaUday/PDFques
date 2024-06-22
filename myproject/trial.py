import fitz
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    extracted_text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        extracted_text += page.get_text()
    return extracted_text

# Your Azure OpenAI API configuration
OPENAI_API_TYPE = "azure"
OPENAI_API_VERSION = "2023-07-01-preview"
OPENAI_API_BASE = "https://genai-stg-westus3-1.openai.azure.com/"
OPENAI_API_KEY = "open_ai_ki"
DEPLOYMENT_NAME = "gpt-4-turbo-2024-04-09-managed"

# Initialize AzureChatOpenAI
llm = AzureChatOpenAI(
    api_key=OPENAI_API_KEY,
    api_version=OPENAI_API_VERSION,
    base_url=OPENAI_API_BASE,
    deployment_name=DEPLOYMENT_NAME,
    model_name="gpt-4-turbo",
    temperature=0  # Set to 0 for precise answers
)

# Extract text from PDF
pdf_path = "C:\\Users\\udayb\\OneDrive\\Desktop\\llmk\\myproject\\FAANGPath_Simple_Template__2_ (1).pdf"
text = extract_text_from_pdf(pdf_path)

# Prepare the prompt
user_ques = "what is my area of expertise?"
prompt = f'You have this text: "{text}". Use this as your reference and answer the following question: "{user_ques}". Answer should be a string.'

# Parse prompt as a HumanMessage
msg = HumanMessage(content=prompt)

# Get response from the model
response = llm([msg])

# Print the response
print(response)
print(response[0].content)
