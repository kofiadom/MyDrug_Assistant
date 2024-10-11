from groq import Groq
from PIL import Image
import streamlit as st
import base64
import pdf2image
#Using the ColPali model
from byaldi import RAGMultiModalModel

api_key = ""

# Initialize RAGMultiModalModel
@st.cache_data(ttl=3600)
def load_model():
    return RAGMultiModalModel.from_pretrained("vidore/colqwen2-v0.1")

model = load_model()

def index_file(uploaded_file, query):
    # Use ColQwen2 to index and store the file
    index_name = "file_index"
    model.index(uploaded_file,
    index_name=index_name,
    store_collection_with_index=True, # Stores base64 images along with the vectors
    overwrite=True
    )

    returned_page = model.search(query, k=1)[0].base64
    return returned_page

def get_response(query, returned_page):
    client = Groq(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{returned_page}",
                        },
                    },
                ],
            }
        ],
        model="llama-3.2-11b-vision-preview",
    )
    return chat_completion.choices[0].message.content

st.title("Medical Instruction Chatbot")
st.write("This app assists you with understanding your medical instruction")

user_input = st.text_input("Enter your question: ")
uploaded_file = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        st.image(images[0], caption="Uploaded PDF", use_column_width=True)
    else:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)


if st.button("Submit"):
    if uploaded_file is not None:
        returned_page = index_file(uploaded_file, user_input)
        with st.spinner("Generating response..."):
            response = get_response(user_input, returned_page)
        st.success("Response Received!")
        st.write(response)
    else:
        st.error("Please upload an image!")
