import os
try:
    import google.generativeai as genai  # type: ignore
except ImportError:
    genai = None

# Configure Gemini API
# Get API key from environment variable for security
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyDW8BCT1fSUKpzOWsHS6_vhY4lOWFQ8eHg")


if not GEMINI_API_KEY:
    print("⚠️ Warning: GEMINI_API_KEY not found in environment variables.")
    print("Please set it using: export GEMINI_API_KEY='your-api-key' (Linux/Mac)")
    print("Or: set GEMINI_API_KEY=your-api-key (Windows)")

def generate_summary(text):
    """
    Generate a summary of the provided text using Google's Gemini API.
    
    Args:
        text (str): The transcript text to summarize
        
    Returns:
        str: The generated summary or an error message
    """
    try:
        if not text or text.strip() == "":
            return "No text available for summarization."
        
        if not GEMINI_API_KEY:
            return "❌ Error: GEMINI_API_KEY not configured. Please set your API key."
        
        if genai is None:
            return "❌ Error: google-generativeai package not installed."

        # Create a prompt for summarization
        prompt = f"""Please provide a concise and comprehensive summary of the following podcast transcript. 
Focus on the main topics discussed, key points, and important insights. 
Keep the summary clear and well-structured.

Transcript:
{text}

Summary:"""

        # Configure and use the Google GenAI SDK
        genai.configure(api_key=GEMINI_API_KEY)  # type: ignore
        model = genai.GenerativeModel("gemini-2.0-flash")  # type: ignore
        response = model.generate_content(prompt)
        if response and hasattr(response, 'text') and response.text:
            return response.text.strip()
        elif isinstance(response, str):
            return response.strip()
        else:
            return "❌ Error: No summary generated from Gemini API."
            
    except Exception as e:
        return f"❌ Error generating summary with Gemini: {str(e)}"
