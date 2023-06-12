import re
import random

commit_types = ['build', 'ci', 'chore', 'docs', 'feat', 'fix', 'perf', 'refactor', 'revert', 'style', 'test']

help_messages = {
    "type": "🔀 Type is a must-have part of the commit message. It denotes the type of change introduced. It can be one of the following: " + ", ".join(commit_types),
    "scope": "🔎 Scope is an optional part of the commit message. It provides additional contextual information about the section of the codebase that the commit changes.",
    "description": "📝 Description is a must-have part of the commit message. It's a short summary of the code changes, and it should be 1-50 characters long.",
    "body": "💡 Body is an optional part of the commit message. It provides additional contextual information about the code changes.",
    "footer": "👣 Footer is an optional part of the commit message. It contains meta-information about the commit, like related pull-requests, reviewers, breaking changes, etc.",
}

_prompts = [
    "🤔 What's the",
    "🔍 Enter the",
    "💬 Give me the",
    "🖋️ Your",
    "✨ Time for",
    "💥 Tell me the",
]

def validate_commit_type(commit_type):
    if commit_type.lower() not in commit_types:
        raise ValueError(f"Invalid type '{commit_type}'. Expected one of {', '.join(commit_types)}")
    return True

def validate_description(description):
    if not 1 <= len(description) <= 50:
        raise ValueError("Description should be 1-50 characters long.")
    return True

def get_input(field_name, validation_func=None):
    while True:
        user_input = input(f"{random.choice(_prompts)} \033[96m{field_name}\033[0m of your commit (or \033[93m?\033[0m for help): ").strip()
        if user_input == "?":
            print(help_messages[field_name])
        else:
            try:
                if validation_func:
                    validation_func(user_input)
                return user_input
            except ValueError as e:
                print(f"\033[91m❌ Invalid input. {str(e)} Please try again.\033[0m")

print("\033[92m🌟 ConvComm-CLI 🌟\033[0m\n")
print("This tool is here to help you create \033[95mperfect\033[0m commit messages in the format of conventional commits.\n \nJust follow the prompts, and remember, you can enter \033[93m?\033[0m at any prompt to get help with that field.")
print("\nHere is an example of a best practice commit message:\n")
print("-------------------------------------------------------------------------------------------------------\n")
print("\033[96m🚀 feat(parser): add ability to parse arrays\n\nThis feature allows the parser to handle array input.\n\nRelated to issue #123\033[0m\n")
print("-------------------------------------------------------------------------------------------------------\n")
print("For more information on Conventional Commits, visit: \033[94mhttps://www.conventionalcommits.org/en/v1.0.0/\033[0m\n")
print("-------------------------------------------------------------------------------------------------------\n")

type_input = get_input("type", validate_commit_type)
while not validate_commit_type(type_input):
    print("\033[91m❌ Invalid type. Please try again.\033[0m")
    type_input = get_input("type", validate_commit_type)

scope_input = get_input("scope")

desc_input = get_input("description", validate_description)
while not validate_description(desc_input):
    print("\033[91m❌ Invalid description. It should be 1-50 characters long.\033[0m")
    desc_input = get_input("description", validate_description)

body_input = get_input("body")
footer_input = get_input("footer")

commit_message = f"{type_input}({scope_input}): {desc_input}\n\n{body_input}\n\n{footer_input}"
print(f"\n\033[92m✨ Great job! Here's your commit message:\033[0m\n\033[96m{commit_message}\033[0m")
