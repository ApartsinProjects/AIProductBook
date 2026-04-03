# Running Examples Master Plan

This document defines 5 diverse running examples that appear throughout the book to demonstrate concepts in context. Each example is designed to highlight different aspects of the Synergy Triangle framework.

---

## Example 1: QuickShip Logistics

**Focus**: Vibe Coding
**Type**: Startup (2-person team)
**Domain**: Logistics/Operations
**AI Complexity**: Medium (LLM + retrieval + agents)

### Product Description
QuickShip is a small logistics startup helping small e-commerce businesses optimize their shipping routes and carrier selection. The founding team consists of a developer and a former logistics manager. They use vibe coding to rapidly prototype and iterate on their product.

### Evolution Across Chapters

| Chapter | Example Content | Callout Type |
|---------|-----------------|--------------|
| **1 - AI Capabilities** | QuickShip decides to build an AI-powered route optimizer. Introduction to the problem space. | **big-picture**: Why logistics is ripe for AI disruption |
| **2 - Synergy Triangle** | How QuickShip's developer handles vibe coding while the logistics manager provides domain expertise. | **key-insight**: The synergy between domain expert and vibe coder |
| **3 - Understanding Vibe Coding** | QuickShip's developer shows their first vibe coding session, using Cursor to build a route visualization dashboard | **practical-example**: First prompt to working UI in 20 minutes |
| **4 - Vibe Coding Workflows** | Iterating on the route algorithm. Multi-file generation for the full dashboard | **code**: Sample prompts that generate complex multi-file structures |
| **5 - Full Lifecycle** | Moving from prototype to testable code. Adding unit tests with AI help | **skill**: Using Claude Code to generate test cases |
| **6 - Skills & Plugins** | QuickShip creates a custom skill for their deployment workflow | **document**: SKILL.md for their deployment pipeline |
| **7 - AI PM Strategy** | The logistics manager defines success metrics: "95% of route suggestions must be within 10% of optimal" | **document**: PRD excerpt with eval criteria |
| **8 - AI PM Toolkit** | Building eval datasets from historical shipping data | **code**: Python script for creating golden datasets |
| **9 - Discovery & Prioritization** | User research with small e-commerce owners | **team-discussion**: Conversation between founder and users |
| **11 - Ethics & Trust** | Addressing bias in route recommendations (some areas have fewer carrier options) | **architecture**: Fallback logic for underserved regions |
| **12 - AI Engineering Principles** | Transitioning from vibe prototype to production architecture | **architecture**: System diagram showing the production stack |
| **13 - Prompts & Agents** | Implementing a multi-agent system: one agent for route calculation, one for carrier selection | **code**: LangGraph agent implementation |
| **15 - Model Selection** | Router strategy: using lightweight models for simple routes, frontier models for complex multi-stop routes | **document**: Model routing decision matrix |
| **16 - Inference & LLMOps** | Cost monitoring dashboard. Optimizing token usage | **code**: Cost tracking implementation |
| **17 - Scaling & Observability** | Monitoring latency for real-time route suggestions | **architecture**: Observability stack with Prometheus/Grafana |
| **18 - Integration Playbook** | QuickShip's complete vibe-to-production journey | **big-picture**: Timeline from idea to launch |
| **19 - Case Studies** | Lessons learned: what worked, what failed | **key-insight**: The importance of eval-first development |

### Callout Box Contents

**Code Callout (Ch 4)**:
```
# QuickShip prompt: Generate route visualization dashboard
"Create a React dashboard showing delivery routes on a map. 
Include a sidebar with route details, carrier info, and cost 
breakdown. Use Tailwind CSS. Make it interactive with hover 
states showing delivery windows."
```

**Skill Callout (Ch 6)**:
```
# SKILL.md for QuickShip Deployment
## Triggers
- "deploy to staging"
- "prepare release"

## Instructions
1. Run full test suite
2. Build Docker image
3. Deploy to staging cluster
4. Run smoke tests
5. Post status to #quickhip-slack
```

