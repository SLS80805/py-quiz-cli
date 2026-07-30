# py-quiz-cli

A lightweight, interactive Command Line Interface (CLI) quiz application built with pure Python. Designed with clean control flow and structured data models, `py-quiz-cli` offers a fast, zero-dependency quiz-taking experience directly inside your terminal.

---

## Project Overview

`py-quiz-cli` showcases fundamental Python programming principles, including dynamic list iteration, input validation, and structured data manipulation using dictionaries and lists.

Users are presented with a series of multiple-choice questions, given real-time feedback after each selection, and provided with a summary of their score and accuracy percentage upon completion.

---

## Key Features

- **Zero External Dependencies:** Built entirely using standard Python—runs out of the box in any Python 3 environment.
- **Robust Input Validation:** Uses input checking via loop control to ensure users can only select valid options (1–4), preventing crashes from invalid inputs.
- **Instant Answer Feedback:** Displays immediate evaluation (`✓ Correct!` or `✗ Wrong!`) for each question and reveals the right answer if you make a mistake.
- **Structured Question Dataset:** Uses a simple data structure, making it effortless to add new questions and options.
- **Performance Summary:** Tallying logic calculates total correct answers and generates an overall accuracy percentage at the end.

---

## How It Works

1. **Data Initialization:** Questions, options, and answer keys are structured as dictionaries within a master list.
2. **Interactive Loop:** The app iterates through the questions, displaying options dynamically.
3. **Input Interception:** The script validates input choices against available options before proceeding.
4. **Result Calculation:** After all questions are answered, the app outputs final performance metrics.

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
