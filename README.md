# 🚀 AI Content Generation & Summarization Tool

A powerful web application that leverages Google Gemini AI to generate high-quality content and create intelligent summaries. Perfect for content creators, writers, marketers, and students.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange.svg)

---

## 📸 Screenshots

### Main Interface
![Main Interface](screenshots/main-interface.png)
*Content generation interface with multiple options*

### Content Generation
![Content Generation](screenshots/content-generation.png)
*Generate blog posts, emails, social media content, and more*

### Text Summarization
![Text Summarization](screenshots/text-summarization.png)
*Intelligent text summarization with multiple formats*

### Generated Output
![Generated Output](screenshots/output-example.png)
*High-quality AI-generated content with copy and download options*

---

## ✨ Features

### 🎯 Content Generation
- **7 Content Types**: Blog posts, emails, social media posts, product descriptions, articles, stories, and advertisements
- **6 Tone Options**: Professional, casual, friendly, formal, persuasive, informative
- **3 Length Options**: Short (150-200 words), Medium (400-500 words), Long (800-1000 words)
- **Smart Prompts**: Pre-engineered prompts optimized for each content type

### 📝 Text Summarization
- **4 Summary Types**: 
  - Brief (2-3 sentences)
  - Detailed (comprehensive summary)
  - Bullet points (key highlights)
  - Academic abstract
- **Word Count Tracking**: Real-time word count display
- **Compression Stats**: Shows original vs summary length

### 🎨 User Experience
- **Modern UI**: Clean, responsive design with gradient backgrounds
- **Easy Export**: Copy to clipboard or download as text file
- **Real-time Feedback**: Loading indicators and toast notifications
- **Tab Navigation**: Seamless switching between generation and summarization
- **Mobile Responsive**: Works on all devices

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Flask (Python) |
| **AI Model** | Google Gemini Pro (FREE) |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **API** | RESTful Architecture |
| **Styling** | Custom CSS with modern design |

---

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key (FREE)
- Modern web browser

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-content-generator.git
cd ai-content-generator
```

### 2. Set Up Backend

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Key

Get your FREE Gemini API key from: https://aistudio.google.com/app/apikey

Create a `.env` file in the `backend` folder:

```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the Application

```bash
# Start backend server
python app.py

# Server will start at http://localhost:5000
```

### 5. Open Frontend

Open `frontend/index.html` in your web browser, or use a local server:

```bash
# Navigate to frontend folder
cd ../frontend

# Start local server (Python 3)
python -m http.server 8000

# Visit http://localhost:8000
```

---

## 📁 Project Structure

```
ai-content-generator/
│
├── backend/
│   ├── venv/                 # Virtual environment
│   ├── app.py                # Main Flask application
│   ├── prompts.py            # Prompt engineering templates
│   ├── requirements.txt      # Python dependencies
│   └── .env                  # API key configuration
│
├── frontend/
│   ├── index.html            # Main HTML page
│   ├── styles.css            # CSS styling
│   └── script.js             # JavaScript logic
│
├── screenshots/              # Application screenshots
│   ├── main-interface.png
│   ├── content-generation.png
│   ├── text-summarization.png
│   └── output-example.png
│
├── README.md                 # This file
└── LICENSE                   # MIT License
```

---

## 📖 Usage Guide

### Generating Content

1. **Select Content Type**: Choose from blog post, email, social media, etc.
2. **Enter Topic**: Describe what you want to write about
3. **Choose Tone**: Select the appropriate writing style
4. **Select Length**: Pick short, medium, or long format
5. **Generate**: Click the "Generate Content" button
6. **Copy/Download**: Use the buttons to save your content

### Summarizing Text

1. **Paste Text**: Input your text (minimum 50 words)
2. **Choose Summary Type**: Select brief, detailed, bullet points, or abstract
3. **Summarize**: Click the "Summarize Text" button
4. **Review**: Check the summary and statistics
5. **Copy/Download**: Save your summary

---

## 🔧 Configuration

### Backend Configuration

Edit `backend/app.py` to customize:

```python
# Change server port
app.run(debug=True, port=5000)

# Switch AI model
model = genai.GenerativeModel('gemini-pro')
```

### Frontend Configuration

Edit `frontend/script.js` to customize:

```javascript
// Change API endpoint
const API_BASE_URL = 'http://localhost:5000/api';

// Customize UI behavior
```

### Prompt Customization

Edit `backend/prompts.py` to modify prompt templates for different content types.

---

## 🌐 API Documentation

### Endpoints

#### Health Check
```http
GET /api/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "Content Gen & Summarization",
  "provider": "Google Gemini",
  "api_configured": true
}
```

