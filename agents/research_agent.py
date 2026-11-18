
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
    temperature=0.4,
    timeout=60
)


# ==========================================
# 3. RESEARCH AGENT
# ==========================================

def research_agent(startup_idea):

    prompt = f"""
You are a senior startup market research analyst,
business strategist, and venture capital research expert.

Your task is to evaluate the startup idea and prepare
a detailed, professional startup research report.

STARTUP IDEA:
{startup_idea}


IMPORTANT INSTRUCTIONS:

1. Provide practical and realistic analysis.
2. Avoid generic statements.
3. Use clear professional business language.
4. Do not invent statistics, market sizes, competitor
   information, customer numbers, or industry facts.
5. Clearly label assumptions and estimates.
6. If exact market data is unavailable, explain how
   the market size could be estimated.
7. Distinguish verified facts from hypotheses.


GENERATE THE REPORT USING THIS STRUCTURE:


# STARTUP MARKET RESEARCH REPORT


## 1. Executive Summary

- Overview of the startup idea.
- Main problem being addressed.
- Proposed solution.
- Primary target market.
- Overall market opportunity.
- Initial assessment of business potential.


## 2. Problem Identification

Analyze:

- What specific problem does the startup solve?
- Why does this problem exist?
- Who experiences this problem?
- What are the limitations of existing solutions?
- Why is solving this problem important?

Identify at least three major customer pain points.


## 3. Proposed Solution and Value Proposition

Explain:

- How the product or service works.
- Main features.
- Unique value proposition.
- Benefits to customers.
- Why customers would choose this solution.

Identify the startup's potential competitive advantage.


## 4. Target Customer Analysis

Identify:

- Primary target customers.
- Secondary target customers.
- Customer demographics.
- Customer behavior.
- Customer needs.
- Potential early adopters.

Create at least two customer personas.

For each persona include:
- Profile.
- Main challenges.
- Requirements.
- Expected benefits.


## 5. Market Opportunity Analysis

Discuss:

- Relevant industry.
- Market demand.
- Growth opportunities.
- Potential geographical markets.
- Barriers to market entry.

### TAM, SAM and SOM

Explain:

- TAM: Total Addressable Market.
- SAM: Serviceable Available Market.
- SOM: Serviceable Obtainable Market.

Do not fabricate numerical market estimates.

If reliable market data is unavailable, provide:
- The calculation methodology.
- Required data.
- Clearly labelled illustrative assumptions.


## 6. Competitor Analysis

Identify:

- Direct competitors.
- Indirect competitors.
- Existing alternative solutions.

Compare competitors using:
- Product offerings.
- Target customers.
- Strengths.
- Limitations.
- Differentiation opportunities.

Do not invent competitor names or capabilities.
Clearly identify examples that require further verification.


## 7. Industry and Technology Trends

Analyze relevant trends such as:

- Emerging technologies.
- Customer behavior changes.
- Industry developments.
- AI and automation opportunities, where relevant.
- Future market possibilities.

Explain how each trend could affect the startup.


## 8. SWOT Analysis

### Strengths
Identify internal advantages.

### Weaknesses
Identify internal limitations.

### Opportunities
Identify external growth opportunities.

### Threats
Identify external risks and competition.


## 9. Business Model Opportunities

Suggest suitable revenue models, such as:

- Subscription model.
- Freemium model.
- Commission-based model.
- Licensing.
- Business partnerships.

Explain which model is most suitable and why.

Clearly identify pricing suggestions as hypotheses,
not established market prices.


## 10. Customer Validation Strategy

Suggest at least five practical experiments.

For each experiment include:

- Objective.
- Target participants.
- Method.
- Success metric.
- Expected learning.

Include customer interviews, surveys, landing page
experiments, prototype testing, and pilot programs
where appropriate.


## 11. Risks and Challenges

Analyze:

- Market risks.
- Technical risks.
- Financial risks.
- Customer adoption risks.
- Competitive risks.
- Operational and regulatory risks, where relevant.

Suggest mitigation strategies for each major risk.


## 12. Market Entry Strategy

Recommend:

- Initial target segment.
- Suitable launch location or market.
- Initial product offering.
- Customer acquisition approach.
- Partnership opportunities.
- First 90-day market entry priorities.


## 13. Final Research Assessment

Provide:

- Overall problem relevance.
- Market opportunity assessment.
- Customer demand hypotheses.
- Competitive positioning.
- Key risks.
- Most important assumptions to validate.
- Final recommendation: Proceed, Validate Further, or Reconsider.

Explain the reasoning behind the recommendation.


## 14. Research Limitations

Clearly mention:
- Information that could not be independently verified.
- Assumptions used in the analysis.
- Market data that needs external validation.
- Areas requiring additional research.


FINAL REQUIREMENT:

Make this report detailed, structured, practical,
and specific to the supplied startup idea.

Avoid unsupported claims and fabricated statistics.
Use Markdown headings, bullet points, and tables
where useful.
"""

    print("\nResearch Agent is analysing your startup idea...")

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
# 5. TEST RESEARCH AGENT
# ==========================================

if __name__ == "__main__":

    idea = (
        "An AI-powered platform that helps college students "
        "prepare for placements by analyzing resumes, identifying "
        "skill gaps, recommending personalized learning paths, "
        "generating role-specific interview questions, and "
        "matching students with suitable job opportunities."
    )

    result = research_agent(idea)

    print("\n========== STARTUP RESEARCH REPORT ==========\n")

    print(result)

    print("\n=============================================")
    print("Research Agent execution completed successfully!")
