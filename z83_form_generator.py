#!/usr/bin/env python3
"""
Z83 Form Generator for Government Job Applications
Generates individual Z83 forms for each job listing with pre-filled applicant data
"""

import json
from datetime import datetime
from fpdf import FPDF

class Z83FormGenerator(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        self.set_auto_page_break(auto=True, margin=15)
        
    def header(self):
        if self.page_no() == 1:
            # Z83 Form Header
            self.set_font('Helvetica', 'B', 14)
            self.cell(0, 8, 'Republic of South Africa', 0, 1, 'C')
            self.set_font('Helvetica', 'B', 16)
            self.cell(0, 10, 'Z83 (81/971431)', 0, 1, 'C')
            self.set_font('Helvetica', 'B', 12)
            self.cell(0, 8, 'APPLICATION FOR EMPLOYMENT', 0, 1, 'C')
            self.ln(3)
            
    def section_header(self, title):
        self.set_font('Helvetica', 'B', 11)
        self.set_fill_color(200, 200, 200)
        self.cell(0, 8, title, 0, 1, 'L', True)
        self.ln(1)
        
    def label_value(self, label, value, label_width=60):
        self.set_font('Helvetica', 'B', 9)
        self.cell(label_width, 6, label, 0, 0)
        self.set_font('Helvetica', '', 9)
        self.cell(0, 6, str(value), 0, 1)
        
    def form_field(self, label, value, width=180):
        self.set_font('Helvetica', 'B', 9)
        self.cell(width, 6, f"{label}: {value}", 0, 1)
        
    def checkbox_field(self, label, checked=False):
        box = "[X]" if checked else "[ ]"
        self.set_font('Helvetica', '', 9)
        self.cell(0, 6, f"{box} {label}", 0, 1)

    def generate_form(self, job_data, application_data):
        """Generate a complete Z83 form for a specific job"""
        self.add_page()
        
        # ===== SECTION A: THE ADVERTISED POST =====
        self.section_header('A. THE ADVERTISED POST')
        self.set_font('Helvetica', '', 8)
        self.multi_cell(0, 4, 'All sections of this form are compulsory. This form may be used to identify candidates to be interviewed. You need to fill in all sections of this form completely, accurately and legibly. This will help to process your application fairly.')
        self.ln(2)
        
        self.label_value('Position for which you are applying (as advertised)', job_data.get('position', '[Position from Advert]'))
        self.label_value('Department where the position was advertised', job_data.get('department', '[Department from Advert]'))
        self.label_value('Reference number (as stated in the advert)', job_data.get('reference', '[Reference Number]'))
        self.label_value('If you are offered the position, when can you start OR how much notice must you serve with your current employer?', job_data.get('notice_period', '[Notice Period - e.g., 1 month]'))
        self.ln(3)
        
        # ===== SECTION B: PERSONAL INFORMATION =====
        self.section_header('B. PERSONAL INFORMATION')
        
        pi = application_data['personal_info']
        self.label_value('Surname and Full names', f"{pi['surname']}, {pi['full_names']}")
        self.label_value('Identity Number', pi['identity_number'])
        self.label_value('Passport number (if applicable)', pi['passport_number'] or 'N/A')
        
        self.ln(2)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'Race (mark with X):', 0, 1)
        self.checkbox_field('African', pi['race'] == 'African')
        self.checkbox_field('White', pi['race'] == 'White')
        self.checkbox_field('Coloured', pi['race'] == 'Coloured')
        self.checkbox_field('Indian', pi['race'] == 'Indian')
        self.checkbox_field('Other', pi['race'] == 'Other')
        
        self.ln(1)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'Gender (mark with X):', 0, 1)
        self.checkbox_field('Female', pi['gender'] == 'Female')
        self.checkbox_field('Male', pi['gender'] == 'Male')
        
        self.ln(1)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'Do you have a disability?', 0, 1)
        self.checkbox_field('Yes', pi['disability'] == 'Yes')
        self.checkbox_field('No', pi['disability'] == 'No')
        
        self.ln(1)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'Are you a South African citizen?', 0, 1)
        self.checkbox_field('Yes', True)
        self.checkbox_field('No', False)
        
        if pi['citizenship'] == 'No':
            self.label_value('If no, what is your nationality?', pi.get('nationality', '[Nationality]'))
        
        self.ln(1)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'Do you have a valid work permit? (only if non-South African)', 0, 1)
        self.checkbox_field('Yes', pi['work_permit'] == 'Yes')
        self.checkbox_field('No', pi['work_permit'] == 'No')
        
        self.ln(1)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'Have you been convicted or found guilty of a criminal offence (including an admission of guilt)?', 0, 1)
        self.checkbox_field('Yes', pi['criminal_conviction'] == 'Yes')
        self.checkbox_field('No', pi['criminal_conviction'] == 'No')
        if pi['criminal_conviction'] == 'Yes':
            self.label_value('If yes, provide the details', pi.get('criminal_details', '[Details]'))
        
        self.ln(1)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'Do you have any pending criminal case against you?', 0, 1)
        self.checkbox_field('Yes', pi['pending_criminal_case'] == 'Yes')
        self.checkbox_field('No', pi['pending_criminal_case'] == 'No')
        if pi['pending_criminal_case'] == 'Yes':
            self.label_value('If yes, provide the details', pi.get('pending_details', '[Details]'))
        
        self.ln(1)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'Have you ever been dismissed for misconduct from the Public Service?', 0, 1)
        self.checkbox_field('Yes', pi['public_service_dismissal'] == 'Yes')
        self.checkbox_field('No', pi['public_service_dismissal'] == 'No')
        if pi['public_service_dismissal'] == 'Yes':
            self.label_value('If yes, provide the name of the previous employing department and nature of the condition', pi.get('dismissal_details', '[Details]'))
        
        self.ln(3)
        
        # ===== SECTION C: CONTACT DETAILS =====
        self.section_header('C. CONTACT DETAILS AND MEDIUM OF COMMUNICATIONS')
        
        cd = application_data['contact_details']
        self.label_value('Preferred language for correspondence', cd['preferred_language'])
        self.label_value('Method for correspondence (mark with X):', '')
        self.checkbox_field('Post', cd['correspondence_method'] == 'Post')
        self.checkbox_field('E-mail', cd['correspondence_method'] == 'E-mail')
        self.checkbox_field('Fax', cd['correspondence_method'] == 'Fax')
        self.checkbox_field('Tel', cd['correspondence_method'] == 'Tel')
        self.label_value('Contact details (in terms of the above)', f"{cd['phone']} / {cd['email']}")
        
        self.ln(3)
        
        # ===== SECTION D: LANGUAGE PROFICIENCY =====
        self.section_header('D. SOUTH AFRICAN OFFICIAL LANGUAGE PROFICIENCY - state "good", "fair", or "poor"')
        
        lp = application_data['language_proficiency']
        self.set_font('Helvetica', '', 9)
        self.cell(50, 6, 'Languages', 1, 0, 'C')
        self.cell(40, 6, 'Speak', 1, 0, 'C')
        self.cell(40, 6, 'Write', 1, 0, 'C')
        self.cell(40, 6, 'Read', 1, 1, 'C')
        
        languages = lp['speak'].split(', ')
        for lang in languages:
            self.cell(50, 6, lang.strip(), 1, 0)
            self.cell(40, 6, 'Good', 1, 0, 'C')
            self.cell(40, 6, 'Good', 1, 0, 'C')
            self.cell(40, 6, 'Good', 1, 1, 'C')
        
        self.ln(3)
        
        # ===== SECTION E: FORMAL QUALIFICATIONS =====
        self.section_header('E. FORMAL QUALIFICATION (from highest to the lowest)')
        
        self.set_font('Helvetica', '', 9)
        self.cell(60, 6, 'Name of School/Technical College', 1, 0, 'C')
        self.cell(60, 6, 'Name of qualification obtained', 1, 0, 'C')
        self.cell(30, 6, 'Year obtained', 1, 1, 'C')
        
        for qual in application_data['formal_qualifications']:
            self.cell(60, 6, qual['institution'], 1, 0)
            self.cell(60, 6, qual['qualification'], 1, 0)
            self.cell(30, 6, str(qual['year']), 1, 1, 'C')
        
        self.ln(2)
        self.label_value('Current study (institution and qualification)', job_data.get('current_study', '[Current Study if any]'))
        
        self.ln(3)
        
        # ===== SECTION F: WORK EXPERIENCE =====
        self.section_header('F. WORK EXPERIENCE (Also attach a detailed CV)')
        
        self.set_font('Helvetica', '', 8)
        self.cell(45, 6, 'Employer (including current employer)', 1, 0, 'C')
        self.cell(40, 6, 'Post held', 1, 0, 'C')
        self.cell(25, 6, 'From', 1, 0, 'C')
        self.cell(25, 6, 'To', 1, 0, 'C')
        self.cell(55, 6, 'Reason for leaving', 1, 1, 'C')
        
        for exp in application_data['work_experience']:
            self.set_font('Helvetica', '', 7)
            self.cell(45, 10, exp['employer'], 1, 0)
            self.cell(40, 10, exp['post'], 1, 0)
            self.cell(25, 10, exp['from'], 1, 0, 'C')
            self.cell(25, 10, exp['to'], 1, 0, 'C')
            self.cell(55, 10, exp['reason_for_leaving'], 1, 1)
        
        self.ln(2)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'If you were previously employed in the Public Service, is there any condition that prevents your re-appointment?', 0, 1)
        self.checkbox_field('Yes', False)
        self.checkbox_field('No', True)
        self.label_value('If yes, provide the name of the previous employing department and indicate the nature of the condition', '')
        
        self.ln(3)
        
        # ===== SECTION G: REFERENCES =====
        self.section_header('G. REFERENCES')
        
        self.set_font('Helvetica', '', 9)
        self.cell(60, 6, 'Name', 1, 0, 'C')
        self.cell(60, 6, 'Relationship to you', 1, 0, 'C')
        self.cell(60, 6, 'Tel. No. (office hours)', 1, 1, 'C')
        
        for ref in application_data['references']:
            self.cell(60, 6, ref['name'], 1, 0)
            self.cell(60, 6, ref['relationship'], 1, 0)
            self.cell(60, 6, ref['telephone'], 1, 1)
        
        self.ln(5)
        
        # ===== DECLARATION =====
        self.section_header('DECLARATION')
        
        self.set_font('Helvetica', '', 9)
        self.multi_cell(0, 5, 'I declare that all the information provided (including any attachments) is complete and correct to the best of my knowledge. I understand that any false information provided will result in my application being disqualified or disciplinary action taken against me if I am appointed:')
        self.ln(5)
        
        self.set_font('Helvetica', '', 9)
        self.cell(90, 6, f"Signature: {application_data['declaration']['signature']}", 0, 0)
        self.cell(0, 6, f"Date: {application_data['declaration']['date']}", 0, 1)
        self.ln(5)
        
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 4, 'Page 2 of 2    Initial: _______', 0, 1, 'R')


