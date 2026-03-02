# Day 1 - Mini Project

print("========================================")
print("   Welcome to the user info collector.  ")
print("========================================")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter you age: "))
email = input("Enter your email address: ")
phone_number = input("Enter your phone number: ")
city = input("Enter your city: ")
no_of_prog = int(input("Enter number of programming languages known: "))
fav_prog_lang = input("Enter your favorite programming language: ")
experience_years = int(input("Enter years of coding experience: "))
student = input("Are you a student(yes/no): ")

birth_year = 2024 - age
avg_lang_learned = no_of_prog / experience_years
exp_level = "Undetermined"
if experience_years < 1:
    exp_level = "Beginner"
elif experience_years > 1 and experience_years < 3:
    exp_level = "Intermediate"
elif experience_years > 3:
    exp_level = "Advanced"
else:
    exp_level = "Undetermined"

# prepare lines for boxed summary
summary_lines = [
    f"Name: {first_name} {last_name}",
    f"Age: {age} years old",
    f"Birth Year: {birth_year}",
    f"Email: {email}",
    f"Phone: {phone_number}",
    f"City: {city}",
    "",
    "Programming Experience:",
    f"  Languages Known: {no_of_prog}",
    f"  Favorite Language: {fav_prog_lang}",
    f"  Years of Experience: {experience_years}",
    f"  Experience Level: {exp_level}",
    f"  Avg Languages/Year: {avg_lang_learned:.1f}",
    f"  Student Status: {student}",
    "",
    "Message: Keep up the great work!"
]

# calculate box width (content + padding)
max_len = max(len(line) for line in summary_lines)
box_width = max_len + 2  # one space of padding each side

# print the box with unicode drawing characters
print("╔" + "═" * box_width + "╗")
title = "USER INFORMATION SUMMARY"
print("║" + title.center(box_width) + "║")
print("╠" + "═" * box_width + "╣")
for line in summary_lines:
    print("║ " + line.ljust(box_width - 2) + " ║")
print("╚" + "═" * box_width + "╝")

