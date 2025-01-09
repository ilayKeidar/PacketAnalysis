import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="Analyze a 60-second network packet capture as though conducting an Army Intelligence task. Provide a precise, intelligent summary of the user's most likely activities based on the data provided, including total packets captured, data sent and received, active protocols, transport counts, and DNS queries. Focus on deducing specific actions, such as browsing, streaming, emailing, or shopping, without generalizations or unnecessary technical details. Your one-paragraph summary should directly state the user's overall activities based on the evidence, with a focus on actionable intelligence. Do not explain your decisions, what you think the user did based on the information is what you're going to provide, no need to give the reason/example to prove your assumption. You are allowed to make some assumptions, even if you're not entirely sure it is correct. Try to build the full \"image\" behind this packet capturing. ",
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)