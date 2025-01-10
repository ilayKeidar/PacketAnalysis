from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

class AIAnalysisWindow(QDialog):
    def __init__(self, analysis_text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("AI Analysis")
        self.setMinimumSize(300, 250)
        self.setup_ui(analysis_text)

    def setup_ui(self, analysis_text):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(0)

        # Title
        title = QLabel("AI Analysis")
        title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        layout.addWidget(title)

        # Analysis text area
        text_label = QLabel(analysis_text)
        text_label.setFont(QFont("Arial", 11))
        text_label.setWordWrap(True)
        layout.addWidget(text_label)

        self.setLayout(layout)


def get_ai_analysis(analysis_data):
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        
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
            system_instruction="Analyze a 60-second network packet capture as if performing a high-level intelligence analysis task. Provide a concise, actionable summary of the user's most likely activities during the capture. Use the packet data to deduce specific actions such as web browsing, video streaming, online gaming, emailing, shopping, social media usage, or downloading files. Focus on reconstructing the overall context of the user's actions in clear, human-readable terms. Your summary should create a vivid and plausible narrative of what the user was doing during this time. Do not include technical details such as specific packet counts, protocol names, or DNS query results in your summary. Avoid explaining your deductions or providing evidence; simply state your conclusions. You may make reasonable assumptions to build a coherent picture of the user's activities, even if the data is ambiguous. The goal is to present an intelligent and actionable understanding of the user's likely behavior. At the end of the summary, add a sentence starting in \"Overall, \" and then give a high level summary of what the user was doing and its goal. For the dns queries, make sure to always ignore queries relating to google play store, ads, or tracking. "
        )

        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(analysis_data)
        
        return response.text
    except Exception as e:
        return f"Error generating AI analysis: {str(e)}"