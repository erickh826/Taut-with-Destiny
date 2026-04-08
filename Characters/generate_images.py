"""
fal.ai image generator for story characters.

Usage:
    pip install fal-client requests python-dotenv
    # Add FAL_KEY=your_api_key_here to a .env file in this folder
    python generate_images.py

    # Generate a single character only:
    python generate_images.py --character 夏星辰

    # Dry run (print prompts without calling API):
    python generate_images.py --dry-run
"""

import os
import re
import sys
import time
import argparse
import requests
import fal_client
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CHARACTERS = {
    "夏星辰": {
        "md_file": os.path.join(BASE_DIR, "character_prompt/character_template/Xia_Xingchen.md"),
        "output_dir": os.path.join(BASE_DIR, "夏星辰"),
    },
    "霍宇翔": {
        "md_file": os.path.join(BASE_DIR, "character_prompt/character_template/Huo_Yuxiang.md"),
        "output_dir": os.path.join(BASE_DIR, "霍宇翔"),
    },
    "程子言": {
        "md_file": os.path.join(BASE_DIR, "character_prompt/character_template/Cheng_Ziyan.md"),
        "output_dir": os.path.join(BASE_DIR, "程子言"),
    },
}

FAL_MODEL = "fal-ai/flux/dev"

FAL_PARAMS = {
    "image_size": "portrait_4_3",
    "num_inference_steps": 28,
    "guidance_scale": 3.5,
    "num_images": 1,
    "enable_safety_checker": False,
}

# ---------------------------------------------------------------------------
# Prompt parser
# ---------------------------------------------------------------------------

def parse_prompts_from_md(md_path: str) -> list[dict]:
    """
    Extract prompts from the Plan B section of a character markdown file.
    Returns a list of dicts: [{"label": "01 | 正面 × 微小溫柔", "prompt": "..."}, ...]
    """
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Match sections like: ### 01 | 正面 × 微小溫柔\n```\n...\n```
    pattern = re.compile(
        r"### (\d{2} \| [^\n]+)\n```\n(.*?)\n```",
        re.DOTALL,
    )
    matches = pattern.findall(content)

    if not matches:
        raise ValueError(f"No prompts found in {md_path}. Check the file format.")

    return [{"label": label.strip(), "prompt": prompt.strip()} for label, prompt in matches]


def label_to_filename(label: str) -> str:
    """
    Convert '01 | 正面 × 微小溫柔' → '01_正面_微小溫柔.png'
    """
    name = label.replace(" | ", "_").replace(" × ", "_").replace(" ", "_")
    return f"{name}.png"


# ---------------------------------------------------------------------------
# fal.ai call
# ---------------------------------------------------------------------------

def generate_image(prompt: str) -> str:
    """Call fal.ai and return the image URL."""
    result = fal_client.subscribe(
        FAL_MODEL,
        arguments={"prompt": prompt, **FAL_PARAMS},
    )
    return result["images"][0]["url"]


def download_image(url: str, save_path: str) -> None:
    """Download image from URL and save to disk."""
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    with open(save_path, "wb") as f:
        f.write(response.content)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run(characters_to_run: list[str], dry_run: bool = False) -> None:
    for char_name in characters_to_run:
        config = CHARACTERS[char_name]
        md_file = config["md_file"]
        output_dir = config["output_dir"]

        os.makedirs(output_dir, exist_ok=True)

        print(f"\n{'='*60}")
        print(f"  Character: {char_name}")
        print(f"  Output:    {output_dir}")
        print(f"{'='*60}")

        prompts = parse_prompts_from_md(md_file)
        print(f"  Found {len(prompts)} prompts\n")

        for entry in prompts:
            label = entry["label"]
            prompt = entry["prompt"]
            filename = label_to_filename(label)
            save_path = os.path.join(output_dir, filename)

            if os.path.exists(save_path):
                print(f"  [SKIP] {filename} already exists")
                continue

            if dry_run:
                print(f"  [DRY RUN] {label}")
                print(f"            {prompt[:80]}...")
                continue

            print(f"  [GEN]  {label} ...", end=" ", flush=True)
            try:
                start = time.time()
                url = generate_image(prompt)
                download_image(url, save_path)
                elapsed = time.time() - start
                print(f"done ({elapsed:.1f}s) → {filename}")
            except Exception as e:
                print(f"FAILED — {e}")

    print("\nAll done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate character images via fal.ai")
    parser.add_argument(
        "--character",
        choices=list(CHARACTERS.keys()),
        help="Generate only one character (default: all)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print prompts without calling the API",
    )
    args = parser.parse_args()

    if not os.environ.get("FAL_KEY") and not args.dry_run:
        print("Error: FAL_KEY environment variable is not set.")
        print("       export FAL_KEY=your_api_key_here")
        sys.exit(1)

    targets = [args.character] if args.character else list(CHARACTERS.keys())
    run(targets, dry_run=args.dry_run)
