
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
    temperature=0.3,
    timeout=60
)


# ==========================================
# 3. FINANCE AGENT
# ==========================================

def finance_agent(
    startup_idea,
    research_report,
    developer_report,
    marketing_report
):

    prompt = f"""
You are a senior startup financial analyst,
financial planning expert, startup investment advisor,
and business valuation consultant.

Your responsibility is to prepare a detailed,
realistic financial plan for the proposed startup.

The startup is assumed to be an early-stage business
being developed by a small student team in India.

All financial estimates must be expressed in
Indian Rupees (INR ₹).

STARTUP IDEA:
{startup_idea}

MARKET RESEARCH REPORT:
{research_report}

TECHNICAL DEVELOPMENT REPORT:
{developer_report}

MARKETING STRATEGY REPORT:
{marketing_report}


IMPORTANT FINANCIAL INSTRUCTIONS:

1. Use INR (₹) for all financial estimates.
2. Clearly distinguish assumptions from verified costs.
3. Do not invent actual vendor prices or quotations.
4. Use reasonable illustrative estimates for an early-stage startup.
5. Explain the assumptions behind every projection.
6. Show formulas and calculations wherever possible.
7. Avoid unrealistic revenue and growth predictions.
8. Consider free-tier and open-source technologies.
9. Do not assume the startup immediately receives funding.
10. Use the proposed technical architecture and marketing strategy
    when calculating expenses.
11. Clearly distinguish revenue, profit, and cash flow.
12. Account for AI API usage costs where applicable.
13. Do not treat unpaid student-founder work as a cash expense.
    Mention its opportunity cost separately where relevant.
14. Make projections illustrative, not guaranteed outcomes.


GENERATE THE REPORT USING THIS STRUCTURE:


# STARTUP FINANCIAL PLANNING AND INVESTMENT REPORT


## 1. Financial Executive Summary

Provide:

- Startup overview.
- Recommended revenue model.
- Estimated initial investment.
- Estimated monthly operating expenses.
- Potential revenue sources.
- Financial sustainability assessment.
- Major financial assumptions.

Summarize the financial feasibility of the startup.


## 2. Initial Startup Cost Estimation

Identify all one-time expenses required
to build and launch the startup.

Consider:

- Domain registration.
- Website development.
- UI/UX design.
- Backend development.
- Frontend development.
- Database setup.
- AI integration.
- Testing.
- Branding.
- Legal and registration expenses.
- Initial marketing.
- Miscellaneous expenses.

Present a table:

| Expense | Estimated Cost (₹) | Explanation |

Provide:

- Minimum budget.
- Recommended budget.
- Higher budget scenario.

Clearly identify expenses that can be avoided
by using student skills and open-source tools.


## 3. Monthly Operating Expenses

Estimate recurring expenses.

Include:

- Cloud hosting.
- Database hosting.
- AI API usage.
- File storage.
- Domain and software subscriptions.
- Marketing.
- Maintenance.
- Customer support.
- Payment gateway charges, where applicable.
- Other operational expenses.

Present a monthly expense table.

Calculate:

- Minimum monthly operating cost.
- Expected monthly operating cost.
- Higher usage monthly cost.

Separate fixed costs from variable costs.


## 4. Technology Cost Analysis

Use the technology stack proposed by the Developer Agent.

Evaluate:

- Frontend hosting.
- Backend hosting.
- Database.
- AI/LLM APIs.
- Storage.
- Authentication.
- Monitoring.
- Development tools.

For each identify:

- Recommended option.
- Free or low-cost alternatives.
- Potential cost drivers.
- Conditions that may increase costs.

Do not claim that free tiers are unlimited.

Clearly mention that vendor pricing must be checked
before actual deployment.


## 5. Revenue Model Analysis

Suggest at least three suitable revenue models.

Consider:

- Freemium subscriptions.
- Monthly or annual premium plans.
- University licensing.
- B2B partnerships.
- Premium interview preparation.
- Recruitment or placement partnerships, where appropriate.

For each explain:

- How revenue is generated.
- Target paying customer.
- Advantages.
- Limitations.
- Implementation complexity.

Recommend the most suitable initial revenue model.


## 6. Pricing Strategy

Suggest affordable pricing suitable for Indian college students.

Consider:

- Free plan.
- Basic premium plan.
- Advanced premium plan.
- University or institutional plan.

Present a pricing table:

| Plan | Illustrative Price (₹) | Features | Target Customer |

Explain the reasoning behind the pricing.

Consider willingness-to-pay validation before
finalizing actual prices.

Clearly label all prices as proposed assumptions.


## 7. Six-Month Revenue Projections

Prepare three financial scenarios:

### Conservative Scenario
### Moderate Scenario
### Optimistic Scenario

For each scenario estimate:

- Total registered users.
- Active users.
- Paying users.
- Conversion rate.
- Average revenue per paying user.
- Monthly revenue.
- Total six-month revenue.

Present month-by-month projections.

Show the assumptions used to estimate user growth
and subscription conversion.

Ensure revenue calculations are mathematically consistent.

Do not present projections as guaranteed outcomes.


## 8. Three-Year Financial Projection

Prepare an illustrative three-year forecast.

Include:

- Revenue.
- Operating expenses.
- Gross profit, where applicable.
- Operating profit or loss.
- Major growth assumptions.

Present a table with Year 1, Year 2, and Year 3.

Explain what must happen for the startup
to achieve the projected growth.


## 9. Break-Even Analysis

Calculate the number of paying customers
required to cover monthly operating expenses.

Use:

Break-even customers =
Monthly fixed costs /
Contribution per paying customer

Account for variable costs per paying customer.

Show at least two pricing scenarios.

Explain:

- Monthly break-even revenue.
- Break-even customer count.
- Factors that could delay break-even.


## 10. Profit and Loss Analysis

Prepare an illustrative profit and loss statement.

Include:

- Revenue.
- Variable expenses.
- Gross profit.
- Fixed operating expenses.
- Marketing expenses.
- Other operating expenses.
- Operating profit or loss.

Explain the difference between
revenue and actual profit.

Mention that taxes, depreciation, and other accounting
items require professional review where applicable.


## 11. Cash Flow Planning

Explain:

- Initial capital requirements.
- Monthly cash outflows.
- Expected customer receipts.
- Working capital.
- Cash reserves.
- Potential cash shortages.

Provide a simple illustrative six-month cash flow table.

Clearly distinguish cash flow from accounting profit.


## 12. Funding Requirements and Strategy

Estimate the amount of initial funding required.

Explore:

- Founder bootstrapping.
- College incubation centers.
- Startup competitions.
- Government startup support schemes.
- Angel investors.
- Accelerator programs.
- Strategic partnerships.

Explain the advantages and limitations
of each funding option.

Recommend the most suitable initial funding approach
for a student-founded startup in India.

Do not guarantee eligibility for any funding scheme.


## 13. Startup Valuation Considerations

Explain the factors that influence early-stage valuation:

- Product readiness.
- Market opportunity.
- User growth.
- Revenue.
- Retention.
- Competitive differentiation.
- Technology and intellectual property.

Explain why an early-stage valuation may be highly uncertain.

Do not invent a definitive company valuation.


## 14. Financial Risk Analysis

Identify financial risks such as:

- High AI API costs.
- Low customer conversion.
- High customer acquisition cost.
- Unexpected cloud expenses.
- Low retention.
- Delayed revenue.
- Dependence on third-party vendors.

For each explain:

- Risk.
- Financial impact.
- Probability assessment.
- Mitigation strategy.

Clearly label probability assessments as qualitative estimates.


## 15. Budget Optimization Strategy

Suggest practical ways to reduce costs.

Consider:

- Open-source frameworks.
- Free development tools.
- Student developer resources.
- Usage-based cloud services.
- AI token optimization.
- Caching.
- Limited MVP features.
- Organic marketing.
- Partnerships with universities.

Identify the expenses that should not be reduced
at the cost of security or reliability.


## 16. Financial Milestones

Define financial milestones for:

### First 30 Days
### First 60 Days
### First 90 Days
### First 6 Months
### First 12 Months

Include:

- Budget milestones.
- Revenue validation.
- Customer payment validation.
- Cost optimization.
- Funding preparation.

Avoid unrealistic revenue targets.


## 17. Final Financial Recommendations

Summarize:

- Recommended initial investment.
- Monthly operating budget.
- Best revenue model.
- Proposed pricing.
- Expected break-even requirements.
- Funding strategy.
- Main financial risks.
- First five financial actions.

Provide an overall financial feasibility assessment.


## 18. Financial Assumptions and Limitations

Clearly mention:

- Estimated rather than quoted vendor costs.
- Assumed customer growth.
- Assumed conversion rates.
- Assumed subscription prices.
- Unverified willingness to pay.
- Taxes and regulatory costs requiring verification.
- Financial projections requiring validation.

Mention that all projections are planning scenarios,
not guaranteed financial outcomes.


FINAL REQUIREMENTS:

Generate a detailed and professional financial report.

Use INR (₹) consistently.

Use Markdown headings, tables, and formulas.

Show calculations clearly.

Ensure all projections are internally consistent.

Do not fabricate vendor quotations,
market statistics, or guaranteed financial results.

Make the recommendations practical for a
student startup operating in India.
"""

    print("\nFinance Agent is preparing your financial plan...")

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
# 5. TEST FINANCE AGENT
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
    platform combining resume analysis, personalized learning,
    interview preparation, and job matching.

    Revenue opportunity: Student subscriptions and
    university partnerships.
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

    marketing = """
    Recommended strategy:

    Campus-first marketing.
    Student ambassador program.
    Instagram and LinkedIn campaigns.
    WhatsApp student communities.
    Free resume analysis as a lead magnet.

    Initial launch through a university campus.
    """

    result = finance_agent(
        idea,
        research,
        developer,
        marketing
    )

    print("\n========== STARTUP FINANCIAL REPORT ==========\n")

    print(result)

    print("\n==============================================")
    print("Finance Agent execution completed successfully!")
