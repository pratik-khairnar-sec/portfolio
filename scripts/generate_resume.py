import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = os.path.join(os.path.dirname(__file__), 'assets', 'pratik_khairnar_resume.pdf')

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=36,
    rightMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

primary_color = colors.HexColor('#0f172a')     # Slate 900
accent_color = colors.HexColor('#dc2626')      # Deep Red
text_color = colors.HexColor('#1e293b')        # Slate 800
meta_color = colors.HexColor('#475569')        # Slate 600
border_color = colors.HexColor('#cbd5e1')      # Slate 300

name_style = ParagraphStyle(
    'Name',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=22,
    textColor=primary_color,
    alignment=1
)

sub_style = ParagraphStyle(
    'SubTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=13,
    textColor=accent_color,
    alignment=1
)

contact_style = ParagraphStyle(
    'Contact',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=meta_color,
    alignment=1
)

sec_heading = ParagraphStyle(
    'SectionHeading',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=13,
    textColor=primary_color,
    spaceAfter=1,
    spaceBefore=4
)

body_style = ParagraphStyle(
    'BodyText',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.3,
    leading=11.3,
    textColor=text_color
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.2,
    leading=11.1,
    textColor=text_color,
    leftIndent=11,
    firstLineIndent=-7
)

story = []

# 1. Header
story.append(Paragraph('PRATIK SANJAY KHAIRNAR', name_style))
story.append(Spacer(1, 2))
story.append(Paragraph('Certified Ethical Hacker (CEH v13) | Associate Penetration Tester &amp; Web VAPT Engineer', sub_style))
story.append(Spacer(1, 2))
story.append(Paragraph('Pune, Maharashtra, India &bull; +91 87999 81052 &bull; <font color="#2563eb"><u>pratik.khairnar.sec@gmail.com</u></font> &bull; <font color="#2563eb"><u>linkedin.com/in/pratik-khairnar-sec</u></font> &bull; <font color="#2563eb"><u>github.com/pratik-khairnar-sec</u></font>', contact_style))
story.append(Spacer(1, 4))
story.append(HRFlowable(width='100%', thickness=1.2, color=accent_color, spaceBefore=1, spaceAfter=4))

# 2. Executive Summary
story.append(Paragraph('PROFESSIONAL SUMMARY', sec_heading))
story.append(Paragraph('Certified Ethical Hacker (CEH v13) pursuing B.Tech in Cyber Security &amp; Forensics (2023&ndash;2027) with operational experience in manual Web Application Penetration Testing (Web VAPT), REST API authorization testing (BOLA / IDOR), and custom offensive security tooling. Demonstrated track record executing vulnerability assessments at Independent Security Research and investigating 15+ live cybercrime cases at the Cyber Police Station, Nashik Police Commissionerate. Testing strictly aligned with OWASP Top 10 (2021), OWASP API Security Top 10 (2023), OWASP WSTG v4.2, and ASVS v4.0 methodologies, delivering actionable CVSS v3.1 reports with verified Proof-of-Concepts (PoCs) and developer-ready remediation roadmaps.', body_style))
story.append(Spacer(1, 3))
story.append(HRFlowable(width='100%', thickness=0.6, color=border_color, spaceBefore=1, spaceAfter=3))