**Team Discussion (Ch 9)**:
```
PM (former logistics manager): "Users keep asking for 
real-time tracking. But they also complain about subscription 
costs. We need to understand if tracking is a differentiator 
or just noise."

Developer: "I can add basic tracking with webhooks from carriers. 
Won't need new AI features. Just data aggregation."
```

---

## Example 2: HealthMetrics Analytics

**Focus**: AI PM
**Type**: Healthcare SaaS (mid-size company)
**Domain**: Healthcare analytics
**AI Complexity**: High (LLM + RAG + strict evals + compliance)

### Product Description
HealthMetrics is a B2B platform helping hospital administrators analyze patient flow, resource utilization, and staff scheduling. Their AI features include natural language queries of operational data and automated report generation.

### Evolution Across Chapters

| Chapter | Example Content | Callout Type |
|---------|-----------------|--------------|
| **1 - AI Capabilities** | HealthMetrics evaluates AI for clinical decision support | **warning**: Regulatory constraints on healthcare AI |
| **2 - Synergy Triangle** | PM team works with compliance officers and clinical advisors | **key-insight**: Healthcare requires extra PM rigor |
| **6 - AI PM Strategy** | Build/buy/bake decision: building custom RAG on their medical literature | **document**: Build vs buy comparison table |
| **7 - AI PM Strategy** | Categorizing their product: copilot (query interface) vs autonomous (auto-scheduling) | **big-picture**: AI product taxonomy in healthcare |
| **8 - AI PM Toolkit** | The USID.O framework adapted for healthcare: longer compliance checkpoints | **document**: Modified USID.O checklist |
| **8 - Eval-First PRDs** | Defining "safe" metrics: AI suggestions must never conflict with clinical guidelines | **document**: PRD excerpt with hard constraints |
| **9 - User Research** | Interviewing hospital administrators about pain points | **team-discussion**: Research synthesis session |
| **10 - Ethics & Governance** | ISO 42001 compliance, bias detection in patient routing | **document**: Compliance checklist |
| **10 - Bias Detection** | Finding that the AI deprioritizes patients from lower-income areas | **warning**: Real-world bias discovered in eval |
| **11 - GTM** | Pricing model: per-query vs per-bed vs enterprise flat fee | **document**: Pricing model comparison |
| **12 - AI Engineering Principles** | Eval-driven development with clinical safety as priority | **key-insight**: Why healthcare can't skip evals |
| **13 - RAG Systems** | Building medical literature RAG with strict relevance scoring | **architecture**: RAG pipeline with guardrails |
| **14 - Advanced RAG** | Graph RAG for connecting patient symptoms to resource availability | **code**: Neo4j integration for knowledge graphs |
| **15 - Model Selection** | Router using Claude for complex queries, smaller models for routine reports | **document**: Model selection matrix with latency/cost/accuracy |
| **16 - Guardrails** | Input validation preventing PII from entering the prompt | **code**: PII detection and redaction module |
| **17 - Observability** | Monitoring "escalation rate" - how often AI defers to human judgment | **big-picture**: Healthcare-specific AI metrics |
| **18 - Integration Playbook** | HealthMetrics' 18-month journey from concept to enterprise rollout | **key-insight**: Healthcare AI timelines |
| **20 - Team Structures** | Specialized roles: Clinical AI PM, Compliance AI Lead, AI Safety Engineer | **document**: Org chart for healthcare AI team |

### Callout Box Contents

**PRD Excerpt (Ch 8)**:
```
## Success Metrics
- Query accuracy: >= 90% on clinical terminology test set
- Response latency: p99 < 3 seconds
- Safety escalation rate: <= 5% (AI defers to human)
- Zero hallucination tolerance on medication interactions

## Hard Constraints
- AI must never suggest overriding physician orders
- All patient data must be anonymized in prompts
- Audit trail required for all AI recommendations
```

