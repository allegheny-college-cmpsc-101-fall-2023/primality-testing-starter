# Primality Testing Engineering Effort

![Proactive Programmers](.github/images/Square-Proactive-Programmers-Logo.svg)

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-blue.svg)](https://github.com/psf/black)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Discord](https://img.shields.io/discord/872320492936257537?logo=discord)](https://discord.gg/kjah8MFYbR)

- Due date: Check the [Proactive Programmers Discord
server](https://discord.gg/kjah8MFYbR).
- This assignment will be submitted on GitHub following
the expectations in the syllabus on
[Assignment Submission](https://github.com/allegheny-college-cmpsc-101-fall-2023/course-materials#assignment-submission).
- Modifications to the gatorgrade.yml file are not permitted without explicit instruction.
- To begin, read this `README` and the
[Primality Testing project description](https://proactiveprogrammers.com/data-abstraction/engineering-efforts/primality-testing/)
on the Proactive Programmers website.
- You can check the
[primality-testing-starter repository](https://github.com/allegheny-college-cmpsc-101-fall-2023/primality-testing-starter)
for any updates to this project's documentation or
source code.

## Learning Objectives

This assignment is about rememebering and understanding
programming language constructs by running programs,
observing output, and describing steps.
The learning objectives of this assignment are to:

1. Use Git and GitHub to manage source code file changes
2. Study type annotation in function declarations, floating point
arithmetic, and modulus operations
3. Write clearly about the programming concepts in this assignment.

## Seeking Assistance

Please review the course expectations on the syllabus about
[Seeking Assistance](https://github.com/allegheny-college-cmpsc-101-fall-2023/course-materials#seeking-assistance).
Students are reminded
to uphold the Honor Code. Cloning the assignment repository is a
commitment to the latter.

For this assignment, you may use class materials, textbooks, notes, and the
internet. However,when asked to write "in your own words", you must use
_your own_ words.

Post questions to the
[Proactive Programmers Discord server](https://discord.gg/kjah8MFYbR).

## Project Overview

After cloning this repository to your computer, please take the following
steps:

- Make sure that you have already installed and know how to use all of the
  programming tools that are mentioned in the description of the [Proactive
  Skills](https://proactiveprogrammers.com/proactive-skills/technical-skills/introduction-technical-skills/).
- Follow the instructions on the Proactive Programmers web site for this project
  to take all of the needed steps and to complete all of the required
  deliverables.
- Use the `cd` command to change into the directory for this repository.
- Specifically, you can change into the program directory by typing `cd primality`.
- Install the dependencies for the project by typing `poetry install`.
- Run the program in the following fashion by typing:
  - `poetry run primality --number 49979687 --approach efficient`
  - `poetry run primality --number 49979687 --approach efficient --profile`
  - Please note that the program will not work unless you add the required
    source code.
  - Please refer to the `writing/reflection.md` file for all ways to run the
    program.
  - Again, please note that there are multiple ways to run this project and you
    should try them all!
- Confirm that the program is producing the expected output by looking in the
  appropriate section of the project description on the Proactive Programmers
  web site.
- If you have already installed the
  [GatorGrade](https://github.com/GatorEducator/gatorgrade) program that runs
  the automated grading checks provided by
  [GatorGrader](https://github.com/GatorEducator/gatorgrader) you can, from the
  repository's base directory, run the automated grading checks by typing
  `gatorgrade --config config/gatorgrade.yml`. If a specific part of a
  `gatorgrade` check does not work on your laptop, please refer to GitHub
  Actions to see if it passed when run on the continuous integration server.
- Again, you may always review the output from running GatorGrader in GitHub
  Actions.
- Don't forget to provide all of the required responses to the technical writing
  prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
  labels from all of the provided source code. This means that instead of only
  deleting the `TODO` marker from the code you should delete the `TODO` marker
  and the entire prompt and then add your own comments to demonstrate that you
  understand all of the source code in this project.
- Please make sure that you also completely delete the `TODO` markers and their
  labels from every line of the `writing/reflection.md` file. This means that
  you should not simply delete the `TODO` marker but instead delete the entire
  prompt so that your reflection is a document that contains polished technical
  writing that is suitable for publication on your professional web site.