# 3. Core Competencies
story.append(Paragraph('CORE TECHNICAL COMPETENCIES', sec_heading))
skills = [
    ('Application Security &amp; VAPT:', 'Manual Web VAPT, OWASP Top 10 (2021), OWASP API Top 10 (2023), Broken Object Level Authorization (BOLA/IDOR), Broken Function Level Authorization (BFLA), Business Logic Flaws, Authentication Bypasses (OAuth 2.0 / JWT), Privilege Escalation, SQL Injection (Blind Time/Boolean), Cross-Site Scripting (DOM/Reflected XSS), SSRF, CORS Misconfigurations.'),
    ('Methodologies &amp; Frameworks:', 'OWASP WSTG v4.2, OWASP ASVS v4.0, SANS Top 25, NIST SP 800-115, CVSS v3.1 Severity Scoring, Threat Modeling, Secure SDLC (SSDLC) Principles, Remediation Verification &amp; Closure Retesting.'),
    ('Security Tools &amp; Arsenal:', 'Burp Suite Professional (Intruder, Repeater, Sequencer, Extension APIs), Postman, Nmap, Wireshark, SQLMap, OWASP ZAP, Git, Linux / Kali Linux CLI, Headless Chrome Automation.'),
    ('Scripting &amp; Automation:', 'Python 3 (Requests, Regex, Custom PoC Automation), Bash Scripting, Java 17/21 (Burp Extension Architecture), JavaScript / DOM Analysis.'),
    ('Digital Forensics &amp; Law Enf.:', 'Evidence Chain of Custody Protocols, CDR / IPDR Telecom Forensics, Android APK Malware Triage, Indicator of Compromise (IOC) Analysis, PCAP Traffic Dissection, CERT-In Reporting Standards.')
]
for title, desc in skills:
    story.append(Paragraph(f'<b>{title}</b> {desc}', body_style))
    story.append(Spacer(1, 1.2))
story.append(Spacer(1, 2))
story.append(HRFlowable(width='100%', thickness=0.6, color=border_color, spaceBefore=1, spaceAfter=3))

# 4. Professional Experience
story.append(Paragraph('PROFESSIONAL EXPERIENCE', sec_heading))

# Cyber Police Station
story.append(Paragraph('<b>Cyber Crime Intern</b> &mdash; <i>Cyber Police Station, Nashik Police Commissionerate</i> &nbsp;|&nbsp; <font color="#475569">Jan 2026 &ndash; May 2026</font>', body_style))
story.append(Paragraph('&bull; Investigated 15+ live cybercrime and digital fraud cases in direct collaboration with cyber cell officers, strictly adhering to legal evidence <b>Chain of Custody</b> protocols.', bullet_style))
story.append(Paragraph('&bull; Performed deep packet-level network traffic analysis using <b>Wireshark</b> to reconstruct malicious communication sessions and trace active attack infrastructure.', bullet_style))
story.append(Paragraph('&bull; Analyzed suspicious Android APK packages, correlated <b>CDR/IPDR telecom intelligence</b>, and isolated high-fidelity Indicators of Compromise (<b>IOCs</b>) to support formal evidentiary proceedings.', bullet_style))
story.append(Spacer(1, 2.5))

# Independent Security Research
story.append(Paragraph('<b>Offensive Security Tool Architect & Researcher</b> &mdash; <i>Independent Security Research</i> &nbsp;|&nbsp; <font color="#475569">Jun 2025 &ndash; Oct 2025</font>', body_style))
story.append(Paragraph('&bull; Executed end-to-end manual Web Application Penetration Testing (<b>Web VAPT</b>) and REST API security audits across multi-tenant environments benchmarked against <b>OWASP Top 10 (2021)</b> and <b>WSTG v4.2</b> standards.', bullet_style))
story.append(Paragraph('&bull; Identified critical vulnerability classes including Broken Object Level Authorization (<b>BOLA / IDOR</b>), OAuth 2.0 authentication bypasses, JWT signature manipulation, and Boolean Blind SQLi.', bullet_style))
story.append(Paragraph('&bull; Authored technical and executive-ready VAPT documentation featuring <b>CVSS v3.1</b> severity ratings, defensible Proof-of-Concepts (PoCs), and pragmatic developer remediation roadmaps.', bullet_style))
story.append(Paragraph('&bull; Conducted post-remediation <b>closure retesting</b> alongside engineering teams, validating root-cause vulnerability resolution prior to production release.', bullet_style))
story.append(Spacer(1, 2.5))
story.append(HRFlowable(width='100%', thickness=0.6, color=border_color, spaceBefore=1, spaceAfter=3))

story.append(PageBreak())

# 5. Security Engineering Projects
story.append(Paragraph('OFFENSIVE SECURITY PROJECTS &amp; TOOLING', sec_heading))

