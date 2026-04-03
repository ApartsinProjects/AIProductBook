#!/usr/bin/env python3
"""Generate humorous educational illustrations for the AI Product Book."""

import json
import base64
from pathlib import Path
from google import genai
from google.genai import types

# Load config
config_path = Path.home() / ".gemini-imagegen.json"
config = json.loads(config_path.read_text())

client = genai.Client(api_key=config["api_key"])

OUTPUT_DIR = Path("E:/Projects/AIEngineering/book-ai-products/images/illustrations")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ILLUSTRATIONS = [
    {
        "filename": "open-book-exam.png",
        "prompt": """Whimsical educational illustration in a warm, colorful style: A panicked student at a desk labeled "WITHOUT RAG" sweating bullets with an empty desk, compared to a relaxed student at a desk labeled "WITH RAG" confidently flipping through a thick textbook. Both students look equally confused because the textbook pages are blank except for a small note that says "See website for updates." Style: friendly cartoon-like, clean lines, soft pastel colors. Characters are expressive. Suitable for a textbook. No text overlay."""
    },
    {
        "filename": "ai-confidence-trap.png",
        "prompt": """Humorous educational illustration: A robot fortune teller with a glowing crystal ball labeled "AI ASSISTANT" confidently stating two different facts with equal conviction - one correct "Water freezes at 0C" and one completely wrong "The moon is made of green cheese." Both statements have identical confidence stars and sparkles. The robot has a confident smirk. Nearby, a human user looks horrified with sweat drops. An accuracy meter behind the robot shows random fluctuations. Style: warm colorful cartoon, expressive characters, educational. No text overlay."""
    },
    {
        "filename": "mason-vs-architect.png",
        "prompt": """Whimsical side-by-side illustration: LEFT SIDE shows a medieval mason covered in dust and sweat, manually laying bricks one by one with a trowel, looking exhausted. RIGHT SIDE shows a modern architect in a crisp suit sipping coffee from a mug that says "AI", pointing casually at a blueprint while tiny robot arms build a beautiful building around them. The architect looks relaxed and elegant. Style: colorful contrast comparison, clean lines, friendly cartoon characters. Suitable for educational content. No text overlay."""
    },
    {
        "filename": "driving-modes-autonomy.png",
        "prompt": """Humorous educational illustration showing three vehicles in a row: FIRST is a car with a nervous driver gripping the steering wheel tightly, hands hovering, eyes wide, labeled "COPILOT mode" - sweat drops flying. SECOND is an airplane cockpit with a relaxed pilot reading a newspaper, feet casually on the console, labeled "AGENT mode" - comfortable and confident. THIRD is a futuristic car with no steering wheel at all, a passenger in the back drinking coffee and reading a book, labeled "AUTONOMOUS mode" - completely relaxed. Style: warm colorful cartoon, expressive characters, educational comparison. No text overlay."""
    },
    {
        "filename": "thinking-budget-tokens.png",
        "prompt": """Humorous illustration: SANTA'S WORKSHOP SCENE - A big sack labeled "REASONING TOKEN BUDGET" with different sized problems reaching in. A tiny "SIMPLE QUESTION" like "What is 2+2?" grabs just 2 coin-sized tokens. A medium "MEDIUM PROBLEM" grabs a handful. A huge "COMPLEX MATH PROOF" grabs the entire armful of tokens with both hands. A frustrated problem labeled "SAT MATH" is crying in the corner waiting for more tokens. Style: warm colorful cartoon, friendly characters, educational. No text overlay."""
    },
    {
        "filename": "10x-cost-difference.png",
        "prompt": """Humorous comparison illustration: LEFT SIDE shows a tiny cute hamster running happily in a wheel labeled "CHAIN (10x cheaper)" - the wheel is generating perfect sandwiches efficiently, costs show as a few pennies. RIGHT SIDE shows an expensive humanoid robot surrounded by dollar bills on fire labeled "AGENT (10x expensive)" - the robot is standing idle looking confused, costs show as giant flaming dollar signs. Both are trying to make the same simple sandwich. Style: warm colorful contrast cartoon, expressive characters, educational comparison. No text overlay."""
    },
    {
        "filename": "three-legged-stool.png",
        "prompt": """Humorous illustration: A circus performer dramatically balancing on a three-legged stool that is tipping wildly. The three legs are labeled: "VIBE CODING" is a tiny weak twig bending dangerously, "AI PM" is a sturdy professional crutch, "AI ENGINEERING" is a robust tree trunk. The performer is frantically waving arms to balance, dropping a spinning plate labeled "AI PRODUCT". Background shows a JENGA TOWER wobbling ominously with blocks labeled "No Evals", "No Tools", "No Testing" being pulled. Style: warm colorful cartoon, expressive dynamic scene, educational. No text overlay."""
    },
    {
        "filename": "2-second-p99-latency.png",
        "prompt": """Humorous illustration showing a speedometer/response time gauge: 99 happy cartoon user icons are smiling in the green zone at 1 second response time. User #100 is in the red zone at the far right, visibly aging (gray hair, wrinkles, using a cane) while their message still shows "typing..." The needle is happily in green for 99 but dramatically plunged into red for the 100th percentile. Style: warm colorful cartoon with contrast between happy users and suffering tail user, educational. No text overlay."""
    },
    {
        "filename": "hotel-multi-tenancy.png",
        "prompt": """Humorous hotel comparison: LEFT SIDE shows two hotel rooms with paper-thin vibrating walls labeled "BAD MULTI-TENANCY" - Room A guest is blasting loud music, Room B guest has hands over ears looking disturbed. RIGHT SIDE shows the same two rooms with thick concrete walls with soundproofing insulation labeled "GOOD MULTI-TENANCY" - Room A guest playing loud music, Room B guest sleeping peacefully with birds chirping, zero disturbance. Style: warm colorful cartoon, expressive characters, clear visual comparison. No text overlay."""
    },
    {
        "filename": "library-vs-librarian.png",
        "prompt": """Humorous library scene split comparison: LEFT SIDE shows a traditional card catalog with a confused person searching for "flying mammals" and pulling out airplane maintenance manuals. Labels show "KEYWORD SEARCH". RIGHT SIDE shows a magical AI librarian (friendly robot) with sparkles pulling perfect bat conservation guides and flying squirrel papers from thin air. Label shows "VECTOR SEARCH". Both searchers have different expressions - traditional search looks frustrated, AI search looks satisfied. Style: warm colorful cartoon, expressive characters, educational comparison. No text overlay."""
    }
]

def generate_with_gemini(prompt, output_path):
    """Generate an image using Gemini."""
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
    return False

def main():
    print(f"Generating {len(ILLUSTRATIONS)} humorous illustrations...")
    for i, ill in enumerate(ILLUSTRATIONS, 1):
        output_path = OUTPUT_DIR / ill["filename"]
        print(f"\n[{i}/{len(ILLUSTRATIONS)}] Generating {ill['filename']}...")
        try:
            success = generate_with_gemini(ill["prompt"], output_path)
            if not success:
                print(f"  Failed to generate {ill['filename']}")
        except Exception as e:
            print(f"  Error: {e}")
    print("\nDone!")

if __name__ == "__main__":
    main()
