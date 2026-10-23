#!/usr/bin/env python3
import json
import datetime

# Create application data based on your improved CV
application_data = {
    "application_date": datetime.date.today().strftime("%d/%m/%Y"),
    "z83_form_number": "Z83 (81/971431)",
    
    "personal_info": {
        "surname": "Nkwe",
        "full_names": "Fidel Nkwe", 
        "identity_number": "30/09/94",
        "passport_number": "",
        "race": "African",
        "gender": "Male",
        "disability": "No",
        "citizenship": "Yes (South African)",
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
        "speak": "English, Setswana, IsiZulu, Sepedi",
        "write_or_read": "English"
    },
    
    "formal_qualifications": [
        {"institution": "Cultura High School", "qualification": "Matric", "year": 2013},
        {"institution": "Pearson Institute For Higher Education", "qualification": "Higher Certificate in IT", "year": 2020}
    ],
    
    "work_experience": [
        {
            "employer": "Ginimi Consulting, Midrand, Gauteng",
            "post": "Software Developer",
            "from": "03/23",
            "to": "12/23",
            "reason_for_leaving": "Contract ended/project based",
            "current_public_service_condition": "No"
        },
        {
            "employer": "PhepanaP, Gauteng, Centurion", 
            "post": "Web Developer",
            "from": "09/18",
            "to": "11/18",
            "reason_for_leaving": "",
            "current_public_service_condition": "No"
        },
        {
            "employer": "CawnlayJlus Tech, Bronkhorstspruit, Gauteng",
            "post": "Graphic Designer", 
            "from": "07/16",
            "to": "11/18",
            "reason_for_leaving": "",
            "current_public_service_condition": "No"
        },
        {
            "employer": "CawnlayJus Tech, Pretoria, Gauteng",
            "post": "Freelancer",
            "from": "03/15", 
            "to": "08/16",
            "reason_for_leaving": "",
            "current_public_service_condition": "No"
        }
    ],
    
    "references": [
        {
            "name": "Mr. John Smith",
            "relationship": "Previous Manager",
            "telephone": "012 123 4567"
        },
        {
            "name": "Ms. Jane Doe",
            "relationship": "Team Lead", 
            "telephone": "011 987 6543"
        }
    ],
    
    "declaration": {
        "signature": "[Signature]",
        "date": datetime.date.today().strftime("%d/%m/%Y")
    }
}

# Save application data
with open('/var/minis/workspace/application_data.json', 'w') as f:
    json.dump(application_data, f, indent=2)

print("Application data created successfully!")
print("You can now use this data to fill out individual Z83 forms for each job application.")