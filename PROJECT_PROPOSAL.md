# AI-Powered Student Wellness Companion
### Team: Three Unknowns | VRSEC | Mini Project 2026

---

## 📌 Project Title
**MindMate: AI-Powered Student Wellness Companion**

---

## 🎯 Problem Statement

**The Problem:**
College students face increasing levels of stress, anxiety, and academic pressure but often:
- Feel hesitant to seek professional help due to stigma
- Don't have 24/7 access to counselors
- Need immediate support during exam stress, personal issues, or overwhelming moments
- Lack a safe, judgment-free space to express their feelings

**Why This Matters:**
- WHO reports 1 in 7 students suffer from mental health issues
- Academic stress leads to poor performance, dropouts, and severe health consequences
- Early intervention through accessible support can prevent serious problems

**Current Gap:**
- Traditional counseling services are limited by time, availability, and social barriers
- Existing apps are either too clinical or not personalized
- No integrated solution for student-specific mental wellness

---

## 💡 Solution Overview

**MindMate** is an AI-powered conversational companion that provides:

1. **24/7 Emotional Support** - Always available to listen and respond
2. **Mental Wellness Tracking** - Monitors mood patterns over time
3. **Personalized Coping Strategies** - Suggests exercises, meditation, resources based on student's state
4. **Anonymous & Safe** - No judgment, complete privacy
5. **Smart Escalation** - Detects crisis situations and recommends professional help

**Why AI is Needed:**
- Natural language understanding to empathize and respond contextually
- Pattern recognition to identify worsening mental health trends
- Personalization that adapts to each student's unique needs
- Scale to support thousands of students simultaneously
- Available 24/7 without human resource constraints

---

## 🎯 Target Users

**Primary Users:**
- College students (18-24 years)
- Students facing academic stress, exam anxiety
- Students dealing with loneliness, relationship issues, or career confusion

**Secondary Users:**
- College counseling centers (as a first-line support tool)
- Educational institutions monitoring student wellness trends

---

## 🛠️ Technologies Used (Azure-Focused)

| Azure Service | Purpose | Why Needed |
|--------------|---------|------------|
| **Azure OpenAI Service** | GPT-4o/GPT-4 for conversational AI | Natural, empathetic conversations |
| **Azure App Service** | Host web application (frontend + backend) | Scalable web hosting with auto-scaling |
| **Azure Cosmos DB** (Free tier) | Store user conversations & mood logs | NoSQL database for flexible data storage |
| **Azure Cognitive Services - Text Analytics** | Sentiment analysis & emotion detection | Understand user's emotional state |
| **Azure Key Vault** | Secure storage of API keys | Security best practice |
| **Azure Monitor** | Track app performance & usage | Monitor costs and performance |
| **Azure Static Web Apps** (Optional) | Host React/Vue frontend | Free tier for static hosting |

**Development Stack:**
- Frontend: React.js / Vue.js (simple chat interface)
- Backend: Python (Flask/FastAPI) or Node.js (Express)
- Database: Azure Cosmos DB (NoSQL)
- AI: Azure OpenAI (GPT-4o or GPT-3.5-turbo)
- Deployment: Azure App Service (Free/Basic tier)

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER (Student)                        │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ (Chat via Web Browser)
                       ▼
┌─────────────────────────────────────────────────────────────┐
│               FRONTEND (React/Vue.js)                        │
│  • Chat Interface                                            │
│  • Mood Tracker Dashboard                                    │
│  • Resources & Tips Section                                  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ HTTPS REST API
                       ▼
┌─────────────────────────────────────────────────────────────┐
│        BACKEND (Python Flask / Node.js Express)              │
│               Hosted on Azure App Service                    │
│                                                              │
│  API Endpoints:                                              │
│  • POST /chat - Handle user messages                         │
│  • POST /mood - Log mood entry                               │
│  • GET /history - Retrieve chat history                      │
│  • GET /insights - Get wellness insights                     │
└─────┬─────────────────────┬─────────────────────┬──────────┘
      │                     │                     │
      ▼                     ▼                     ▼
