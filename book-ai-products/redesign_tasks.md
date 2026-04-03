# Book Redesign Tasks

**Source**: `ai_product_book_deep_review_plan.md`  
**Date Created**: 2026-04-02  
**Status**: Ready for execution

---

## Overview

The book needs a fundamental redesign to become a true end-to-end operating manual for AI-powered products. This document captures every suggestion from the deep review.

---

## Part I — Redesign Macro-Architecture (7 Parts, 33 Chapters)

### Current Structure (5 Parts)
- Foundations
- Vibe Coding
- AI Product Management
- AI Engineering
- Integration

### New Structure (7 Parts, 33 Chapters + Appendices)

#### Part I — Why AI Changes Product Creation
1. The New Economics of Building with AI
2. What AI Can and Cannot Reliably Do
3. The Human-AI Product Stack (Synergy Triangle repositioned)
4. Scientific and Philosophical Principles for AI Products

#### Part II — AI-Native Product Discovery and Design
5. Finding Problems Worth Solving with AI
6. AI Product Strategy and Portfolio Thinking
7. AI-Native Product Discovery
8. **Designing AI User Experiences** (NEW - add as first-class discipline)
9. Requirements for Probabilistic Products

#### Part III — Vibe-Coding and AI-Native Prototyping
10. What Vibe-Coding Is Really For
11. AI-Native Prototyping Workflow
12. Prompting, Context, Memory, and Reusable Skills
13. Multi-Agent and Tool-Based Build Flows
14. From Prototype to Reviewable System

#### Part IV — Engineering AI Products
15. Reference Architectures for AI Products
16. Models, Routing, and Capability Allocation
17. Retrieval and Knowledge Systems
18. **State, Memory, and Workflow Orchestration** (NEW - dedicated concepts)
19. Building with Protocols and Interoperability (MCP, A2A)
20. **Security, Privacy, and Abuse Resistance** (NEW)

#### Part V — Evaluation, Reliability, and Governance
21. **Evals as the Core Development Discipline** (NEW - elevated from scattered)
22. Observability, Debugging, and Failure Analysis
23. Reliability, Guardrails, and Recovery
24. Cost, Latency, and Unit Economics
25. Governance, Compliance, and Trustworthy AI

#### Part VI — Shipping, Scaling, and Operating the Product
26. Launching AI Features and Products
27. **Post-Launch Learning Loops** (NEW)
28. Team Topologies and AI-Native Operating Models
29. Building the AI Product Organization
30. Strategic Positioning and Future-Proofing

#### Part VII — End-to-End Practice and Teaching Kit
31. End-to-End Capstone Playbook
32. Case Studies in Full
33. Teaching the Material as a Course

#### Appendices
- Tool comparison matrices
- Templates and PRDs
- Evaluation rubric library
- Architecture checklists
- Prompt/rules/skills examples
- Companion repo guide
- Glossary
- Update tracker

---

## Part II — Priority 1: Structural Redesign Tasks

### 1.1 Replace 5-part architecture with 7-part lifecycle architecture
- Create new part directories: part-1-why-ai-changes, part-2-discovery-design, part-3-vibe-coding, part-4-engineering, part-5-evaluation-reliability, part-6-shipping-scaling, part-7-practice-teaching
- Move/reorganize all existing chapters into new structure
- Update all cross-references and navigation links

### 1.2 Add full AI-native product design/UX layer
- Create Chapter 8: Designing AI User Experiences covering:
  - AI UX patterns beyond chatbots
  - Copilots, agents, invisible AI, review loops, hybrid interfaces
  - Trust calibration and explanation design
  - Fallbacks and recovery paths
  - Multimodal interaction design
- Integrate design thinking throughout other chapters

### 1.3 Elevate evals to dedicated Part V
- Consolidate all eval-related content into Part V
- Create Chapter 21: Evals as the Core Development Discipline
- Ensure eval-first is the thread connecting all parts

### 1.4 Add teaching/capstone packaging
- Create Chapter 31: End-to-End Capstone Playbook
- Create Chapter 33: Teaching the Material as a Course
- Add explicit course scaffolding throughout

