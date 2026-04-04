# Module Content QA Checklist

Use this checklist after generating each module’s `lecture-notes.html`, `lab.html`, `lab-solution.html`, and `slides.html`.

## 1. Pedagogy And Depth

- Does the module start from the large picture before details?
- Does it explain why the topic matters before mechanics?
- Does it build clear mental models?
- Does it include deep insights rather than only definitions?
- Does it explain how the topic connects to production AI engineering?
- Does it clearly show how the concepts fit together?
- Does it explain how the module connects backward to previous modules and forward to later modules?
- Are there misconceptions or failure modes explicitly addressed?

## 2. Completeness Of Deliverables

- Are all four files present?
- Is `lecture-notes.html` present?
- Is `lab.html` present?
- Is `lab-solution.html` present?
- Is `slides.html` present?

## 3. Lecture Notes Quality

- Does the lecture notes page include:
  - module title
  - module purpose
  - why the module matters in the course
  - prerequisites from earlier modules
  - learning outcomes
  - a large-picture map or orientation section
  - mental models
  - examples
  - production implications
  - misconceptions or failure modes
  - sources
- Are the explanations detailed and informative?
- Are bridge/connection callouts present between major sections?
- Are deep-insight callouts present where useful?
- Are common misconceptions called out where useful?
- Are the sections sequenced logically?

## 4. Examples And Practicality

- Are there many concrete examples?
- Are examples realistic rather than purely toy examples?
- Are there relevant code examples?
- Do examples show real AI engineering system thinking?
- Are there contrast examples where useful:
  - bad vs better framing
  - prototype vs production
  - brittle vs robust
  - unsafe vs safer
- Is the module hands-on in spirit, not just descriptive?

## 5. Visuals And Illustrations

- Are there enough diagrams and illustrations?
- Are diagrams pedagogically useful rather than decorative?
- Is there at least one strong large-picture diagram?
- Are there system diagrams where architecture matters?
- Are there flow/lifecycle diagrams where workflows matter?
- Are there failure-mode or tradeoff diagrams where appropriate?
- If third-party images are used, are they clearly labeled with sources?
- If Gemini-generated visuals are used, was `.env.all` used for the Gemini API key?

## 6. Research Quality

- Were modern, authoritative sources used?
- Were primary sources preferred for technical content?
- Are source links included in the lecture notes?
- Are claims consistent with current AI engineering practice?
- Is the module modern and up to date?

## 7. Cross-References

- Does the lecture notes page cross-reference earlier modules when older concepts are reused?
- Do those references explicitly name the prior concept/module?
- Does the lecture notes page link to:
  - this module’s lab
  - this module’s lab solution where useful
  - this module’s slides where useful
- Does the lab link to exact supporting lecture sections?
- Does the lab solution link to exact supporting lecture sections?
- Do the slides link back to notes and lab?
- Do the slides reference earlier modules when relying on prior concepts?
- Do anchors and links actually work?

## 8. Lab Quality

- Does the lab include:
  - objectives
  - preparation
  - exercises/challenges
  - deliverables
  - rubric
  - wrap-up
- Are the exercises realistic and production-oriented?
- Can a student run the lab without missing context?
- Is the lab clearly tied to the lecture material?

## 9. Lab Solution Quality

- Does each exercise solution include:
  - the complete original assignment/challenge description
  - the expected deliverable
  - supporting lecture links
  - the worked solution
  - explanation of why the solution is strong
- Is there a final “full lab challenge at a glance” summary?
- Is the solution pedagogically useful, not just terse?

## 10. Slides Quality

- Are the slides interactive HTML, separate from the notes?
- Do the slides have:
  - previous/next controls
  - keyboard navigation
  - progress indicator
  - overview/jump mode
- Do the slides present a coherent live-teaching sequence?
- Do they preserve intuition-first pedagogy?
- Do they distill the lecture rather than merely copying it?
- Are the slides visually clear and presentation-friendly?
- Are the links back to lecture notes/lab/lab solution present?

## 11. Technical Validation

- Is the HTML structure balanced in each file?
- Are major tags balanced?
- Are local paths correct?
- Are anchors correct?
- Does the slide navigation script work?
- Are there any obvious rendering issues?

## 12. Final Quality Gate

- Does the module feel like high-quality professional course material?
- Does it avoid shallow summary-style writing?
- Does it avoid generic AI boilerplate?
- Does it feel memorable and teachable?
- Does it support both self-study and live instruction?
- Would a serious aspiring AI engineer find this genuinely useful?
