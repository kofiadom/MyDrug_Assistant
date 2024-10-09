
# **Medical Instruction Chatbot**

## **Description**
The Medical Instruction Chatbot is a web-based RAG application designed to assist users in understanding their medical instructions. By leveraging natural language processing (NLP) and computer vision, the chatbot provides personalized responses to user queries. Users can upload images of their medical instructions and ask questions related to the uploaded content, receiving accurate and relevant answers.

## **Features**
- Upload medical instruction images in various formats (jpg, jpeg, png, pdf)
- Ask questions about the uploaded instructions
- Receive personalized, relevant answers from the chatbot
- Supports multiple file formats, including PDFs for versatile uploads

## **Installation**
The Medical Instruction Chatbot is a web-based platform, so no installation is required for users. To run the application locally, follow the instructions below.

### **Dependencies**
Ensure you have the following dependencies installed:
- Python 3.8 or later
- Streamlit
- Groq API key
- ColQwen2 model
- pdf2image library

### **How to Run Locally**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/kofiadom/MyDrug_Assistant
   ```
2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set your Groq API key**:
   Insert your api key in the app.py file

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```
5. **Access the application**:
   Open your browser and navigate to `http://localhost:8501`.

## **Usage Instructions**
1. **Upload an Image**: Upload your medical instruction by selecting a file (jpg, jpeg, png, or pdf) using the file uploader.
2. **Ask a Question**: Enter your question related to the uploaded instructions in the input field.
3. **Submit**: Click the "Submit" button to receive a personalized response from the chatbot.


## **Technical Details**
- Built using **Streamlit**, a Python framework for creating web applications
- Utilizes the **ColQwen2** model for efficient image indexing and search capabilities
- Leverages the **Groq API** to generate chatbot responses from Llama3.2
- Supports multiple file formats, including PDFs, with the **pdf2image** library

## **License**
This project is licensed under the MIT License. See the LICENSE file for more details.
