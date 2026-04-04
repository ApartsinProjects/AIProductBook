# Book Redesign Notes - Phase 1

## Overview
This document tracks the restructuring of the book from 5 parts/20 chapters to 7 parts/33 chapters.

## Old Structure (5 Parts, 20 Chapters)
- Part I: Foundations (Chapters 1-2)
- Part II: Vibe Coding (Chapters 3-6)
- Part III: AI PM (Chapters 7-11)
- Part IV: AI Engineering (Chapters 12-16)
- Part V: Integration (Chapters 17-20)

## New Structure (7 Parts, 33 Chapters)
- Part I: Why AI Changes Product Creation (Chapters 1-4)
- Part II: AI-Native Product Discovery and Design (Chapters 5-9)
- Part III: Vibe-Coding and AI-Native Prototyping (Chapters 10-14)
- Part IV: Engineering AI Products (Chapters 15-20)
- Part V: Evaluation, Reliability, and Governance (Chapters 21-25)
- Part VI: Shipping, Scaling, and Operating the Product (Chapters 26-30)
- Part VII: End-to-End Practice and Teaching Kit (Chapters 31-33)

## Content Mapping: Old Chapters to New Chapters

### Part I: Why AI Changes Product Creation

| Old Chapter | New Chapter | Status | Notes |
|-------------|-------------|--------|-------|
| Ch 1: AI Capabilities | Ch 1: New Economics | REVISED | Combined with economics content from Ch 1-2 |
| Ch 2: Synergy Triangle | Ch 3: Human-AI Product Stack | REPOSITIONED | Renamed and reframed |
| - | Ch 1: Economics of AI | NEW | 50x cost reduction, reasoning models |
| - | Ch 2: What AI Can/Cannot Do | REVISED | Split from old Ch 1 |
| - | Ch 4: Scientific Principles | NEW | Cognitive load, complementary change |

### Part II: AI-Native Product Discovery and Design

| Old Chapter | New Chapter | Status | Notes |
|-------------|-------------|--------|-------|
| Ch 7: AI Product Strategy | Ch 6: AI Product Strategy | REVISED | Expanded with portfolio thinking |
| Ch 8: AI PM Toolkit | Ch 9: Requirements | SPLIT | USID.O, eval-first PRDs split out |
| Ch 9: Discovery | Ch 5: Finding Problems | REVISED | Revised discovery methodology |
| - | Ch 7: AI-Native Discovery | NEW | Systematic approaches |
| - | Ch 8: Designing AI UX | NEW | First-class design discipline |

### Part III: Vibe-Coding and AI-Native Prototyping

| Old Chapter | New Chapter | Status | Notes |
|-------------|-------------|--------|-------|
| Ch 3: Understanding Vibe Coding | Ch 10: What Vibe-Coding Is For | REVISED | Reframed as discovery tool |
| Ch 4: Vibe Coding Workflows | Ch 11: AI-Native Prototyping | REVISED | Expanded workflow |
| Ch 5: Full Lifecycle | Ch 14: Prototype to System | REVISED | Production readiness |
| Ch 6: Claude Code Skills | Ch 12: Prompting/Skills | SPLIT | Prompting content split |
| Ch 13: Prompts/Chains/Agents | Ch 13: Multi-Agent | SPLIT | Multi-agent split out |

### Part IV: Engineering AI Products

| Old Chapter | New Chapter | Status | Notes |
|-------------|-------------|--------|-------|
| Ch 12: Core Principles | Ch 15: Reference Architectures | NEW STRUCTURE | Consolidated architecture |
| Ch 13: Prompts/Chains/Agents | Ch 16: Models/Routing | SPLIT | Model selection split |
| Ch 13: Prompts/Chains/Agents | Ch 19: Protocols | EXPANDED | MCP, A2A expanded |
| Ch 14: Advanced RAG | Ch 17: Retrieval | EXPANDED | RAG content expanded |
| - | Ch 18: State/Memory | NEW | Workflow orchestration |
| - | Ch 20: Security/Privacy | NEW | Prompt injection, etc. |

### Part V: Evaluation, Reliability, and Governance

| Old Chapter | New Chapter | Status | Notes |
|-------------|-------------|--------|-------|
| - | Ch 21: Evals | NEW ELEVATED | Eval-first approach elevated |
| Ch 17: Scaling/Observability | Ch 22: Observability | SPLIT | Observability split |
| Ch 17: Scaling/Observability | Ch 23: Reliability | SPLIT | Guardrails split |
| Ch 16: LLMOps | Ch 24: Cost/Latency | SPLIT | Unit economics split |
| Ch 10: Ethics/Trust | Ch 25: Governance | EXPANDED | NIST, ISO, EU AI Act |

