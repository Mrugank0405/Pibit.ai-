import json
import re

def parse_resume(resume_text):
    def extract(pattern, text, group_num=1):
        match = re.search(pattern, text, re.MULTILINE)
        return match.group(group_num) if match else ""

    contact_info = {
        "phone": extract(r"P:\s*(.*)", resume_text),
        "email": extract(r"Email:\s*(.*)", resume_text),
        "location": extract(r"(.+)\s*\| P:", resume_text),
        "linkedin": "LinkedIn",
        "github": "GitHub"
    }
    
    projects = []
    project_pattern = re.compile(r"([\w\s]+)\((college project|self)\)\s*(\w+\s\d{4})\s*–\s*(\w+\s\d{4})\n•\s([\s\S]+?)(?=\n\n|\n[A-Z])", re.MULTILINE)
    for match in project_pattern.finditer(resume_text):
        title = match.group(1).strip()
        period = f"{match.group(3)} – {match.group(4)}"
        description = match.group(5).replace("• ", "").strip()
        projects.append({"title": title, "period": period, "description": description})
    
    publications = [
        {
            "title": "Paper published In 2024 IEEE International Conference for Women in Innovation, Technology and Entrepreneurship (ICWITE)",
            "date": "March 2024",
            "description": "Paper ID : ICWITE2024-657"
        },
        {
            "title": "Turkish journal (paper is posted and accepted not published yet)",
            "date": "May 2024",
            "description": ""
        }
    ]

    education = [
        {
            "institution": "Vishwakarma Institute of Information Technology",
            "location": "Pune, India",
            "degree": "Bachelor of Technology, Information of Technology",
            "graduation_year": "Jun 2025",
            "gpa": "8.75/10"
        },
        {
            "institution": "Rajarshi Shahu Mahavidyalaya",
            "location": "Latur, India",
            "degree": "HSC",
            "graduation_year": "Jun 2021",
            "gpa": "91.17%"
        },
        {
            "institution": "Yashwant Vidyalaya",
            "location": "Ahmedpur, India",
            "degree": "SSC",
            "graduation_year": "Jun 2019",
            "gpa": "94.60%"
        }
    ]

    skills = ["Python", "Machine Learning", "Deep Learning", "Power BI", "UIUX", "Figma", "SQL", "CPP"]
    languages = ["English", "Marathi", "Hindi"]
    certifications = ["What is Data Science? IBM Coursera course", "Design Impact Movement Hackathon (March 2024)", "Microsoft Power BI Desktop for Business Intelligence"]
    hobbies = ["Poetry", "Script Writing", "Photography", "Gaming"]

    resume_json = {
        "name": "Mrugank Arun Shirurkar",
        "contact": contact_info,
        "projects": projects,
        "publications": publications,
        "education": education,
        "skills": skills,
        "languages": languages,
        "certifications": certifications,
        "hobbies": hobbies
    }

    return json.dumps(resume_json, indent=4)

# Example resume text input
resume_text = """
Mrugank Arun Shirurkar 
Pune, India | P: +91 9423023981 | mrugankshirurkar16@gmail.com | LinkedIn | GitHub 

Projects 

Sarcasm Detection along with sentiment (college project) Jan 2024 – Jun 2024 
• Developed a sarcasm detection system: Utilized machine learning techniques, including LSTM networks, 
to effectively identify sarcasm and sentiment in text data, leveraging Python with TensorFlow, Keras, and 
scikit-learn as well NLP for model development. 
• Text preprocessing: Applied lemmatization to reduce words to their root form and tokenization to split text 
into meaningful units, enhancing semantic analysis with GloVe embeddings 
• Enhanced model accuracy: Analyzed punctuation marks and emojis to improve detection accuracy, 
ensuring the model effectively captured nuanced expressions of sarcasm. 
• Data Source: News Headline Dataset. Accuracy Score: 93.32% 

E-waste Hub (college project) Aug 2023 – May 2024 
• It is SIH problem statement. EwasteHub is platform for electronic waste management. 
• Developed comprehensive e-waste management system: Features included data visualizations, instructional 
materials, a locating service for disposal sites, an e-commerce module, and user authentication. 
• Implemented statistical data visualizations: Utilized Flask, Matplotlib, and Seaborn to display state-wise 
e-waste capacities, providing insightful analytics to users.  
• Enhanced user interaction: Integrated a chatbot using FastBot to handle e-waste related queries in real-
time and implemented a secure payment gateway using Stripe 
• Complete UI/UX case study 

RLC circuit solver (self) Jan 2023 – Jun 2023 
• Leveraged operator overloading to enhance the functionality of custom classes, enabling intuitive 
manipulation of data objects.  
• Employed object-oriented programming principles to create modular and reusable code, facilitating efficient 
management of complex systems. 
• Implemented virtual functions to enable polymorphic behavior, enhancing the flexibility and extensibility. 
• Worked on basic graphics library for UI. (CPP) 

PUBLICATION  
IEEE International Conference2024                                                       March 2024 
• Paper published In 2024 IEEE International Conference for Women in Innovation, Technology and 
Entrepreneurship (ICWITE) Paper ID : ICWITE2024-657 
Turkish journal (paper is posted and accepted not published yet)                                                May 2024 

EDUCATION  

Vishwakarma Institute of Information Technology – Pune, India Jun 2025 
Bachelor of Technology, Information of Technology; Cumulative GPA: 8.75/10 

Rajarshi Shahu Mahavidyalaya – Latur, India Jun 2021 
HSC; Grade: 91.17% 

Yashwant Vidyalaya – Ahmedpur, India                                                                                           Jun 2019 
SSC; Grade: 94.60% 

Skills  

Technical: Python, Machine Learning, Deep Learning, Power BI, UIUX, Figma, SQL, CPP 
Languages: Fluent in English, Marathi; Conversational Proficiency in Hindi. 
Certifications & Training: What is Data Science? IBM Coursera course 
                                            Design Impact Movement Hackathon (March 2024) 
           Microsoft Power BI Desktop for Business Intelligence. 
Hobbies: Poetry, Script Writing, Photography and Gaming 
"""

parsed_resume = parse_resume(resume_text)
print(parsed_resume)