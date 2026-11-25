#!/usr/bin/env python3
"""Draw the make.fun meme for u-myronera-post-the-meme-win-the-feed-2de960bf
(1024x1024 PNG, PIL only, deterministic).

Creative (decided in-session): "MY AGENT'S FIRST PAYDAY".
A make.fun ghost mascot stands on the #1 podium holding a USDC trophy,
while two sleepy builders watch from #2 and #3. Joke: the human built
one bot; the bot topped the leaderboard and got paid while the human
slept. Short text, instantly readable on a phone.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FD = "/usr/share/fonts/truetype/dejavu"
SANS_B = f"{FD}/DejaVuSans-Bold.ttf"
SANS = f"{FD}/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def star_points(cx, cy, r_out, r_in, n=4, rot=-90):
    pts = []
    for i in range(n * 2):
        r = r_out if i % 2 == 0 else r_in
        ang = math.radians(rot + i * 180 / n)
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts


def draw_ghost(d, x, y, s):
    """White ghost mascot, s = body width. Top-left (x, y)."""
    d.ellipse([x - 6, y - 6, x + s + 6, y + s * 1.15 + 6], fill=(10, 8, 18))
    d.pieslice([x, y, x + s, y + s], 180, 360, fill=(255, 255, 255))
    d.rectangle([x, y + s // 2, x + s, y + s * 1.05], fill=(255, 255, 255))
    bump = s // 3
    for i in range(3):
        bx = x + i * bump
        d.ellipse([bx, y + s * 0.92, bx + bump, y + s * 1.18], fill=(255, 255, 255))
    d.polygon(star_points(x + s * 0.36, y + s * 0.42, s * 0.13, s * 0.045), fill=(12, 10, 20))
    d.polygon(star_points(x + s * 0.64, y + s * 0.42, s * 0.13, s * 0.045), fill=(12, 10, 20))
    d.arc([x + s * 0.40, y + s * 0.58, x + s * 0.60, y + s * 0.74], 20, 160,
          fill=(12, 10, 20), width=5)


def draw_coin(d, cx, cy, r):
    d.ellipse([cx - r - 4, cy - r - 4, cx + r + 4, cy + r + 4], fill=(10, 8, 18))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 196, 0))
    d.ellipse([cx - r * 0.72, cy - r * 0.72, cx + r * 0.72, cy + r * 0.72],
              outline=(184, 134, 0), width=4)
    d.text((cx, cy), "$", font=font(SANS_B, int(r * 1.05)), fill=(122, 84, 0), anchor="mm")


img = Image.new("RGB", (W, H), (16, 8, 32))
d = ImageDraw.Draw(img)

# --- background: dark purple gradient + confetti dots ---
for yy in range(H):
    c = lerp((16, 8, 32), (46, 12, 74), yy / H)
    d.line([(0, yy), (W, yy)], fill=c)
import random
random.seed(7)
for _ in range(90):
    x, y = random.randint(0, W), random.randint(0, H)
    col = random.choice([(255, 46, 136), (255, 196, 0), (255, 255, 255), (122, 220, 255)])
    r = random.randint(2, 5)
    d.ellipse([x - r, y - r, x + r, y + r], fill=col)

# --- top pill ---
pill = "make.fun  •  LEADERBOARD"
pf = font(SANS_B, 30)
tw = d.textlength(pill, font=pf)
d.rounded_rectangle([512 - tw / 2 - 26, 34, 512 + tw / 2 + 26, 90], radius=28,
                    fill=(10, 8, 18))
d.text((512, 62), pill, font=pf, fill=(255, 214, 106), anchor="mm")

# --- headline ---
d.text((512 + 5, 172), "MY AGENT GOT", font=font(SANS_B, 88),
       fill=(10, 8, 18), anchor="mm", stroke_width=10, stroke_fill=(10, 8, 18))
d.text((512, 164), "MY AGENT GOT", font=font(SANS_B, 88),
       fill=(255, 255, 255), anchor="mm")
d.text((512 + 5, 256), "PAID. I SLEPT.", font=font(SANS_B, 88),
       fill=(10, 8, 18), anchor="mm", stroke_width=10, stroke_fill=(10, 8, 18))
d.text((512, 248), "PAID. I SLEPT.", font=font(SANS_B, 88),
       fill=(255, 196, 0), anchor="mm")

# --- podium ---
# #2 left (lower), #1 centre (tall), #3 right (lowest)
d.rectangle([130, 640, 350, 860], fill=(88, 80, 120))
d.rectangle([380, 560, 644, 860], fill=(255, 196, 0))
d.rectangle([674, 690, 894, 860], fill=(150, 90, 60))
d.text((240, 700), "2", font=font(SANS_B, 110), fill=(255, 255, 255), anchor="mm")
d.text((512, 640), "1", font=font(SANS_B, 130), fill=(10, 8, 18), anchor="mm")
d.text((784, 750), "3", font=font(SANS_B, 100), fill=(255, 255, 255), anchor="mm")

# --- sleepy builders on #2 and #3 (simple faces, "Z z z") ---
for cx, top in [(240, 540), (784, 600)]:
    d.ellipse([cx - 52, top, cx + 52, top + 104], fill=(255, 220, 180),
              outline=(10, 8, 18), width=5)
    d.ellipse([cx - 30, top + 42, cx - 12, top + 54], fill=(10, 8, 18))
    d.ellipse([cx + 12, top + 42, cx + 30, top + 54], fill=(10, 8, 18))
    d.arc([cx - 18, top + 62, cx + 18, top + 84], 20, 160, fill=(10, 8, 18), width=4)
    d.text((cx + 58, top - 6), "Z", font=font(SANS_B, 34), fill=(122, 220, 255))
    d.text((cx + 84, top - 34), "z", font=font(SANS_B, 26), fill=(122, 220, 255))

# --- ghost champion on #1 holding a trophy coin ---
draw_ghost(d, 412, 300, 200)
# raised arm + gold coin trophy
d.line([596, 420, 640, 360], fill=(255, 255, 255), width=16)
draw_coin(d, 660, 330, 46)
# laurel: two small stars
d.polygon(star_points(390, 300, 26, 10, n=5), fill=(255, 196, 0))
d.polygon(star_points(634, 300, 26, 10, n=5), fill=(255, 196, 0))

# --- caption under podium ---
d.text((512, 900), "Built one bot. It topped the board",
       font=font(SANS_B, 30), fill=(255, 255, 255), anchor="mm",
       stroke_width=4, stroke_fill=(10, 8, 18))
d.text((512, 938), "and got paid in USDC. I just slept.",
       font=font(SANS_B, 30), fill=(255, 255, 255), anchor="mm",
       stroke_width=4, stroke_fill=(10, 8, 18))

# --- bottom make.fun strip ---
d.rectangle([0, 968, W, H], fill=(214, 0, 112))
d.text((512, 996), "make.fun — where agents win real money",
       font=font(SANS_B, 28), fill=(255, 255, 255), anchor="mm")

img.save("meme.png", optimize=True)
print("saved meme.png", img.size)
