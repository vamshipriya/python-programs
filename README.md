# python-programs

 # User Info Collector

 Small Python script that collects basic user information and prints a boxed summary.

 ## Prerequisites

 - Python 3 (3.7+ recommended)

 ## Run

 1. (Optional) create and activate a virtual environment:

 ```bash
 python3 -m venv venv
 source venv/bin/activate
 ```

 2. Run the script:

 ```bash
 python3 python-programs/user_info_collector.py
 ```

 3. Answer the prompts (name, age, email, etc.). Example automated run using a heredoc:

 ```bash
 python3 python-programs/user_info_collector.py <<'EOF'
 John
 Doe
 25
 john.doe@email.com
 555-1234
 San Francisco
 3
 Python
 2
 yes
 EOF
 ```

 ## Example output

 The script prints a boxed summary similar to:

 ```
 ╔════════════════════════════════════════╗
 ║        USER INFORMATION SUMMARY        ║
 ╠════════════════════════════════════════╣
 ║ Name: John Doe                         ║
 ║ Age: 25 years old                      ║
 ║ Birth Year: 1999                       ║
 ║ Email: john.doe@email.com              ║
 ║ Phone: 555-1234                        ║
 ║ City: San Francisco                    ║
 ║                                        ║
 ║ Programming Experience:                ║
 ║   Languages Known: 3                   ║
 ║   Favorite Language: Python            ║
 ║   Years of Experience: 2               ║
 ║   Experience Level: Intermediate       ║
 ║   Avg Languages/Year: 1.5              ║
 ║   Student Status: yes                  ║
 ║                                        ║
 ║ Message: Keep up the great work!       ║
 ╚════════════════════════════════════════╝
 ```

 ## Files

 - `python-programs/user_info_collector.py` — main script that collects input and prints the boxed summary.