### Part VI: Shipping, Scaling, and Operating

| Old Chapter | New Chapter | Status | Notes |
|-------------|-------------|--------|-------|
| Ch 11: GTM | Ch 26: Launching | REVISED | AI-specific launch strategies |
| - | Ch 27: Learning Loops | NEW | Post-launch improvement |
| Ch 20: Team Structures | Ch 28: Team Topologies | REVISED | AI-native topologies |
| Ch 20: Team Structures | Ch 29: AI Organization | REVISED | Organizational focus |
| Ch 21: Future-Proofing | Ch 30: Positioning | REVISED | Strategic positioning |

### Part VII: End-to-End Practice and Teaching

| Old Chapter | New Chapter | Status | Notes |
|-------------|-------------|--------|-------|
| Ch 18: Playbook | Ch 31: Capstone | NEW | End-to-end workflow |
| Ch 19: Case Studies | Ch 32: Case Studies | REVISED | Full case studies |
| - | Ch 33: Teaching | NEW | Course creation guidance |

## Status Summary

### Chapters with Full Content (from existing material)
- Ch 1 (partial), Ch 2 (partial), Ch 3 (partial), Ch 6 (partial), Ch 9 (partial)
- Ch 10, Ch 11, Ch 12, Ch 13, Ch 14 (from current Part II-III)
- Ch 17, Ch 19 (from current Part IV)
- Ch 25 (from current Ch 10)
- Ch 26, Ch 28, Ch 29, Ch 30 (from current Part V-VI)

### Chapters Needing Full Content Creation
- Ch 1: Economics of AI - NEW (requires combining current Ch 1-2 content)
- Ch 4: Scientific Principles - NEW (requires original content)
- Ch 5: Finding Problems - REVISED (needs update)
- Ch 7: AI-Native Discovery - NEW (requires original content)
- Ch 8: Designing AI UX - NEW (requires original content)
- Ch 15: Reference Architectures - NEW STRUCTURE (requires combining/synthesizing)
- Ch 16: Models/Routing - SPLIT (needs work)
- Ch 18: State/Memory - NEW (requires original content)
- Ch 20: Security - NEW (requires original content)
- Ch 21: Evals - NEW ELEVATED (requires combining existing eval content)
- Ch 22: Observability - SPLIT (needs work)
- Ch 23: Reliability - SPLIT (needs work)
- Ch 24: Cost/Latency - SPLIT (needs work)
- Ch 27: Learning Loops - NEW (requires original content)
- Ch 31: Capstone - NEW (requires original content)
- Ch 33: Teaching - NEW (requires original content)

### Appendices Status
- Appendix A: Glossary - PARTIAL (has basic entries)
- Appendix B: Tool Comparison - PLACEHOLDER
- Appendix C: Templates - PLACEHOLDER
- Appendix D: Evaluation Rubrics - PLACEHOLDER
- Appendix E: Architecture Checklists - PLACEHOLDER
- Appendix F: Prompts/Skills - PLACEHOLDER

## Files Created/Modified

### Directories Created
- part-1-why-ai-changes/ (with chapter-1 through chapter-4)
- part-2-discovery-design/ (with chapter-5 through chapter-9)
- part-3-vibe-coding/ (with chapter-10 through chapter-14)
- part-4-engineering/ (with chapter-15 through chapter-20)
- part-5-evaluation-reliability/ (with chapter-21 through chapter-25)
- part-6-shipping-scaling/ (with chapter-26 through chapter-30)
- part-7-practice-teaching/ (with chapter-31 through chapter-33, appendices/)
- legacy-structure/ (contains old parts I-V)

### Files Created
- 7 BOOK_CONFIG.md files (one per part)
- 7 part index.html files
- 33 chapter index.html files
- 6 appendix files (placeholders)
- Updated toc.html
- REDESIGN_NOTES.md

### Files in Legacy Structure
- part-1-foundations/ (original Part I)
- part-2-vibe-coding/ (original Part II)
- part-3-ai-pm/ (original Part III)
- part-4-ai-engineering/ (original Part IV)
- part-5-integration/ (original Part V)
- back-matter/ (original back matter)

## Next Steps (Phase 2+)

1. **Content Migration**: Move existing content from legacy chapters to new structure
2. **Section Creation**: Create actual section content for all 33 chapters
3. **Placeholder Resolution**: Replace placeholders in appendices with full content
4. **Cross-Reference Updates**: Update all internal links to point to new structure
5. **Image/Asset Organization**: Organize images for new structure
6. **Index Updates**: Update master index.html to reflect new structure

## Notes
- All new HTML files use the existing book.css stylesheet
- Golden titles, callout boxes, and existing styling preserved
- Navigation structure follows existing patterns
- Placeholder sections are clearly marked for future content
