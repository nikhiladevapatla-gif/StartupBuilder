
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


# ==========================================
# VALIDATION AGENT
# ==========================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.1,
    max_retries=2,
    timeout=90
)


def validation_agent(
    startup_idea,
    research_report,
    developer_report,
    marketing_report,
    finance_report
):

    print("\nValidation Agent is checking all agent reports...")

    prompt = f"""
You are a senior startup auditor, product strategist,
technical reviewer and financial validation expert.

Your responsibility is to critically evaluate the outputs
of the Research, Developer, Marketing and Finance Agents.

You must identify inconsistencies, unrealistic assumptions,
missing information, execution risks and recommendations.

Do not rewrite the original reports.

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
VALIDATION TASKS
==================================================

1. MARKET AND BUSINESS VALIDATION

- Check whether the identified customer problem is clear.
- Evaluate whether the target audience matches the proposed solution.
- Check whether the proposed value proposition is differentiated.
- Identify unsupported market-size or demand claims.
- Check whether competitor analysis is sufficiently addressed.
- Identify assumptions that require customer interviews or surveys.
- Evaluate whether the business model can realistically generate revenue.

2. TECHNICAL VALIDATION

- Check whether the proposed technology stack is consistent.
- Identify incompatible or unnecessarily duplicated technologies.
- Check whether the proposed architecture supports the MVP.
- Evaluate whether AI/ML features are technically realistic.
- Identify missing integrations and infrastructure requirements.
- Check whether the proposed development timeline is achievable.
- Evaluate data security, privacy and access control.
- Distinguish the technology used by this multi-agent system
  from the technology proposed for the startup product.

3. FINANCIAL VALIDATION

- Compare initial investment and monthly operating expenses.
- Check whether the pricing strategy is consistent across reports.
- Verify arithmetic in financial tables wherever possible.
- Check whether revenue projections match the stated number
  of paying users and average revenue per user.
- Examine break-even calculations and contribution margins.
- Check whether AI API usage costs are adequately considered.
- Identify missing expenses such as payment gateway charges,
  customer support, taxes and maintenance where relevant.
- Identify unrealistic growth or profitability assumptions.
- Do not invent financial figures.
- If a calculation cannot be verified, explain why.

4. PRODUCT AND MVP VALIDATION

- Check whether the MVP features are consistent across reports.
- Identify features that should be postponed until later versions.
- Evaluate whether the MVP solves the main customer problem.
- Check whether the proposed features can be delivered
  within the estimated development timeline.
- Identify unnecessary complexity.
- Recommend a realistic MVP scope.

5. MARKETING VALIDATION

- Check whether the marketing strategy reaches the target users.
- Evaluate whether the proposed acquisition channels are suitable.
- Check whether the marketing budget matches the strategy.
- Examine customer acquisition and conversion assumptions.
- Check whether the pricing and promotional strategy are aligned.
- Identify unrealistic user-growth targets.
- Recommend measurable early-stage marketing experiments.

6. PRIVACY, SECURITY AND LEGAL VALIDATION

- Check whether user data protection is addressed.
- Identify risks associated with storing resumes and personal data.
- Check whether consent, data retention and deletion policies
  have been considered.
- Identify potential legal and regulatory requirements
  that require professional verification.
- Do not claim legal compliance without evidence.

7. CROSS-AGENT CONSISTENCY

Compare all four reports and identify:

- Conflicting technology recommendations.
- Different product feature descriptions.
- Different target customer definitions.
- Inconsistent pricing.
- Different budget estimates.
- Unrealistic development and marketing timelines.
- Financial projections unsupported by marketing assumptions.
- Missing dependencies between proposed features.

Do not automatically treat different recommendations as conflicts.
Explain whether each difference is an actual contradiction,
a reasonable alternative or an assumption requiring clarification.

8. RISK ASSESSMENT

Evaluate the following categories:

- Market and customer risk.
- Technical and implementation risk.
- Financial and cash-flow risk.
- Marketing and customer acquisition risk.
- Competition risk.
- Privacy and security risk.
- Operational and scalability risk.

For every major risk, explain its impact and a practical mitigation.

9. RECOMMENDED CORRECTIONS

Provide specific corrections in priority order.

Classify each correction as:

- HIGH: Must be addressed before MVP launch.
- MEDIUM: Should be addressed during MVP development.
- LOW: Can be addressed after initial validation.

Do not rewrite the complete reports.

10. VALIDATION SCORECARD

Give a score from 1 to 10 for:

- Market readiness.
- Technical feasibility.
- Financial feasibility.
- Product clarity.
- Marketing readiness.
- Risk management.

Explain each score briefly.

Do not give high scores without supporting evidence.
If information is missing, reduce the score and explain why.

==================================================
OUTPUT FORMAT
==================================================

# STARTUP VALIDATION REPORT

## 1. Executive Validation Summary

Summarize the overall quality of the startup plan.

## 2. Market and Business Validation

## 3. Technical Consistency and Feasibility

## 4. Financial Consistency and Calculation Checks

Include a table with:
- Item checked
- Reported information
- Validation result
- Required action

## 5. Product and MVP Validation

## 6. Marketing Validation

## 7. Privacy, Security and Legal Considerations

## 8. Cross-Agent Inconsistencies

Include a table with:
- Agent reports involved
- Identified issue
- Why it matters
- Recommended correction

If no major conflict exists, state that clearly.

## 9. Risk Assessment

Include risk, potential impact, severity and mitigation.

## 10. Recommended Corrections

Separate recommendations into HIGH, MEDIUM and LOW priority.

## 11. Validation Scorecard

Show all six scores and explain them.

## 12. Overall Validation Status

Choose exactly one:

PASS:
No major inconsistencies or critical gaps identified.

PASS WITH WARNINGS:
The startup plan is broadly consistent, but some assumptions
or gaps need attention.

NEEDS REVISION:
Major inconsistencies, feasibility problems or missing
information must be addressed before proceeding.

Explain the decision and identify the most important next steps.

## 13. Final Validator Recommendation

Give a practical recommendation on whether the startup
should proceed to MVP development, conduct further market
validation, or revise its plan first.

==================================================
STRICT VALIDATION RULES
==================================================

- Evaluate the supplied reports, not an imaginary startup.
- Never invent market research, vendor prices or customer data.
- Do not present assumptions as verified facts.
- Use INR when discussing financial information.
- Treat all financial projections as estimates.
- Do not silently correct figures; identify errors explicitly.
- Do not mark missing information as a confirmed failure.
- Clearly distinguish actual contradictions from alternatives.
- Be objective, critical and practical.
- Avoid generic praise and unsupported high scores.
- If information is unavailable, write "Not specified".
- Keep recommendations actionable and specific.
"""

    response = llm.invoke(prompt)

    content = response.content

    # Normalize Gemini response into a plain string
    if isinstance(content, list):
        text_parts = []

        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
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
# TEST VALIDATION AGENT
# ==========================================

if __name__ == "__main__":

    idea = """
    An AI-powered platform that helps college students
    prepare for placements by analyzing resumes, identifying
    skill gaps, recommending personalized learning paths,
    generating role-specific interview questions and matching
    students with suitable job opportunities.
    """

    research = "Research report: Placement preparation platform with student target audience."

    developer = "Developer report: React, FastAPI, PostgreSQL and AI-powered resume analysis."

    marketing = "Marketing report: Campus-first strategy with student ambassadors and freemium model."

    finance = "Finance report: INR-based pricing, operating expenses and revenue projections."

    result = validation_agent(
        idea,
        research,
        developer,
        marketing,
        finance
    )

    print("\n========== STARTUP VALIDATION REPORT ==========\n")
    print(result)
    print("\n===============================================")
    print("Validation Agent execution completed successfully!")