---

## Part III — Priority 2: Chapter Surgery Tasks

### 2.1 Split oversized chapters

**Split "The AI PM Toolkit" into:**
- Requirements for Probabilistic Products (Chapter 9)
- AI-Native Product Discovery (Chapter 7)
- Experimentation Methods (within Part III or PM)
- AI Tools for PMs (sidebars/appendix reference)

**Split "Prompts, Chains, Agents, and Orchestration" into:**
- Prompting, Context, Memory, and Reusable Skills (Chapter 12)
- Multi-Agent and Tool-Based Build Flows (Chapter 13)
- State, Memory, and Workflow Orchestration (Chapter 18)

**Split "Scaling, Reliability, and Observability" into:**
- Observability, Debugging, and Failure Analysis (Chapter 22)
- Reliability, Guardrails, and Recovery (Chapter 23)
- Cost, Latency, and Unit Economics (Chapter 24)

### 2.2 Remove duplicated/mismatched navigation entries
- Audit toc.html for duplicated entries
- Fix chapter references and numbering inconsistencies
- Standardize section labels

### 2.3 Standardize chapter template
Every chapter should follow this 11-element template:
1. Why this chapter matters
2. Reader relevance by role (PM, designer, engineer, student, leader)
3. Core concepts and deeper principle
4. Practical framework or taxonomy
5. One or two worked examples
6. AI-assisted workflow demonstration
7. Common failure modes
8. Decision checklist
9. Exercise or lab
10. Summary
11. References and current tool snapshot

---

## Part IV — Priority 3: Add Core Missing Content

### 4.1 Add scientific/philosophical foundations
Create Chapter 4: Scientific and Philosophical Principles for AI Products
- Probabilistic systems vs deterministic software
- Bounded rationality and approximation
- Human-AI complementarity
- Sociotechnical systems
- Evidence over intuition
- Control loops and feedback systems
- Economics of near-zero marginal artifact generation
- Trust, uncertainty, and calibration
- Interfaces as contracts between humans, models, and tools

### 4.2 Add state/memory/workflow as dedicated concepts
Create Chapter 18: State, Memory, and Workflow Orchestration
- Prompts vs workflow graphs
- Session state and user memory
- Task memory and agent handoffs
- Durable execution
- Interruptibility and approval checkpoints

### 4.3 Add security and abuse resistance
Create Chapter 20: Security, Privacy, and Abuse Resistance
- Prompt injection
- Data leakage
- Tool misuse
- Authorization/authentication patterns
- Enterprise boundaries
- Red teaming
- Policy enforcement

### 4.4 Add post-launch learning loops
Create Chapter 27: Post-Launch Learning Loops
- Production evals
- Drift detection
- User-feedback harvesting
- Data flywheels
- Prompt/library evolution
- Roadmap updates from real usage

### 4.5 Add missing topics from current book gaps
- Protocol-driven interoperability (MCP, A2A)
- Human-in-the-loop workflows
- Uncertainty communication
- Multimodal UX
- Workflow redesign (not just screen redesign)

---

## Part V — Priority 4: Companion Ecosystem Tasks

### 5.1 Create GitHub repository structure
- Starter templates
- Reusable evaluation datasets
- Notebooks and minimal starter projects
- Prompt/rules/skills library

### 5.2 Create instructor materials
- Slide deck per part
- Instructor handbook
- Assignment bank
- Rubric bank

### 5.3 Create living companion page
- Update log for tool/version changes
- Latest ecosystem updates page

---

## Part VI — Priority 5: Visual and Pedagogical Polish

### 6.1 Add recurring conceptual spine callout boxes
Add these 6 principles as recurring callout boxes throughout:
1. **AI systems are probabilistic, not fully programmable**
   - Requirements must be behavioral
   - Evals must be continuous
   - Reliability is managed, not assumed

2. **AI product quality is fundamentally sociotechnical**
   - Quality depends on prompt, model, tools, data, UX, policy, and human workflow together

