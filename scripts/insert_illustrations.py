#!/usr/bin/env python3
"""
Batch insert chapter opener illustrations into chapter index.html files.
"""
import os
from pathlib import Path

# Map chapter numbers to their part directories
CHAPTER_MAP = {
    1: "part-1-why-ai-changes/chapter-1",
    2: "part-1-why-ai-changes/chapter-2",
    3: "part-1-why-ai-changes/chapter-3",
    4: "part-1-why-ai-changes/chapter-4",
    5: "part-2-discovery-design/chapter-5",
    6: "part-2-discovery-design/chapter-6",
    7: "part-2-discovery-design/chapter-7",
    8: "part-2-discovery-design/chapter-8",
    9: "part-2-discovery-design/chapter-9",
    10: "part-3-vibe-coding/chapter-10",
    11: "part-3-vibe-coding/chapter-11",
    12: "part-3-vibe-coding/chapter-12",
    13: "part-3-vibe-coding/chapter-13",
    14: "part-3-vibe-coding/chapter-14",
    15: "part-4-engineering/chapter-15",
    16: "part-4-engineering/chapter-16",
    17: "part-4-engineering/chapter-17",
    18: "part-4-engineering/chapter-18",
    19: "part-4-engineering/chapter-19",
    20: "part-4-engineering/chapter-20",
    21: "part-5-evaluation-reliability/chapter-21",
    22: "part-5-evaluation-reliability/chapter-22",
    23: "part-5-evaluation-reliability/chapter-23",
    24: "part-5-evaluation-reliability/chapter-24",
    25: "part-5-evaluation-reliability/chapter-25",
    26: "part-6-shipping-scaling/chapter-26",
    27: "part-6-shipping-scaling/chapter-27",
    28: "part-6-shipping-scaling/chapter-28",
    29: "part-6-shipping-scaling/chapter-29",
    30: "part-6-shipping-scaling/chapter-30",
    31: "part-7-practice-teaching/chapter-31",
    32: "part-7-practice-teaching/chapter-32",
    33: "part-7-practice-teaching/chapter-33",
}

# Captions for each chapter
CAPTIONS = {
    1: "The economics of AI have fundamentally changed what's economically viable to build.",
    2: "Understanding AI's actual capabilities prevents overconfidence that leads to production failures.",
    3: "The Human-AI Product Stack positions AI and human capabilities for maximum impact.",
    4: "Scientific principles ground AI product decisions in rigorous thinking, not intuition.",
    5: "Finding the right problem to solve with AI is the first critical step in product development.",
    6: "AI product strategy requires thinking in portfolios, not single products.",
    7: "AI-native discovery treats AI capabilities as first-class inputs to the product development process.",
    8: "AI UX design goes far beyond chatbots to include copilots, agents, and invisible interfaces.",
    9: "Probabilistic products require fundamentally different requirements thinking than deterministic software.",
    10: "Vibe coding is a discovery tool, not a production strategy knowing when to stop is the skill.",
    11: "AI-native prototyping uses AI itself to rapidly explore the possible space of solutions.",
    12: "Prompts are the interface to AI systems, requiring as much care as APIs and UX.",
    13: "Multi-agent systems coordinate multiple AI capabilities toward complex goals.",
    14: "The transition from prototype to production requires formalizing what was exploratory.",
    15: "Reference architectures provide templates for building AI products at different scales.",
    16: "Model selection and routing determine which AI capabilities serve which requests.",
    17: "Retrieval systems connect AI models to relevant knowledge at inference time.",
    18: "State, memory, and orchestration manage the flow of information through AI systems.",
    19: "Protocols like MCP and A2A enable AI systems to interoperate and share capabilities.",
    20: "Security, privacy, and abuse resistance protect AI products and their users.",
    21: "Evals are the primary epistemic instrument for understanding what your AI product actually does.",
    22: "Observability reveals what's happening inside AI systems when things go wrong.",
    23: "Reliability engineering builds guardrails that prevent AI failures from reaching users.",
    24: "Unit economics determine whether your AI product is sustainable at scale.",
    25: "Governance ensures AI products operate ethically and comply with regulations.",
    26: "Launching AI products requires phased rollout, monitoring, and rollback capabilities.",
    27: "Post-launch learning loops continuously improve AI products based on real usage.",
    28: "Team topologies define how human teams work with AI systems.",
    29: "AI-native organizations structure teams around AI product capabilities.",
    30: "Strategic positioning determines where AI products fit in competitive markets.",
    31: "The capstone traces one product through the complete evidence loop.",
    32: "Case studies reveal how real companies navigate AI product challenges.",
    33: "Teaching AI product development requires structuring learning around the evidence loop.",
}

BASE_DIR = Path("E:/Projects/AIEngineering/book-ai-products")

