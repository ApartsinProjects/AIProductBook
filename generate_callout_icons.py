#!/usr/bin/env python3
"""Generate all callout box icons using Gemini."""

import json
from pathlib import Path
from google import genai
from google.genai import types

config_path = Path.home() / ".gemini-imagegen.json"
config = json.loads(config_path.read_text())
client = genai.Client(api_key=config["api_key"])

OUTPUT_DIR = Path("E:/Projects/AIEngineering/book-ai-products/styles/icons")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ICONS = [
    {
        "filename": "callout-big-picture.png",
        "prompt": """Minimalist icon for "Big Picture" callout box. A stylized eye or binoculars symbol suggesting broad vision and overview. Clean simple design, purple and white color scheme. Style: flat icon, minimal, professional. Size: 48x48 pixels, transparent background. No text."""
    },
    {
        "filename": "callout-key-insight.png",
        "prompt": """Minimalist icon for "Key Insight" callout box. A lightbulb symbol suggesting a key idea or mental model. Clean simple design, green and white color scheme. Style: flat icon, minimal, professional. Size: 48x48 pixels, transparent background. No text."""
    },
    {
        "filename": "callout-note.png",
        "prompt": """Minimalist icon for "Note" callout box. A sticky note or paperclip symbol suggesting additional information. Clean simple design, blue and white color scheme. Style: flat icon, minimal, professional. Size: 48x48 pixels, transparent background. No text."""
    },
    {
        "filename": "callout-warning.png",
        "prompt": """Minimalist icon for "Warning" callout box. A triangle warning sign with exclamation mark. Clean simple design, amber/orange and white color scheme. Style: flat icon, minimal, professional. Size: 48x48 pixels, transparent background. No text."""
    },
    {
        "filename": "callout-practical-example.png",
        "prompt": """Minimalist icon for "Practical Example" callout box. A wrench and gear symbol suggesting engineering practice. Clean simple design, teal and white color scheme. Style: flat icon, minimal, professional. Size: 48x48 pixels, transparent background. No text."""
    },
    {
        "filename": "callout-fun-note.png",
        "prompt": """Minimalist icon for "Fun Note" callout box. A star or sparkle symbol suggesting something fun and memorable. Clean simple design, pink and white color scheme. Style: flat icon, minimal, professional. Size: 48x48 pixels, transparent background. No text."""
    },
    {
        "filename": "callout-research-frontier.png",
        "prompt": """Minimalist icon for "Research Frontier" callout box. A telescope or radar symbol suggesting looking into the future. Clean simple design, cyan/teal and white color scheme. Style: flat icon, minimal, professional. Size: 48x48 pixels, transparent background. No text."""
    },
    {
        "filename": "callout-algorithm.png",
        "prompt": """Minimalist icon for "Algorithm" callout box. A flowchart or step-by-step diagram symbol suggesting a process. Clean simple design, indigo and white color scheme. Style: flat icon, minimal, professional. Size: 48x48 pixels, transparent background. No text."""
    },
    {
        "filename": "callout-tip.png",
        "prompt": """Minimalist icon for "Tip" callout box. A thumbs up or checkmark symbol suggesting helpful advice. Clean simple design, cyan and white color scheme. Style: flat icon, minimal, professional. Size: 48x48 pixels, transparent background. No text."""
    },
    {
        "filename": "callout-exercise.png",
        "prompt": """Minimalist icon for "Exercise" callout box. A pencil or puzzle piece symbol suggesting hands-on practice. Clean simple design, deep orange and white color scheme. Style: flat icon, minimal, professional. Size: 48x48 pixels, transparent background. No text."""
    },
    {
        "filename": "callout-real-world-scenario.png",
        "prompt": """Minimalist icon for "Real World Scenario" callout box. A briefcase or building factory symbol suggesting real industry practice. Clean simple design, navy blue and white color scheme. Style: flat icon, minimal, professional. Size: 48x48 pixels, transparent background. No text."""
    },
]

def generate_icon(icon_info):
    """Generate a single icon."""
    response = client.models.generate_content(
        model=config.get("default_model", "gemini-3.1-flash-image-preview"),
        contents=icon_info["prompt"],
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio="1:1",
                image_size="1K",
            ),
        ),
    )
    
    output_path = OUTPUT_DIR / icon_info["filename"]
    for part in response.parts:
        if part.inline_data is not None:
            image = part.as_image()
            image.save(output_path)
            print(f"  Saved: {output_path.name}")
            return True
    return False

def main():
    print(f"Generating {len(ICONS)} callout icons...")
    for i, icon in enumerate(ICONS, 1):
        print(f"\n[{i}/{len(ICONS)}] Generating {icon['filename']}...")
        try:
            generate_icon(icon)
        except Exception as e:
            print(f"  Error: {e}")
    print("\nDone!")

if __name__ == "__main__":
    main()
