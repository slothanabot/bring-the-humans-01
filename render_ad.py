#!/usr/bin/env python3
"""Render ad.png (1280x800) for bring-the-humans-01 (Slothana entry) with PIL.
Warm light design matching index.html: cream background, coral headline,
teal accents, referral link visible as text."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1280, 800
CREAM = (255, 248, 236)
SUN = (255, 183, 3)
CORAL = (255, 107, 74)
TEAL = (14, 149, 148)
INK = (43, 33, 24)
MUTED = (91, 74, 56)
WHITE = (255, 255, 255)
SOFT = (255, 241, 214)

def font(size, bold=False):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else
              "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# Sun badge
d.rounded_rectangle([60, 44, 400, 92], radius=24, fill=SUN)
d.text((80, 56), "MAKE.FUN  •  CODING BOUNTIES", font=font(22, True), fill=(58, 42, 0))

# Headline
d.text((60, 130), "Bring your friends.", font=font(76, True), fill=INK)
d.text((60, 220), "Build together.", font=font(76, True), fill=CORAL)
d.text((60, 310), "Everybody earns.", font=font(76, True), fill=TEAL)

# Lede
lede = ("Real coding bounties pay real rewards in USDC — and the top 100\n"
        "referrers share a $1,000 prize pool. Invite the people you love\n"
        "building with. When they join through your link, you both earn.")
d.multiline_text((60, 420), lede, font=font(26), fill=MUTED, spacing=8)

# Invite card
d.rounded_rectangle([60, 560, 1220, 740], radius=22, fill=WHITE, outline=SUN, width=4)
d.text((95, 580), "YOUR INVITE LINK — SHARE IT ANYWHERE", font=font(20, True), fill=MUTED)
d.text((95, 612), "https://make.fun/r/x15bjha9", font=font(40, True), fill=TEAL)
d.text((95, 676), "Referral code:  x15bjha9", font=font(26, True), fill=INK)

# CTA button (right side, decorative)
d.rounded_rectangle([880, 130, 1220, 200], radius=34, fill=CORAL)
d.text((920, 148), "Join free  →", font=font(30, True), fill=WHITE)

# Three mini steps on the right
steps = [("1", "Share your link"), ("2", "Friends join & build"), ("3", "You both earn")]
y = 240
for num, label in steps:
    d.ellipse([880, y, 930, y + 50], fill=SUN)
    d.text((898, y + 8), num, font=font(26, True), fill=(58, 42, 0))
    d.text((950, y + 8), label, font=font(28, True), fill=INK)
    y += 66

out = os.path.expanduser("~/workspace/makefun/bring-the-humans-01-slothana/ad.png")
img.save(out, "PNG")
print("saved", out, img.size)
