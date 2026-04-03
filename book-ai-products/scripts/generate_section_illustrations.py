#!/usr/bin/env python3
"""
Generate additional section-level illustrations for the AI Product Book.
This generates concept-specific illustrations for key sections.
"""

import json
from pathlib import Path
from google import genai
from google.genai import types
import time

# Load config
config_path = Path.home() / ".gemini-imagegen.json"
config = json.loads(config_path.read_text())

client = genai.Client(api_key=config["api_key"])

OUTPUT_DIR = Path("E:/Projects/AIEngineering/book-ai-products/images/illustrations")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Additional section-specific illustrations to generate
# Each represents a key concept that needs visual reinforcement
SECTION_ILLUSTRATIONS = [
    # Part 1 - Why AI Changes (Ch 1-4)
    {
        "filename": "section-1-2-ai-lifecycle.png",
        "prompt": """Humorous educational illustration: A cute baby AI model taking its first steps, labeled "New Model Release", compared to a wizened old grandparent AI with a cane labeled "Legacy Model". The baby is excited and energetic, the grandparent is wise but slow. They are having a conversation. Style: warm colorful cartoon, friendly characters, educational. No text overlay."""
    },
    {
        "filename": "section-2-1-llm-limitations.png",
        "prompt": """Humorous illustration: An AI model as a very enthusiastic but inexperienced intern - holding a stack of papers labeled "Knowledge" high above its head like a trophy, saying "I know EVERYTHING!" while standing in a small puddle labeled "Training Data". The puddle is tiny compared to an ocean labeled "Real World" in the background. Style: warm colorful cartoon, educational metaphor, expressive character. No text overlay."""
    },
    {
        "filename": "section-2-2-synthetic-data.png",
        "prompt": """Humorous illustration showing synthetic data as fake food: A chef in a kitchen labeled "SYNTHETIC DATA GENERATOR" cooking up weird looking but technically edible food. Some dishes look perfect (high quality), some look like abstract art (low quality), some are glowing green (poor quality). A nutritionist nearby is tasting and grading each dish. Style: warm colorful cartoon, educational metaphor. No text overlay."""
    },
    {
        "filename": "section-3-1-tripartite-loop.png",
        "prompt": """Humorous illustration of three circus performers (AI PM, Vibe Coder, AI Engineer) spinning plates on sticks while running in a circle. Each one keeps adding more plates while the others try not to let theirs fall. The plate stand in the center has labels: "Product", "Code", "Infrastructure". A judge labeled "Evaluation" is scorekeeping. Style: warm colorful cartoon, dynamic scene, educational. No text overlay."""
    },
    {
        "filename": "section-4-1-ai-evolution.png",
        "prompt": """A timeline comic showing AI evolving: Panel 1 shows a simple calculator labeled "Tool" - Panel 2 shows a helpful assistant labeled "Copilot" - Panel 3 shows a capable colleague labeled "Agent" - Panel 4 shows an equal partner labeled "Teammate". Each panel shows the AI getting more sophisticated and the human getting more relaxed. Style: educational comic strip, warm colors, clear progression. No text overlay."""
    },
    
    # Part 2 - Discovery & Design (Ch 5-9)
    {
        "filename": "section-5-1-prompt-engineering.png",
        "prompt": """Humorous illustration: A director (user) giving instructions to an actor (AI) through a megaphone. The megaphone is labeled "PROMPT" and the sound waves are transforming as they reach the actor - vague instructions become clear actions. The actor is taking notes on a clipboard. Some megaphones are tiny and broken (bad prompts), others are powerful and clear (good prompts). Style: warm colorful cartoon, educational. No text overlay."""
    },
    {
        "filename": "section-6-1-eval-metrics.png",
        "prompt": """Humorous illustration: A robot scientist in a labcoat holding different colored test tubes labeled with evaluation metrics - blue for accuracy, green for relevance, red for safety, yellow for latency. The robot is carefully mixing them in precise amounts labeled "WEIGHTING" to create the perfect evaluation formula. A chart on the wall shows the recipe. Style: educational, warm colors, lab setting. No text overlay."""
    },
    {
        "filename": "section-7-1-cost-estimation.png",
        "prompt": """Humorous illustration: A construction foreman (AI PM) holding blueprints with price tags. Different building components have different costs: a fancy roof labeled "Advanced Model" costs $1000, a simple roof labeled "Fast Model" costs $10, foundation labeled "Data Pipeline" costs $500. The foreman is comparing costs with a calculator and looking stressed. Style: warm colorful cartoon, clear cost metaphor. No text overlay."""
    },
    {
        "filename": "section-8-1-user-research.png",
        "prompt": """Humorous illustration: An anthropologist observing AI interactions in the wild - sitting in a jungle hide with binoculars labeled "USER RESEARCH" watching humans and AI creatures interact. The AI creatures have different personalities: one is helpful, one is confused, one is overly helpful. The researcher is taking detailed notes. Style: educational, warm colors, safari theme. No text overlay."""
    },
    {
        "filename": "section-9-1-business-model.png",
        "prompt": """Humorous illustration: Different business models shown as different restaurant styles - a fast food drive-through labeled "API Pricing", a fancy restaurant labeled "Enterprise License", a buffet labeled "Usage-Based", a food truck labeled "Freemium". Each has different customers, different prices, different service styles. A sign says "CHOOSE YOUR MODEL". Style: warm colorful cartoon, clear business metaphor. No text overlay."""
    },
    
    # Part 3 - Vibe Coding (Ch 10-14)
    {
        "filename": "section-10-1-vibe-coding-intro.png",
        "prompt": """Humorous illustration: An artist using a magic brush labeled "Natural Language" to paint not on canvas but directly into reality - the brush strokes create working code, UI elements, and database connections. The artist is in a flow state with music notes around them labeled "VIBE". Traditional programmers in the background are staring in amazement holding traditional programming books. Style: whimsical, warm colors, educational. No text overlay."""
    },
    {
        "filename": "section-11-1-prompt-library.png",
        "prompt": """Humorous illustration: A chef in a kitchen surrounded by recipe books labeled "PROMPT LIBRARY" - pulling out different recipes (prompts) for different dishes (tasks). Some recipes are short notes, others are detailed cookbooks. The chef is cooking up AI outputs. A whiteboard shows "RECIPE OPTIMIZATION" with different ingredient adjustments. Style: warm colorful cartoon, kitchen metaphor. No text overlay."""
    },
    {
        "filename": "section-12-1-iterative-development.png",
        "prompt": """Humorous illustration: A potter at a wheel rapidly creating and destroying pottery - each pot labeled "Prototype v1", "Prototype v2", etc. The AI is the potter's powerful arms making things faster. Some pots collapse (failed prototypes), some look beautiful (good ones). The potter is smiling with each iteration getting better. Background shows "ITERATION COUNT" going up. Style: warm colorful cartoon, educational. No text overlay."""
    },
    {
        "filename": "section-13-1-rapid-prototyping.png",
        "prompt": """Humorous illustration: A race car pit crew - the AI is the crew chief yelling rapid instructions, developers are the pit crew rapidly changing wheels and adding fuel, the car is the prototype. Each stop is lightning fast labeled "SPRINT". The finish line shows "GO-TO-MARKET". The crowd is cheering. Style: warm colorful cartoon, racing metaphor. No text overlay."""
    },
    {
        "filename": "section-14-1-design-sprint.png",
        "prompt": """Humorous illustration: A sprint relay race where each runner is a different phase of design sprint - Runner 1 labeled "UNDERSTAND" passing baton to Runner 2 "DIVERGE", Runner 3 "DECIDE", Runner 4 "PROTOTYPE", Runner 5 "VALIDATE". Each runner has a different expression - some confused, some excited, some tired. The baton is the prototype getting refined. Style: warm colorful cartoon, clear process flow. No text overlay."""
    },
    
    # Part 4 - Engineering (Ch 15-20)
    {
        "filename": "section-15-1-pipeline-architecture.png",
        "prompt": """Humorous illustration: A factory assembly line with different stations - Station 1 labeled "DATA PREPARATION" with raw ingredients coming in, Station 2 labeled "MODEL TRAINING" with workers refining the product, Station 3 labeled "DEPLOYMENT" with packaged products shipping out. Quality control inspectors at each station with clipboards labeled "EVALUATION". The factory is labeled "AI PIPELINE". Style: warm colorful cartoon, factory metaphor. No text overlay."""
    },
    {
        "filename": "section-16-1-rag-retrieval.png",
        "prompt": """Humorous illustration: A detective's office with evidence boards - the detective (LLM) is looking at a case file (user query), while a research assistant (retriever) is frantically pulling relevant documents from a massive filing cabinet. Red strings connect clues (relevant documents) to the case. Some files glow (high relevance), some are dusty (low relevance). A corkboard shows "RETRIEVAL ACCURACY". Style: warm colorful cartoon, detective metaphor. No text overlay."""
    },
    {
        "filename": "section-17-1-multi-agent.png",
        "prompt": """Humorous illustration: An orchestra conductor (main agent) directing different musicians (specialized agents) - the string section is labeled "RESEARCH", brass is "CODE GENERATION", percussion is "VALIDATION", piano is "PLANNING". Each musician plays their part in harmony. A music stand shows the "ORCHESTRATION PLAN". The audience (users) is applauding. Style: warm colorful cartoon, orchestra metaphor. No text overlay."""
    },
    {
        "filename": "section-18-1-observability.png",
        "prompt": """Humorous illustration: An air traffic control tower - radar screens labeled "METRICS" show planes (requests) flying, a log book labeled "LOGS" tracks every movement, a red phone labeled "ALERTS" rings when something goes wrong. The controller (engineer) is monitoring everything. A status board shows "SYSTEM HEALTH". Style: warm colorful cartoon, control tower metaphor. No text overlay."""
    },
    {
        "filename": "section-19-1-fine-tuning.png",
        "prompt": """Humorous illustration: A personal trainer (fine-tuning process) working out a baby AI model (base model) at a gym labeled "TRAINING DATA". The trainer is adding weights labeled "DOMAIN KNOWLEDGE" to make the model stronger. The model is getting more defined muscles (capabilities) but also learning bad habits if the trainer isn't careful (overfitting). A nutrition label shows "DATA QUALITY". Style: warm colorful cartoon, gym metaphor. No text overlay."""
    },
    {
        "filename": "section-20-1-guardrails.png",
        "prompt": """Humorous illustration: A bouncer at a club entrance labeled "GUARDRAILS" - checking IDs and stopping trouble. The bouncer checks a list labeled "POLICY" and stops suspicious characters (harmful prompts) from entering. A VIP list (allowed inputs) gets easy entry. Some rejected requests are throwing a fit, some are sneaking in disguise. The club inside is "AI SYSTEM". Style: warm colorful cartoon, bouncer metaphor. No text overlay."""
    },
    
    # Part 5 - Evaluation & Reliability (Ch 21-25)
    {
        "filename": "section-21-1-evaluation-framework.png",
        "prompt": """Humorous illustration: A judge's bench in a courtroom labeled "EVALUATION" - the judge (evaluation system) is reviewing evidence (model outputs) with different colored folders: green for "PASS", yellow for "NEEDS WORK", red for "FAIL". A jury of metrics (accuracy, latency, cost) is deliberating. The defendant (AI model) looks nervous. Style: warm colorful cartoon, courtroom metaphor. No text overlay."""
    },
    {
        "filename": "section-22-1-testing-automation.png",
        "prompt": """Humorous illustration: A robot quality inspector at a factory - checking AI outputs like products on a conveyor belt. Some products have green checkmarks (pass), some have red X (fail). The robot has different tools: magnifying glass for "UNIT TESTS", hammer for "INTEGRATION TESTS", binoculars for "E2E TESTS". A sign says "AUTOMATED QC". Style: warm colorful cartoon, factory QC metaphor. No text overlay."""
    },
    {
        "filename": "section-23-1-compliance.png",
        "prompt": """Humorous illustration: A compliance officer as a librarian organizing books (regulations) - GDPR is a blue book, HIPAA is a green book, SOC2 is an orange book. The officer is checking if the AI library follows all the rules. A checklist shows "REQUIREMENTS" with checkmarks. A alarm goes off if anything is out of place. Style: warm colorful cartoon, librarian metaphor. No text overlay."""
    },
    {
        "filename": "section-24-1-bias-detection.png",
        "prompt": """Humorous illustration: A security scanner at an airport labeled "BIAS DETECTOR" - the AI is going through the scanner, and different items light up: a bag labeled "TRAINING DATA" might have hidden biases, shoes labeled "ALGORITHM" might have embedded preferences, a watch labeled "OUTPUT" might be showing skewed results. A security guard (engineer) is investigating each alert. Style: warm colorful cartoon, airport security metaphor. No text overlay."""
    },
    {
        "filename": "section-25-1-ethics-board.png",
        "prompt": """Humorous illustration: A round table of wise owls labeled "ETHICS BOARD" - each owl represents a principle: fairness, transparency, accountability, privacy, safety. They are discussing an AI product proposal (a small creature) and giving thumbs up or down. A scale shows "BENEFIT VS RISK". The creature is hoping to pass. Style: warm colorful cartoon, council metaphor. No text overlay."""
    },
    
    # Part 6 - Shipping & Scaling (Ch 26-30)
    {
        "filename": "section-26-1-deployment-strategy.png",
        "prompt": """Humorous illustration: Different deployment strategies as different launch methods - a big bang launch shown as fireworks, a gradual rollout shown as a rising sun, a canary release shown as a bird testing the air first, feature flags shown as light switches. Each has different risk levels. A mission control center is choosing which method. Style: warm colorful cartoon, space mission metaphor. No text overlay."""
    },
    {
        "filename": "section-27-1-monitoring-dashboard.png",
        "prompt": """Humorous illustration: A mission control center with many screens - each screen shows different metrics: a speedometer for "LATENCY", a thermometer for "ERROR RATE", a battery meter for "RESOURCE USAGE", a heart rate monitor for "SYSTEM HEALTH". Engineers are at consoles monitoring. Warning lights flash when something is wrong. Style: warm colorful cartoon, sci-fi control room. No text overlay."""
    },
    {
        "filename": "section-28-1-case-study-lessons.png",
        "prompt": """Humorous illustration: A classroom where different students (companies) are presenting their AI project posters - each poster shows a different story: success story, failure story, lessons learned. A teacher (reader) is taking notes. Stars and stickers show ratings. The wall says "CASE STUDY FAIR". Style: warm colorful cartoon, classroom metaphor. No text overlay."""
    },
    {
        "filename": "section-29-1-team-topology.png",
        "prompt": """Humorous illustration: Different team topologies as different sports teams - a swim team (stream-aligned) swimming in sync, a rugby team (platform) pushing together, a relay team (enabling) passing work, a solo gymnast (complicated subsystem). Each has different uniforms and strategies. A coach (organization) is calling plays. Style: warm colorful cartoon, sports metaphor. No text overlay."""
    },
    {
        "filename": "section-30-1-future-trends.png",
        "prompt": """Humorous illustration: A crystal ball labeled "FUTURE" showing different visions - one shows AI and humans working side by side as partners, one shows AI doing all the boring work while humans do creative stuff, one shows AI as a utility like electricity. A fortune teller (strategist) is interpreting the visions. Stars show probability. Style: warm colorful cartoon, fortune telling metaphor. No text overlay."""
    },
    
    # Part 7 - Practice & Teaching (Ch 31-33)
    {
        "filename": "section-31-1-capstone-overview.png",
        "prompt": """Humorous illustration: A final exam where the student (learner) is presenting a full AI product - they have built a complete building (product) with all components: foundation (data), walls (model), roof (UI), utilities (API). Teachers (evaluators) are inspecting the building with clipboards. The student looks proud. Style: warm colorful cartoon, exam metaphor. No text overlay."""
    },
    {
        "filename": "section-32-1-teaching-methods.png",
        "prompt": """Humorous illustration: A teacher in a classroom with different teaching tools - a projector showing "LECTURES", a lab with computers for "HANDS-ON", a discussion circle for "SEMINARS", a project board for "ASSIGNMENTS". Students are engaged in different activities. A curriculum map shows the "LEARNING PATH". Style: warm colorful cartoon, classroom setting. No text overlay."""
    },
    {
        "filename": "section-33-1-continuing-learning.png",
        "prompt": """Humorous illustration: A journey map showing the path of lifelong learning - different stops show "READ PAPERS", "BUILD PROJECTS", "JOIN COMMUNITY", "ATTEND CONFERENCES", "CONTRIBUTE OPEN SOURCE". A traveler (learner) is hiking along the path with a backpack labeled "SKILLS". Signposts show "NEXT MILESTONE". The path goes into the clouds labeled "EXPERTISE". Style: warm colorful cartoon, journey metaphor. No text overlay."""
    },
]

