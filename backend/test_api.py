"""
Test script to verify Gemini API connection
"""

import os
import google.generativeai as genai

# Try to load .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ .env file loaded")
except Exception as e:
    print(f"⚠️  Warning: Could not load .env file: {e}")

def test_connection():
    """Test if Gemini API is working"""
    
    print("\n🔍 Testing Gemini API Connection...\n")
    
    # Check if API key exists
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("❌ ERROR: GEMINI_API_KEY not found!")
        return False
    
    print(f"✅ API Key found: {api_key[:10]}...{api_key[-5:]}")
    
    try:
        # Configure Gemini
        genai.configure(api_key=api_key)
        
        # Try the models that are actually available
        model_names = [
            'gemini-2.5-flash',           # From your list
            'models/gemini-2.5-flash',    # With models/ prefix
            'gemini-2.5-pro',             # Pro version
            'models/gemini-2.5-pro',      # Pro with prefix
            'gemini-2.0-flash-exp',       # Experimental
            'models/gemini-2.0-flash-exp' # Experimental with prefix
        ]
        
        for model_name in model_names:
            try:
                print(f"\n🔄 Trying model: {model_name}")
                model = genai.GenerativeModel(model_name)
                
                # Test generation
                print("📝 Testing content generation...")
                response = model.generate_content("Write a short haiku about AI")
                
                print("\n✅ SUCCESS! API is working!\n")
                print(f"✨ Working model: {model_name}")
                print("Generated content:")
                print("-" * 50)
                print(response.text)
                print("-" * 50)
                print("\n🎉 Use this model name in your app.py!")
                
                return True
            except Exception as e:
                error_msg = str(e)
                if len(error_msg) > 100:
                    error_msg = error_msg[:100] + "..."
                print(f"❌ Failed: {error_msg}")
                continue
        
        print("\n❌ None of the models worked")
        print("💡 Try running with verbose error messages:")
        print("   Run this: python -c \"import google.generativeai as genai; genai.configure(api_key='YOUR_KEY'); m = genai.GenerativeModel('gemini-2.5-flash'); print(m.generate_content('test').text)\"")
        return False
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_connection()
    if not success:
        print("\n🔧 Troubleshooting Steps:")
        print("1. Verify API key is correct")
        print("2. Check internet connection")
        print("3. Try generating a new API key at: https://makersuite.google.com/app/apikey")
        print("4. Check API quota at: https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com")