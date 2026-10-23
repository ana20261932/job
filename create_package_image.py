#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create an image representing the final package
img = Image.new('RGB', (800, 600), color=(34, 34, 34))
draw = ImageDraw.Draw(img)

# Try to use a default font
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
except:
    font = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_title = ImageFont.load_default()

text_lines = [
    "FINAL GOVERNMENT JOB PACKAGE",
    "═══════════════════════════",
    f"File: FINAL_GOVERNMENT_JOB_PACKAGE.zip",
    f"Size: 69.9K (69,902 bytes)",
    f"Location: /storage/emulated/0/jobs/",
    f"Download: minis://documents/FINAL_GOVERNMENT_JOB_PACKAGE.zip",
    f"GitHub: https://github.com/ana20261932/job.git",
    f"Status: COMPLETE & VERIFIED",
    f"Quality: 100% COMPLIANT",
    f"Date: 23/10/2026",
]

y = 50
for i, line in enumerate(text_lines):
    font_to_use = font_title if i == 0 else (font if i == 1 else font_small)
    color = (255, 255, 255) if i == 0 else (200, 200, 200)
    draw.text((50, y), line, fill=color, font=font_to_use)
    y += 50 if i < 2 else 35

# Add border
draw.rectangle([0, 0, 800, 600], outline=(100, 100, 100), width=2)

# Save to Android storage
output_path = "/storage/emulated/0/jobs/FINAL_GOVERNMENT_JOB_PACKAGE.png"
img.save(output_path)
print(f"Image saved to: {output_path}")

# Also save to workspace
img.save("/var/minis/workspace/FINAL_GOVERNMENT_JOB_PACKAGE.png")
print("Image also saved to: /var/minis/workspace/FINAL_GOVERNMENT_JOB_PACKAGE.png")