3. **Evaluation is the primary epistemic instrument**
   - Evals are not a QA afterthought
   - They are how teams know what they built

4. **Marginal cost of creating artifacts has collapsed, but judgment has become more valuable**
   - Roles evolve toward steering, critique, and system shaping

5. **Interfaces are control systems**
   - Prompts, UI constraints, tools, approval gates, and memory are all parts of behavioral control

6. **AI products require explicit trust design**
   - Confidence, uncertainty, escalation, and explanation are part of the product itself

### 6.2 Add role-specific lenses at chapter starts
For each chapter, add explicit sections:
- Why PMs should care
- Why designers should care
- Why engineers should care
- Why students/instructors should care
- Why leaders/strategists should care

### 6.3 Add end-of-chapter operational assets
Each chapter should include:
- Key concepts summary
- Decision checklist
- Pitfalls to avoid
- Exercise
- Mini-lab
- AI-assisted workflow example
- Further reading
- Artifact templates

### 6.4 Redistribute case studies throughout book
Recurring case studies (not just late in book):
- One lightweight startup-style product
- One enterprise product
- One multimodal product
- One failure/postmortem
- One academic/research translation case

### 6.5 Add practical templates
Create templates for:
- Eval-first PRD
- AI opportunity brief
- Risk register
- Architecture review
- Launch readiness checklist
- Failure review
- Model selection scorecard
- Routing policy template
- System prompt review worksheet
- Agent approval policy

### 6.6 Add multi-track reading paths
Provide explicit pathways:
- PM/designer path
- Engineer path
- Instructor/student path
- Executive/strategist path
- Founder/solo-builder path

### 6.7 Add comparison tables
Add decision tables for:
- When to use workflow vs agent
- When to use RAG vs fine-tuning vs memory
- When to self-host vs managed
- When to route models
- When to use multi-agent vs single-agent
- When to expose autonomy vs require approval

### 6.8 Add bridge notes
Add "From prototype to production" boxes:
- What was okay in prototype but unacceptable in production
- Which shortcuts to remove
- What to formalize next
- How to phase the hardening work

### 6.9 Add lab boxes
Each major chapter should have:
- "Try this in 30 minutes"
- "Build this in a weekend"
- "Production hardening exercise"
- "Classroom discussion prompt"

### 6.10 Add visual diagrams
Add diagram-rich content:
- Lifecycle diagrams
- Architecture maps
- Decision trees
- Comparison matrices
- Failure loops
- Trust/escalation flows
- Feedback loop diagrams

---

## Part VII — Editorial and Layout Tasks

### 7.1 Improve hierarchy clarity
Use explicit hierarchy:
- Part
- Chapter
- Section
- Pattern/Checklist/Lab/Case box

### 7.2 Standardize chapter depth
- Some chapters = short conceptual
- Others = operational reference chapters
- Avoid equal breadth across all chapters

### 7.3 Use denser but more navigable layouts
Add elements:
- Margin summaries
- Chapter maps
- Role icons
- Comparison tables
- Checklists
- Architecture diagrams
- "Production note" boxes
- "Course note" boxes

### 7.4 Separate stable from volatile content
Inside each chapter structure:
- **Core principles** section (durable)
- **Current practice snapshot** section
- **Tooling notes** section (volatile, updateable)

### 7.5 Fix structural issues
- Remove duplicated entries in ToC
- Fix chapter references and numbering
- Fix mismatched chapter labels/pages
- Address uneven section depth

---

## Part VIII — Academic Course Packaging Tasks

### 8.1 12-week course structure
- Week 1: Why AI changes products
- Week 2: AI capabilities, limits, and mental models
- Week 3: AI-native discovery and product strategy
- Week 4: AI UX and trust design
- Week 5: Eval-first requirements
- Week 6: Vibe-coding and prototyping
- Week 7: Retrieval, memory, and orchestration
- Week 8: Models, routing, and architecture
- Week 9: Evals and observability
- Week 10: Governance, security, and trust
- Week 11: Launch, metrics, and post-launch learning
- Week 12: Capstone demos and postmortems

