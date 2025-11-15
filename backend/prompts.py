"""
Prompt Engineering Module - Optimized for Google Gemini API
Contains optimized prompts for different content types
"""

def get_prompt_template(content_type, topic, tone="professional", length="medium"):
    """
    Generate optimized prompts for Gemini API based on content type
    
    Args:
        content_type: Type of content to generate
        topic: Main topic/subject
        tone: Desired tone of writing
        length: Desired length (short/medium/long)
    
    Returns:
        Engineered prompt string optimized for Gemini
    """
    
    length_instructions = {
        "short": "Write approximately 150-200 words.",
        "medium": "Write approximately 400-500 words.",
        "long": "Write approximately 800-1000 words."
    }
    
    tone_instructions = {
        "professional": "Use a professional and authoritative tone.",
        "casual": "Write in a conversational and relaxed manner.",
        "friendly": "Use a warm, approachable, and friendly tone.",
        "formal": "Maintain a formal and academic tone throughout.",
        "persuasive": "Use persuasive language to convince and engage readers.",
        "informative": "Focus on providing clear, factual information."
    }
    
    # Get length and tone settings
    length_instr = length_instructions.get(length, length_instructions['medium'])
    tone_instr = tone_instructions.get(tone, tone_instructions['professional'])
    
    # Content-specific prompt templates optimized for Gemini
    prompts = {
        "blog": f"""You are an expert content writer. Write a compelling blog post about: {topic}

{tone_instr}
{length_instr}

Structure your blog post as follows:

1. **Title**: Create an attention-grabbing, SEO-friendly headline
2. **Introduction**: Hook the reader with an engaging opening (2-3 paragraphs)
3. **Main Content**: Organize with clear subheadings and provide valuable insights
4. **Conclusion**: Summarize key points and include a call-to-action

Make sure to:
- Use clear subheadings to organize content
- Include actionable takeaways
- Write in an engaging, readable style
- Naturally incorporate relevant keywords

Write the complete blog post now:""",
        
        "email": f"""You are a professional email writer. Compose an email about: {topic}

{tone_instr}
{length_instr}

Create a complete email with:

1. **Subject Line**: Clear, specific, and compelling
2. **Greeting**: Appropriate professional greeting
3. **Opening**: State the purpose clearly in the first sentence
4. **Body**: Keep paragraphs short (2-3 sentences each)
5. **Call-to-Action**: Clear next steps or action required
6. **Closing**: Professional sign-off

Guidelines:
- Use bullet points for multiple items
- Be concise and scannable
- Maintain professional courtesy
- Include clear action items

Write the complete email now:""",
        
        "social": f"""You are a social media content strategist. Create engaging social media posts about: {topic}

{tone_instr}

Requirements:
- Write attention-grabbing opening lines
- Include 3-5 relevant hashtags
- Use emojis strategically (if appropriate)
- Make content shareable and engaging
- Optimize for maximum engagement

Create 3 distinct variations:

**Twitter/X Post** (280 characters max):
[Write concise, punchy content]

**LinkedIn Post** (150-200 words):
[Write professional, value-driven content]

**Instagram Caption** (100-150 words):
[Write visual, engaging content with storytelling]

Write all three variations now:""",
        
        "product": f"""You are an expert product copywriter. Write a compelling product description for: {topic}

{tone_instr}
{length_instr}

Structure:

1. **Headline**: Captivating product title that grabs attention
2. **Hook**: One-sentence value proposition
3. **Features & Benefits**: Highlight key features, focusing on customer benefits (use bullet points)
4. **Why This Product**: Address customer pain points and solutions
5. **Technical Details**: Include relevant specifications if applicable
6. **Call-to-Action**: Persuasive, action-oriented closing

Guidelines:
- Focus on benefits over features
- Use sensory and emotional language
- Create urgency or desire
- Be specific and credible
- Make it conversion-oriented

Write the complete product description now:""",
        
        "article": f"""You are an experienced journalist and content writer. Write an in-depth article about: {topic}

{tone_instr}
{length_instr}

Structure:

1. **Title**: Informative, SEO-friendly headline
2. **Introduction**: Strong hook with thesis statement (2-3 paragraphs)
3. **Main Sections**: 3-5 major sections with clear subheadings
4. **Supporting Content**: Include explanations, examples, and evidence
5. **Conclusion**: Comprehensive summary and key takeaways

Guidelines:
- Maintain logical flow between sections
- Use data, examples, or case studies where relevant
- Write with depth and thoroughness
- Include transition sentences between sections
- Make it informative and authoritative

Write the complete article now:""",
        
        "story": f"""You are a creative fiction writer. Write an engaging story about: {topic}

{tone_instr}
{length_instr}

Story Elements:

1. **Setup**: Introduce characters, setting, and context
2. **Conflict**: Present the central problem or tension
3. **Rising Action**: Build tension and develop the plot
4. **Climax**: Reach the peak of the story
5. **Resolution**: Provide a satisfying conclusion

Guidelines:
- Create relatable, three-dimensional characters
- Use vivid descriptions and sensory details
- Include dialogue to show character personality
- Build emotional connection with readers
- Maintain engaging pacing throughout
- Deliver a meaningful or memorable ending

Write the complete story now:""",
        
        "ad": f"""You are an expert advertising copywriter. Create compelling advertisement copy for: {topic}

{tone_instr}
{length_instr}

Create TWO versions:

**SHORT-FORM AD (50-75 words):**
- Attention-grabbing headline
- One key benefit/USP
- Strong call-to-action
- Create immediate impact

**LONG-FORM AD (150-200 words):**
- Compelling headline
- Problem-solution narrative
- Multiple benefits highlighted
- Social proof or credibility elements
- Urgency or scarcity element
- Powerful call-to-action

Guidelines for both:
- Use power words and emotional triggers
- Highlight unique selling proposition (USP)
- Create desire and urgency
- Be memorable and persuasive
- Focus on customer transformation

Write both versions now:""",
    }
    
    # Return appropriate prompt or default
    default_prompt = f"""You are an expert content writer. Create high-quality content about: {topic}

{tone_instr}
{length_instr}

Requirements:
- Start with a strong, engaging opening
- Structure content logically with clear sections
- Provide valuable, actionable information
- Use clear, concise language
- End with a memorable conclusion

Write the complete content now:"""
    
    return prompts.get(content_type, default_prompt)


