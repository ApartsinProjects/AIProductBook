# Module Content Operator Prompt

Use this shorter prompt when you want a compact execution version of the full process.

```text
Create the full teaching package for Module [N]: [MODULE TITLE].

Produce these four HTML files inside the module folder:
- `lecture-notes.html`
- `lab.html`
- `lab-solution.html`
- `slides.html`

Requirements:
- The course is ground-up, self-contained, complete, modern, and hands-on.
- Start every topic from the large picture, why it matters, and the intuition before details.
- Make the module deep, detailed, highly informative, and production-oriented.
- Include many realistic examples, code examples, diagrams, and visual explanations.
- Strengthen intuition, mental models, and the high-level picture.
- Make the structure and sequence logical.
- Show clearly how all concepts connect and fit together.
- Include deep insights, common misconceptions, production implications, and failure modes.

Cross-referencing:
- Cross-reference earlier modules whenever previously introduced concepts are used.
- Lecture notes must link to previous lecture notes, this module’s lab, this module’s lab solution where useful, and this module’s slides where useful.
- Slides must link to previous modules when relevant, plus this module’s lecture notes and lab.
- Lab must link to exact supporting lecture note sections.
- Lab solution must include the complete assignment description, expected deliverable, supporting lecture links, and worked solution for each exercise.

Research and visuals:
- Search the web for current, authoritative, preferably primary sources.
- Include source links in the lecture notes.
- Search for useful illustrations/diagrams when needed.
- If useful, generate images/diagrams with Gemini API using `.env.all` for the API key.
- Prefer original inline SVG diagrams when possible.
- If using third-party images, label the source clearly.

Lecture notes:
- Create a polished standalone HTML teaching document.
- Include:
  - module purpose
  - why this module matters in the overall course
  - prerequisites from earlier modules
  - learning outcomes
  - large-picture orientation/map
  - mental models
  - conceptual and system-level explanations
  - deep examples
  - failure modes and misconceptions
  - production perspective
  - sources
- Add bridge/connection callouts between major sections.
- Add backward references to earlier modules and forward references to later ones.

Lab:
- Make it hands-on and realistic.
- Include objectives, prep, exercises, deliverables, rubric, and wrap-up.
- Tie each exercise to the lecture.

Lab solution:
- Include the full assignment/challenge description before each solution.
- Explain why the solution is strong, not just what the answer is.

Slides:
- Create interactive HTML slides, separate from the notes.
- Include next/previous controls, keyboard navigation, progress indicator, and overview mode.
- Distill the lecture into a clean live-teaching sequence.
- Keep the same intuition-first pedagogy.
- Link back to notes, lab, and lab solution.

Before finalizing:
- verify HTML structure
- verify all local links and anchors
- verify cross-references to earlier modules
- verify slides navigation
- verify the module feels deep, coherent, modern, and production-relevant
```
