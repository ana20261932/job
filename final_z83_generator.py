#!/usr/bin/env python3
"""
Final Z83 Form Generator - Properly Formatted and Corrected Version
Fixes all identified formatting issues for government compliance.
"""

import json
from datetime import datetime
from fpdf import FPDF

class FinalZ83FormGenerator(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        self.set_auto_page_break(auto=True, margin=15)
        
    def header(self):
        if self.page_no() == 1:
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
        
    def checkbox_field(self, label, checked=False):
        box = "[X]" if checked else "[ ]"
        self.set_font('Helvetica', '', 9)
        self.cell(0, 6, f"{box} {label}", 0, 1)

    def generate_form(self, job_data, application_data):
        """Generate a complete Z83 form - Final Correct Version"""
        self.add_page()
        
        # SECTION A
        self.section_header('A. THE ADVERTISED POST')
        self.set_font('Helvetica', '', 8)
        self.multi_cell(0, 4, 'All sections of this form are compulsory. This form may be used to identify candidates to be interviewed. You need to fill in all sections of this form completely, accurately and legibly. This will help to process your application fairly.')
        self.ln(2)
        self.label_value('Position for which you are applying (as advertised)', job_data.get('position', '[Position from Advert]'))
        self.label_value('Department where the position was advertised', job_data.get('department', '[Department from Advert]'))
        self.label_value('Reference number (as stated in the advert)', job_data.get('reference', '[Reference Number]'))
        self.label_value('If you are offered the position, when can you start OR how much notice must you serve with your current employer?', job_data.get('notice_period', '[Notice Period - e.g., 1 month]'))
        self.ln(3)
        
        # SECTION B
        self.section_header('B. PERSONAL INFORMATION')
        pi = application_data['personal_info']
        self.label_value('Surname', pi['surname'])
        self.label_value('Full names', pi['full_names'])
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
        
        self.ln(1)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'Do you have any pending criminal case against you?', 0, 1)
        self.checkbox_field('Yes', pi['pending_criminal_case'] == 'Yes')
        self.checkbox_field('No', pi['pending_criminal_case'] == 'No')
        
        self.ln(1)
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'Have you ever been dismissed for misconduct from the Public Service?', 0, 1)
        self.checkbox_field('Yes', pi['public_service_dismissal'] == 'Yes')
        self.checkbox_field('No', pi['public_service_dismissal'] == 'No')
        
        self.ln(3)
        
        # SECTION C
        self.section_header('C. CONTACT DETAILS AND MEDIUM OF COMMUNICATIONS')
        cd = application_data['contact_details']
        self.label_value('Preferred language for correspondence', cd['preferred_language'])
        self.label_value('Method for correspondence (mark with X):', '')
        self.checkbox_field('Post', cd['correspondence_method'] == 'Post')
        self.checkbox_field('E-mail', cd['correspondence_method'] == 'E-mail')
        self.checkbox_field('Fax', cd['correspondence_method'] == 'Fax')
        self.checkbox_field('Tel', cd['correspondence_method'] == 'Tel')
        self.label_value('Contact details (in terms of the above)', cd['phone'])
        self.ln(3)
        
        # SECTION D - FIXED LANGUAGE PROFICIENCY
        self.section_header('D. SOUTH AFRICAN OFFICIAL LANGUAGE PROFICIENCY - state "good", "fair", or "poor"')
        lp = application_data['language_proficiency']
        self.set_font('Helvetica', '', 9)
        self.cell(50, 6, 'Languages', 1, 0, 'C')
        self.cell(40, 6, 'Speak', 1, 0, 'C')
        self.cell(40, 6, 'Write', 1, 0, 'C')
        self.cell(40, 6, 'Read', 1, 1, 'C')
        
        all_languages = []
        for l in lp['speak']:
            all_languages.append(l)
        for l in lp.get('write_or_read', []):
            all_languages.append(l)
        
        for lang in all_languages:
            self.cell(50, 6, lang['language'], 1, 0)
            self.cell(40, 6, lang['proficiency'], 1, 0, 'C')
            self.cell(40, 6, lang['proficiency'], 1, 0, 'C')
            self.cell(40, 6, lang['proficiency'], 1, 1, 'C')
        
        self.ln(3)
        
        # SECTION E
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
        self.label_value('Current study (institution and qualification)', 'None')
        self.ln(3)
        
        # SECTION F
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
        self.ln(3)
        
        # SECTION G
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
        
        # DECLARATION
        self.section_header('DECLARATION')
        self.set_font('Helvetica', '', 9)
        self.multi_cell(0, 5, 'I declare that all the information provided (including any attachments) is complete and correct to the best of my knowledge. I understand that any false information provided will result in my application being disqualified or disciplinary action taken against me if I am appointed:')
        self.ln(5)
        self.set_font('Helvetica', '', 9)
        self.cell(90, 6, f"Signature: Fidel Nkwe", 0, 0)
        self.cell(0, 6, f"Date: 23/10/2026", 0, 1)
        self.ln(5)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 4, 'Page 2 of 2    Initial: _______', 0, 1, 'R')

def generate_single_form(job_data, application_data):
    generator = FinalZ83FormGenerator()
    generator.generate_form(job_data, application_data)
    return generator

if __name__ == '__main__':
    with open('/var/minis/workspace/final_application_data.json', 'r') as f:
        app_data = json.load(f)
    
    job = {
        "position": "IT Specialist / Systems Administrator",
        "department": "Department of Public Service and Administration",
        "reference": "DPSA/IT/2026/001",
        "notice_period": "1 month"
    }
    
    generator = generate_single_form(job, app_data)
    generator.output('/var/minis/workspace/FINAL_Z83_TEST.pdf')
    print("Final Z83 form generated successfully!")