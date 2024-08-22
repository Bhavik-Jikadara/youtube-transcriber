from youtube_transcript_api import YouTubeTranscriptApi
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

class YoutubeVideoSummarizer:
    def __init__(self, video_url: str, api_key: str):
        self.url = video_url
        self.prompt = """
        You are an expert YouTube video summarizer. Your task is to take the provided transcript text and distill it into a concise, bullet-point summary that captures the key points and important insights of the video. The summary should be clear, easy to understand, and limited to 250 words. Please focus on highlighting the most critical information and main ideas, avoiding unnecessary details. The transcript text will be appended below.
        Based on the provided transcript, generate the summary:
        """
        self.api_key = genai.configure(api_key=api_key)
    
    def extract_transcript(self):
        try:
            video_id = self.url.split("=")[1]
            transcript_text = YouTubeTranscriptApi.get_transcript(
                video_id=video_id)
            
            transcript = ""
            for i in transcript_text:
                transcript += " " + i['text']
            
            return transcript
        
        except Exception as e:
            return e
        
    def generate_summary(self, transcript_text):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(self.prompt + transcript_text)
        return response.text