#!/usr/bin/env python3
"""
Final Comprehensive Package Generator - Adds all 5 additional jobs to final package
"""
import json
import os
from datetime import datetime
from fpdf import FPDF

class FinalComprehensivePackage:
    def __init__(self):
        self.app_data = {
            "application_date": "23/10/2026",
            "z83_form_number": "Z83 (81/971431)",
            "personal_info": {
                "surname": "Nkwe",
                "full_names": "Fidel Nkwe",
                "identity_number": "30/09/1994",
                "passport_number": "",
                "race": "African",
                "gender": "Male",
                "disability": "No",
                "citizenship": "Yes",
                "work_permit": "Yes",
                "criminal_record": "No",
                "pending_criminal_case": "No",
                "public_service_dismissal": "No",
                "criminal_conviction": "No"
            },
            "contact_details": {
                "preferred_language": "English",
                "correspondence_method": "Tel",
                "phone": "064 551 0575",
                "email": "fidelkekana@gmail.com"
            },
            "language_proficiency": {
                "speak": [
                    {"language": "English", "proficiency": "Good"},
                    {"language": "Setswana", "proficiency": "Good"},
                    {"language": "Sepedi", "proficiency": "Good"},
                    {"language": "IsiZulu", "proficiency": "Good"}
                ],
                "write_or_read": [
                    {"language": "English", "proficiency": "Good"}
                ]
            },
            "formal_qualifications": [
                {"institution": "Cultura High School", "qualification": "Matric", "year": 2013},
                {"institution": "Pearson Institute For Higher Education", "qualification": "Higher Certificate in IT", "year": 2020}
            ],
            "work_experience": [
                {
                    "employer": "Ginimi Consulting, Midrand, Gauteng",
                    "post": "Software Developer",
                    "from": "03/2023",
                    "to": "12/2023",
                    "reason_for_leaving": "Contract ended/project based",
                    "current_public_service_condition": "No"
                },
                {
                    "employer": "PhepanaP, Gauteng, Centurion", 
                    "post": "Web Developer",
                    "from": "09/2018",
                    "to": "11/2018",
                    "reason_for_leaving": "Project completion",
                    "current_public_service_condition": "No"
                },
                {
                    "employer": "CawnlayJlus Tech, Bronkhorstspruit, Gauteng",
                    "post": "Graphic Designer", 
                    "from": "07/2016",
                    "to": "11/2018",
                    "reason_for_leaving": "Contract ended",
                    "current_public_service_condition": "No"
                },
                {
                    "employer": "CawnlayJus Tech, Pretoria, Gauteng",
                    "post": "Freelancer",
                    "from": "03/2015",
                    "to": "08/2016",
                    "reason_for_leaving": "Client project completion",
                    "current_public_service_condition": "No"
                },
                {
                    "employer": "Phethagatsa Solutions",
                    "post": "Freelance App Developer",
                    "from": "06/2026",
                    "to": "09/2026",
                    "reason_for_leaving": "Project completion",
                    "current_public_service_condition": "No"
                }
            ],
            "references": [
                {
                    "name": "Ginini Consulting",
                    "relationship": "Company - Project Based",
                    "telephone": "076 243 1883",
                    "project_details": "Worked 1 project in 2022, project based"
                },
                {
                    "name": "Phethagatsa Solutions",
                    "relationship": "Company - Freelance App",
                    "telephone": "082 956 4472",
                    "project_details": "Freelance app project based from June 2026 till last month (September 2026)"
                }
            ],
            "declaration": {
                "signature": "Fidel Nkwe",
                "date": "23/10/2026"
            }
        }
    
    def create_z83(self, job, filename):
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        
        # Header
        pdf.set_font('Helvetica', 'B', 14)
        pdf.cell(0, 8, 'Republic of South Africa', 0, 1, 'C')
        pdf.set_font('Helvetica', 'B', 16)
        pdf.cell(0, 10, 'Z83 (81/971431)', 0, 1, 'C')
        pdf.set_font('Helvetica', 'B', 12)
        pdf.cell(0, 8, 'APPLICATION FOR EMPLOYMENT', 0, 1, 'C')
        
        # Section A
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 8, 'A. THE ADVERTISED POST', 0, 1, 'L')
        pdf.set_font('Helvetica', '', 8)
        pdf.multi_cell(0, 4, 'All sections of this form are compulsory. This form may be used to identify candidates to be interviewed. You need to fill in all sections of this form completely, accurately and legibly. This will help to process your application fairly.')
        pdf.ln(2)
        pdf.set_font('Helvetica', 'B', 9)
        pdf.cell(60, 6, 'Position for which you are applying (as advertised)', 0, 0)
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 6, job['position'], 0, 1)
        pdf.set_font('Helvetica', 'B', 9)
        pdf.cell(60, 6, 'Department where the position was advertised', 0, 0)
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 6, job['department'], 0, 1)
        pdf.set_font('Helvetica', 'B', 9)
        pdf.cell(60, 6, 'Reference number (as stated in the advert)', 0, 0)
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 6, job['reference'], 0, 1)
        pdf.ln(3)
        
        # Section B
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 8, 'B. PERSONAL INFORMATION', 0, 1, 'L')
        pi = self.app_data['personal_info']
        pdf.set_font('Helvetica', 'B', 9)
        pdf.cell(60, 6, 'Surname', 0, 0)
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 6, pi['surname'], 0, 1)
        pdf.set_font('Helvetica', 'B', 9)
        pdf.cell(60, 6, 'Full names', 0, 0)
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 6, pi['full_names'], 0, 1)
        pdf.set_font('Helvetica', 'B', 9)
        pdf.cell(60, 6, 'Identity Number', 0, 0)
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 6, pi['identity_number'], 0, 1)
        pdf.ln(3)
        
        # Section C
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 8, 'C. CONTACT DETAILS AND MEDIUM OF COMMUNICATIONS', 0, 1, 'L')
        cd = self.app_data['contact_details']
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 6, f"Preferred language for correspondence: {cd['preferred_language']}", 0, 1)
        pdf.cell(0, 6, f"Method for correspondence (mark with X): [X] Tel", 0, 1)
        pdf.cell(0, 6, f"Contact details (in terms of the above): {cd['phone']}", 0, 1)
        pdf.ln(3)
        
        # Section D
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 8, 'D. SOUTH AFRICAN OFFICIAL LANGUAGE PROFICIENCY - state "good", "fair", or "poor"', 0, 1, 'L')
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 6, "Speak: English (Good), Setswana (Good), Sepedi (Good), IsiZulu (Good)", 0, 1)
        pdf.cell(0, 6, "Write: English (Good)", 0, 1)
        pdf.cell(0, 6, "Read: English (Good)", 0, 1)
        pdf.ln(3)
        
        # Section E
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 8, 'E. FORMAL QUALIFICATION (from highest to the lowest)', 0, 1, 'L')
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(0, 6, "Cultura High School - Matric - 2013", 0, 1)
        pdf.cell(0, 6, "Pearson Institute For Higher Education - Higher Certificate in IT - 2020", 0, 1)
        pdf.ln(3)
        
        # Section F
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 8, 'F. WORK EXPERIENCE (Also attach a detailed CV)', 0, 1, 'L')
        pdf.set_font('Helvetica', '', 9)
        for exp in self.app_data['work_experience']:
            pdf.cell(0, 6, f"Employer: {exp['employer']}", 0, 1)
            pdf.cell(0, 6, f"Post: {exp['post']}", 0, 1)
            pdf.cell(0, 6, f"From: {exp['from']}  To: {exp['to']}", 0, 1)
            pdf.cell(0, 6, f"Reason for leaving: {exp['reason_for_leaving']}", 0, 1)
            pdf.ln(2)
        
        # Section G
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 8, 'G. REFERENCES', 0, 1, 'L')
        pdf.set_font('Helvetica', '', 9)
        for ref in self.app_data['references']:
            pdf.cell(0, 6, f"Name: {ref['name']}", 0, 1)
            pdf.cell(0, 6, f"Relationship: {ref['relationship']}", 0, 1)
            pdf.cell(0, 6, f"Telephone: {ref['telephone']}", 0, 1)
            if 'project_details' in ref:
                pdf.cell(0, 6, f"Project Details: {ref['project_details']}", 0, 1)
            pdf.ln(2)
        
        # Declaration
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 8, 'DECLARATION', 0, 1, 'L')
        pdf.set_font('Helvetica', '', 9)
        pdf.multi_cell(0, 5, 'I declare that all the information provided (including any attachments) is complete and correct to the best of my knowledge. I understand that any false information provided will result in my application being disqualified or disciplinary action taken against me if I am appointed:')
        pdf.ln(5)
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(90, 6, f"Signature: Fidel Nkwe", 0, 0)
        pdf.cell(0, 6, f"Date: 23/10/2026", 0, 1)
        
        pdf.output(filename)
    
    def generate_all(self, jobs, output_dir="/var/minis/workspace/"):
        for i, job in enumerate(jobs, 1):
            filename = f"/var/minis/workspace/Z83_{job['reference'].replace('/', '_')}.pdf"
            self.create_z83(job, filename)
            print(f"Generated: {job['position']} - {job['reference']}")