def generate_with_gemini(prompt, output_path):
    """Generate an image using Gemini with retry logic."""
    max_retries = 3
    delay = 5
    
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=config.get("default_model", "gemini-3.1-flash-image-preview"),
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE"],
                    image_config=types.ImageConfig(
                        aspect_ratio="16:9",
                        image_size="1K",
                    ),
                ),
            )
            
            for part in response.parts:
                if part.inline_data is not None:
                    image = part.as_image()
                    image.save(output_path)
                    print(f"  Saved: {output_path.name}")
                    return True
                    
        except Exception as e:
            if attempt < max_retries - 1:
                wait = delay * (2 ** attempt)
                print(f"  Retry {attempt+1}/{max_retries} after {wait}s: {e}")
                time.sleep(wait)
            else:
                print(f"  FAILED: {output_path.name} - {e}")
                raise
    
    return False

def main():
    print(f"Generating {len(SECTION_ILLUSTRATIONS)} section-level illustrations...")
    
    for i, ill in enumerate(SECTION_ILLUSTRATIONS, 1):
        output_path = OUTPUT_DIR / ill["filename"]
        
        # Skip if already exists
        if output_path.exists():
            print(f"[{i}/{len(SECTION_ILLUSTRATIONS)}] Skipping {ill['filename']} (already exists)")
            continue
            
        print(f"\n[{i}/{len(SECTION_ILLUSTRATIONS)}] Generating {ill['filename']}...")
        try:
            success = generate_with_gemini(ill["prompt"], output_path)
            if not success:
                print(f"  Failed to generate {ill['filename']}")
        except Exception as e:
            print(f"  Error: {e}")
    
    print("\nDone!")

if __name__ == "__main__":
    main()