┌──────────────┐  ┌──────────────────┐  ┌─────────────────┐
│ Azure OpenAI │  │ Text Analytics   │  │ Azure Cosmos DB │
│   Service    │  │   (Sentiment)    │  │                 │
│              │  │                  │  │ Collections:    │
│ GPT-4o API   │  │ Emotion Detection│  │ • users         │
│              │  │                  │  │ • conversations │
│ Empathetic   │  │ Crisis Detection │  │ • mood_logs     │
│ Responses    │  │                  │  │ • resources     │
└──────────────┘  └──────────────────┘  └─────────────────┘
```

---

## 📊 Data Flow (Step-by-Step)

### **Scenario: Student Starts a Conversation**

**Step 1: User Opens the App**
- Student opens the web app in browser
- Frontend loads a clean chat interface
- Optional: Anonymous user ID generated (no personal info required)

**Step 2: Student Types a Message**
```
Example: "I'm feeling really stressed about my exams tomorrow"
```

**Step 3: Frontend Sends Message to Backend**
- Frontend makes POST request to `/chat` endpoint
- Payload: `{ "user_id": "anon_12345", "message": "I'm feeling really stressed..." }`

**Step 4: Backend Processes the Message**

**4a. Sentiment Analysis**
- Backend sends message to Azure Text Analytics
- Receives sentiment score: `{ "sentiment": "negative", "confidence": 0.85 }`
- Detects emotions: `{ "emotions": ["stress", "anxiety"] }`

**4b. Crisis Detection**
- Checks for keywords indicating severe distress (self-harm, suicide, etc.)
- If detected: Flag for immediate professional help recommendation
- If normal: Proceed with empathetic response

**4c. Build Context for AI**
- Retrieves last 5 messages from Cosmos DB for context
- Creates system prompt:
```
You are MindMate, an empathetic AI companion for college students.
Your role is to:
- Listen without judgment
- Provide emotional support
- Suggest coping strategies
- Never give medical advice
User's current emotion: stressed, anxious
Context: Exam tomorrow
```

**Step 5: Azure OpenAI Generates Response**
- Backend calls Azure OpenAI API with:
  - System prompt (context)
  - Conversation history
  - User's message
- GPT-4o generates empathetic response:
```
"I hear you. Exam stress is really tough, especially the night before.
It's completely normal to feel this way. Have you tried any breathing
exercises? Sometimes taking 5 minutes for deep breathing can help calm
your mind. Would you like me to guide you through one?"
```

**Step 6: Store Conversation**
- Backend saves to Cosmos DB:
```json
{
  "user_id": "anon_12345",
  "timestamp": "2026-01-01T10:30:00Z",
  "user_message": "I'm feeling really stressed...",
  "ai_response": "I hear you...",
  "sentiment": "negative",
  "emotions": ["stress", "anxiety"]
}
```

**Step 7: Return Response to Frontend**
- Backend sends JSON response:
```json
{
  "response": "I hear you. Exam stress is...",
  "suggestions": ["breathing_exercise", "study_tips"],
  "sentiment": "negative"
}
```

**Step 8: Frontend Displays Response**
- Chat bubble appears with AI response
- Optional: Shows suggestion buttons for breathing exercises
- Updates mood indicator if enabled

### **Bonus Flow: Mood Tracking**

**Step 1: User Logs Daily Mood**
- User clicks mood icon (😊 😐 😢)
- Selects: "Stressed" + optional note

**Step 2: Stored in Database**
```json
{
  "user_id": "anon_12345",
  "date": "2026-01-01",
  "mood": "stressed",
  "note": "Too many assignments",
  "timestamp": "2026-01-01T18:00:00Z"
}
```

**Step 3: Analytics & Insights**
- Weekly/monthly mood patterns analyzed
- If negative mood persists > 7 days → Recommend counseling
- Show visual mood chart to user

---

## 🚀 MVP Features (Minimal Viable Product)

### **Phase 1: Core Features (Must Have)**

1. **AI Chatbot**
   - Text-based conversation
   - Empathetic, supportive responses
   - Context-aware (remembers recent conversation)
   - Uses Azure OpenAI GPT-4o

2. **Sentiment Analysis**
   - Real-time emotion detection
   - Identifies stress, anxiety, sadness, happiness
   - Uses Azure Text Analytics

3. **Simple Mood Logger**
   - Daily mood check-in (Happy/Neutral/Sad)
   - Basic mood history view (last 7 days)

4. **Resource Library**
   - Static content: breathing exercises, study tips, helpline numbers
   - Categorized: Stress, Anxiety, Sleep, Focus

5. **Crisis Detection**
   - Keyword-based detection for severe distress
   - Auto-suggest professional helplines
   - Display emergency resources

### **Phase 2: Nice to Have (If Time Permits)**

6. **Mood Analytics Dashboard**
   - Weekly mood trends (chart/graph)
   - Insights: "You felt stressed 4/7 days this week"

7. **Personalized Tips**
   - AI suggests resources based on conversation patterns

8. **Anonymous Data Sharing**
   - Aggregate campus-wide mental health trends (privacy-preserved)
   - Insights for college counseling centers

---

## ✅ Advantages of This Solution

### **1. Accessibility**
- 24/7 availability - students get support anytime
- No appointment needed - instant response
- Anonymous - removes social stigma

### **2. Scalability**
- One system can support thousands of students
- No limit on concurrent conversations
- Low operational cost (mostly Azure credits)

### **3. Early Intervention**
- Detects patterns of declining mental health
- Recommends professional help before crisis
- Reduces dropout rates and academic failures

### **4. Data-Driven Insights**
- Colleges can identify peak stress periods (exam weeks)
- Allocate counseling resources better
- Evidence-based wellness programs

### **5. Cost-Effective**
- No need to hire 24/7 counselors for first-line support
- Azure for Students credits cover MVP completely
- Scalable pricing as user base grows

### **6. Privacy & Safety**
- No personal information required (anonymous usage)
- Data encrypted (Azure Key Vault)
- GDPR/privacy compliant (Azure data centers)

---

## 🔮 Future Enhancements (Post-MVP / Major Project)

1. **Voice Interface**
   - Azure Speech Services for voice chat
   - Accessibility for visually impaired students

2. **Multi-Language Support**
   - Support regional languages (Hindi, Telugu, etc.)
   - Azure Translator API

3. **Integration with Campus Systems**
   - Connect with college LMS (attendance, grades)
   - Predict stress based on academic performance

4. **Peer Support Groups**
   - Match students with similar challenges
   - Moderated anonymous group chats

5. **Gamification**
   - Wellness streaks, badges for consistent mood logging
   - Engagement rewards

6. **AI-Powered Journaling**
   - Guided journaling prompts
   - Reflection analysis using AI

7. **Counselor Dashboard**
   - For campus counselors to monitor trends
   - Prioritize students who need intervention

8. **Mobile App**
   - React Native / Flutter app
   - Push notifications for daily check-ins

---

## 🏆 Why This Project Fits Imagine Cup

### **1. Aligns with Imagine Cup Themes**
- **Education** - Supports student success
- **Health** - Addresses mental wellness crisis
- **Lifestyle** - Improves quality of student life

### **2. Real-World Impact**
- Addresses a genuine, growing problem (student mental health crisis)
- Target users: 100+ million college students globally
- Potential to save lives through early intervention

### **3. Innovation**
- Combines AI (GPT-4) with mental health support
- Not just a chatbot - includes mood tracking, pattern detection, personalization
- Uses cutting-edge Azure AI services

### **4. Scalability & Feasibility**
- Can start with one college campus (VRSEC)
- Scale to all colleges in Andhra Pradesh/India
- Global potential (language localization)

### **5. Technical Excellence**
- Uses modern cloud architecture (Azure)
- Demonstrates AI/ML skills (OpenAI, Sentiment Analysis)
- Secure, scalable, and well-architected

### **6. Social Good**
- Free for students - removes financial barriers to mental health support
- Reduces stigma around seeking help
- Empowers students to take control of their wellness

### **7. Sustainability**
- Low operational cost (AI scales efficiently)
- Revenue model possible: B2B (colleges/universities buy for students)
- Freemium for individual users

---

## 💰 Azure Credit Estimation (For MVP)

**Azure for Students: $100 Credit**

| Service | Estimated Cost/Month | Usage |
|---------|---------------------|-------|
| Azure OpenAI (GPT-4o) | $30-40 | ~1000 conversations |
| Azure App Service (Basic B1) | $13 | Always-on hosting |
| Azure Cosmos DB (Free tier) | $0 | Up to 1000 RU/s free |
| Azure Text Analytics | $10 | ~5000 API calls |
| Azure Key Vault | $0 | Secrets storage (minimal) |
| Azure Monitor | $0 | Basic monitoring free |
| **TOTAL** | **~$50-60/month** | **MVP for 2 months** |

**Optimization Tips:**
- Use GPT-3.5-turbo instead of GPT-4 (5x cheaper, still good)
- Free tier Cosmos DB for development
- Azure Static Web Apps (free) for frontend
- Implement caching to reduce API calls

**Extended Credits:**
- Students get $100 initial + renewals
- Apply for additional credits via Azure for Students
- Imagine Cup participants often get extra Azure credits

---

## 📋 Project Execution Plan (6-8 Weeks)

### **Week 1-2: Research & Design**
- Finalize problem statement
- Design UI/UX mockups (Figma)
- Create system architecture diagram
- Set up Azure account & resources

### **Week 3-4: Backend Development**
- Set up Azure OpenAI integration
- Build REST API (Flask/Express)
- Implement sentiment analysis
- Set up Cosmos DB schema

### **Week 5-6: Frontend Development**
- Build chat interface (React)
- Implement mood logger UI
- Integrate with backend APIs
- Responsive design (mobile-friendly)

### **Week 7: Integration & Testing**
- End-to-end testing
- Crisis detection testing
- Performance optimization
- Bug fixes

### **Week 8: Deployment & Documentation**
- Deploy to Azure App Service
- Write project report
- Create demo video (3-5 min)
- Prepare presentation (10 slides)

---

## 📝 Deliverables for College Review

1. **Project Report** (20-30 pages)
   - Problem statement, literature survey
   - System design, architecture diagrams
   - Implementation details (code snippets)
   - Testing & results
   - Screenshots & user flow

2. **Working Prototype**
   - Live web app (deployed on Azure)
   - Demo video (showing key features)

3. **Source Code**
   - GitHub repository (well-documented)
   - README with setup instructions

4. **Presentation** (PPT)
   - 10-15 slides
   - Problem → Solution → Demo → Impact

5. **Imagine Cup Submission** (if participating)
   - 3-minute pitch video
   - Project description (500 words)
   - Screenshots/demo link

---

## 🎤 Elevator Pitch (For Judges/Reviewers)

> **"MindMate is an AI-powered mental wellness companion for college students. Using Azure OpenAI and sentiment analysis, it provides 24/7 emotional support, tracks mood patterns, and detects early signs of mental health decline. Unlike traditional counseling limited by time and stigma, MindMate is always available, completely anonymous, and scalable to support thousands of students. Our mission: make mental health support as accessible as checking your phone."**

---

## 🔗 Additional Resources

### **Learning Resources:**
- Azure OpenAI Documentation: https://learn.microsoft.com/azure/ai-services/openai/
- Azure for Students: https://azure.microsoft.com/free/students/
- Imagine Cup: https://imaginecup.microsoft.com/

### **Similar Inspirations (Study but Don't Copy):**
- Woebot (mental health chatbot)
- Replika (AI companion)
- Wysa (emotional wellness)

### **Key Differentiators:**
- Student-specific (exam stress, academic pressure)
- Campus integration potential
- Free & accessible (not freemium with paywalls)
- Built on Azure (not proprietary infrastructure)

---

## 📞 Support & Next Steps

**For Your Team:**
1. Review this proposal together
2. Decide if you want to pursue this or modify it
3. Assign roles: Frontend dev, Backend dev, Documentation, Testing
4. Set up weekly milestones
5. Create a GitHub repo and start building!

**Need Modifications?**
- Different problem statement? (e.g., agriculture, education, accessibility)
- Different tech stack preferences?
- Specific feature requests?

**Questions to Clarify:**
- Do you have programming experience in React/Python?
- Have you used Azure before?
- Any specific constraints from your college guide?

---

**Good luck, Team Three Unknowns! 🚀**

This project has real potential to make a difference. Stay focused on building an MVP first, and iterate based on user feedback. You've got this!

---

*Document Version: 1.0*  
*Date: January 1, 2026*  
*Team: Three Unknowns | VRSEC*
