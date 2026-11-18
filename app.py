
import os
import re
import io
import html
import time
from datetime import datetime

import streamlit as st

from workflow import run_startup_workflow_with_progress


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Multi-Agent Startup Builder",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# 2. DARK THEME + REPORT PRESENTATION CSS
# ============================================================

st.markdown(
    """
    <style>
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    [data-testid="stMain"] {
        background-color: #080D19 !important;
        color: #FFFFFF !important;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3, h4, h5 {
        color: #FFFFFF !important;
        font-weight: 800 !important;
    }

    h1 { font-size: 2.4rem !important; }
    h2 { font-size: 1.65rem !important; }
    h3 { font-size: 1.15rem !important; }

    p, li, label, span {
        color: #D1D9E6;
    }

    [data-testid="stMarkdownContainer"] p {
        color: #C2CDDC;
        line-height: 1.65;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #111C2E !important;
        border: 1px solid #293B55 !important;
        border-radius: 14px !important;
    }

    [data-testid="stMetric"] {
        background-color: #111C2E !important;
        border: 1px solid #293B55 !important;
        border-radius: 13px !important;
        padding: 18px !important;
    }

    [data-testid="stMetricLabel"] {
        color: #AAB8CC !important;
        font-weight: 700 !important;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: 900 !important;
    }

    [data-testid="stMetricDelta"] {
        color: #AAB8CC !important;
    }

    [data-testid="stTextArea"] label {
        color: #FFFFFF !important;
        font-weight: 800 !important;
    }

    [data-testid="stTextArea"] textarea {
        background-color: #111C2E !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        border: 1px solid #3B4D68 !important;
        border-radius: 11px !important;
        font-size: 15px !important;
        padding: 14px !important;
        caret-color: #FFFFFF !important;
    }

    [data-testid="stTextArea"] textarea::placeholder {
        color: #94A3B8 !important;
        -webkit-text-fill-color: #94A3B8 !important;
        opacity: 1 !important;
    }

    [data-testid="stTextArea"] textarea:focus {
        border: 1px solid #6488C5 !important;
        box-shadow: 0 0 0 1px #6488C5 !important;
    }

    .stButton > button,
    .stDownloadButton > button {
        background-color: #344F85 !important;
        color: #FFFFFF !important;
        border: 1px solid #506D9F !important;
        border-radius: 10px !important;
        font-weight: 800 !important;
        min-height: 44px;
        transition: 0.2s ease;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        background-color: #45649A !important;
        color: #FFFFFF !important;
        border: 1px solid #7895C4 !important;
    }

    .stButton > button p,
    .stDownloadButton > button p {
        color: #FFFFFF !important;
    }

    [data-testid="stVerticalBlockBorderWrapper"] h3 {
        color: #FFFFFF !important;
    }

    [data-testid="stVerticalBlockBorderWrapper"] p {
        color: #AAB8CC !important;
    }

    [data-baseweb="tab-list"] {
        background-color: #111C2E !important;
        border-radius: 10px !important;
        gap: 5px !important;
    }

    button[data-baseweb="tab"] {
        color: #B7C4D6 !important;
        font-weight: 700 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #FFFFFF !important;
        border-bottom: 3px solid #6488C5 !important;
    }

    [data-testid="stTabContent"] {
        background-color: #0D1626 !important;
        border: 1px solid #293B55 !important;
        border-radius: 10px !important;
        padding: 20px !important;
    }

    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMarkdownContainer"] h4 {
        color: #FFFFFF !important;
    }

    [data-testid="stMarkdownContainer"] strong {
        color: #FFFFFF !important;
    }

    [data-testid="stMarkdownContainer"] li {
        color: #D1D9E6 !important;
    }

    [data-testid="stMarkdownContainer"] table {
        width: 100%;
        border-collapse: collapse;
        border: 1px solid #344968;
    }

    [data-testid="stMarkdownContainer"] th {
        background-color: #1B2C46 !important;
        color: #FFFFFF !important;
        padding: 12px !important;
    }

    [data-testid="stMarkdownContainer"] td {
        color: #D1D9E6 !important;
        padding: 10px !important;
        border-bottom: 1px solid #293B55 !important;
    }

    [data-testid="stMarkdownContainer"] blockquote {
        border-left: 4px solid #6488C5;
        background-color: #14233A;
        padding: 12px 18px;
        border-radius: 5px;
    }

    [data-testid="stProgressBar"] {
        background-color: #263449 !important;
    }

    [data-testid="stProgressBar"] > div > div {
        background-color: #6488C5 !important;
    }

    [data-testid="stAlert"] {
        border-radius: 10px !important;
    }

    [data-testid="stAlert"] p {
        color: #FFFFFF !important;
    }

    hr {
        border-color: #293B55 !important;
    }

    .footer-note {
        color: #94A3B8;
        text-align: center;
        font-size: 13px;
    }

    .report-label {
        color: #8FAFE4;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 3. CONSTANTS
# ============================================================

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


AGENTS = [
    {
        "key": "research",
        "name": "Research Agent",
        "icon": "🔍",
        "description": "Analyses the market, competitors and target customers."
    },
    {
        "key": "developer",
        "name": "Developer Agent",
        "icon": "💻",
        "description": "Creates the technical architecture and development roadmap."
    },
    {
        "key": "marketing",
        "name": "Marketing Agent",
        "icon": "📢",
        "description": "Plans branding, marketing and customer acquisition."
    },
    {
        "key": "finance",
        "name": "Finance Agent",
        "icon": "💰",
        "description": "Estimates startup costs, revenue and profitability."
    },
    {
        "key": "validation",
        "name": "Validation Agent",
        "icon": "✅",
        "description": "Evaluates feasibility, risks and startup readiness."
    },
    {
        "key": "ceo",
        "name": "CEO Agent",
        "icon": "👔",
        "description": "Combines all reports into the final startup blueprint."
    }
]


REPORT_DETAILS = [
    ("Research Report", "research_report"),
    ("Developer Report", "developer_report"),
    ("Marketing Report", "marketing_report"),
    ("Finance Report", "finance_report"),
    ("Validation Report", "validation_report"),
    ("Final Startup Blueprint", "final_report")
]


# ============================================================
# 4. REPORT PRESENTATION HELPERS
# ============================================================

def get_executive_summary(report_text, max_paragraphs=2):
    """
    Extract the first meaningful paragraphs from a report.
    This is a preview of the report, not a newly generated summary.
    """

    if not report_text:
        return "No executive summary is available."

    paragraphs = []
    current_paragraph = []

    for raw_line in str(report_text).splitlines():

        line = raw_line.strip()

        if not line:
            if current_paragraph:
                paragraphs.append(" ".join(current_paragraph))
                current_paragraph = []
            continue

        if (
            line.startswith("#")
            or line.startswith(("- ", "* ", "> "))
            or re.match(r"^\d+[.)]\s+", line)
            or line.startswith("|")
            or line in ("---", "***", "___")
        ):
            continue

        current_paragraph.append(line)

    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph))

    meaningful = [
        paragraph for paragraph in paragraphs
        if len(paragraph) > 35
    ]

    if not meaningful:
        return (
            "The complete report is available below. "
            "Review the blueprint for detailed information."
        )

    return "\n\n".join(meaningful[:max_paragraphs])


def safe_float(value, default=0.0):
    """Safely convert a value to a float."""

    try:
        return float(value)
    except (TypeError, ValueError):
        return default


# ============================================================
# 5. PDF GENERATION
# ============================================================

def create_pdf(
    report_text,
    title="Startup Report",
    executive_summary=None
):

    try:
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import (
            getSampleStyleSheet,
            ParagraphStyle
        )
        from reportlab.lib.units import inch
        from reportlab.platypus import (
            SimpleDocTemplate,
            Paragraph,
            Spacer,
            PageBreak,
            HRFlowable,
            KeepTogether,
            Table,
            TableStyle
        )

        buffer = io.BytesIO()

        document = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=0.7 * inch,
            leftMargin=0.7 * inch,
            topMargin=0.8 * inch,
            bottomMargin=0.7 * inch,
            title=title,
            author="Multi-Agent Startup Builder"
        )

        styles = getSampleStyleSheet()

        NAVY = colors.HexColor("#080D19")
        BLUE = colors.HexColor("#6488C5")
        DARK_BLUE = colors.HexColor("#172A4D")
        LIGHT_GREY = colors.HexColor("#64748B")
        BODY_COLOR = colors.HexColor("#263449")
        TABLE_BORDER = colors.HexColor("#CBD5E1")

        cover_title = ParagraphStyle(
            "CoverTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=29,
            leading=38,
            textColor=colors.white,
            alignment=TA_CENTER,
            spaceAfter=20
        )

        cover_subtitle = ParagraphStyle(
            "CoverSubtitle",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=13,
            leading=21,
            textColor=colors.HexColor("#CBD5E1"),
            alignment=TA_CENTER
        )

        section_title = ParagraphStyle(
            "SectionTitle",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=19,
            leading=25,
            textColor=DARK_BLUE,
            spaceBefore=14,
            spaceAfter=12,
            keepWithNext=True
        )

        heading_style = ParagraphStyle(
            "ReportHeading",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=17,
            textColor=BLUE,
            spaceBefore=13,
            spaceAfter=7,
            keepWithNext=True
        )

        body_style = ParagraphStyle(
            "ReportBody",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=14,
            textColor=BODY_COLOR,
            alignment=TA_LEFT,
            spaceAfter=7
        )

        bullet_style = ParagraphStyle(
            "ReportBullet",
            parent=body_style,
            leftIndent=17,
            firstLineIndent=-10,
            spaceAfter=5
        )

        contents_style = ParagraphStyle(
            "ContentsItem",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=18,
            textColor=BODY_COLOR,
            leftIndent=10,
            spaceAfter=5
        )

        summary_style = ParagraphStyle(
            "SummaryBody",
            parent=body_style,
            fontSize=10,
            leading=17,
            spaceAfter=10
        )

        table_header_style = ParagraphStyle(
            "TableHeader",
            parent=body_style,
            fontName="Helvetica-Bold",
            fontSize=8,
            leading=11,
            textColor=colors.white
        )

        table_body_style = ParagraphStyle(
            "TableBody",
            parent=body_style,
            fontSize=8,
            leading=11
        )

        def draw_cover(canvas, doc):

            canvas.saveState()
            width, height = A4

            canvas.setFillColor(NAVY)
            canvas.rect(0, 0, width, height, fill=1, stroke=0)

            canvas.setFillColor(BLUE)
            canvas.rect(
                0,
                height - 0.18 * inch,
                width,
                0.18 * inch,
                fill=1,
                stroke=0
            )

            canvas.setStrokeColor(colors.HexColor("#344F85"))
            canvas.setLineWidth(1)

            canvas.roundRect(
                0.55 * inch,
                0.55 * inch,
                width - 1.1 * inch,
                height - 1.1 * inch,
                14,
                fill=0,
                stroke=1
            )

            canvas.setFillColor(colors.HexColor("#94A3B8"))
            canvas.setFont("Helvetica-Bold", 10)

            canvas.drawCentredString(
                width / 2,
                0.9 * inch,
                "AI-POWERED STARTUP PLANNING WORKSPACE"
            )

            canvas.restoreState()

        def draw_content(canvas, doc):

            canvas.saveState()
            width, height = A4

            canvas.setFillColor(NAVY)
            canvas.rect(
                0,
                height - 0.12 * inch,
                width,
                0.12 * inch,
                fill=1,
                stroke=0
            )

            canvas.setFont("Helvetica-Bold", 8)
            canvas.setFillColor(DARK_BLUE)

            canvas.drawString(
                0.7 * inch,
                height - 0.48 * inch,
                "MULTI-AGENT STARTUP BUILDER"
            )

            canvas.setStrokeColor(colors.HexColor("#CBD5E1"))
            canvas.line(
                0.7 * inch,
                0.58 * inch,
                width - 0.7 * inch,
                0.58 * inch
            )

            canvas.setFont("Helvetica", 8)
            canvas.setFillColor(LIGHT_GREY)

            canvas.drawString(
                0.7 * inch,
                0.4 * inch,
                "Confidential Startup Planning Report"
            )

            canvas.drawRightString(
                width - 0.7 * inch,
                0.4 * inch,
                f"Page {doc.page}"
            )

            canvas.restoreState()

        def format_inline(text):

            text = html.escape(str(text))

            text = re.sub(
                r"\*\*(.*?)\*\*",
                r"<b>\1</b>",
                text
            )

            text = re.sub(
                r"(?<!\*)\*([^*]+)\*(?!\*)",
                r"<i>\1</i>",
                text
            )

            text = re.sub(
                r"`([^`]+)`",
                r'<font name="Courier">\1</font>',
                text
            )

            return text

        def parse_table_row(line):

            cells = line.strip().strip("|").split("|")

            return [cell.strip() for cell in cells]

        story = [
            Spacer(1, 2.6 * inch),

            Paragraph(
                "MULTI-AGENT<br/>STARTUP BUILDER",
                cover_title
            ),

            HRFlowable(
                width="35%",
                thickness=2,
                color=BLUE,
                hAlign="CENTER",
                spaceBefore=8,
                spaceAfter=25
            ),

            Paragraph(
                html.escape(title),
                cover_subtitle
            ),

            Spacer(1, 0.35 * inch),

            Paragraph(
                "A Comprehensive AI-Generated Startup Proposal",
                cover_subtitle
            ),

            Spacer(1, 2.0 * inch),

            Paragraph(
                datetime.now().strftime("%d %B %Y"),
                cover_subtitle
            ),

            PageBreak()
        ]

        # ----------------------------------------------------
        # EXECUTIVE SUMMARY PAGE
        # ----------------------------------------------------

        if executive_summary:

            story.append(
                Paragraph("EXECUTIVE SUMMARY", section_title)
            )

            story.append(
                HRFlowable(
                    width="100%",
                    thickness=1.5,
                    color=BLUE,
                    spaceAfter=15
                )
            )

            for paragraph in str(executive_summary).split("\n\n"):

                if paragraph.strip():

                    story.append(
                        Paragraph(
                            format_inline(paragraph.strip()),
                            summary_style
                        )
                    )

            story.append(PageBreak())

        # ----------------------------------------------------
        # TABLE OF CONTENTS
        # ----------------------------------------------------

        headings = []

        for raw_line in str(report_text).splitlines():

            line = raw_line.strip()

            if line.startswith("#"):

                heading = re.sub(
                    r"^#+\s*",
                    "",
                    line
                ).strip()

                if heading and heading not in headings:
                    headings.append(heading)

        story.append(
            Paragraph("TABLE OF CONTENTS", section_title)
        )

        story.append(
            HRFlowable(
                width="100%",
                thickness=1,
                color=BLUE,
                spaceAfter=15
            )
        )

        if headings:

            for heading in headings:

                story.append(
                    Paragraph(
                        "&#8226;&nbsp;&nbsp;" + format_inline(heading),
                        contents_style
                    )
                )

        else:

            story.append(
                Paragraph(
                    "Startup report sections",
                    contents_style
                )
            )

        story.append(PageBreak())

        # ----------------------------------------------------
        # REPORT CONTENT
        # ----------------------------------------------------

        lines = str(report_text).splitlines()
        index = 0

        while index < len(lines):

            line = lines[index].strip()

            if not line:
                story.append(Spacer(1, 4))
                index += 1
                continue

            # Markdown table
            if line.startswith("|"):

                table_lines = []

                while (
                    index < len(lines)
                    and lines[index].strip().startswith("|")
                ):
                    table_lines.append(lines[index].strip())
                    index += 1

                rows = []

                for table_line in table_lines:

                    if re.match(
                        r"^\|?[\s:|-]+\|?$",
                        table_line
                    ):
                        continue

                    rows.append(parse_table_row(table_line))

                if rows:

                    column_count = max(
                        len(row) for row in rows
                    )

                    table_data = []

                    for row_index, row in enumerate(rows):

                        row = row + [""] * (
                            column_count - len(row)
                        )

                        style = (
                            table_header_style
                            if row_index == 0
                            else table_body_style
                        )

                        table_data.append([
                            Paragraph(
                                format_inline(cell),
                                style
                            )
                            for cell in row
                        ])

                    report_table = Table(
                        table_data,
                        colWidths=[
                            document.width / column_count
                        ] * column_count,
                        repeatRows=1,
                        hAlign="LEFT"
                    )

                    report_table.setStyle(
                        TableStyle([
                            (
                                "BACKGROUND",
                                (0, 0),
                                (-1, 0),
                                DARK_BLUE
                            ),
                            (
                                "TEXTCOLOR",
                                (0, 0),
                                (-1, 0),
                                colors.white
                            ),
                            (
                                "GRID",
                                (0, 0),
                                (-1, -1),
                                0.5,
                                TABLE_BORDER
                            ),
                            (
                                "VALIGN",
                                (0, 0),
                                (-1, -1),
                                "TOP"
                            ),
                            (
                                "LEFTPADDING",
                                (0, 0),
                                (-1, -1),
                                7
                            ),
                            (
                                "RIGHTPADDING",
                                (0, 0),
                                (-1, -1),
                                7
                            ),
                            (
                                "TOPPADDING",
                                (0, 0),
                                (-1, -1),
                                7
                            ),
                            (
                                "BOTTOMPADDING",
                                (0, 0),
                                (-1, -1),
                                7
                            ),
                            (
                                "BACKGROUND",
                                (0, 1),
                                (-1, -1),
                                colors.HexColor("#F8FAFC")
                            )
                        ])
                    )

                    story.append(Spacer(1, 6))
                    story.append(report_table)
                    story.append(Spacer(1, 10))

                continue

            # Main heading
            if line.startswith("# "):

                heading = line[2:].strip()

                story.append(
                    KeepTogether([
                        Paragraph(
                            format_inline(heading),
                            section_title
                        ),
                        HRFlowable(
                            width="100%",
                            thickness=1,
                            color=TABLE_BORDER,
                            spaceAfter=9
                        )
                    ])
                )

            # Subheadings
            elif line.startswith("## ") or line.startswith("### "):

                heading = re.sub(
                    r"^#{2,3}\s*",
                    "",
                    line
                ).strip()

                story.append(
                    Paragraph(
                        format_inline(heading),
                        heading_style
                    )
                )

            # Bullets
            elif line.startswith(("- ", "* ")):

                content = format_inline(line[2:].strip())

                story.append(
                    Paragraph(
                        "&#8226;&nbsp;&nbsp;" + content,
                        bullet_style
                    )
                )

            # Numbered lists
            elif re.match(r"^\d+[.)]\s+", line):

                story.append(
                    Paragraph(
                        format_inline(line),
                        bullet_style
                    )
                )

            # Horizontal rules
            elif line in ("---", "***", "___"):

                story.append(
                    HRFlowable(
                        width="100%",
                        thickness=0.7,
                        color=TABLE_BORDER,
                        spaceBefore=5,
                        spaceAfter=9
                    )
                )

            # Normal paragraph
            else:

                story.append(
                    Paragraph(
                        format_inline(line),
                        body_style
                    )
                )

            index += 1

        document.build(
            story,
            onFirstPage=draw_cover,
            onLaterPages=draw_content
        )

        buffer.seek(0)

        return buffer.getvalue()

    except ImportError:

        st.error(
            "ReportLab is missing. Install it using: "
            "pip install reportlab"
        )

        return None

    except Exception as error:

        st.error(f"PDF generation failed: {error}")

        return None


# ============================================================
# 6. SAVE REPORTS
# ============================================================

def save_reports(results):

    for _, report_key in REPORT_DETAILS:

        report_content = results.get(report_key)

        if report_content:

            filepath = os.path.join(
                OUTPUT_DIR,
                f"{report_key}.md"
            )

            with open(filepath, "w", encoding="utf-8") as file:
                file.write(str(report_content))


# ============================================================
# 7. HERO SECTION
# ============================================================

with st.container(border=True):

    st.markdown("# 🚀 Multi-Agent Startup Builder")

    st.markdown(
        """
        Transform your startup ideas into actionable business plans
        using a coordinated team of intelligent AI agents.
        """
    )

    st.caption("AI-POWERED STARTUP PLANNING WORKSPACE")


st.write("")


# ============================================================
# 8. OVERVIEW METRICS
# ============================================================

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric("🤖 AI Agents", "06")

with metric2:
    st.metric("📑 Reports", "06")

with metric3:
    st.metric("🚀 Final Blueprint", "01")


st.write("")


# ============================================================
# 9. STARTUP IDEA INPUT
# ============================================================

with st.container(border=True):

    st.markdown("## 💡 Enter Your Startup Idea")

    st.markdown(
        """
        Describe your idea below. Your AI team will research,
        develop, validate and prepare a complete startup blueprint.
        """
    )

    startup_idea = st.text_area(
        "Startup Idea",
        placeholder=(
            "Example: An AI-powered platform that helps college "
            "students prepare for placements by analysing resumes, "
            "identifying skill gaps, recommending personalized "
            "learning paths and generating interview questions."
        ),
        height=170,
        key="startup_idea_input",
        label_visibility="collapsed"
    )

    generate_button = st.button(
        "🚀 Generate Startup Blueprint",
        use_container_width=True
    )


# ============================================================
# 10. AGENT DASHBOARD
# ============================================================

st.write("")

st.markdown("## 🤖 AI Agent Execution Dashboard")

st.markdown(
    """
    Monitor the progress of your six specialized AI agents
    as they work together to build your startup plan.
    """
)

agent_columns = st.columns(3)
agent_slots = []

for index, agent in enumerate(AGENTS):

    with agent_columns[index % 3]:
        agent_slots.append(st.empty())


def render_agent_card(slot, agent, status):

    with slot.container(border=True):

        st.markdown(f"### {agent['icon']} {agent['name']}")
        st.caption(agent["description"])

        if status == "Completed":
            st.success("✓ Completed")

        elif status == "Running":
            st.info("⏳ Running")

        elif status == "Failed":
            st.error("✗ Failed")

        else:
            st.caption("○ Pending")


def update_agent_dashboard(statuses):

    for index, agent in enumerate(AGENTS):

        render_agent_card(
            agent_slots[index],
            agent,
            statuses[agent["key"]]
        )


# ============================================================
# 11. LIVE EXECUTION TIMELINE
# ============================================================

st.write("")

st.markdown("## ⏱️ Live Execution Timeline")

st.markdown(
    """
    Track when each AI agent starts and finishes,
    along with its individual execution duration.
    """
)

timeline_placeholder = st.empty()

timeline_data = {
    agent["key"]: {
        "status": "Pending",
        "started": "—",
        "completed": "—",
        "duration": "—"
    }
    for agent in AGENTS
}

timeline_start_times = {}


def render_execution_timeline():

    with timeline_placeholder.container(border=True):

        st.markdown("### Agent Execution History")

        header = st.columns([2, 1.1, 1, 1, 1])

        header[0].markdown("**Agent**")
        header[1].markdown("**Status**")
        header[2].markdown("**Started**")
        header[3].markdown("**Completed**")
        header[4].markdown("**Duration**")

        for agent in AGENTS:

            data = timeline_data[agent["key"]]

            columns = st.columns([2, 1.1, 1, 1, 1])

            columns[0].write(
                f"{agent['icon']} {agent['name']}"
            )

            if data["status"] == "Completed":
                columns[1].success("Completed")

            elif data["status"] == "Running":
                columns[1].info("Running")

            elif data["status"] == "Failed":
                columns[1].error("Failed")

            else:
                columns[1].write("Pending")

            columns[2].write(data["started"])
            columns[3].write(data["completed"])
            columns[4].write(data["duration"])


render_execution_timeline()


# ============================================================
# 12. INITIAL AGENT STATUS
# ============================================================

initial_statuses = {
    agent["key"]: "Pending"
    for agent in AGENTS
}

update_agent_dashboard(initial_statuses)


# ============================================================
# 13. RUN STARTUP WORKFLOW
# ============================================================

if generate_button:

    if not startup_idea.strip():

        st.warning(
            "Please enter your startup idea before generating the blueprint."
        )

    else:

        statuses = {
            agent["key"]: "Pending"
            for agent in AGENTS
        }

        # Reset timeline for every new execution
        timeline_start_times.clear()

        for agent in AGENTS:

            timeline_data[agent["key"]] = {
                "status": "Pending",
                "started": "—",
                "completed": "—",
                "duration": "—"
            }

        render_execution_timeline()
        update_agent_dashboard(statuses)

        progress_bar = st.progress(0)
        progress_text = st.empty()

        try:

            def progress_callback(
                node_name,
                agent_name,
                completed_count,
                status
            ):

                if node_name in statuses:
                    statuses[node_name] = status

                update_agent_dashboard(statuses)

                current_time = time.perf_counter()
                display_time = time.strftime("%H:%M:%S")

                if node_name in timeline_data:

                    data = timeline_data[node_name]

                    if status == "Running":

                        timeline_start_times[node_name] = current_time

                        data["status"] = "Running"
                        data["started"] = display_time
                        data["completed"] = "—"
                        data["duration"] = "Running..."

                    elif status == "Completed":

                        data["status"] = "Completed"
                        data["completed"] = display_time

                        start_time = timeline_start_times.get(node_name)

                        if start_time is not None:

                            duration = current_time - start_time

                            data["duration"] = (
                                f"{duration:.2f} sec"
                            )

                    elif status == "Failed":

                        data["status"] = "Failed"
                        data["completed"] = display_time

                        start_time = timeline_start_times.get(node_name)

                        if start_time is not None:

                            duration = current_time - start_time

                            data["duration"] = (
                                f"{duration:.2f} sec"
                            )

                    render_execution_timeline()

                percentage = int(
                    completed_count / len(AGENTS) * 100
                )

                progress_bar.progress(
                    min(percentage, 100)
                )

                if status == "Running":

                    progress_text.info(
                        f"⏳ Currently running: {agent_name}"
                    )

                elif status == "Completed":

                    progress_text.markdown(
                        f"**Progress: {percentage}%** — "
                        f"✓ {agent_name} completed."
                    )

                elif status == "Failed":

                    progress_text.error(
                        f"✗ {agent_name} failed."
                    )

            with st.spinner(
                "Your AI agents are working together. Please wait..."
            ):

                results = run_startup_workflow_with_progress(
                    startup_idea.strip(),
                    progress_callback=progress_callback
                )

            # Validate workflow output
            if not isinstance(results, dict):

                raise ValueError(
                    "The workflow did not return a valid result."
                )

            print("\n========== DEBUG CHECK ==========")

            print(
                "WORKFLOW FILE:",
                __import__("workflow").__file__
            )

            print("RESULT KEYS:", list(results.keys()))

            print("AGENT METRICS:", results.get("agent_metrics"))

            print("TOTAL TIME:", results.get("total_execution_time"))

            print("=================================")

            # Save generated reports
            save_reports(results)

            # Store results in Streamlit session
            st.session_state["startup_results"] = results

            st.session_state["startup_generated"] = True

            st.session_state["last_startup_idea"] = (
                startup_idea.strip()
            )

            # Ensure all agents show Completed after success
            for agent in AGENTS:

                key = agent["key"]
                statuses[key] = "Completed"

                if timeline_data[key]["status"] != "Completed":

                    timeline_data[key]["status"] = "Completed"

                    if timeline_data[key]["completed"] == "—":

                        timeline_data[key]["completed"] = time.strftime(
                            "%H:%M:%S"
                        )

            update_agent_dashboard(statuses)
            render_execution_timeline()

            progress_bar.progress(100)

            progress_text.success(
                "All six AI agents have completed their tasks!"
            )

            st.success(
                "Your startup blueprint has been generated successfully!"
            )

        except Exception as error:

            st.error(
                "An error occurred while generating your startup blueprint."
            )

            st.exception(error)


# ============================================================
# 14. DISPLAY GENERATED REPORTS
# ============================================================

if st.session_state.get("startup_generated", False):

    results = st.session_state.get("startup_results", {})

    st.divider()

    st.markdown("## 📑 Generated Startup Reports")

    st.markdown(
        """
        Your AI agents have completed their analysis.
        Explore the individual reports and the final consolidated blueprint.
        """
    )

    # --------------------------------------------------------
    # REPORT OVERVIEW
    # --------------------------------------------------------

    st.markdown("### 📌 Report Overview")

    overview_col1, overview_col2, overview_col3 = st.columns(3)

    with overview_col1:
        st.metric("Total Reports", "06")

    with overview_col2:
        st.metric("Specialized Agents", "05")

    with overview_col3:
        st.metric("Final Blueprint", "01")

    st.write("")

    # --------------------------------------------------------
    # REPORT TABS
    # --------------------------------------------------------

    report_tabs = st.tabs([
        "🔍 Research",
        "💻 Developer",
        "📢 Marketing",
        "💰 Finance",
        "✅ Validation",
        "👔 CEO Blueprint"
    ])

    for index, (tab, report_detail) in enumerate(
        zip(report_tabs, REPORT_DETAILS)
    ):

        report_title, report_key = report_detail

        with tab:

            report_content = results.get(report_key, "")

            if not report_content:

                st.warning(
                    "This report was not returned by the workflow."
                )

                continue

            report_content = str(report_content)

            # Report header
            st.markdown(
                f'<div class="report-label">AI AGENT REPORT {index + 1:02d}</div>',
                unsafe_allow_html=True
            )

            st.markdown(f"### {report_title}")

            st.caption(
                "Generated by the Multi-Agent Startup Builder"
            )

            st.divider()

            # CEO blueprint presentation
            if report_key == "final_report":

                st.markdown("### 🚀 Executive Summary")

                summary = get_executive_summary(report_content)

                with st.container(border=True):

                    st.markdown(summary)

                st.write("")

                st.markdown("### 📘 Complete Startup Blueprint")

                st.caption(
                    "The consolidated output from all six AI agents."
                )

                with st.container(border=True):

                    st.markdown(report_content)

            else:

                # Individual agent report
                with st.container(border=True):

                    st.markdown(report_content)

            # Individual report download
            st.write("")

            st.download_button(
                label=f"⬇️ Download {report_title}",
                data=report_content,
                file_name=f"{report_key}.md",
                mime="text/markdown",
                key=f"download_{report_key}",
                use_container_width=True
            )


# ============================================================
# 15. AGENT PERFORMANCE ANALYTICS
# ============================================================

if st.session_state.get("startup_generated", False):

    results = st.session_state.get("startup_results", {})

    agent_metrics = results.get("agent_metrics") or {}

    total_execution_time = safe_float(
        results.get("total_execution_time")
    )

    st.divider()

    st.markdown("## 📊 Agent Performance Analytics")

    st.markdown(
        """
        Analyse the execution performance of your AI agents
        and monitor the overall workflow efficiency.
        """
    )

    completed_agents = len(agent_metrics)
    total_agents = len(AGENTS)

    completion_percentage = (
        completed_agents / total_agents * 100
        if total_agents else 0
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            label="✅ Completed Agents",
            value=f"{completed_agents}/{total_agents}"
        )

    with col2:

        st.metric(
            label="⏱️ Total Execution Time",
            value=f"{total_execution_time:.2f} sec"
        )

    with col3:

        st.metric(
            label="📈 Workflow Completion",
            value=f"{completion_percentage:.0f}%"
        )

    st.write("")

    st.markdown("### ⏳ Individual Agent Execution Time")

    agent_names = [
        agent["name"]
        for agent in AGENTS
        if agent["key"] in agent_metrics
    ]

    execution_times = [
        safe_float(agent_metrics[agent["key"]])
        for agent in AGENTS
        if agent["key"] in agent_metrics
    ]

    if agent_names:

        chart_col, table_col = st.columns([1.5, 1])

        with chart_col:

            st.markdown("#### Execution Time Comparison")

            chart_data = {
                "Agent": agent_names,
                "Execution Time (seconds)": execution_times
            }

            st.bar_chart(
                chart_data,
                x="Agent",
                y="Execution Time (seconds)",
                horizontal=True
            )

        with table_col:

            st.markdown("#### Performance Details")

            for name, duration in zip(
                agent_names,
                execution_times
            ):

                with st.container(border=True):

                    st.markdown(f"**{name}**")

                    st.markdown(
                        f"⏱️ {duration:.2f} seconds"
                    )

        st.success(
            f"{completed_agents} out of {total_agents} "
            "agents completed successfully."
        )

    else:

        st.warning(
            "Agent performance information is not available."
        )


# ============================================================
# 16. DOWNLOAD FINAL BLUEPRINT
# ============================================================

if st.session_state.get("startup_generated", False):

    results = st.session_state.get("startup_results", {})

    final_report = results.get("final_report", "")

    st.divider()

    st.markdown("## 📥 Download Your Startup Blueprint")

    st.markdown(
        "Download your consolidated startup execution plan."
    )

    if final_report:

        download_col1, download_col2 = st.columns(2)

        with download_col1:

            st.download_button(
                label="⬇️ Download Markdown",
                data=str(final_report),
                file_name="final_startup_blueprint.md",
                mime="text/markdown",
                use_container_width=True
            )

        with download_col2:

            executive_summary = get_executive_summary(
                final_report
            )

            pdf_data = create_pdf(
                final_report,
                title="Final Startup Blueprint",
                executive_summary=executive_summary
            )

            if pdf_data:

                st.download_button(
                    label="⬇️ Download PDF",
                    data=pdf_data,
                    file_name="final_startup_blueprint.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

    else:

        st.warning(
            "The CEO Agent did not return a final startup blueprint."
        )


# ============================================================
# 17. FOOTER
# ============================================================

st.divider()

st.markdown("### Multi-Agent Startup Builder")

st.caption(
    "Built using Python, Streamlit, LangGraph and Generative AI."
)
