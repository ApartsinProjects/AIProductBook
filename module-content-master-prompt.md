# Module Content Master Prompt

Use this prompt/template to repeat the full content-production process for every module in the AI Engineering course.

```text
Create a complete teaching package for Module [N]: [MODULE TITLE] in the AI Engineering course.

You are producing four high-quality HTML deliverables inside the module’s lecture-notes subfolder:
1. `lecture-notes.html`
2. `lab.html`
3. `lab-solution.html`
4. `slides.html`

General standard:
- The course is ground-up, self-contained, complete, modern, and hands-on.
- Assume only basic software engineering knowledge unless the course sequence has already introduced a concept.
- The material must be deep, detailed, and production-oriented.
- Always start each subject from the large picture, why it matters, and the intuition before going into mechanisms, implementation details, or edge cases.
- Strive to be highly informative, not superficial.
- Include many examples, many illustrations, and concrete code examples.
- Use clear modern AI engineering framing, aligned with current production practice.

Core pedagogical requirements:
- Strengthen intuition and high-level picture presentation so students build mental models.
- Show how concepts connect to each other and fit into the larger AI engineering map.
- Make the structure and sequence logical inside the module.
- Include really deep insights, not just definitions and lists.
- Explain not only what something is, but:
  - why it exists,
  - what problem it solves,
  - how it changes system design,
  - where it fails,
  - how it connects to previous modules,
  - how it shows up in production.
- When a concept has already been introduced earlier in the course, cross-reference the earlier lecture notes and slides wherever relevant.
- Explicitly remind the student when a new concept builds on a previously introduced one.

Cross-reference requirements:
- Lecture notes must cross-reference:
  - previous modules’ lecture notes when using earlier concepts
  - this module’s lab
  - this module’s lab solution where useful
  - this module’s slides where useful
- Slides must also cross-reference:
  - previous modules when they rely on prior concepts
  - this module’s lecture notes
  - this module’s lab
- Lab must cross-reference the exact supporting lecture note sections.
- Lab solution must cross-reference the exact supporting lecture note sections and include the complete assignment/challenge description before each solution.
- Whenever referencing a previous module concept, name it explicitly and link it clearly, for example:
  - “This builds on the retrieval mental model introduced in Module 5”
  - “Recall the autonomy ladder from Module 1”
  - “This uses the eval framing introduced in Module 13”
- Do not assume students will remember earlier material without reminders.

Web research requirements:
- Search the web for modern, authoritative, primary or highly credible sources relevant to the module.
- Use current official docs, leading technical blogs, research references, and top-quality educational materials where appropriate.
- Prefer primary sources for technical claims.
- Include source links in the final HTML notes.
- If using any third-party image or diagram, explicitly label the source in the page.
- Search the web for illustrations and diagrams if useful.
- If needed, generate new diagrams or images using Gemini API.
- When generating images with Gemini API, use `.env.all` for the Gemini API key.
- If original diagrams are sufficient, prefer self-contained original diagrams to reduce dependency/licensing issues.

Visual/illustration requirements:
- Include many graphical illustrations of systems and concepts.
- Use original inline SVG diagrams whenever practical.
- Add a few more full-page diagrams where appropriate, not just small diagrams.
- Diagrams should clarify:
  - system architecture,
  - conceptual distinctions,
  - lifecycle/flow,
  - failure modes,
  - production maturity,
  - tradeoffs,
  - interaction between components,
  - where the module fits into the overall course.
- Favor teaching diagrams over decorative diagrams.
- If a concept is abstract, add a visual mental model for it.

Code/example requirements:
- Include many concrete examples.
- Include code examples where appropriate in Python, TypeScript, shell, SQL, API payloads, config examples, architecture notes, or pseudocode depending on the module.
- Code examples should demonstrate how the concept appears in a real system.
- Include both “minimal version” and “production version” thinking where useful.
- Include contrast examples:
  - bad framing vs better framing
  - prototype vs production
  - brittle vs robust design
  - weak eval vs strong eval
  - unsafe vs safer system design
- Include realistic AI engineering examples, not toy examples only.

Lecture notes requirements:
Create `lecture-notes.html` as a detailed, rich, standalone HTML teaching document.

It must:
- Be polished, readable, and visually structured.
- Start with:
  - module title
  - module purpose
  - why this module matters in the overall course
  - prerequisites from earlier modules
  - what students should be able to do by the end
- Include a “large-picture map” or equivalent orientation section early in the document.
- Include explicit bridge sections/callouts between major sections so students can see how topics connect.
- Include mental models, conceptual frameworks, and deep heuristics.
- Include sections such as:
  - big picture
  - why now / why this matters
  - conceptual map
  - mental models
  - system/design implications
  - examples
  - failure modes / misconceptions
  - production implications
  - summary / what to retain
  - sources
  Adapt section names as appropriate to the module.
- Include “common misconceptions” callouts where useful.
- Include “deep insight” callouts where useful.
- Include “connection forward” and “connection backward” callouts:
  - backward to prior modules
  - forward to later modules
- Include source attribution section.
- Clearly indicate if diagrams are original or third-party.

Lab requirements:
Create `lab.html` as a separate standalone HTML lab for the module.

It must:
- Be hands-on and production-oriented.
- Reinforce the module’s main ideas through exercises and mini-project work.
- Include:
  - objectives
  - preparation
  - exercises/challenges
  - deliverables
  - rubric
  - wrap-up
- Cross-reference exact supporting lecture note sections.
- Use realistic tasks, not only academic questions.
- Include enough detail that an instructor or student can run the lab without missing context.

Lab solution requirements:
Create `lab-solution.html` as a separate standalone HTML worked solution.

It must:
- Include the complete assignment/challenge description for each exercise, not only the answer.
- For each exercise include:
  - original assignment prompt
  - expected deliverable
  - supporting lecture links
  - worked solution
  - explanation of why the solution is strong
- Include a final section summarizing the full lab challenge at a glance.
- Be pedagogically useful, not just a terse answer key.

Slides requirements:
Create `slides.html` as interactive HTML slides derived from the module.

It must:
- Be separate from the long-form notes, not a replacement.
- Be presentation-friendly and slide-sized.
- Include:
  - previous/next controls
  - keyboard navigation
  - progress indicator
  - slide overview/jump mode
- Distill the lecture into a coherent live-teaching sequence.
- Keep the same intuition-first pedagogy:
  - large picture first
  - mental models second
  - mechanisms third
  - implementation/examples later
- Include selected diagrams and strong visual summaries.
- Cross-reference prior modules when relying on earlier concepts.
- Link back to lecture notes, lab, and lab solution.
- Prioritize clarity for teaching over exhaustive density.

Course-wide consistency requirements:
- Preserve a coherent visual identity across modules, while allowing small thematic variation.
- Maintain a consistent structure so students know how to navigate each module.
- Whenever the module uses a previously introduced concept, explicitly cross-reference prior modules in both notes and slides.
- Build cumulative understanding across the course.
- Treat the course as one connected system, not isolated modules.

Quality bar:
- This should feel like high-quality professional course material.
- Avoid shallow summaries.
- Avoid generic AI boilerplate.
- Avoid disconnected lists of topics with no conceptual integration.
- Make the module feel teachable, memorable, and practically useful for future AI engineers.

Output constraints:
- Produce all four HTML files.
- Keep them self-contained unless linking to other course files.
- Ensure HTML structure is valid and balanced.
- Verify that cross-references point to the right local files/anchors.
- Verify that prior-module references are explicit wherever earlier concepts are reused.
- Verify the slides have working navigation.
- Verify labs and solutions link correctly to lecture note sections.

Before finalizing, perform a final pass to ensure:
- deep presentation of topics
- strong intuition and high-level picture
- logical structure and sequencing
- many examples
- many illustrations
- deep insights
- practical skills and production relevance
- cross-references to earlier modules where concepts recur
- cross-references between lecture notes, lab, solution, and slides
- modernity and alignment with current AI engineering practice
- completeness for the scope of the module
```
