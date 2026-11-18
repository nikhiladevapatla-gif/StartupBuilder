
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
# 3. DEVELOPER AGENT
# ==========================================

def developer_agent(startup_idea, research_report):

    prompt = f"""
You are a senior software architect, full-stack developer,
AI/ML engineer, database architect, and cloud solutions expert.

Your responsibility is to convert a startup idea and its
market research into a practical technical implementation plan.

The proposed solution must be realistic, scalable,
secure, and suitable for a student startup with a limited budget.

STARTUP IDEA:
{startup_idea}

MARKET RESEARCH REPORT:
{research_report}


IMPORTANT INSTRUCTIONS:

1. Understand the startup idea and research report carefully.
2. Recommend technologies that fit the actual requirements.
3. Prefer open-source and affordable technologies.
4. Explain why each major technology is recommended.
5. Avoid unnecessary complexity and overengineering.
6. Clearly distinguish proposed designs from implemented features.
7. Do not claim that code, APIs, models, or infrastructure
   have already been developed or tested.
8. Do not invent performance benchmarks or implementation results.
9. Identify assumptions wherever technical details are missing.


GENERATE THE REPORT USING THIS STRUCTURE:


# TECHNICAL DEVELOPMENT AND ARCHITECTURE REPORT


## 1. Technical Executive Summary

Explain:

- What the application will do.
- Main technical components.
- How users will interact with it.
- How data will flow through the system.
- Main technical objectives.
- Recommended implementation approach.


## 2. Functional Requirements

Identify the main application requirements.

### User Features
Explain the features available to normal users.

### Administrator Features
Explain administrative functionality.

### System Features
Explain authentication, notifications, data processing,
logging, and other background operations.

Separate essential MVP requirements from future enhancements.


## 3. System Architecture

Propose a suitable high-level architecture.

Explain the responsibilities of:

- Frontend.
- Backend.
- API layer.
- Authentication service.
- Database.
- AI/ML service.
- File storage.
- Notification service.
- Cloud infrastructure.

Describe how these components communicate.

Include a simple architecture diagram using Mermaid.

Use realistic architecture components and avoid unnecessary services.


## 4. Technology Stack Recommendations

Provide a comparison table containing:

| Layer | Recommended Technology | Purpose | Reason |

Cover:

- Frontend.
- Backend.
- Programming language.
- Database.
- AI/ML frameworks.
- Authentication.
- File storage.
- Cloud hosting.
- Development tools.
- Version control.

Mention affordable alternatives where appropriate.

Explain the final recommended stack.


## 5. MVP Feature Development

Identify the minimum features needed for the first usable version.

For each feature explain:

- Feature name.
- Purpose.
- User benefit.
- Implementation complexity.
- Priority: High, Medium, or Low.

Clearly separate:

- Must-have MVP features.
- Should-have features.
- Future enhancements.

Avoid building every proposed feature in the first release.


## 6. Database Architecture and Schema

Recommend a suitable database.

Design the main database tables.

For each table include:

- Table name.
- Important columns.
- Data types.
- Primary keys.
- Foreign keys.
- Relationships.

Consider tables such as:

- Users.
- UserProfiles.
- Sessions.
- Products or core application entities.
- Transactions or activity records, if relevant.
- Notifications.
- Feedback.

Adapt the schema to the actual startup idea.
Do not include irrelevant tables.

Explain the relationships between the tables.


## 7. API Design

Recommend the required REST API endpoints.

Present a table with:

| HTTP Method | Endpoint | Purpose | Authentication |

Include relevant operations for:

- User registration and login.
- User profile management.
- Core application features.
- AI/ML processing.
- Data retrieval.
- Notifications.
- Administrator operations.

Provide example request and response JSON for
two important endpoints.

Ensure the API design matches the proposed application.


## 8. AI AND MACHINE LEARNING INTEGRATION

If AI/ML is relevant, explain:

- Which features need AI.
- Suitable models or algorithms.
- Input data.
- Expected output.
- Model integration approach.
- Model evaluation methods.
- Inference workflow.

For each proposed AI feature, distinguish between
pretrained models, third-party APIs, and models that
would require custom training.

If AI/ML is not essential to a feature, do not force it.

Identify the simplest practical AI implementation
for the MVP.


## 9. Application Workflow

Explain the complete user journey step by step.

Include:

1. User registration.
2. Login and authentication.
3. Main application interaction.
4. Backend processing.
5. Database operations.
6. AI processing, where applicable.
7. Result generation.
8. User feedback.

Include a Mermaid sequence diagram showing the
main request and response flow.


## 10. Security and Data Privacy

Explain:

- Password hashing.
- Authentication and authorization.
- Input validation.
- API security.
- Database security.
- Secure file uploads.
- Data encryption.
- Rate limiting.
- Backup strategy.
- Privacy considerations.

Identify any relevant regulatory or data protection
requirements that need further verification.


## 11. Testing Strategy

Recommend:

- Unit testing.
- API testing.
- Integration testing.
- Frontend testing.
- Database testing.
- AI/ML evaluation.
- Security testing.
- User acceptance testing.

Mention suitable testing tools and explain
what each test should validate.


## 12. Deployment and Cloud Architecture

Explain:

- Development environment.
- Production environment.
- Frontend hosting.
- Backend hosting.
- Database hosting.
- File storage.
- Environment variables and secrets.
- CI/CD workflow.
- Monitoring and logging.
- Backup and recovery.

Recommend an affordable deployment strategy
for the initial MVP.

Mention how the application could scale later.


## 13. Technical Challenges and Solutions

Identify at least five realistic technical challenges.

For each provide:

- Challenge.
- Why it occurs.
- Potential impact.
- Recommended solution.

Consider scalability, data quality, API costs,
security, integration, and model reliability where relevant.


## 14. Development Roadmap

Create a phased implementation roadmap.

### Phase 1: Planning and Requirements
### Phase 2: UI/UX and Database Design
### Phase 3: Backend Development
### Phase 4: Frontend Development
### Phase 5: AI/ML Integration
### Phase 6: Testing and Debugging
### Phase 7: Deployment and MVP Launch

For each phase specify:

- Main tasks.
- Expected deliverables.
- Dependencies.
- Estimated duration.

Provide a realistic timeline for a small student team.


## 15. Future Scalability and Enhancements

Explain how the system can evolve with:

- More users.
- Increased data volume.
- Additional application features.
- Advanced AI models.
- Third-party integrations.
- Mobile applications.

Avoid introducing complex infrastructure before it is needed.


## 16. Final Technical Recommendations

Summarize:

- Recommended architecture.
- Final technology stack.
- Essential MVP features.
- Database choice.
- AI/ML approach.
- Deployment approach.
- Biggest technical risks.
- First five development tasks.

Provide a final technical feasibility assessment.


## 17. Assumptions and Technical Limitations

Clearly mention:

- Assumptions made due to missing requirements.
- Features requiring further clarification.
- Technologies requiring compatibility checks.
- External services requiring API access.
- Costs that need verification.
- Technical decisions that should be validated
  through an MVP prototype.


FINAL REQUIREMENTS:

Make the report detailed, practical, and specific
to the supplied startup idea.

Use Markdown headings, tables, bullet points,
JSON examples, and Mermaid diagrams where useful.

Do not fabricate implementation results.
Do not claim that the application has already been built.
"""


    print("\nDeveloper Agent is preparing the technical architecture...")

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
# 5. TEST DEVELOPER AGENT
# ==========================================

if __name__ == "__main__":

    idea = """
    An AI-powered platform that helps college students
    prepare for placements by analyzing resumes, identifying
    skill gaps, recommending personalized learning paths,
    generating role-specific interview questions, and
    matching students with suitable job opportunities.
    """

    sample_research = """
    Target customers: College students and recent graduates.

    Problem: Students struggle to identify skill gaps
    and prepare effectively for placement opportunities.

    Opportunity: An integrated career-readiness platform
    combining resume analysis, personalized learning,
    interview preparation, and job matching.

    Potential challenge: Competition from existing
    resume builders and career platforms.
    """

    result = developer_agent(idea, sample_research)

    print("\n========== TECHNICAL DEVELOPMENT REPORT ==========\n")

    print(result)

    print("\n==================================================")
    print("Developer Agent execution completed successfully!")
