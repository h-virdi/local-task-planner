# Local Task Planner
This is a local AI-based task planner utilising [Ollama](https://ollama.com). The 'clienati' library is used to break down the input goal into smaller, more manageable tasks with the estimated duration and  necessary resources for each task.

## Features
- **Goal-Oriented Task Planning**: Obtain a structured project outline for your goal.
- **Timeline Validation**: A realistic timeline is created using reasonable time estimates for each sub-task.
- **Plan Formatting**: The generated plan is cleanly formatted to clearly display the sub-tasks, deadlines, and required resources.

## Installation

### Prerequisites

- Python 3.6 or later
- `pip` (Python package installer)
- [Ollama](https://ollama.com) installed locally

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/h-virdi/local-task-planner.git

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt

3. Install Ollama and pull the required model, llama3:
   ```bash
   ollama pull llama3

## Running the Planner

1. Navigate to the project directory:
   ```bash
   cd local-task-planner
   
2. Run the task planner:
   ```bash
   python task_planner.py

3. As per the on-screen prompt, enter a goal for which the system will generate a practical, timeline-based plan. 

## Example Usage
Task Planner (Local AI)
Enter your goal, and I'll create a practical, timeline-based plan.
Type 'quit' to exit.

==================================================

Enter your goal: Create a personal portfolio website

Your Plan:

Here's a potential design for your personal portfolio website based on the provided timeline and project plan:

**Project Title:** Personal Portfolio Website

**Objective:** To create an online platform showcasing my skills, experience, and projects as a [Your Profession/Student].

**Timeline:**

* Task 1: Research and planning (2025-05-06, 2 hours)
* Task 2: Design and development (2025-05-06 to 2025-05-07, 3+4=7 hours)
* Task 3: Testing and refinement (2025-05-06 to 2025-05-07, 4 hours)

**Required Resources:**

* Computer
* Internet

**Project Plan:**

I. Research and Planning (Task 1)

* Conduct a SWOT analysis of my strengths, weaknesses, opportunities, and threats in the industry/profession.
* Identify key projects and experiences to feature on the website.
* Define the target audience for the portfolio.

II. Design and Development (Task 2 & Task 3)

* Create a visually appealing design concept for the website, incorporating my personal brand and style.
* Develop the website using [Your preferred web development framework/technology].
* Implement necessary features, such as:
	+ Projects showcase with descriptions, images, and links to live demos or GitHub repositories (if applicable).
	+ About page with a brief introduction, skills summary, and contact information.
	+ Testimonials or feedback from previous clients, colleagues, or mentors.

III. Testing and Refinement (Task 3)

* Conduct usability testing on the website using [Your preferred testing tool/technique].
* Gather feedback from peers, mentors, or industry experts to identify areas for improvement.
* Make necessary updates and refinements to ensure a high-quality, user-friendly experience.

**Deliverables:**

1. A fully functional personal portfolio website showcasing my skills, experience, and projects.
2. A written reflection on the project process, including lessons learned and future improvements.

By following this plan, I aim to create a professional online presence that effectively communicates my value as a [Your Profession/Student] and helps me stand out in the industry/profession.

Please let me know if you'd like me to make any changes or if you have any specific requirements!
