#!/usr/bin/env python3
"""Generate Part 2 Vibe Coding Workflow illustration."""

import json
from pathlib import Path
from google import genai
from google.genai import types

config_path = Path.home() / ".gemini-imagegen.json"
config = json.loads(config_path.read_text())
client = genai.Client(api_key=config["api_key"])

OUTPUT_DIR = Path("E:/Projects/AIEngineering/book-ai-products/images/illustrations")

prompt = """Whimsical educational illustration in a warm, colorful style: A friendly robot developer sitting at a modern desk with multiple screens labeled "CURSOR", "CLAUDE CODE", "WINDSURF". The robot is pointing at a flowchart on a wall showing 4 steps: 1) IDEA (lightbulb) -> 2) PROTOTYPE (code window) -> 3) EVAL (checklist) -> 4) SHIP (rocket). An arrow loops back from SHIP to IDEA with a label "Iterate until perfect". The robot has a coffee mug that says "VIBE". On the desk there are sticky notes, a laptop showing code, and a small plant. Background shows a cozy office with a window showing sunset. Style: warm colorful cartoon illustration, clean lines, friendly characters. Suitable for a textbook chapter opener. No text overlay."""

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

output_path = OUTPUT_DIR / "part-2-vibe-coding-workflow.png"
for part in response.parts:
    if part.inline_data is not None:
        image = part.as_image()
        image.save(output_path)
        print(f"Saved: {output_path}")
