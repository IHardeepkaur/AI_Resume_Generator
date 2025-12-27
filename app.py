print("=== AI Resume & Cover Letter Generator (Mock Version) ===\n")

job_role = input("Enter Job Role: ")
skills = input("Enter Skills (comma separated): ")
experience = input("Enter Experience Level (Fresher / Mid / Senior): ")

resume = f"""
RESUME SUMMARY
--------------
A motivated {job_role} with strong knowledge of {skills}.
Currently at a {experience} level, eager to apply skills in real-world projects,
learn new technologies, and contribute effectively to team success.
"""

cover_letter = f"""
COVER LETTER
------------
Dear Hiring Manager,

I am writing to apply for the position of {job_role}.
With skills in {skills} and a {experience} level of experience,
I am confident in my ability to contribute positively to your organization.

Thank you for considering my application.

Sincerely,
Candidate
"""

print("\n===== Generated Resume =====\n")
print(resume)

print("\n===== Generated Cover Letter =====\n")
print(cover_letter)

with open("data/output.txt", "w", encoding="utf-8") as file:
    file.write(resume + "\n" + cover_letter)

print("\n✅ Output saved in data/output.txt")
