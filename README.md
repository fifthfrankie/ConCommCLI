# Conventional Commit CLI

<img width="1277" alt="Screenshot 2023-06-12 at 09 01 52" src="https://github.com/fifthfrankie/ConCommCLI/assets/75613843/dce2af52-20db-47d7-a8ff-ab622ebe6025">

## Summary
The Conventional Commit CLI is a command-line tool designed to help users create well-formatted commit messages following the conventions of Conventional Commits. Conventional Commits provide a standardized format for commit messages, making it easier to understand the nature of changes introduced by a commit. This tool guides users through the process of creating a conventional commit message by prompting for the necessary information.

## Conventional Commits
Conventional Commits is a commit message convention that defines a specific structure for commit messages. It consists of the following parts:

1. **Type**: Denotes the type of change introduced by the commit. It can be one of the predefined types, such as `feat` (for new features), `fix` (for bug fixes), `docs` (for documentation changes), etc.

2. **Scope** (Optional): Provides additional contextual information about the section of the codebase that the commit changes.

3. **Description**: A short summary (1-50 characters) of the code changes introduced by the commit.

4. **Body** (Optional): Additional contextual information about the code changes.

5. **Footer** (Optional): Contains meta-information about the commit, such as related pull requests, reviewers, breaking changes, etc.

For more information on Conventional Commits, you can refer to the [Conventional Commits website](https://www.conventionalcommits.org/en/v1.0.0/).

## How to Use the Conventional Commit CLI

1. **Installation**: Clone the project repository and navigate to the "dist" folder.

2. **Running the CLI**: In the "dist" folder, locate the "ConCommCLI" executable file.

3. **Executing the CLI**: Run the "ConCommCLI" executable from the command line or terminal. The CLI will guide you through the process of creating a conventional commit message.

4. **Prompts**: The CLI will prompt you for different parts of the commit message, such as type, scope, description, body, and footer. You can enter `?` at any prompt to get help with that specific field.

5. **Validation**: The CLI performs validation on certain fields to ensure that they meet the required criteria. If an invalid input is provided, an error message will be displayed, and you will be prompted to enter a valid value.

6. **Commit Message**: Once you have provided all the necessary information, the CLI will display the final commit message based on the inputs provided.

## Example Commit Message
--------------------

🚀 feat(parser): add ability to parse arrays

This feature allows the parser to handle array input.

Related to issue 123

--------------------
## Repository Structure
- `ConCommCLI.py`: The Python script that implements the Conventional Commit CLI functionality.
- `dist/`: The dist folder containing the executable file.
- `README.md`: The README file providing instructions and information about the Conventional Commit CLI.

## Running the ConCommCLI Executable
To run the "ConCommCLI" executable from the dist folder, open a command line or terminal and navigate to the dist directory. Then, execute the following command:

--------------------

./ConCommCLI

--------------------
Follow the prompts to provide the necessary information and create a conventional commit message.

Please note that this README assumes you have Python installed on your system to run the `ConCommCLI.py` script. If Python is not installed, you will need to install it before executing the script.

That's it! You're ready to start creating well-formatted conventional commit messages using the Conventional Commit CLI. Happy committing!