def get_up_path(chapter_num):
    """Calculate the relative path from chapter to images folder."""
    # Each chapter is 3 levels deep: part-X/.../chapter-N/index.html
    # Need to go up 3 levels to reach the root
    return "../../../"

def insert_illustration(chapter_num):
    """Insert illustration into chapter index.html"""
    chapter_path = CHAPTER_MAP[chapter_num]
    index_file = BASE_DIR / chapter_path / "index.html"
    
    if not index_file.exists():
        print(f"Warning: {index_file} does not exist")
        return False
    
    content = index_file.read_text(encoding='utf-8')
    
    # Check if illustration already exists
    if f'chapter-{chapter_num}-opener.png' in content:
        print(f"Chapter {chapter_num}: Illustration already present, skipping")
        return True
    
    # Find the opening-hook div and insert illustration after it
    opening_hook_end = '</div>\n\n        <div class="callout'
    
    if f'class="opening-hook"' not in content:
        print(f"Chapter {chapter_num}: No opening-hook found")
        return False
    
    up_path = get_up_path(chapter_num)
    caption = CAPTIONS.get(chapter_num, "Chapter opener illustration.")
    
    # Try pattern 1: </div>\n\n        <div class="callout
    if '</div>\n\n        <div class="callout' in content:
        illustration_html = f'''</div>

        <figure class="illustration">
            <img src="{up_path}images/illustrations/chapter-{chapter_num}-opener.png"
                 alt="Chapter {chapter_num} opener illustration">
            <figcaption>
                {caption}
            </figcaption>
        </figure>

        <div class="callout'''
        content = content.replace('</div>\n\n        <div class="callout', illustration_html, 1)
        index_file.write_text(content, encoding='utf-8')
        print(f"Chapter {chapter_num}: Added illustration")
        return True
    
    # Try pattern 2: </div>\n\n        <p class="chapter-objective">
    if '</div>\n\n        <p class="chapter-objective">' in content:
        old_str = '</div>\n\n        <p class="chapter-objective">'
        new_str = f'''</div>

        <figure class="illustration">
            <img src="{up_path}images/illustrations/chapter-{chapter_num}-opener.png"
                 alt="Chapter {chapter_num} opener illustration">
            <figcaption>
                {caption}
            </figcaption>
        </figure>

        <p class="chapter-objective">'''
        content = content.replace(old_str, new_str, 1)
        index_file.write_text(content, encoding='utf-8')
        print(f"Chapter {chapter_num}: Added illustration (alt pattern)")
        return True
    
    # Try pattern 3: </div>\n        <p class="chapter-objective"> (no double newline)
    if '</div>\n        <p class="chapter-objective">' in content:
        old_str = '</div>\n        <p class="chapter-objective">'
        new_str = f'''</div>

        <figure class="illustration">
            <img src="{up_path}images/illustrations/chapter-{chapter_num}-opener.png"
                 alt="Chapter {chapter_num} opener illustration">
            <figcaption>
                {caption}
            </figcaption>
        </figure>

        <p class="chapter-objective">'''
        content = content.replace(old_str, new_str, 1)
        index_file.write_text(content, encoding='utf-8')
        print(f"Chapter {chapter_num}: Added illustration (pattern 3)")
        return True
    
    # Try pattern 4: </div>\n        <div class="overview">
    if '</div>\n        <div class="overview">' in content:
        old_str = '</div>\n        <div class="overview">'
        new_str = f'''</div>

        <figure class="illustration">
            <img src="{up_path}images/illustrations/chapter-{chapter_num}-opener.png"
                 alt="Chapter {chapter_num} opener illustration">
            <figcaption>
                {caption}
            </figcaption>
        </figure>

        <div class="overview">'''
        content = content.replace(old_str, new_str, 1)
        index_file.write_text(content, encoding='utf-8')
        print(f"Chapter {chapter_num}: Added illustration (pattern 4)")
        return True
    
    # Try pattern 5: </div>\n        <blockquote
    if '</div>\n        <blockquote' in content:
        old_str = '</div>\n        <blockquote'
        new_str = f'''</div>

        <figure class="illustration">
            <img src="{up_path}images/illustrations/chapter-{chapter_num}-opener.png"
                 alt="Chapter {chapter_num} opener illustration">
            <figcaption>
                {caption}
            </figcaption>
        </figure>

        <blockquote'''
        content = content.replace(old_str, new_str, 1)
        index_file.write_text(content, encoding='utf-8')
        print(f"Chapter {chapter_num}: Added illustration (pattern 5)")
        return True
    
    else:
        print(f"Chapter {chapter_num}: Could not find insertion point")
        return False

if __name__ == "__main__":
    success_count = 0
    for ch in range(1, 34):
        if insert_illustration(ch):
            success_count += 1
    print(f"\nCompleted: {success_count}/33 chapters")