**Bias Warning (Ch 10)**:
```
## Bias Detection Finding
During eval on 10,000 historical patient records, we discovered:
- AI deprioritized patients from zip codes with median income < $45k
- False negative rate 3x higher for patients with non-commercial insurance
- Required adding fairness constraints to the model router
```

**Team Discussion (Ch 9)**:
```
Senior PM: "Dr. Martinez says the query interface works great 
for simple questions. But she never uses it for complex cases."

Junior PM: "Is that because she doesn't trust the AI for complex 
cases, or because the interface is too slow?"

Senior PM: "She wants to verify the source. Show me the evidence.
That's our next sprint: citation links and confidence scores."
```

---

## Example 3: DataForge Enterprise

**Focus**: AI Engineering
**Type**: Enterprise software company
**Domain**: Data pipeline/ETL automation
**AI Complexity**: Very High (multi-agent orchestration + RAG + LLMOps)

### Product Description
DataForge helps enterprises automate their data pipelines using natural language. Users describe what data transformation they want in plain English, and DataForge's AI generates and maintains the corresponding ETL code.

### Evolution Across Chapters

| Chapter | Example Content | Callout Type |
|---------|-----------------|--------------|
| **2 - Synergy Triangle** | DataForge's engineering team needs to understand PM requirements before building | **key-insight**: Why engineering can't ignore PM |
| **6 - Skills** | Engineering team creates shared skills for their ML pipeline development | **skill**: Multi-agent orchestration skill for data validation |
| **12 - AI Engineering Principles** | Eval-driven development: building evals before writing code | **big-picture**: Enterprise AI development differs from startups |
| **13 - Prompts & Agents** | Multi-agent architecture: Parser Agent, Code Generator Agent, Validator Agent | **architecture**: Agent orchestration diagram |
| **13 - MCP Connectors** | Integrating with enterprise data sources via MCP | **code**: MCP server implementation for Snowflake |
| **14 - Advanced RAG** | RAG on internal enterprise data schemas and documentation | **code**: Schema-aware retrieval implementation |
| **15 - Model Selection** | Dynamic model selection based on query complexity | **document**: Router configuration with thresholds |
| **16 - Inference Serving** | vLLM deployment for low-latency code generation | **architecture**: Inference stack with batching |
| **16 - CI/CD for Prompts** | Prompt version control with A/B testing | **code**: Git-based prompt deployment workflow |
| **17 - Scaling** | Multi-tenancy with enterprise isolation | **architecture**: Tenant isolation architecture |
| **17 - Observability** | Custom metrics: code acceptance rate, pipeline success rate, user satisfaction | **code**: Prometheus metrics definitions |
| **18 - Integration Playbook** | DataForge's 2-year journey to production | **big-picture**: Enterprise sales cycles |
| **19 - Case Studies** | Lessons from building in the enterprise | **key-insight**: Why enterprise AI is slower but more stable |
| **20 - Team Structures** | Roles: AI Pipeline Engineer, Prompt Engineer, ML Ops, Enterprise Integration Lead | **document**: Team structure diagram |
| **21 - Future-Proofing** | Plans for autonomous pipeline maintenance agents | **research-frontier**: Agentic AI for enterprise |

### Callout Box Contents

**Architecture Diagram (Ch 13)**:
```
User: "Create a pipeline that joins customer data with orders, 
      filters for high-value customers, and outputs to Redshift"

Agents:
[Parser Agent] -> [Code Generator Agent] -> [Validator Agent]
       |                  |                        |
       v                  v                        v
  Extracts intent    Generates Python     Validates against
  and entities      with pandas/dbt     enterprise schema
```

**MCP Code (Ch 13)**:
```python
# Snowflake MCP server excerpt
class SnowflakeConnector:
    async def execute_query(self, query: str, tenant_id: str) -> dict:
        # Tenant isolation enforced at connection level
        connection = await self.pool.get_connection(
            tenant_id=tenant_id,
            query_timeout=30
        )
        result = await connection.execute(query)
        return {"rows": result.fetchall(), "schema": result.schema}
```