# Create instances for each job
jobs = [
    {
        "position": "Administrative Assistant",
        "department": "Gauteng Provincial Government",
        "reference": "GPG/AA/2026/089",
        "salary_range": "R210,000 - R375,000 per annum",
        "closing_date": "2026-10-30",
        "location": "Johannesburg, Gauteng",
        "requirements": "Matric + Admin experience, office management, communication",
        "notice_period": "1 month"
    },
    {
        "position": "Office Coordinator",
        "department": "Department of Transport",
        "reference": "DOT/OC/2026/042",
        "salary_range": "R215,000 - R380,000 per annum",
        "closing_date": "2026-10-30",
        "location": "Pretoria, Gauteng",
        "requirements": "Matric + Office admin, coordination, admin support",
        "notice_period": "1 month"
    },
    {
        "position": "Grants Administrator",
        "department": "Department of Social Development",
        "reference": "DSD/GA/2026/035",
        "salary_range": "R210,000 - R375,000 per annum",
        "closing_date": "2026-10-30",
        "location": "Pretoria, Gauteng",
        "requirements": "Matric + admin, grants processing, admin skills",
        "notice_period": "1 month"
    },
    {
        "position": "Asset Clerk",
        "department": "Department of Public Works",
        "reference": "DPW/AC/2026/067",
        "salary_range": "R205,000 - R360,000 per annum",
        "closing_date": "2026-10-30",
        "location": "Cape Town, Western Cape",
        "requirements": "Matric + admin, asset management, inventory",
        "notice_period": "1 month"
    },
    {
      "position": "Administrative Officer",
      "department": "Department of Home Affairs",
      "reference": "DHA/AO/2026/048",
      "salary_range": "R235,000 - R420,000 per annum",
      "closing_date": "2026-10-30",
      "location": "Pretoria, Gauteng",
      "requirements": "Matric + admin, office admin, records management",
      "notice_period": "1 month"
    }
]

if __name__ == '__main__':
    gen = FinalComprehensivePackage()
    gen.generate_all(jobs)
    print("Generated Z83 forms for all additional jobs!")