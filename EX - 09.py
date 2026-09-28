# Step 1: Import the regular expression module
import re

# Step 2: Store the text containing email addresses
text = """
Hello John,
Please contact us at support@example.com
or admin@company.org or .
"""

# Step 3: Create a pattern to find email addresses
pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

# Step 4: Find all email addresses in the text


emails = re.findall(pattern, text)

# Step 5: Display the extracted email addresses
for email in emails:
  print(email)

