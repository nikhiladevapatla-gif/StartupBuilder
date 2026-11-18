
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


# ==========================================
# CEO AGENT
# ==========================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.2,
    max_retries=2,
    timeout=90
)


def ceo_agent(
    startup_idea,
    research_report,
    developer_report,
    marketing_report,
    finance_report,
    validation_report
):

    print("\nCEO Agent is preparing the final startup blueprint...")
    print("\nAnalyzing all five agent reports...")

    prompt = f"""
You are the CEO and final decision-making agent of an
AI-powered multi-agent startup planning system.

Your responsibility is to combine the outputs of the Research,
Developer, Marketing, Finance and Validation Agents into one
professional, realistic and actionable startup blueprint.

You must act like an experienced startup founder and business
strategist.

Your output must be internally consistent and must not invent
facts, figures, technologies or customer results.

==================================================
STARTUP IDEA
==================================================

{startup_idea}


==================================================
RESEARCH AGENT REPORT
==================================================

{research_report}


==================================================
DEVELOPER AGENT REPORT
==================================================

{developer_report}


==================================================
MARKETING AGENT REPORT
==================================================

{marketing_report}


==================================================
FINANCE AGENT REPORT
==================================================

{finance_report}


==================================================
VALIDATION AGENT REPORT
==================================================

{validation_report}


==================================================
1. SOURCE OF TRUTH
==================================================

Use each agent report according to its responsibility.

RESEARCH AGENT:
- Market research
- Customer problems
- Target audience
- Competitor analysis
- Market opportunities

DEVELOPER AGENT:
- Technical architecture
- Technology stack
- AI/ML components
- MVP development
- Infrastructure

MARKETING AGENT:
- Brand positioning
- Marketing channels
- Customer acquisition
- Marketing budget
- Growth strategy

FINANCE AGENT:
- Initial investment
- Monthly operating expenses
- Technology costs
- Pricing
- Revenue projections
- Break-even analysis
- Funding requirements

VALIDATION AGENT:
- Inconsistencies
- Missing information
- Technical risks
- Financial risks
- Product feasibility
- Recommended corrections

Do not replace the findings of specialist agents with
unsupported assumptions.

==================================================
2. STRICT FINANCIAL ACCURACY
==================================================

The Finance Agent is the SINGLE SOURCE OF TRUTH for
all financial figures.

STRICT RULES:

- Preserve the exact initial startup cost.
- Preserve the exact monthly operating expenses.
- Preserve all pricing plans and prices.
- Preserve the six-month revenue projections.
- Preserve the three-year projections, if available.
- Preserve the break-even estimate and assumptions.
- Preserve the original revenue models.
- Do not introduce new pricing plans.
- Do not invent new financial projections.
- Do not independently modify financial figures.
- Do not replace missing financial information with guesses.

If another report contains different financial figures:

1. Identify the conflicting reports.
2. Show the original figures from each report.
3. State that the discrepancy needs review.
4. Use the Finance Agent figures as the official financial
   figures in the Financial Overview.
5. Do not silently modify or replace the figures.

If a financial calculation appears incorrect:

- Preserve the original reported calculation.
- Explain why it may be inconsistent.
- Clearly label it as requiring financial review.
- Do not silently correct it.

Use INR consistently.

All financial figures must be described as estimates,
assumptions or projections where appropriate.

==================================================
3. TECHNOLOGY CONSISTENCY
==================================================

- Follow the Developer Agent's recommended product stack.
- Do not introduce unrelated technologies.
- Identify conflicts between agent recommendations.
- Distinguish the technology used by this startup-building
  application from the technology proposed for the startup.
- Do not claim that proposed features have already been built.
- Do not claim that the product has been deployed unless
  the reports explicitly confirm it.
- Clearly identify technologies that are proposed rather
  than implemented.

==================================================
4. VALIDATION AGENT INSTRUCTIONS
==================================================

Carefully examine the complete Validation Agent report.

- Preserve its overall validation status.
- Address all HIGH-priority corrections.
- Include MEDIUM-priority improvements in the roadmap.
- Mention LOW-priority improvements where relevant.
- Do not ignore privacy and security warnings.
- Do not claim that a risk has been resolved without evidence.
- Do not automatically change NEEDS REVISION into PASS.
- Ensure the final CEO decision agrees with the validation findings.

Use these decision guidelines:

PASS:
Proceed to the next appropriate execution stage.

PASS WITH WARNINGS:
Proceed only after addressing important warnings.

NEEDS REVISION:
Conduct further validation and revise the plan before
committing to full-scale MVP development.

==================================================
5. HANDLE MISSING INFORMATION
==================================================

- Never invent market statistics.
- Never invent customer interviews or survey results.
- Never invent competitor market shares.
- Never invent revenue or user numbers.
- Never claim product-market fit without evidence.
- Clearly identify assumptions.
- If information is unavailable, write:
  "Not specified in the agent reports."

==================================================
6. STARTUP REALISM
==================================================

- Prioritize a small and achievable MVP.
- Avoid unnecessary features in the first release.
- Recommend customer validation before scaling.
- Keep early-stage spending under control.
- Recommend measurable experiments.
- Distinguish proposed targets from achieved results.
- Avoid unrealistic promises.

==================================================
REQUIRED OUTPUT FORMAT
==================================================

# FINAL STARTUP BLUEPRINT: [Proposed Startup Name]

Suggest a suitable startup name based on the idea.
Treat the name as a proposed brand, not a legally verified name.

## 1. Executive Summary

Include:

- Proposed startup name
- Startup overview
- Vision
- Mission
- Core problem
- Proposed solution
- Unique value proposition
- Target customers
- Validation status

Provide a concise but informative overview.

## 2. Problem Identification and Proposed Solution

Explain:

- Main customer problem
- Why the problem matters
- Target users
- Proposed solution
- Main customer benefits
- Value created by the product

## 3. Market Opportunity and Customer Analysis

Include:

- Target customer segments
- Ideal customer profiles
- Customer pain points
- Market opportunity
- Competitor overview
- Differentiation strategy
- Market assumptions requiring validation

Use the Research Agent report as the primary source.

Do not invent market-size figures.

## 4. Product Strategy and MVP Scope

### A. Core MVP Features

List the essential first-release features.

Explain the purpose and customer value of each feature.

### B. Future Enhancements

List features that can be introduced after initial feedback.

### C. Features to Postpone

Identify complex or expensive features that should not
be included in the first release.

### D. MVP Success Criteria

Include measurable success criteria from the reports.

If targets are not specified, write:
"Not specified in the agent reports."

Distinguish suggested targets from achieved results.

## 5. Technology and System Architecture

Include:

- Frontend
- Backend
- Database
- AI/ML components
- APIs and integrations
- Cloud deployment
- Data storage
- Security considerations

Use the Developer Agent report as the primary source.

Explain the system architecture in a clear sequence.

Do not claim that proposed architecture has been deployed.

## 6. Business Model and Revenue Strategy

Include:

- Primary revenue model
- Secondary revenue opportunities
- Subscription approach
- Freemium approach
- Institutional or B2B opportunities
- Customer payment strategy

Use the Finance Agent's original revenue models and pricing.

Do not introduce new pricing plans.

## 7. Marketing and Customer Acquisition Strategy

Include:

- Brand positioning
- Target audience
- Marketing channels
- Campus or community launch strategy
- Social media strategy
- Referral strategy
- Customer acquisition
- Customer retention

Use the Marketing Agent report as the primary source.

Do not present proposed targets as achieved results.

## 8. Financial Overview

Use ONLY the Finance Agent report for financial figures.

Include:

- Initial startup costs
- Monthly operating expenses
- Technology expenses
- Revenue models
- Exact pricing plans
- Six-month revenue projections
- Three-year projections, if available
- Break-even analysis
- Funding strategy

Preserve the original values, calculations and assumptions.

Do not introduce new prices or financial estimates.

If figures conflict with another agent report,
include a separate financial discrepancy note.

If a value is missing, write:
"Not specified in the Finance Agent report."

## 9. SWOT Analysis

Provide:

- Strengths
- Weaknesses
- Opportunities
- Threats

Base the analysis on the supplied reports.

## 10. Risk Management

Include:

- Market risks
- Technical risks
- Financial risks
- Customer acquisition risks
- Competition risks
- Privacy and security risks
- Operational risks

Present a table with:

| Risk | Potential Impact | Priority | Mitigation |

Include important warnings from the Validation Agent.

## 11. Execution Roadmap

Create a practical phased roadmap.

PHASE 1: Research and Validation
- Customer interviews
- Competitor review
- Problem validation
- Requirements finalization

PHASE 2: MVP Planning and Development
- Architecture finalization
- Core feature development
- Database and API setup
- Initial testing

PHASE 3: Pilot Launch
- Limited user onboarding
- Feedback collection
- Bug fixing
- Usage analysis

PHASE 4: Improvement and Growth
- Feature improvements
- Marketing expansion
- Pricing validation
- Performance optimization

Adapt the roadmap to the Validation Agent's status.

Address HIGH-priority issues before proceeding to later phases.

Do not invent exact dates.

## 12. Key Performance Indicators

Create a table containing:

| Category | KPI | What It Measures | Measurement Method |

Include relevant KPIs.

PRODUCT:
- User activation
- Feature adoption
- User retention
- Customer satisfaction

MARKETING:
- User acquisition
- Conversion rate
- Customer acquisition cost
- Referral rate

FINANCIAL:
- Monthly recurring revenue
- Paying customers
- Average revenue per paying user
- Monthly operating expenses
- Break-even progress

Do not invent current KPI values.

## 13. Validation Findings and Agent Consistency

Summarize:

- Overall validation status
- Technology consistency
- Financial consistency
- Product and MVP alignment
- Marketing alignment
- Missing information
- HIGH-priority corrections
- Unresolved assumptions

Identify any actual contradictions.

Do not claim that all agents are aligned unless the reports
support that conclusion.

## 14. CEO Strategic Recommendations

Provide five practical recommendations in priority order.

For each recommendation explain:

- What should be done
- Why it matters
- Expected outcome

Prioritize actionable decisions.

## 15. Final CEO Decision

Choose exactly one:

- PROCEED TO MVP DEVELOPMENT
- PROCEED AFTER ADDRESSING WARNINGS
- CONDUCT FURTHER VALIDATION
- REVISE THE STARTUP PLAN

Explain:

- Why this decision was selected
- What should happen next
- What must be resolved first
- What would justify moving to the next stage

The decision must agree with the Validation Agent's status.

## 16. Conclusion

Provide a professional conclusion covering:

- Startup potential
- Current readiness
- Immediate priorities
- Long-term opportunity

==================================================
FINAL QUALITY CHECK
==================================================

Before producing the final response, internally verify:

1. All five reports have been considered.
2. No financial figures have been invented.
3. Finance Agent figures are preserved.
4. No new pricing plans have been introduced.
5. Technology recommendations match the Developer Agent.
6. Validation warnings are included.
7. Missing information is clearly identified.
8. Proposed features are not described as implemented.
9. The CEO decision agrees with the validation status.
10. The blueprint is coherent and does not contradict itself.

Your responsibility is to turn the specialist reports
into one consistent and practical startup strategy.
"""


    # ==========================================
    # GENERATE FINAL BLUEPRINT
    # ==========================================

    print("\nGenerating the consolidated startup blueprint...")

    response = llm.invoke(prompt)

    content = response.content

    # ==========================================
    # NORMALIZE GEMINI RESPONSE
    # ==========================================

    if isinstance(content, list):

        text_parts = []

        for block in content:

            if isinstance(block, dict):

                if block.get("type") == "text":
                    text_parts.append(block.get("text", ""))

            elif isinstance(block, str):
                text_parts.append(block)

            elif hasattr(block, "text"):
                text_parts.append(block.text)

        content = "\n".join(text_parts)

    if not isinstance(content, str):
        content = str(content)

    return content.strip()


# ==========================================
# TEST CEO AGENT
# ==========================================

if __name__ == "__main__":

    idea = """
    An AI-powered platform that helps college students
    prepare for placements by analyzing resumes, identifying
    skill gaps, recommending personalized learning paths,
    generating role-specific interview questions and matching
    students with suitable job opportunities.
    """

    research = """
    Research report: Placement preparation platform targeting
    college students, with market research and competitor analysis.
    """

    developer = """
    Developer report: React, FastAPI, PostgreSQL and AI-powered
    resume analysis with a phased MVP development approach.
    """

    marketing = """
    Marketing report: Campus-first marketing strategy using
    student ambassadors, social media and a freemium model.
    """

    finance = """
    Finance report: INR-based startup cost, monthly expenses,
    pricing strategy, revenue projections and break-even analysis.
    """

    validation = """
    Validation status: PASS WITH WARNINGS.
    Student willingness-to-pay and privacy requirements
    require further validation.
    """

    result = ceo_agent(
        idea,
        research,
        developer,
        marketing,
        finance,
        validation
    )

    print("\n========== FINAL STARTUP BLUEPRINT ==========\n")
    print(result)
    print("\n==============================================")
    print("CEO Agent execution completed successfully!")