projects = [
    ('AUTHENTIX Enterprise v2.1.0', 'Burp Suite Extension | Java 17/21 | BOLA/IDOR Testing', 'Native Burp Suite extension for automated authorization (BOLA/IDOR) testing, session validation, and token replay verification. Analyzes multi-tenant API endpoints in real time with verifiable reproduction logs.'),
    ('ReconForge v3', 'OSINT Framework | 52,600+ Dork Vault | 30 Master Phases', 'Client-side Bug Bounty reconnaissance workspace featuring 30 structured target phases and 52,630+ curated dorks. Automates asset triage, attack surface mapping, and tool-major CLI syntax pipelines executing 100% locally with zero cloud leakage.'),
    ('Reflectra v7.0.0', 'Context-Aware DOM XSS Engine | Python 3 | Headless Chrome', 'High-accuracy Cross-Site Scripting scanner evaluating 2,600+ context-prioritized payloads across HTML, attribute, and JS execution contexts. Validates genuine exploitability via automated headless browser dialog evaluation with zero false positives.'),
    ('BlindStrike v7.0.0', 'Statistical Blind SQLi Framework | Python 3 | Multi-DB Support', 'Empirical latency calibration framework for Time-Based and Boolean Blind SQL Injection. Implements Interquartile Range (IQR) network variance filtering and multi-threaded extraction across multi-database environments.'),
    ('CORSair v3.0.0', 'CORS Misconfiguration Auditor | Shannon Entropy | PoC Suite', 'Dynamic origin reflection scanner evaluating ACAO/ACAC header misconfigurations, credential exposure, Shannon entropy token leakage, and automated exploit PoC generation.')
]

for name, meta, desc in projects:
    story.append(Paragraph(f'<b>{name}</b> &mdash; <i>{meta}</i>', body_style))
    story.append(Paragraph(f'&bull; {desc}', bullet_style))
    story.append(Spacer(1, 1.5))

story.append(Spacer(1, 1.5))
story.append(HRFlowable(width='100%', thickness=0.6, color=border_color, spaceBefore=1, spaceAfter=3))

# 6. Education
story.append(Paragraph('EDUCATION', sec_heading))
story.append(Paragraph('<b>B.Tech in Computer Science &amp; Engineering (Cyber Security &amp; Forensics)</b> &nbsp;|&nbsp; <font color="#475569">2023 &ndash; 2027</font><br/>Sandip University, Nashik, Maharashtra &bull; <b>CGPA: 7.42 / 10</b><br/><i>Relevant Coursework:</i> Application Security (VAPT), Secure Software Development Lifecycle (SSDLC), Network Defense, Cryptography, Reverse Engineering, Digital Forensics, Linux Operating Systems.', body_style))
story.append(Spacer(1, 2.5))
story.append(HRFlowable(width='100%', thickness=0.6, color=border_color, spaceBefore=1, spaceAfter=3))

# 7. Certifications
story.append(Paragraph('CERTIFICATIONS &amp; CREDENTIALS', sec_heading))
story.append(Paragraph('&bull; <b>Certified Ethical Hacker (CEH v13)</b> &mdash; EC-Council &bull; Credential Verification Exam ID: ECC8042517936<br/>&bull; <b>Cisco Certified Network Associate (CCNA)</b> &mdash; Cisco Networking Academy<br/>&bull; <i>Domain Expertise:</i> Enterprise Network Defense, Web Application Attacks, Threat Intelligence, and Penetration Testing Methodologies.', body_style))
story.append(Spacer(1, 2.5))
story.append(HRFlowable(width='100%', thickness=0.6, color=border_color, spaceBefore=1, spaceAfter=3))

# 8. Hiring Availability & Attributes
story.append(Paragraph('HIRING AVAILABILITY &amp; ATTRIBUTES', sec_heading))
story.append(Paragraph('<b>Availability:</b> Immediate Joining &bull; Open to Full-Time Associate Penetration Tester &amp; AppSec roles in <b>Pune / Hybrid / Remote</b>.<br/><b>Operational Strengths:</b> Defensible PoC Formulation, Zero False-Positive Triage, Secure Code Remediation Advisory, Collaborative Team Problem Solving.', body_style))

doc.build(story)
print('PDF generated successfully at:', pdf_path)
