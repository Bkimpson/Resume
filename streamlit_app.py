import streamlit as st

st.set_page_config(
    page_title="Brantley C. Kimpson | Resume",
    layout="centered"
)

# ===== HEADER =====
st.title("Brantley C. Kimpson")
st.subheader("IT Professional | Technical Business Integrator")

st.write("""
📍 Hampton, GA  
📧 brantleykimpson@gmail.com  
📞 (404) 973-7786  
""")

st.divider()

# ===== SUMMARY =====
st.header("Professional Summary")
st.write(
    "Motivated IT professional and aspiring Technical Business Integrator skilled in "
    "system implementation, vendor coordination, and cloud-based solution delivery. "
    "Experienced supporting agile project execution, analyzing business–IT needs, "
    "and aligning technology solutions with organizational standards. Strong communicator "
    "with hands-on experience in AWS, SQL, and business process integration."
)

# ===== EDUCATION =====
st.header("Education")

st.write("""
**Albany State University** — Albany, GA  
*Bachelor of Science in Management Information Systems*  
Magna Cum Laude | August 2021 – May 2025  

*Associate of Science in Business Administration*  
With Distinction | GPA: 3.7 / 4.0  
""")

st.write("""
**Relevant Coursework:**  
Business Internship I, Foundations of Financial Management, Management Science and Operations Management,  
Principles of Marketing, Human-Computer Interaction, Database Management, Computer Programming in Business
""")

# ===== SKILLS =====
st.header("Skills & Software Proficiencies")

st.write("""
**Cloud & Integration:**  
AWS (S3, EC2, Lambda, API Gateway), RESTful APIs, SQL, DynamoDB, PostgreSQL  

**Programming:**  
JavaScript, HTML, CSS, React.js (Familiar)  

**Project Tools:**  
Agile (Scrum, Kanban), Jira, Confluence, DevOps Concepts, GitHub  

**Systems:**  
IT Infrastructure, Network Administration, System Deployment, Microsoft 365  

**Security:**  
Data Compliance, Configuration Management, Incident Response
""")

# ===== CERTIFICATIONS =====
st.header("Certifications")
st.write("• CompTIA Security+ (Expected March 2026)")

# ===== EXPERIENCE =====
st.header("Work & Leadership Experience")

st.subheader("IT Project & Supplier Coordination Assistant")
st.caption("Atlanta, GA | Jan 2024 – Present")
st.write("""
- Coordinate with vendors and internal teams to deliver solutions aligned with security and design standards  
- Support requirement gathering, documentation, and testing for system deployments  
- Track deliverables, risks, and milestones to ensure on-time and on-budget delivery  
- Translate business needs into technical implementation plans and provide improvement recommendations
""")

st.subheader("Kimbro Recycling — IT Lead")
st.caption("East Point, GA | May 2021 – Present")
st.write("""
- Implement and maintain IT systems supporting daily operations and data reliability  
- Align IT processes with compliance requirements and business goals  
- Develop tracking methods improving performance visibility and reducing downtime  
- Train users and ensure system adoption with emphasis on cybersecurity hygiene
""")

st.subheader("Albany State University — Information Technology Intern")
st.caption("Albany, GA | Sept 2023 – May 2024")
st.write("""
- Supported setup, testing, and integration of network and cloud-connected systems  
- Documented technical changes and optimized configurations across university IT  
- Collaborated on troubleshooting and secure deployment of software applications
""")

# ===== ACTIVITIES =====
st.header("Activities & Honors")

st.write("""
- Omega Psi Phi Fraternity Incorporated — Chapter President (2023–2024)  
- Velma Fudge Grant Honors Program (2022–2025)  
- Men Advocates for Leadership, Excellence & Success (M.A.L.E.S)  
- Resident Assistant (2023–2024)  
- Mr. Honors Council (2023–2024)  
- 7th District Honor Society Inductee (2024–2025)  
- Alonza A. Bennett Scholarship Recipient (2024)  
- GoodwillSR Round Up Scholarship Recipient (2022)
""")
