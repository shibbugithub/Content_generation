// ==================== Configuration ====================
const API_BASE_URL = 'http://localhost:5000/api';

// ==================== DOM Elements ====================
const tabBtns = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');
const generateForm = document.getElementById('generateForm');
const summarizeForm = document.getElementById('summarizeForm');
const inputText = document.getElementById('inputText');
const wordCountSpan = document.getElementById('wordCount');
const toast = document.getElementById('toast');

// ==================== Initialize ====================
document.addEventListener('DOMContentLoaded', () => {
    setupTabs();
    setupForms();
    setupWordCount();
    checkAPIHealth();
});

// ==================== Tab Switching ====================
function setupTabs() {
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.dataset.tab;
            
            // Update active states
            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            btn.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });
}

// ==================== Form Handlers ====================
function setupForms() {
    // Generate Content Form
    generateForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        await handleGenerate();
    });

    // Summarize Form
    summarizeForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        await handleSummarize();
    });

    // Copy buttons
    document.getElementById('copyGenerated').addEventListener('click', () => {
        copyToClipboard('generatedContent');
    });

    document.getElementById('copySummary').addEventListener('click', () => {
        copyToClipboard('summaryContent');
    });

    // Download buttons
    document.getElementById('downloadGenerated').addEventListener('click', () => {
        downloadText('generatedContent', 'generated-content.txt');
    });

    document.getElementById('downloadSummary').addEventListener('click', () => {
        downloadText('summaryContent', 'summary.txt');
    });
}

// ==================== Word Count ====================
function setupWordCount() {
    inputText.addEventListener('input', () => {
        const text = inputText.value.trim();
        const words = text ? text.split(/\s+/).length : 0;
        wordCountSpan.textContent = `${words} words`;
        
        if (words > 0 && words < 50) {
            wordCountSpan.style.color = 'var(--warning)';
        } else {
            wordCountSpan.style.color = 'var(--gray)';
        }
    });
}

// ==================== Handle Content Generation ====================
async function handleGenerate() {
    const contentType = document.getElementById('contentType').value;
    const topic = document.getElementById('topic').value;
    const tone = document.getElementById('tone').value;
    const length = document.getElementById('length').value;

    const btn = document.getElementById('generateBtn');
    const btnText = btn.querySelector('.btn-text');
    const loader = btn.querySelector('.loader');

    try {
        // Show loading state
        btn.disabled = true;
        btnText.textContent = 'Generating...';
        loader.style.display = 'block';

        const response = await fetch(`${API_BASE_URL}/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                content_type: contentType,
                topic: topic,
                tone: tone,
                length: length
            })
        });

        const data = await response.json();

        if (data.success) {
            // Display generated content
            document.getElementById('generatedContent').textContent = data.content;
            document.getElementById('genTokens').textContent = `📊 Tokens used: ${data.tokens_used}`;
            document.getElementById('generateOutput').style.display = 'block';
            
            // Scroll to output
            document.getElementById('generateOutput').scrollIntoView({ 
                behavior: 'smooth', 
                block: 'nearest' 
            });
            
            showToast('Content generated successfully!', 'success');
        } else {
            showToast(`Error: ${data.error}`, 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showToast('Failed to generate content. Please check your API configuration.', 'error');
    } finally {
        // Reset button state
        btn.disabled = false;
        btnText.textContent = 'Generate Content';
        loader.style.display = 'none';
    }
}

// ==================== Handle Summarization ====================
async function handleSummarize() {
    const text = inputText.value.trim();
    const summaryType = document.getElementById('summaryType').value;

    // Validate word count
    const wordCount = text.split(/\s+/).length;
    if (wordCount < 50) {
        showToast('Text must be at least 50 words long', 'error');
        return;
    }

    const btn = document.getElementById('summarizeBtn');
    const btnText = btn.querySelector('.btn-text');
    const loader = btn.querySelector('.loader');

    try {
        // Show loading state
        btn.disabled = true;
        btnText.textContent = 'Summarizing...';
        loader.style.display = 'block';

        const response = await fetch(`${API_BASE_URL}/summarize`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                summary_type: summaryType
            })
        });

        const data = await response.json();

        if (data.success) {
            // Display summary
            document.getElementById('summaryContent').textContent = data.summary;
            document.getElementById('originalLength').textContent = `📄 Original: ${data.original_length} words`;
            document.getElementById('summaryLength').textContent = `📝 Summary: ${data.summary_length} words`;
            document.getElementById('sumTokens').textContent = `📊 Tokens used: ${data.tokens_used}`;
            document.getElementById('summarizeOutput').style.display = 'block';
            
            // Scroll to output
            document.getElementById('summarizeOutput').scrollIntoView({ 
                behavior: 'smooth', 
                block: 'nearest' 
            });
            
            showToast('Text summarized successfully!', 'success');
        } else {
            showToast(`Error: ${data.error}`, 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showToast('Failed to summarize text. Please check your API configuration.', 'error');
    } finally {
        // Reset button state
        btn.disabled = false;
        btnText.textContent = 'Summarize Text';
        loader.style.display = 'none';
    }
}

// ==================== Copy to Clipboard ====================
function copyToClipboard(elementId) {
    const content = document.getElementById(elementId).textContent;
    
    navigator.clipboard.writeText(content).then(() => {
        showToast('Copied to clipboard!', 'success');
    }).catch(err => {
        console.error('Failed to copy:', err);
        showToast('Failed to copy to clipboard', 'error');
    });
}

// ==================== Download as Text File ====================
function downloadText(elementId, filename) {
    const content = document.getElementById(elementId).textContent;
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    showToast('File downloaded!', 'success');
}

// ==================== Show Toast Notification ====================
function showToast(message, type = 'success') {
    toast.textContent = message;
    toast.className = `toast show ${type}`;
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// ==================== API Health Check ====================
async function checkAPIHealth() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        const data = await response.json();
        console.log('✅ API Status:', data);
    } catch (error) {
        console.warn('⚠️ API health check failed. Make sure backend is running:', error);
        showToast('Warning: Cannot connect to API. Please start the backend server.', 'error');
    }
}