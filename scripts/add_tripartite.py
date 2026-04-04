#!/usr/bin/env python3
"""
Add tripartite loop callout to remaining chapters in Parts 4-7.
"""
from pathlib import Path
import re

base = Path('E:/Projects/AIEngineering/book-ai-products')

# Chapter to part mapping and tripartite loop descriptions
chapter_info = {
    # Part 4 - Engineering
    16: ("part-4-engineering", "Model Selection, Routing, and Fine-Tuning",
         "Model selection and routing decisions activate all three disciplines: <strong>AI PM</strong> defines performance requirements, cost constraints, and quality thresholds that guide model choice; <strong>Vibe-Coding</strong> tests different models and routing strategies against real workloads to find the best performance per dollar; <strong>AI Engineering</strong> implements the selection logic, fallback chains, and monitoring that ensure the right model serves each request."),
    17: ("part-4-engineering", "Retrieval Systems and Knowledge",
         "Building retrieval systems requires all three disciplines working together: <strong>AI PM</strong> defines what knowledge the product needs access to and how relevance should be measured; <strong>Vibe-Coding</strong> experiments with different retrieval strategies, chunking approaches, and ranking algorithms to find what works; <strong>AI Engineering</strong> implements the retrieval pipeline, vector database, and caching that make retrieval fast and reliable."),
    18: ("part-4-engineering", "State, Memory, and Workflow Orchestration",
         "Managing state and memory in AI products requires all three disciplines: <strong>AI PM</strong> defines how long conversations should remain coherent and what memory patterns users expect; <strong>Vibe-Coding</strong> prototypes different memory architectures to test which create the best user experience; <strong>AI Engineering</strong> implements the actual state management, session handling, and workflow orchestration that make stateful AI products work."),
    19: ("part-4-engineering", "Protocols, Interoperability, and MCP",
         "Building interoperable AI systems requires all three disciplines: <strong>AI PM</strong> decides which protocols matter for your product ecosystem and what interoperability means for users; <strong>Vibe-Coding</strong> tests protocol integrations quickly to verify they work before full implementation; <strong>AI Engineering</strong> implements the actual protocol handling, message translation, and service connections that make interoperability real."),
    20: ("part-4-engineering", "Security, Privacy, and Abuse Resistance",
         "Securing AI products requires all three disciplines working in parallel: <strong>AI PM</strong> defines the threat model, acceptable risk levels, and privacy requirements that guide security decisions; <strong>Vibe-Coding</strong> rapidly probes for vulnerabilities, tests prompt injection attacks, and explores failure modes; <strong>AI Engineering</strong> implements the actual security measures, guardrails, and monitoring that protect the product."),
    # Part 5 - Evaluation
    21: ("part-5-evaluation-reliability", "Evaluation Core",
         "Building evaluation infrastructure requires all three disciplines: <strong>AI PM</strong> defines what quality means for the product and what metrics matter most to users; <strong>Vibe-Coding</strong> rapidly generates test cases, benchmarks, and evaluation scenarios to measure performance; <strong>AI Engineering</strong> builds the eval pipelines, scoring systems, and reporting that make quality visible and actionable."),
    22: ("part-5-evaluation-reliability", "Observability and Debugging",
         "Observing AI systems requires all three disciplines working together: <strong>AI PM</strong> identifies what behaviors matter to track and what alerts indicate user-facing problems; <strong>Vibe-Coding</strong> explores different failure modes to understand what could go wrong and how to detect it; <strong>AI Engineering</strong> implements the tracing, logging, and monitoring that make debugging possible."),
    23: ("part-5-evaluation-reliability", "Reliability and Guardrails",
         "Building reliable AI products requires all three disciplines: <strong>AI PM</strong> defines what failures are acceptable and how the product should degrade gracefully; <strong>Vibe-Coding</strong> probes for failure modes and tests different response strategies; <strong>AI Engineering</strong> implements the validation, retry logic, and guardrails that protect users from failures."),
    24: ("part-5-evaluation-reliability", "Unit Economics and Cost Optimization",
         "Optimizing AI economics requires all three disciplines: <strong>AI PM</strong> defines the cost targets and trade-offs between quality, latency, and price; <strong>Vibe-Coding</strong> experiments with different optimization strategies to find what actually reduces cost; <strong>AI Engineering</strong> implements the caching, batching, and routing that make optimization real."),
    25: ("part-5-evaluation-reliability", "Governance and Compliance",
         "Governing AI products requires all three disciplines: <strong>AI PM</strong> defines the policies, compliance requirements, and ethical boundaries the product must respect; <strong>Vibe-Coding</strong> tests policy enforcement to see if rules actually work in practice; <strong>AI Engineering</strong> implements the controls, auditing, and reporting that demonstrate compliance."),
    # Part 6 - Shipping/Scaling
    26: ("part-6-shipping-scaling", "Launch and Rollout",
         "Launching AI products requires all three disciplines: <strong>AI PM</strong> defines the rollout strategy, success metrics, and rollback criteria; <strong>Vibe-Coding</strong> tests rollout mechanisms and monitors early signals before full launch; <strong>AI Engineering</strong> implements the deployment, monitoring, and rollback infrastructure that makes rollout safe."),
    27: ("part-6-shipping-scaling", "Post-Launch Learning Loops",
         "Building learning loops requires all three disciplines: <strong>AI PM</strong> defines what feedback to collect and how to prioritize improvement areas; <strong>Vibe-Coding</strong> experiments with feedback collection mechanisms to see what actually works; <strong>AI Engineering</strong> implements the data pipelines, retraining triggers, and model updates that make learning happen."),
    28: ("part-6-shipping-scaling", "Team Topologies",
         "Organizing AI teams requires all three disciplines: <strong>AI PM</strong> defines roles, responsibilities, and how different functions collaborate; <strong>Vibe-Coding</strong> tests different team structures to find what actually improves delivery; <strong>AI Engineering</strong> implements the processes, hand-offs, and documentation that make team structure work."),
    29: ("part-6-shipping-scaling", "AI-Native Organizations",
         "Building AI-native organizations requires all three disciplines: <strong>AI PM</strong> decides how to structure teams for AI product development and what capabilities to build internally; <strong>Vibe-Coding</strong> experiments with organizational patterns to test what actually improves velocity; <strong>AI Engineering</strong> implements the tools, infrastructure, and standards that enable AI-native ways of working."),
    30: ("part-6-shipping-scaling", "Strategic Positioning",
         "Positioning AI products strategically requires all three disciplines: <strong>AI PM</strong> identifies competitive differentiation and market positioning; <strong>Vibe-Coding</strong> tests different positioning strategies through experiments and rapid validation; <strong>AI Engineering</strong> builds the capabilities that make positioning real, not just marketing."),
    # Part 7 - Practice/Teaching
    31: ("part-7-practice-teaching", "The Capstone",
         "The capstone synthesizes all three disciplines into practice: <strong>AI PM</strong> leads the product definition, prioritization, and stakeholder management; <strong>Vibe-Coding</strong> drives rapid prototyping and iteration to test assumptions quickly; <strong>AI Engineering</strong> builds the production-quality system that can actually ship."),
    32: ("part-7-practice-teaching", "Case Studies",
         "Case studies reveal how all three disciplines work in practice: <strong>AI PM</strong> perspectives show how product decisions were made; <strong>Vibe-Coding</strong> perspectives show how rapid iteration was achieved; <strong>AI Engineering</strong> perspectives show how production challenges were solved."),
    33: ("part-7-practice-teaching", "Teaching AI Product Development",
         "Teaching AI product development requires all three disciplines: <strong>AI PM</strong> teaches product thinking and prioritization; <strong>Vibe-Coding</strong> teaches rapid experimentation and iteration; <strong>AI Engineering</strong> teaches production thinking and reliability."),
}

for ch, (part_dir, chapter_title, tripartite_text) in chapter_info.items():
    html = base / part_dir / f'chapter-{ch}/index.html'
    if not html.exists():
        print(f'SKIP: {html} does not exist')
        continue
    
    content = html.read_text(encoding='utf-8', errors='ignore')
    
    # Check if already has tripartite callout
    if 'The Tripartite Loop' in content:
        print(f'SKIP Ch {ch}: already has tripartite callout')
        continue
    
    # Find the pattern: after opening-hook, before figure
    pattern = r'(<div class="opening-hook">.*?</div>)(\s*<figure class="illustration">)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        callout = '''
        <div class="callout key-insight">
            <div class="callout-title">The Tripartite Loop in ''' + chapter_title + '''</div>
            <p>''' + tripartite_text + '''</p>
        </div>
'''
        content = content[:match.end(1)] + callout + content[match.start(2):]
        html.write_text(content, encoding='utf-8')
        print(f'ADDED Ch {ch}: tripartite callout')
    else:
        print(f'FAIL Ch {ch}: could not find pattern')

print('\\nDone!')