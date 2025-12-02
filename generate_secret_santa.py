
import random
import base64
import re

# List of participants
NAMES = ["Amel", "Mayline", "Lara", "Franz", "Amelia", "Elvis", "Elias"]

def generate_secret_santa(names):
    """
    Generate a valid Secret Santa assignment.
    Returns a dictionary mapping giver -> receiver.
    """
    # Create a derangement (permutation where no element appears in its original position)
    attempts = 0
    max_attempts = 1000

    while attempts < max_attempts:
        shuffled = names.copy()
        random.shuffle(shuffled)

        # Check if it's a valid derangement (nobody gets themselves)
        valid = True
        for i, name in enumerate(names):
            if name == shuffled[i]:
                valid = False
                break

        if valid:
            # Create the assignment dictionary
            assignment = {names[i]: shuffled[i] for i in range(len(names))}
            return assignment

        attempts += 1

    raise Exception("Could not generate valid assignment after many attempts")

def encode_base64(text):
    """Encode text to Base64."""
    return base64.b64encode(text.encode()).decode()

def update_script_js(assignments, script_path="script.js"):
    """Update the script.js file with new assignments."""

    # Read the current script.js
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build the new assignments object
    assignments_lines = []
    for giver, receiver in assignments.items():
        encoded = encode_base64(receiver)
        assignments_lines.append(f'    "{giver}": "{encoded}",       // Base64 encoded')

    # Remove trailing comma from last line
    assignments_lines[-1] = assignments_lines[-1].replace(',       //', '        //')

    new_assignments_block = "const assignments = {\n" + "\n".join(assignments_lines) + "\n  };"

    # Replace the assignments block using regex
    pattern = r'const assignments = \{[^}]+\};'
    new_content = re.sub(pattern, new_assignments_block, content, flags=re.DOTALL)

    # Write back to file
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✅ Secret Santa assignments generated and updated in script.js!")
    print("\n⚠️  IMPORTANT: The assignments are now hidden. Don't decode them if you want to participate!")

if __name__ == "__main__":
    print("🎅 Generating Secret Santa assignments...\n")

    # Generate assignments
    assignments = generate_secret_santa(NAMES)

    # Update script.js
    update_script_js(assignments)

    print("\n🎄 You can now share the website with participants!")
    print("💡 To generate a new assignment, run this script again: python3 generate_secret_santa.py")