### 8.2 14-week course structure
Same as above with dedicated weeks for:
- Design
- Security/governance
- Organizational strategy

### 8.3 Course outputs
- Opportunity memo
- AI PRD
- UX flow + trust plan
- Working prototype
- Eval suite
- Architecture document
- Launch + governance plan
- Final capstone demo and report

---

## Part IX — Refactoring Guidance for Current Book

### 9.1 Keep, but reposition
- Synergy Triangle → Part I as human-AI operating model
- Vibe coding → narrower, more disciplined Part III
- AI PM toolkit → split across discovery, requirements, and evals
- Orchestration/RAG/model selection → central in engineering Part IV
- Team structures/culture → move to operating model Part VI

### 9.2 Add entirely new major areas
- AI product design / UX
- State/memory/workflow as dedicated concepts
- Security and abuse resistance
- Post-launch learning loops
- Explicit academic course packaging
- Scientific/philosophical foundations chapter
- End-to-end capstone framework
- Design of uncertainty and trust

### 9.3 Reduce tool lock-in in core chapters
Move fast-changing tool specifics into:
- Comparison tables
- Boxed examples
- Online companion updates
- Per-chapter "current ecosystem snapshot" sections

---

## Part X — Running Examples (from RUNNING_EXAMPLES_PLAN.md)

Maintain and redistribute these 5 case studies throughout the book:
1. **QuickShip Logistics** - Startup, logistics, vibe coding focus
2. **HealthMetrics Analytics** - Enterprise SaaS, healthcare, AI PM focus
3. **DataForge Enterprise** - Enterprise, data/ETL, AI engineering focus
4. **RetailMind AI** - Series A, retail, integration focus
5. **EduGen Platform** - Bootstrapped, EdTech, cross-functional focus

---

## Execution Order

### Phase 1: Foundation (High Priority)
1. Redesign macro-architecture (7 parts, 33 chapters)
2. Update toc.html and navigation structure
3. Create new part directories
4. Move/reorganize existing content into new structure

### Phase 2: Content Additions (High Priority)
5. Add AI-native product design/UX (Chapter 8)
6. Add scientific/philosophical foundations (Chapter 4)
7. Add state/memory/workflow (Chapter 18)
8. Add security/abuse resistance (Chapter 20)
9. Add post-launch learning loops (Chapter 27)
10. Elevate evals to Part V (Chapter 21)

### Phase 3: Chapter Surgery (High Priority)
11. Split oversized chapters
12. Fix structural/editorial issues
13. Implement chapter template (11 elements)
14. Add role-specific lenses
15. Add end-of-chapter operational assets

### Phase 4: Pedagogical Enhancement (Medium Priority)
16. Add recurring conceptual spine callout boxes
17. Redistribute case studies throughout
18. Add practical templates
19. Add multi-track reading paths
20. Add comparison tables
21. Add bridge notes

### Phase 5: Course Packaging (Medium Priority)
22. Create 12/14-week course structures
23. Add capstone framework
24. Add lab boxes
25. Add exercises

### Phase 6: Companion Assets (Low Priority)
26. Create GitHub repo structure
27. Create instructor materials
28. Add appendices
29. Visual/pedagogical polish

---

## Completion Criteria

The redesign is complete when:
- [ ] Book has 7-part, 33-chapter lifecycle-based structure
- [ ] AI-native design is a first-class discipline
- [ ] Evals are the central connective tissue (Part V)
- [ ] Every chapter follows the 11-element template
- [ ] Role-specific lenses appear in every chapter
- [ ] 6 conceptual spine principles recur throughout
- [ ] Case studies appear throughout (not just late)
- [ ] Academic course packaging is complete (12/14-week)
- [ ] All 5 case studies (QuickShip, HealthMetrics, DataForge, RetailMind, EduGen) are integrated
- [ ] All structural/editorial issues are resolved
- [ ] Companion ecosystem (repo, templates, labs) is created
- [ ] Book projects operational precision and unified identity