**Observability Code (Ch 17)**:
```python
# Prometheus metrics for DataForge
CODE_ACCEPTANCE = Counter(
    'dataforge_code_acceptance_total',
    'User acceptance of generated code',
    ['user_tier', 'complexity']
)
PIPELINE_SUCCESS = Histogram(
    'dataforge_pipeline_success_duration_seconds',
    'Time for generated pipeline to first success',
    buckets=[60, 300, 900, 3600]
)
```

---

## Example 4: RetailMind AI

**Focus**: Integration (Full Vibe-to-Production)
**Type**: Retail AI startup (series A)
**Domain**: Retail personalization
**AI Complexity**: Medium-High (LLM + recommendations + real-time)

### Product Description
RetailMind helps brick-and-mortar retailers personalize in-store experiences using AI. Their product includes: AI shopping assistants on tablets, personalized promotions, and inventory predictions.

### Evolution Across Chapters

| Chapter | Example Content | Callout Type |
|---------|-----------------|--------------|
| **1 - AI Capabilities** | RetailMind evaluates AI for real-time personalization | **big-picture**: Why retail is a different AI challenge than e-commerce |
| **2 - Synergy Triangle** | How RetailMind synchronizes vibe coding, PM, and engineering | **key-insight**: Full triangle demonstration |
| **3 - Vibe Coding Intro** | Weekend prototype: shopping assistant chat interface | **practical-example**: First 24-hour prototype |
| **4 - Vibe Workflows** | Rapid iteration on the recommendation algorithm | **code**: Prompt engineering for retail persona |
| **5 - Full Lifecycle** | Adding analytics and testing to vibe prototype | **skill**: Testing skill for AI features |
| **6 - Skills** | Team-specific skills for deployment and monitoring | **skill**: Shared team deployment skill |
| **7 - AI PM Strategy** | Pivot decision: from B2C to B2B after week 4 | **big-picture**: When to pivot based on vibes |
| **8 - Eval-First PRDs** | Defining "engagement" metrics for in-store AI | **document**: PRD with multi-metric success criteria |
| **9 - Discovery** | User research at retail locations | **team-discussion**: Store manager interview |
| **10 - Ethics** | Privacy concerns with in-store tracking | **warning**: Customer privacy in physical spaces |
| **11 - GTM** | Pilot program with 3 retail chains | **document**: Pilot program structure |
| **12 - AI Engineering** | Production architecture for real-time inference | **architecture**: Edge + cloud hybrid architecture |
| **13 - Agents** | Shopping assistant agent with personality | **code**: Retail persona prompt template |
| **14 - RAG** | Product knowledge base RAG | **code**: Product embedding pipeline |
| **15 - Model Selection** | Balancing cost and quality for in-store devices | **document**: Edge deployment model comparison |
| **16 - LLMOps** | Cost management for retail scale (thousands of stores) | **key-insight**: AI economics at retail scale |
| **17 - Reliability** | Offline mode for stores with poor connectivity | **architecture**: Graceful degradation design |
| **18 - Integration Playbook** | Complete 12-month journey from idea to 100 stores | **big-picture**: Timeline with key milestones |
| **19 - Case Studies** | What RetailMind learned about physical retail AI | **key-insight**: The importance of store associate buy-in |
| **20 - Team Structures** | Cross-functional retail AI team | **document**: Team composition and roles |

### Callout Box Contents

**Prototype Code (Ch 3)**:
```
# First weekend prototype prompt
"Build a chat interface for a retail shopping assistant.
It should ask about preferences, suggest products, and
show promotions. Use a warm, friendly tone. Add a store
map showing product locations."
```

**Team Discussion (Ch 9)**:
```
Store Manager: "I like the idea. But my associates are 
already overwhelmed. They can't learn another system."

RetailMind PM: "What if the AI surfaces information 
your associates already know, just faster?"

Store Manager: "Maybe. But if it gives wrong info, 
customers will blame us, not the AI."
```

