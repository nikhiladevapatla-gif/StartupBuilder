
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# ==========================================
# 1. LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()


# ==========================================
# 2. INITIALIZE GEMINI
# ==========================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.5,
    timeout=60
)


# ==========================================
# 3. MARKETING AGENT
# ==========================================

def marketing_agent(startup_idea, research_report, developer_report):

    prompt = f"""
You are a senior startup marketing strategist,
brand consultant, digital marketing expert,
and customer acquisition specialist.

Your responsibility is to create a complete,
practical, and measurable marketing strategy
for the proposed startup.

The strategy must be suitable for an early-stage
student startup with a limited marketing budget.

STARTUP IDEA:
{startup_idea}

MARKET RESEARCH REPORT:
{research_report}

TECHNICAL DEVELOPMENT REPORT:
{developer_report}


IMPORTANT INSTRUCTIONS:

1. Understand the startup idea and research findings.
2. Use the research report to identify real customer problems.
3. Align marketing promises with the proposed product features.
4. Avoid unrealistic growth predictions.
5. Do not invent customer statistics or market research results.
6. Clearly label budget estimates and marketing assumptions.
7. Recommend affordable marketing channels first.
8. Make every recommendation actionable.
9. Distinguish marketing experiments from proven strategies.
10. Keep promotional content natural and engaging.


GENERATE THE REPORT USING THIS STRUCTURE:


# STARTUP MARKETING AND GROWTH STRATEGY REPORT


## 1. Marketing Executive Summary

Explain:

- What the startup offers.
- The main customer problem.
- The marketing objective.
- Primary target audience.
- Recommended marketing approach.
- Expected early-stage marketing priorities.

Provide a concise marketing strategy overview.


## 2. Target Audience Segmentation

Identify the major customer segments.

For each segment explain:

- Customer type.
- Age group or professional stage, where relevant.
- Needs and challenges.
- Purchasing motivation.
- Preferred communication channels.
- Likely adoption barriers.

Separate:

- Primary audience.
- Secondary audience.
- Potential future audience.

Prioritize the most suitable initial customer segment.


## 3. Ideal Customer Personas

Create at least three realistic customer personas.

For each persona include:

- Persona name.
- Background.
- Goals.
- Problems.
- Needs.
- Online behavior.
- Preferred platforms.
- Reasons to use the startup.
- Reasons they might reject the product.

Explain how marketing messages should differ
for each persona.


## 4. Brand Identity and Positioning

Suggest three possible startup brand names.

For each name include:

- Brand name.
- Meaning or concept.
- Brand personality.
- Suggested tagline.

Select the strongest recommendation.

Then define:

- Brand mission.
- Brand vision.
- Brand values.
- Brand voice.
- Brand personality.
- Unique Selling Proposition (USP).
- Main customer promise.
- Key brand differentiation.

Do not claim that suggested brand names or domains
are legally available. Recommend checking trademarks
and domain availability before adoption.


## 5. Competitive Positioning

Use the market research report to identify
relevant competitor categories.

Explain:

- Competitor positioning.
- Their likely customer appeal.
- Potential strengths.
- Possible market gaps.
- How the startup can differentiate itself.

Create a simple positioning comparison table.

Do not invent competitor market shares or unsupported facts.


## 6. Marketing Channel Strategy

Evaluate suitable marketing channels.

Consider:

- Instagram.
- LinkedIn.
- YouTube.
- WhatsApp communities.
- College communities.
- Student ambassadors.
- University partnerships.
- Email marketing.
- SEO and website content.
- Campus events and workshops.

For each recommended channel explain:

- Target audience.
- Content type.
- Marketing objective.
- Estimated effort.
- Priority.

Rank the most suitable channels for the MVP launch.


## 7. Customer Acquisition Strategy

Create a step-by-step strategy to acquire the first 100 users.

Divide it into:

### Stage 1: Initial Awareness
Explain how to introduce the startup.

### Stage 2: Interest Generation
Explain how to attract interested users.

### Stage 3: Sign-ups
Explain how to convert interested people into registrations.

### Stage 4: Activation
Explain how to encourage users to try the core features.

### Stage 5: Referrals
Explain how existing users can invite others.

Suggest practical acquisition experiments.

Do not guarantee a specific number of sign-ups.


## 8. Content Marketing Strategy

Create a content strategy for the startup.

Include:

- Educational content.
- Product demonstrations.
- Customer problem awareness.
- Testimonials and user stories.
- Behind-the-scenes content.
- Feature announcements.

Suggest at least five social media campaign ideas.

For each campaign provide:

- Campaign name.
- Objective.
- Target audience.
- Content format.
- Main message.
- Call to action.

Make the campaigns specific to the startup.


## 9. Promotional Content Generation

Generate ready-to-use promotional content.

### A. Instagram Captions

Create five engaging Instagram captions.

### B. LinkedIn Posts

Create three professional LinkedIn post drafts.

### C. WhatsApp Promotions

Create three short promotional messages.

### D. Taglines

Generate five catchy taglines.

### E. Website Hero Section

Write:

- Main headline.
- Supporting description.
- Primary call-to-action.
- Secondary call-to-action.

### F. Short Elevator Pitch

Write a 30-second startup introduction.

Make the content natural, convincing,
and appropriate for the target audience.


## 10. Campus Launch Strategy

Create a practical launch strategy for one university campus.

Include:

- Pre-launch activities.
- Student ambassador program.
- Campus awareness campaigns.
- Demonstration sessions.
- Club and department partnerships.
- Launch-day activities.
- Post-launch engagement.

Provide a four-week campus launch schedule.

Keep activities realistic for a student team.


## 11. Marketing Budget Allocation

Suggest three budget plans:

### Plan A: Zero-Budget Marketing
Organic marketing and student communities.

### Plan B: Low-Budget Marketing
Small promotional campaigns and campus activities.

### Plan C: Growth Marketing
Paid advertisements and larger promotional activities.

Present a table containing:

| Activity | Estimated Budget | Purpose |

Use clearly labelled illustrative estimates
and specify the currency.

Avoid presenting estimates as actual market prices.

Explain how to prioritize spending when funds are limited.


## 12. SEO and Online Presence Strategy

Recommend:

- Website structure.
- Important landing pages.
- Search keywords.
- Blog topics.
- SEO improvements.
- Social media profile optimization.
- Conversion-focused landing page elements.

Explain how organic traffic can be developed over time.

Do not claim that suggested keywords have verified
search volume.


## 13. Customer Retention and Engagement

Explain how to retain early users through:

- Onboarding.
- Personalized communication.
- Notifications.
- Feedback collection.
- Referral rewards.
- Community engagement.
- Product improvement.
- Re-engagement campaigns.

Suggest ways to increase repeat usage.


## 14. 90-Day Marketing Roadmap

Create a practical 90-day marketing plan.

Divide it into:

### Days 1-30: Brand Awareness and Pre-launch
### Days 31-60: Product Launch and User Acquisition
### Days 61-90: Engagement and Growth

For each phase include:

- Main objectives.
- Marketing activities.
- Deliverables.
- Channels.
- Success indicators.

Make the timeline suitable for a small startup team.


## 15. Marketing KPIs and Performance Measurement

Recommend important marketing metrics.

Include:

- Website visitors.
- Registration conversion rate.
- Customer acquisition cost (CAC).
- Activation rate.
- User retention.
- Referral rate.
- Social media engagement.
- Campaign conversion rate.

Explain:

- What each metric measures.
- How it is calculated.
- Why it matters.

Provide realistic ways to track performance
using affordable tools.


## 16. Marketing Risks and Mitigation

Identify possible risks such as:

- Low brand awareness.
- Limited marketing budget.
- Low conversion rates.
- Strong competition.
- Poor customer retention.
- Negative feedback.
- Dependence on social media platforms.

For each risk provide a mitigation strategy.


## 17. Final Marketing Recommendations

Summarize:

- Recommended brand direction.
- Most important customer segment.
- Strongest USP.
- Best marketing channels.
- First 100-user acquisition approach.
- Recommended launch budget.
- Most important KPIs.
- First five marketing actions.

Provide a final marketing readiness assessment.


## 18. Assumptions and Limitations

Clearly identify:

- Assumptions about customer behavior.
- Estimated marketing costs.
- Unverified competitor information.
- Channels requiring experimentation.
- Customer preferences requiring validation.
- Brand names requiring legal checks.


FINAL REQUIREMENTS:

Make the report detailed, structured,
and specific to the startup idea.

Use Markdown headings, tables, and bullet points.

Generate actual promotional content rather than
only describing what promotional content should contain.

Keep all recommendations practical for an early-stage
student startup with limited resources.

Do not fabricate market research results or guarantee growth.
"""

    print("\nMarketing Agent is preparing your strategy...")

    response = llm.invoke(prompt)

    # ==========================================
    # 4. EXTRACT CLEAN TEXT FROM GEMINI RESPONSE
    # ==========================================

    content = response.content

    if isinstance(content, list):

        text_parts = []

        for block in content:

            if isinstance(block, dict) and block.get("type") == "text":

                text_parts.append(block.get("text", ""))

            elif isinstance(block, str):

                text_parts.append(block)

        content = "\n".join(text_parts)

    if not isinstance(content, str):

        content = str(content)

    return content.strip()


# ==========================================
# 5. TEST MARKETING AGENT
# ==========================================

if __name__ == "__main__":

    idea = """
    An AI-powered platform that helps college students
    prepare for placements by analyzing resumes, identifying
    skill gaps, recommending personalized learning paths,
    generating role-specific interview questions, and
    matching students with suitable job opportunities.
    """

    research = """
    Target customers: College students and recent graduates.

    Problem: Students struggle to identify skill gaps,
    improve resumes, and prepare for placement interviews.

    Opportunity: An integrated AI-powered career-readiness
    platform that combines resume analysis, personalized
    learning paths, interview preparation, and job matching.

    Potential challenge: Competition from existing
    resume builders and career platforms.
    """

    developer = """
    Proposed architecture:

    Frontend: React.
    Backend: FastAPI and Python.
    Database: PostgreSQL.
    AI integration: LLM APIs.
    Hosting: Vercel and Render.

    MVP features:
    Resume analysis, skill-gap identification,
    interview question generation, and student dashboard.
    """

    result = marketing_agent(idea, research, developer)

    print("\n========== MARKETING STRATEGY REPORT ==========\n")

    print(result)

    print("\n================================================")
    print("Marketing Agent execution completed successfully!")
