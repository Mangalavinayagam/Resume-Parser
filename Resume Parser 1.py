import os
import spacy
from spacy.matcher import Matcher
import re

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define a function to extract name, skills, and experience from a resume
def extract_information(resume_text):
    # Process the resume text using spaCy
    doc = nlp(resume_text)

    # Initialize the Matcher
    matcher = Matcher(nlp.vocab)

    # Define patterns for identifying name, skills, and experience (customize as needed)
    name_pattern = [{"POS": {"in": ["PROPN"]}}, {"POS": {"in": ["PROPN"]}}]
    # Specify programming skills explicitly
    programming_skills = [
        {"LOWER": {"in": ["python", "java", "javascript", "c++", "c#", "php", "ruby", "swift", "html", "css"]}}
    ]
    skill_pattern = [{"IS_TITLE": True}, {"IS_TITLE": True}, {"IS_TITLE": True}, {"IS_TITLE": True}]
    # Refine the experience pattern
    experience_pattern = [
        {"LOWER": {"in": ["experience", "expertise"]}},
        {"OP": "?"},
        {"LOWER": {"in": ["years", "yrs", "year"]}},
        {"OP": "?"},
        {"LIKE_NUM": True}
    ]

    # Add patterns to the Matcher
    matcher.add("Name", [name_pattern])
    matcher.add("Skills", [programming_skills, skill_pattern])
    matcher.add("Experience", [experience_pattern])

    # Use the Matcher to find matches in the document
    matches = matcher(doc)

    # Extract matched information from the document
    name = [doc[start:end].text for match_id, start, end in matches if doc.vocab.strings[match_id] == "Name"]
    skills = [doc[start:end].text for match_id, start, end in matches if doc.vocab.strings[match_id] == "Skills"]

    # Extract experience using noun chunks
    experience = []
    for chunk in doc.noun_chunks:
        if re.search(r"(experience|work)", chunk.text.lower()):
            experience.append(chunk.text)

    return name[0] if name else None, skills, ' '.join(experience) if experience else None

# Define a function to process all resumes in a folder
def process_resumes(folder_path):
    skill_data = {}

    for filename in os.listdir(folder_path):
        if filename.endswith((".txt")):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                resume_text = file.read()
                name, skills, experience = extract_information(resume_text)

                if name is not None:
                    # Assuming each candidate has a unique name
                    candidate_name = " ".join(name)
                    skill_data[candidate_name] = {'Skills': skills, 'Experience': experience}

                    # Display information for each candidate
                    print(f"Candidate: {candidate_name}")
                    print(f"Skills: {', '.join(skills) if skills else 'N/A'}")
                    print(f"Experience: {experience}" if experience else "Experience not found")
                    print("\n" + "=" * 30 + "\n")

    return skill_data

# Ask the user for the folder path
folder_path = input("Enter the path to the folder containing resume files: ")

# Process resumes in the specified folder
skill_data = process_resumes(folder_path)