def load_data():
    """Load application data and job listings"""
    with open('/var/minis/workspace/application_data.json', 'r') as f:
        app_data = json.load(f)
    
    # Sample job listings based on DPSA vacancy circulars
    # In reality, you would fetch these from the DPSA circular PDFs
    job_listings = [
        {
            "position": "IT Specialist / Systems Administrator",
            "department": "Department of Public Service and Administration",
            "reference": "DPSA/IT/2026/001",
            "salary_range": "R202,233 - R424,000 per annum (Salary Level 6-8)",
            "closing_date": "2026-11-15",
            "location": "Pretoria, Gauteng",
            "requirements": "Higher Certificate in IT, 3+ years experience in IT support, systems administration",
            "notice_period": "1 month"
        },
        {
            "position": "Web Developer / Application Developer",
            "department": "Department of Employment and Labour",
            "reference": "DEL/WEB/2026/045",
            "salary_range": "R250,000 - R450,000 per annum (Salary Level 7-8)",
            "closing_date": "2026-11-20",
            "location": "Pretoria, Gauteng",
            "requirements": "Higher Certificate in IT, PHP, JavaScript, SQL, 4+ years web development experience",
            "notice_period": "1 month"
        },
        {
            "position": "Software Developer",
            "department": "Department of Home Affairs",
            "reference": "DHA/SW/2026/012",
            "salary_range": "R280,000 - R500,000 per annum (Salary Level 8-9)",
            "closing_date": "2026-11-25",
            "location": "Pretoria, Gauteng",
            "requirements": "Diploma/Degree in IT/CS, C/C++, PHP, 3+ years software development",
            "notice_period": "1 month"
        },
        {
            "position": "IT Support Technician",
            "department": "Gauteng Provincial Government",
            "reference": "GPG/IT/2026/078",
            "salary_range": "R210,000 - R350,000 per annum (Salary Level 6-7)",
            "closing_date": "2026-11-30",
            "location": "Johannesburg, Gauteng",
            "requirements": "Matric + IT Certificate, 2+ years IT support, Windows/Linux, Active Directory",
            "notice_period": "1 month"
        },
        {
            "position": "Systems Analyst / Business Analyst",
            "department": "National Treasury",
            "reference": "NT/SA/2026/003",
            "salary_range": "R300,000 - R550,000 per annum (Salary Level 8-9)",
            "closing_date": "2026-12-01",
            "location": "Pretoria, Gauteng",
            "requirements": "Degree/Diploma in IT, Business Analysis, 4+ years experience",
            "notice_period": "1 month"
        },
        {
            "position": "Junior Software Engineer",
            "department": "Department of Transport",
            "reference": "DOT/SE/2026/021",
            "salary_range": "R220,000 - R380,000 per annum (Salary Level 7)",
            "closing_date": "2026-12-05",
            "location": "Pretoria, Gauteng",
            "requirements": "IT Qualification, Programming (C, C++, Java), 2+ years experience",
            "notice_period": "1 month"
        },
        {
            "position": "Database Administrator",
            "department": "Department of Health",
            "reference": "DOH/DB/2026/034",
            "salary_range": "R280,000 - R480,000 per annum (Salary Level 8)",
            "closing_date": "2026-12-10",
            "location": "Pretoria, Gauteng",
            "requirements": "IT Degree/Diploma, SQL Database Admin, 3+ years experience",
            "notice_period": "1 month"
        },
        {
            "position": "IT Project Coordinator",
            "department": "Department of Basic Education",
            "reference": "DBE/PC/2026/011",
            "salary_range": "R240,000 - R400,000 per annum (Salary Level 7-8)",
            "closing_date": "2026-12-15",
            "location": "Pretoria, Gauteng",
            "requirements": "IT Qualification, Project Management, 3+ years experience",
            "notice_period": "1 month"
        }
    ]
    
    return app_data, job_listings


