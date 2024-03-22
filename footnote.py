# Randomize footnote identifiers in multiple Quarto files to avoid conflicts

import re
import glob
import os
import random
import string


def randomize_footnote_identifiers(qmd_content):
    # Find all existing footnote identifiers (numbers)
    existing_ids = set(re.findall(r'\[\^(\d+)\]', qmd_content))

    # Generate a unique random identifier for each existing footnote
    unique_ids = {}
    for id in existing_ids:
        # Generate a random string of 5 characters
        new_id = ''.join(random.choices(
            string.ascii_letters + string.digits, k=5))
        while new_id in unique_ids.values():  # Ensure it's unique
            new_id = ''.join(random.choices(
                string.ascii_letters + string.digits, k=5))
        unique_ids[id] = new_id

    # Replace all footnote references and definitions with new identifiers
    for old_id, new_id in unique_ids.items():
        qmd_content = re.sub(
            rf'\[\^{old_id}\]', f'[^{new_id}]', qmd_content)
        qmd_content = re.sub(
            rf'\[\^{old_id}\]:', f'[^{new_id}]:', qmd_content)

    return qmd_content


# Change directory to 'contents'
os.chdir('contents')
qmd_files = glob.glob('*.qmd')

for file_name in qmd_files:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    new_content = randomize_footnote_identifiers(content)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(new_content)
