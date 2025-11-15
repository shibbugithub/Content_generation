# 🚀 AI Content Generation & Summarization Tool

A powerful web application that leverages Google Gemini AI to generate high-quality content and create intelligent summaries. Built with Flask backend and vanilla JavaScript frontend.

## ✨ Features

### Content Generation
- **Multiple Content Types**: Blog posts, emails, social media, product descriptions, articles, stories, and advertisements
- **Customizable Tone**: Professional, casual, friendly, formal, persuasive, informative
- **Variable Length**: Short, medium, and long-form content
- **Optimized Prompts**: Pre-engineered prompts specifically tuned for Gemini AI

### Text Summarization
- **Multiple Summary Types**: Brief, detailed, bullet points, academic abstract
- **Smart Compression**: Maintains key information while reducing length
- **Word Count Tracking**: Real-time word count display
- **Quality Metrics**: Shows original vs summary length and token usage

### User Experience
- **Clean Interface**: Modern, responsive design
- **Easy Export**: Copy to clipboard or download as text file
- **Real-time Feedback**: Loading indicators and success/error notifications
- **Tab Navigation**: Seamless switching between generation and summarization

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **LLM Integration**: Google Gemini API (gemini-1.5-flash)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with modern design principles

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key (FREE - Get from [Google AI Studio](https://makersuite.google.com/app/apikey))
- Modern web browser

## 🚀 Installation & Setup

### Step 1: Clone or Create Project Structure

```bash
# Create project directory
mkdir content-gen-summarizer
cd content-gen-summarizer

# Create folder structure
mkdir backend frontend
```

### Step 2: Set Up Backend

1. **Create virtual environment:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

2. **Install dependencies:**
```bash
cd backend
pip install flask flask-cors google-generativeai python-dotenv
```

3. **Create backend files:**
   - Save `app.py` in the `backend` folder
   - Save `prompts.py` in the `backend` folder
   - Create `requirements.txt`:

```txt
flask==3.0.0
flask-cors==4.0.0
google-generativeai==0.3.2
python-dotenv==1.0.0
```

4. **Get your FREE Gemini API key:**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy your API key

5. **Configure environment variables:**
```bash
# Create .env file in backend folder
touch .env  # On Windows: type nul > .env

# Add your Gemini API key to .env:
GEMINI_API_KEY=your-gemini-api-key-here
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
```

### Step 3: Set Up Frontend

1. **Create frontend files in the `frontend` folder:**
   - Save `index.html`
   - Save `styles.css`
   - Save `script.js`

2. **Update API URL (if needed):**
   - Open `script.js`
   - Modify `API_BASE_URL` if your backend runs on a different port

### Step 4: Run the Application

1. **Start the backend server:**
```bash
# Make sure you're in the backend folder with venv activated
cd backend
python app.py
```

You should see:
```
Initializing Gemini Content Generator...
Gemini API initialized successfully!
Ready to generate content!
* Running on http://127.0.0.1:5000
```

2. **Open the frontend:**
   - Open `frontend/index.html` in your web browser
   - Or use a local server:
   ```bash
   cd frontend
   # Python 3
   python -m http.server 8000
   # Then visit http://localhost:8000
   ```

## 📖 Usage Guide

### Generating Content

1. **Select Content Type**: Choose from blog post, email, social media, etc.
2. **Enter Topic**: Describe what you want to write about
3. **Choose Tone**: Select the appropriate writing style
4. **Select Length**: Pick short, medium, or long
5. **Click Generate**: Wait for Gemini AI to create your content
6. **Copy or Download**: Use the buttons to save your content

### Summarizing Text

1. **Paste Text**: Input text (minimum 50 words) into the text area
2. **Choose Summary Type**: Select brief, detailed, bullet points, or abstract
3. **Click Summarize**: Gemini AI will create your summary
4. **Review Stats**: Check original vs summary length
5. **Copy or Download**: Save your summary

## 🔧 Configuration Options

### Using Different Gemini Models

You can switch between different Gemini models in `app.py`:

```python
# In ContentGenerator.__init__():

# Fastest and most cost-effective (default)
self.model = genai.GenerativeModel('gemini-1.5-flash')

# More capable for complex tasks
self.model = genai.GenerativeModel('gemini-1.5-pro')

# Latest experimental model
self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
```

### Model Comparison

| Model | Speed | Quality | Free Tier Limit |
|-------|-------|---------|-----------------|
| gemini-1.5-flash | ⚡⚡⚡ | ⭐⭐⭐ | 15 RPM / 1M TPM |
| gemini-1.5-pro | ⚡⚡ | ⭐⭐⭐⭐ | 2 RPM / 32K TPM |
| gemini-2.0-flash-exp | ⚡⚡⚡ | ⭐⭐⭐⭐ | 10 RPM / 4M TPM |

*RPM = Requests Per Minute, TPM = Tokens Per Minute*

### Adjusting Generation Settings

Modify the generation parameters in `app.py`:

```python
# Add generation config to model
generation_config = {
    "temperature": 0.7,  # Creativity (0.0-1.0)
    "top_p": 0.9,        # Diversity (0.0-1.0)
    "top_k": 40,         # Token selection
    "max_output_tokens": 2048,
}

response = self.model.generate_content(
    prompt,
    generation_config=generation_config
)
```

### Customizing Prompts

Edit `prompts.py` to modify the prompt templates:

```python
# Example: Customize blog post prompt
"blog": f"""You are an expert content writer. Write a compelling blog post about: {topic}

[YOUR CUSTOM INSTRUCTIONS HERE]

Write the complete blog post now:"""
```

## 🎨 Customization

### Frontend Styling
Modify `styles.css` to change:
- Color scheme (update CSS variables in `:root`)
- Layout and spacing
- Typography
- Animations

### Backend API
Extend `app.py` to add:
- New endpoints
- Additional content types
- Custom processing logic
- Database integration

## 🔍 API Endpoints

### Generate Content
```http
POST /api/generate
Content-Type: application/json

{
  "content_type": "blog",
  "topic": "AI in Healthcare",
  "tone": "professional",
  "length": "medium"
}
```

**Response:**
```json
{
  "success": true,
  "content": "Generated content here...",
  "model": "gemini-1.5-flash",
  "tokens_used": 450
}
```

### Summarize Text
```http
POST /api/summarize
Content-Type: application/json

{
  "text": "Long text to summarize...",
  "summary_type": "brief"
}
```

**Response:**
```json
{
  "success": true,
  "summary": "Summary here...",
  "original_length": 500,
  "summary_length": 75,
  "model": "gemini-1.5-flash"
}
```

### Health Check
```http
GET /api/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "Content Gen & Summarization (Gemini)",
  "api_configured": true
}
```

### Get Content Types
```http
GET /api/content-types
```

## 🐛 Troubleshooting

### Common Issues

**1. CORS Errors**
- Ensure `flask-cors` is installed
- Check that CORS is enabled in `app.py`

**2. Gemini API Key Issues**
```bash
# Verify .env file exists and contains:
GEMINI_API_KEY=your-actual-key-here

# Test your API key:
python -c "import google.generativeai as genai; genai.configure(api_key='YOUR_KEY'); print('API Key Valid!')"
```

**3. Rate Limit Errors**
- Free tier: 15 requests/minute for gemini-1.5-flash
- Add delays between requests
- Implement retry logic with exponential backoff

**4. Module Not Found**
```bash
# Activate virtual environment first
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall requirements
pip install -r requirements.txt
```

**5. Port Already in Use**
```bash
# Change port in .env or app.py
# Kill process using the port:
# macOS/Linux:
lsof -ti:5000 | xargs kill
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**6. Frontend Can't Connect to Backend**
- Check backend is running: `http://localhost:5000/api/health`
- Update `API_BASE_URL` in `script.js`
- Check browser console for errors
- Verify CORS is enabled

**7. "API Key Not Found" Error**
```bash
# Make sure .env is in the same directory as app.py
# Check file is named .env (not .env.txt)
# Restart Flask after changing .env
```

## 🚀 Deployment

### Deploy Backend (Render/Railway)

**Render.com:**
```bash
# 1. Push code to GitHub
# 2. Connect Render to your repository
# 3. Add environment variable:
GEMINI_API_KEY=your-key

# 4. Set build command:
pip install -r requirements.txt

# 5. Set start command:
python app.py
```

**Railway.app:**
```bash
# 1. Install Railway CLI
# 2. Login and link project
railway login
railway init
railway link

# 3. Add environment variable
railway variables set GEMINI_API_KEY=your-key

# 4. Deploy
railway up
```

### Deploy Frontend (Netlify/Vercel)

1. Update `API_BASE_URL` in `script.js` to your backend URL:
```javascript
const API_BASE_URL = 'https://your-backend.onrender.com';
```

2. Deploy to Netlify:
   - Drag and drop `frontend` folder
   - Or connect GitHub repository

3. Deploy to Vercel:
```bash
npm i -g vercel
cd frontend
vercel
```

### Environment Variables for Production

```bash
# Backend .env for production
GEMINI_API_KEY=your-gemini-api-key
FLASK_ENV=production
FLASK_DEBUG=False
PORT=5000
```

## 💰 Cost & Limits

### Gemini API Pricing (as of 2024)

**Free Tier:**
- gemini-1.5-flash: 15 requests/minute, 1M tokens/minute
- gemini-1.5-pro: 2 requests/minute, 32K tokens/minute
- Perfect for development and small projects

**Paid Tier (Pay-as-you-go):**
- gemini-1.5-flash: $0.35 / 1M tokens (input), $1.05 / 1M tokens (output)
- gemini-1.5-pro: $3.50 / 1M tokens (input), $10.50 / 1M tokens (output)
- Much cheaper than OpenAI!

## 📈 Future Enhancements

- [ ] User authentication and saved content
- [ ] Multiple language support
- [ ] Content templates library
- [ ] SEO optimization suggestions
- [ ] Plagiarism detection
- [ ] Export to various formats (PDF, DOCX)
- [ ] Collaborative editing
- [ ] Content scheduling
- [ ] Analytics dashboard
- [ ] Image generation integration
- [ ] Voice input support

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Google Gemini AI for powerful language models
- Flask framework for robust backend
- Open source community

## 📚 Additional Resources

- [Gemini API Documentation](https://ai.google.dev/docs)
- [Get Free API Key](https://makersuite.google.com/app/apikey)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Prompt Engineering Guide](https://ai.google.dev/docs/prompt_best_practices)

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Check existing documentation
- Review troubleshooting section
- Visit [Google AI Forum](https://discuss.ai.google.dev/)

## ⚡ Quick Start Commands

```bash
# Clone and setup
git clone <your-repo>
cd content-gen-summarizer

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
echo "GEMINI_API_KEY=your-key-here" > .env
python app.py

# In new terminal - Frontend
cd frontend
python -m http.server 8000
# Visit http://localhost:8000
```

---

**Built with ❤️ using Google Gemini AI | Perfect for content creators and writers**

**🌟 Star this repo if you find it helpful!**