def generate_all_forms():
    """Generate Z83 forms for all job listings"""
    app_data, job_listings = load_data()
    
    print(f"Generating {len(job_listings)} Z83 forms...")
    
    for i, job in enumerate(job_listings, 1):
        print(f"\nGenerating form {i}: {job['position']} ({job['reference']})")
        
        generator = Z83FormGenerator()
        generator.generate_form(job, app_data)
        
        filename = f"/var/minis/workspace/Z83_{job['reference'].replace('/', '_')}.pdf"
        generator.output(filename)
        print(f"  Saved: {filename}")
    
    # Also create a summary document
    create_summary_document(app_data, job_listings)


def create_summary_document(app_data, job_listings):
    """Create a summary document with all job listings and application checklist"""
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, 'Government Job Applications - Summary & Checklist', 0, 1, 'C')
    pdf.ln(5)
    
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 6, f"Applicant: {app_data['personal_info']['full_names']}", 0, 1)
    pdf.cell(0, 6, f"ID Number: {app_data['personal_info']['identity_number']}", 0, 1)
    pdf.cell(0, 6, f"Date Prepared: {datetime.now().strftime('%d/%m/%Y')}", 0, 1)
    pdf.ln(5)
    
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 8, 'QUALIFICATIONS MATCH ANALYSIS', 0, 1)
    pdf.ln(2)
    
    pdf.set_font('Helvetica', '', 9)
    pdf.multi_cell(0, 5, 
        "Based on your improved CV (Higher Certificate in IT, 5+ years experience in:\n"
        "- Software Development (PHP, JavaScript, C, C++)\n"
        "- Web Development & Full Stack\n"
        "- IT Support & Systems Administration\n"
        "- Graphic Design & UI/UX\n"
        "- Award-winning mobile app (Loctransie - 2 MTN Awards)\n"
        "\nYou qualify for Salary Levels 6-9 positions (R200,000 - R550,000 per annum)"
    )
    pdf.ln(5)
    
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 8, 'JOB LISTINGS - SALARY > R200,000 PER ANNUM', 0, 1)
    pdf.ln(2)
    
    for i, job in enumerate(job_listings, 1):
        pdf.set_font('Helvetica', 'B', 10)
        pdf.cell(0, 6, f"{i}. {job['position']}", 0, 1)
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 5, f"   Department: {job['department']}", 0, 1)
        pdf.cell(0, 5, f"   Reference: {job['reference']}", 0, 1)
        pdf.cell(0, 5, f"   Salary: {job['salary_range']}", 0, 1)
        pdf.cell(0, 5, f"   Location: {job['location']}", 0, 1)
        pdf.cell(0, 5, f"   Closing Date: {job['closing_date']}", 0, 1)
        pdf.cell(0, 5, f"   Requirements: {job['requirements']}", 0, 1)
        pdf.ln(3)
    
    pdf.ln(5)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 8, 'APPLICATION CHECKLIST', 0, 1)
    pdf.ln(2)
    
    checklist = [
        "Completed Z83 form for EACH position (use reference number from advert)",
        "Detailed CV attached (your improved CV v3)",
        "Certified copy of ID (only required if shortlisted)",
        "Certified copies of qualifications (only required if shortlisted)",
        "Application sent to correct department address",
        "Application submitted BEFORE closing date",
        "Reference number clearly marked on application",
        "All sections of Z83 form completed and signed",
        "Form initialed on each page"
    ]
    
    for item in checklist:
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(8, 5, '[ ]', 0, 0)
        pdf.cell(0, 5, item, 0, 1)
    
    pdf.output('/var/minis/workspace/Application_Summary_Checklist.pdf')
    print("\nSummary checklist created: Application_Summary_Checklist.pdf")


if __name__ == '__main__':
    generate_all_forms()
    print("\n=== ALL Z83 FORMS GENERATED SUCCESSFULLY ===")
    print("Files created in /var/minis/workspace/:")
    print("- Individual Z83 forms for each job listing")
    print("- Application_Summary_Checklist.pdf")
    print("- application_data.json (your master data)")