**Architecture (Ch 12)**:
```
┌─────────────────────────────────────────────────────┐
│ Edge Layer (in-store)                              │
│ ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│ │ Shopping    │  │ Inventory   │  │ Promo       │ │
│ │ Assistant   │  │ Scanner     │  │ Engine      │ │
│ └──────┬──────┘  └──────┬──────┘  └──────┬──────┘ │
│        │                 │                 │        │
│        └─────────────────┼─────────────────┘        │
│                          │                          │
│              ┌───────────▼───────────┐              │
│              │ Edge Inference Server │              │
│              │ (Local model cache)   │              │
│              └───────────┬───────────┘              │
└──────────────────────────┼──────────────────────────┘
                           │ Limited connectivity
                           ▼
┌──────────────────────────────────────────────────────┐
│ Cloud Layer                                          │
│ ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │
│ │ RAG Server  │  │ Model       │  │ Analytics   │   │
│ │ (Products)  │  │ Router      │  │ Pipeline    │   │
│ └─────────────┘  └─────────────┘  └─────────────┘   │
└──────────────────────────────────────────────────────┘
```

---

## Example 5: EduGen Platform

**Focus**: Cross-functional (Complete Concept to Deployment)
**Type**: EdTech startup (bootstrapped to seed)
**Domain**: Education/Personalized learning
**AI Complexity**: Medium (LLM + learning analytics + assessments)

### Product Description
EduGen creates AI-powered personalized learning paths for vocational training. Their platform assesses learner knowledge, identifies gaps, and generates customized curriculum.

### Evolution Across Chapters

| Chapter | Example Content | Callout Type |
|---------|-----------------|--------------|
| **1 - AI Capabilities** | EduGen's founding story: why AI for vocational training | **big-picture**: The $30B vocational training market |
| **2 - Synergy Triangle** | Founder balancing all three pillars as solo operator | **key-insight**: Synergy triangle in a 1-person team |
| **3 - Vibe Coding** | First prototype: AI-generated lesson plans | **practical-example**: Weekend hackathon to MVP |
| **4 - Vibe Workflows** | Iterating on the assessment engine | **code**: Adaptive quiz generation prompts |
| **5 - Full Lifecycle** | Adding user authentication and progress tracking | **skill**: EduGen development skill |
| **6 - Skills** | Custom skill for curriculum generation workflow | **document**: SKILL.md for lesson generation |
| **7 - AI PM Strategy** | First 100 users: gathering feedback | **team-discussion**: User interview synthesis |
| **8 - Eval-First PRDs** | Defining "learning outcome" metrics | **document**: PRD with measurable outcomes |
| **9 - Discovery** | Research on vocational learner pain points | **big-picture**: Why workers need AI learning |
| **10 - Ethics** | Ensuring equitable access to AI learning | **warning**: Digital divide in vocational training |
| **11 - GTM** | First paid customers: small trade schools | **document**: Pricing and packaging |
| **12 - AI Engineering** | Productionizing the curriculum generator | **architecture**: Content generation pipeline |
| **13 - Agents** | Learner agent that adapts to student pace | **code**: Learning path agent implementation |
| **14 - RAG** | RAG on curriculum standards and industry certifications | **code**: Certification-aware retrieval |
| **15 - Model Selection** | Router balancing quality and cost for content generation | **document**: Cost per course analysis |
| **16 - LLMOps** | Monitoring content quality and learner engagement | **code**: Quality scoring implementation |
| **17 - Scaling** | Growing from 100 to 10,000 learners | **key-insight**: Scaling challenges in EdTech |
| **18 - Integration Playbook** | Complete journey: bootstrapped to seed in 18 months | **big-picture**: EduGen's funding story |
| **19 - Case Studies** | Comparing EduGen to competitors (Coursera, Udacity) | **comparison-table**: AI approach comparison |
| **20 - Team Structures** | Growing the team: first hires | **document**: Org chart evolution |
| **21 - Future-Proofing** | Plans for AI tutors and skill certification | **research-frontier**: Autonomous learning companions |

### Callout Box Contents

