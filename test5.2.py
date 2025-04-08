import streamlit as st
from google import generativeai as genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch

# Khởi tạo ứng dụng Streamlit
st.title("Google Gemini Chatbot")

# Lưu trữ lịch sử hội thoại
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lịch sử hội thoại
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Ô nhập truy vấn
query = st.chat_input("Nhập câu hỏi của bạn...")

# Xử lý truy vấn khi người dùng gửi
if query:
    # Hiển thị câu hỏi của người dùng trong lịch sử hội thoại
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    # Gửi yêu cầu đến API Gemini
    client = genai.Client(api_key="AIzaSyBBRBfkvzjngvok5MT6yqveb7hY6Gk8b7k")
    model_id = "gemini-2.0-flash"
    
    google_search_tool = Tool(


        google_search=GoogleSearch()
    )
    
    response = client.models.generate_content(
        model=model_id,
        contents=query,
        config=GenerateContentConfig(
            tools=[google_search_tool],
            response_modalities=["TEXT"],
        )
    )

    # Nhận phản hồi từ Gemini
    bot_reply = "\n".join([part.text for part in response.candidates[0].content.parts])

    # Hiển thị phản hồi của bot trong lịch sử hội thoại
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
#để chạy trên localhost , copy lệnh này vào terminal: python -m streamlit run test5.2.py

#AIzaSyAtTQhC6EX50GmcwkL8so5q0lswPwMojiM