#### Generate Content
```http
POST /api/generate
Content-Type: application/json
```

**Request Body:**
```json
{
  "content_type": "blog",
  "topic": "Benefits of AI in Education",
  "tone": "professional",
  "length": "medium"
}
```

**Response:**
```json
{
  "success": true,
  "content": "Generated content here...",
  "tokens_used": "N/A (Gemini API)"
}
```

#### Summarize Text
```http
POST /api/summarize
Content-Type: application/json
```

**Request Body:**
```json
{
  "text": "Long text to summarize...",
  "summary_type": "brief"
}
```

**Response:**
```json
{
  "success": true,
  "summary": "Summary text here...",
  "original_length": 150,
  "summary_length": 30,
  "tokens_used": "N/A (Gemini API)"
}
```

#### Get Content Types
```http
GET /api/content-types
```

**Response:**
```json
{
  "content_types": [...],
  "tones": [...],
  "lengths": [...],
  "summary_types": [...]
}
```

---

## 🎨 Customization

### Changing Colors

Edit `frontend/styles.css`:

```css
:root {
    --primary: #6366f1;      /* Primary color */
    --success: #10b981;      /* Success messages */
    --danger: #ef4444;       /* Error messages */
    /* Customize other colors */
}
```

### Adding New Content Types

1. Edit `backend/prompts.py`:
```python
prompts = {
    "your_new_type": f"Your custom prompt for {topic}..."
}
```

2. Update `frontend/index.html`:
```html
<option value="your_new_type">Your New Type</option>
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "API key not configured"**
- Solution: Check `.env` file exists in `backend` folder
- Verify API key format: `GEMINI_API_KEY=AIza...`
- Restart the server

**Issue: "Module not found"**
- Solution: Activate virtual environment and reinstall dependencies
```bash
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
```

**Issue: "Cannot connect to API"**
- Solution: Ensure backend server is running
- Check backend terminal for errors
- Verify `API_BASE_URL` in `script.js`

**Issue: CORS errors**
- Solution: Already handled in code with `flask-cors`
- If persists, reinstall: `pip install --upgrade flask-cors`

---

## 💰 Cost Information

This project uses **Google Gemini API** which is:
- ✅ **100% FREE** for personal use
- ✅ No credit card required
- ✅ Generous rate limits (60 requests/minute)

Perfect for:
- Learning and experimentation
- Personal projects
- Small to medium applications

---

## 🚀 Deployment

### Deploy Backend (Heroku)

```bash
# Install Heroku CLI and login
heroku login

# Create new app
heroku create your-app-name

# Set environment variable
heroku config:set GEMINI_API_KEY=your-key

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### Deploy Frontend (Netlify)

1. Update `API_BASE_URL` in `script.js` to your backend URL
2. Drag and drop `frontend` folder to [Netlify](https://app.netlify.com/)
3. Deploy!

### Deploy Frontend (GitHub Pages)

```bash
# Update API_BASE_URL in script.js
# Push to GitHub
git add .
git commit -m "Deploy to GitHub Pages"
git push origin main

# Enable GitHub Pages in repository settings
# Select branch: main, folder: /frontend
```

---

## 📈 Future Enhancements

- [ ] User authentication and saved content
- [ ] Content history and version control
- [ ] Multiple language support
- [ ] SEO optimization suggestions
- [ ] Plagiarism detection
- [ ] Export to PDF, DOCX formats
- [ ] Collaborative editing
- [ ] Content scheduling
- [ ] Analytics dashboard
- [ ] AI image generation integration
- [ ] Voice input support
- [ ] Browser extension

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Use meaningful commit messages
- Update documentation for new features
- Add tests for new functionality
- Ensure all tests pass before submitting PR

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- [Google Gemini](https://ai.google.dev/) for providing the FREE AI API
- [Flask](https://flask.palletsprojects.com/) for the excellent web framework
- [OpenAI](https://openai.com/) for inspiration in prompt engineering
- All contributors who help improve this project

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search existing [Issues](https://github.com/yourusername/ai-content-generator/issues)
3. Create a new [Issue](https://github.com/yourusername/ai-content-generator/issues/new) with:
   - Detailed description
   - Steps to reproduce
   - Error messages
   - Screenshots (if applicable)

---

## ⭐ Star History

If you find this project helpful, please consider giving it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/ai-content-generator&type=Date)](https://star-history.com/#yourusername/ai-content-generator&Date)

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/ai-content-generator?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/ai-content-generator?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/yourusername/ai-content-generator?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/ai-content-generator)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/ai-content-generator)

---

<div align="center">

### Made with ❤️ by developers, for developers

**[⬆ Back to Top](#-ai-content-generation--summarization-tool)**

</div>