def get_summarization_prompt(text, summary_type="brief"):
    """
    Generate optimized summarization prompts for Gemini API
    
    Args:
        text: Text to summarize
        summary_type: Type of summary needed
    
    Returns:
        Engineered summarization prompt optimized for Gemini
    """
    
    prompts = {
        "brief": f"""You are an expert at summarization. Provide a brief, concise summary of the following text.

Requirements:
- Write 2-3 sentences only
- Focus on the main idea and key takeaways
- Be clear and direct
- Capture the essence without unnecessary details

Text to summarize:
{text}

Write the brief summary now:""",
        
        "detailed": f"""You are an expert at creating comprehensive summaries. Provide a detailed summary of the following text.

Include:
- Main themes and central arguments
- Key supporting points and evidence
- Important details, examples, and data
- Overall conclusions and implications

Guidelines:
- Be thorough but organized
- Maintain logical flow
- Preserve important context
- Use clear, professional language

Text to summarize:
{text}

Write the detailed summary now:""",
        
        "bullet": f"""You are an expert at creating structured summaries. Summarize the following text as clear bullet points.

Requirements:
- Use bullet points (•) for each key point
- Extract the most important information
- Make it scannable and easy to read
- Each bullet should be one complete idea
- Organize from most to least important
- Keep bullets concise (1-2 sentences each)

Text to summarize:
{text}

Write the bullet point summary now:""",
        
        "abstract": f"""You are an academic writer. Write a formal abstract for the following text.

Structure your abstract with:
- **Background/Context**: Brief overview of the topic
- **Objective**: Main purpose or research question
- **Key Points**: Central arguments or findings
- **Conclusion**: Main implications or conclusions

Requirements:
- Use formal, academic tone
- Write 150-250 words
- Be objective and precise
- Follow abstract conventions
- Make it self-contained

Text to summarize:
{text}

Write the academic abstract now:"""
    }
    
    return prompts.get(summary_type, prompts["brief"])


# Additional helper function for Gemini-specific optimization
def optimize_for_gemini(prompt):
    """
    Apply Gemini-specific optimizations to any prompt
    
    Args:
        prompt: Base prompt string
    
    Returns:
        Optimized prompt for Gemini
    """
    # Gemini works best with:
    # 1. Clear role definition
    # 2. Explicit instructions
    # 3. Structured format requirements
    # 4. Action-oriented endings
    
    if not prompt.startswith("You are"):
        prompt = f"You are an expert content creator. {prompt}"
    
    if not prompt.rstrip().endswith(":"):
        prompt = f"{prompt}\n\nProvide your response now:"
    
    return prompt