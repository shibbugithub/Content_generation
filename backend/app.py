"""
Content Generation & Summarization API using Google Gemini
Requires: pip install flask flask-cors google-generativeai
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
from prompts import get_prompt_template

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

class ContentGenerator:
    """Handle content generation using Google Gemini API"""
    
    def __init__(self, api_key=None):
        # Get API key from environment variable or parameter
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found. Please set it as environment variable or pass it to constructor.")
        
        # Configure Gemini
        genai.configure(api_key=self.api_key)
        
        # Initialize the model - Use Gemini 2.5 Flash (latest available)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        print("Gemini API initialized successfully!")
    
    def generate_content(self, content_type, topic, tone="professional", length="medium"):
        """Generate content using Gemini API"""
        
        prompt = get_prompt_template(content_type, topic, tone, length)
        
        try:
            # Generate content
            response = self.model.generate_content(prompt)
            
            generated_text = response.text
            
            # Count tokens (approximate)
            token_count = len(generated_text.split())
            
            return {
                "success": True,
                "content": generated_text,
                "model": "gemini-2.5-flash",
                "tokens_used": token_count
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def summarize_content(self, text, summary_type="brief", ratio=0.3):
        """Summarize text using Gemini API"""
        
        try:
            # Create summary prompt based on type
            summary_prompts = {
                "brief": f"Provide a brief summary of the following text in 2-3 sentences:\n\n{text}",
                "detailed": f"Provide a detailed summary of the following text, covering all main points:\n\n{text}",
                "bullet": f"Summarize the following text in bullet points (use • symbol):\n\n{text}",
                "abstract": f"Write an abstract summarizing the following text:\n\n{text}"
            }
            
            prompt = summary_prompts.get(summary_type, summary_prompts["brief"])
            
            # Generate summary
            response = self.model.generate_content(prompt)
            summary = response.text
            
            return {
                "success": True,
                "summary": summary,
                "original_length": len(text.split()),
                "summary_length": len(summary.split()),
                "model": "gemini-2.5-flash"
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


# Initialize generator with API key
print("Initializing Gemini Content Generator...")
try:
    generator = ContentGenerator()
    print("Ready to generate content!")
except ValueError as e:
    print(f"ERROR: {e}")
    print("Please set GEMINI_API_KEY environment variable before running.")
    generator = None

@app.route('/')
def home():
    return jsonify({
        "message": "Content Generation & Summarization API (Google Gemini)",
        "version": "2.0 - Gemini Edition",
        "model": "gemini-2.5-flash",
        "endpoints": {
            "/api/generate": "POST - Generate content",
            "/api/summarize": "POST - Summarize text",
            "/api/content-types": "GET - Get available content types",
            "/api/health": "GET - Health check"
        },
        "note": "Requires GEMINI_API_KEY environment variable"
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy" if generator else "error",
        "service": "Content Gen & Summarization (Gemini)",
        "api_configured": generator is not None
    })

@app.route('/api/generate', methods=['POST'])
def generate_content():
    """Generate content endpoint"""
    if not generator:
        return jsonify({
            "success": False,
            "error": "Gemini API not configured. Please set GEMINI_API_KEY."
        }), 500
    
    try:
        data = request.get_json()
        
        if not data.get('content_type') or not data.get('topic'):
            return jsonify({
                "success": False,
                "error": "Missing required fields: content_type and topic"
            }), 400
        
        content_type = data.get('content_type')
        topic = data.get('topic')
        tone = data.get('tone', 'professional')
        length = data.get('length', 'medium')
        
        result = generator.generate_content(content_type, topic, tone, length)
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify(result), 500
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500

@app.route('/api/summarize', methods=['POST'])
def summarize_content():
    """Summarize content endpoint"""
    if not generator:
        return jsonify({
            "success": False,
            "error": "Gemini API not configured. Please set GEMINI_API_KEY."
        }), 500
    
    try:
        data = request.get_json()
        
        if not data.get('text'):
            return jsonify({
                "success": False,
                "error": "Missing required field: text"
            }), 400
        
        text = data.get('text')
        summary_type = data.get('summary_type', 'brief')
        ratio = data.get('ratio', 0.3)
        
        if len(text.split()) < 50:
            return jsonify({
                "success": False,
                "error": "Text too short. Please provide at least 50 words."
            }), 400
        
        result = generator.summarize_content(text, summary_type, ratio)
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify(result), 500
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500

@app.route('/api/content-types', methods=['GET'])
def get_content_types():
    """Return available content types"""
    return jsonify({
        "content_types": [
            {"id": "blog", "name": "Blog Post"},
            {"id": "email", "name": "Email"},
            {"id": "social", "name": "Social Media"},
            {"id": "product", "name": "Product Description"},
            {"id": "article", "name": "Article"},
            {"id": "story", "name": "Story"},
            {"id": "ad", "name": "Advertisement"}
        ],
        "tones": ["professional", "casual", "friendly", "formal", "persuasive", "informative"],
        "lengths": ["short", "medium", "long"],
        "summary_types": ["brief", "detailed", "bullet", "abstract"],
        "note": "Powered by Google Gemini API (gemini-2.5-flash)"
    })

if __name__ == '__main__':
    # You can set the API key here for testing (not recommended for production)
    # os.environ['GEMINI_API_KEY'] = 'your-api-key-here'
    
    app.run(debug=True, port=5000, host='0.0.0.0')