**Founding Story (Ch 1)**:
```
"I was working as an electrician when I realized: the 
 apprenticeship system hasn't changed in 50 years. 
 Young workers learn on the job, slowly. I thought:
 what if AI could accelerate skilled trades training?"

- Maria Chen, Founder of EduGen
```

**Learning Path Agent Code (Ch 13)**:
```python
# Learner adaptation logic
def adapt_learning_path(learner_id: str, progress: dict) -> LearningPath:
    learner = get_learner(learner_id)
    
    if progress.completion_rate < 0.6:
        # Learner struggling - add prerequisites
        return LearningPath(
            additional_topics=[prerequisite_skills],
            pace="slower",
            practice_ratio=0.7  # More practice problems
        )
    elif progress.completion_rate > 0.9 and progress.quiz_scores > 0.85:
        # Learner excelling - accelerate
        return LearningPath(
            skip_review=True,
            pace="faster",
            advanced_topics=True
        )
    else:
        # On track - standard path
        return LearningPath(pace="standard")
```

**Pricing Document (Ch 11)**:
```
## EduGen Pricing (Year 1)

Individual Learner: $29/month
- Access to all courses
- AI tutoring
- Certification prep

Trade School (up to 50 students): $199/month
- Everything in Individual
- Cohort analytics
- Instructor dashboard
- Custom curriculum import

Enterprise (unlimited): $599/month
- Everything in Trade School
- API access
- Custom AI model fine-tuning
- Dedicated success manager
```

---

## Summary: Example Diversity

| Example | Company Type | Domain | AI Focus | Primary Book Focus |
|---------|--------------|--------|----------|-------------------|
| QuickShip | Startup (2 ppl) | Logistics | Medium | Vibe Coding |
| HealthMetrics | Enterprise SaaS | Healthcare | High | AI PM |
| DataForge | Enterprise | Data/ETL | Very High | AI Engineering |
| RetailMind | Series A Startup | Retail | Medium-High | Integration |
| EduGen | Bootstrapped | EdTech | Medium | Cross-functional |

---

## Callout Box Type Reference

The following callout types will be used throughout the examples:

| Callout Type | CSS Class | Purpose |
|--------------|-----------|---------|
| big-picture | `callout big-picture` | Strategic context and market opportunities |
| key-insight | `callout key-insight` | Core takeaways and lessons learned |
| practical-example | `callout practical-example` | Real code and workflows |
| warning | `callout warning` | Cautionary notes and pitfalls |
| document | `callout info` or custom | PRDs, skills, specs |
| code | `example-box` | Implementation examples |
| architecture | `example-box` | System diagrams |
| team-discussion | `callout` | Conversations between roles |
| skill | `callout info` | SKILL.md examples |
| comparison-table | `comparison-table` | Feature comparisons |

---

## Cross-Reference Index

### Examples by Chapter

**Chapter 1 (AI Capabilities)**: All 5 examples introduced with context for why AI fits their domain

**Chapter 2 (Synergy Triangle)**: All 5 examples show how the triangle works in their context

**Chapters 3-6 (Vibe Coding)**: QuickShip primary, RetailMind and EduGen secondary

**Chapters 7-11 (AI PM)**: HealthMetrics primary, EduGen secondary

**Chapters 12-17 (AI Engineering)**: DataForge primary, HealthMetrics secondary

**Chapters 18-21 (Integration)**: All 5 examples in case study format

### Key Theme: Eval-First Development

All examples demonstrate eval-first principles:
- QuickShip: Route accuracy evals
- HealthMetrics: Clinical safety evals
- DataForge: Code acceptance evals
- RetailMind: Engagement metrics evals
- EduGen: Learning outcome evals

### Key Theme: Cost as a Feature

All examples address AI economics:
- QuickShip: Route computation cost optimization
- HealthMetrics: Model routing for cost/quality balance
- DataForge: Enterprise-scale inference costs
- RetailMind: Edge computing to reduce cloud costs
- EduGen: Content generation cost per learner
