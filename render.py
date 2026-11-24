from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
navy = '#10263a'
ink = '#25313a'
muted = '#51616b'
red = '#bd3b3b'
teal = '#087c7e'
line = '#d8e0e2'
im = Image.new('RGB', (1024, 1024), 'white')
d = ImageDraw.Draw(im)
def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REG, size)
def text(xy, value, size, color=ink, bold=False):
    d.text(xy, value, font=font(size, bold), fill=color, stroke_width=0)

d.rectangle((0, 0, 1023, 185), fill=navy)
text((40, 23), '24 NOVEMBER 2026', 48, 'white', True)
text((810, 38), 'TUESDAY', 23, '#ffffff', True)
text((42, 103), 'THE WORLD IN ONE DAY', 32, 'white', True)
d.rectangle((40, 163, 984, 167), fill=teal)

stories = [
    ('KOREA', ['Suspected North Korean', 'aircraft crosses border'], ['Seoul says aircraft crossed near Ulleung;', 'island residents ordered to shelter.']),
    ('STRAIT OF HORMUZ', ['Sea mines hit', 'three oil tankers'], ["Iran's Revolutionary Guard says tankers", 'caught fire passing through the strait.']),
    ('MYANMAR', ['UK sanctions Myanmar', 'leaders after ruling'], ['14 countries say ICJ ruling on Rohingya', 'genocide is binding.']),
    ('GAZA', ['Israeli strikes kill', 'at least three'], ['Those killed include a UN aid agency', 'worker, Al Jazeera reported.']),
    ('LIBYA', ['Libya seeks answers', 'on Benghazi strikes'], ['Government asks Kyiv to explain strikes', 'on Russian vessels and seeks inquiry.']),
    ('SPORT', ["Women's World Cup", 'hosts announced'], ['US, Mexico, Costa Rica, Jamaica: 2031;', 'United Kingdom: 2035.']),
]
for i, (kicker, headline, body) in enumerate(stories):
    col, row = i % 2, i // 2
    x = 42 + col * 493
    y = 200 + row * 256
    if i == 0:
        d.rectangle((x, y + 3, x + 5, y + 224), fill=red)
    tx = x + 17 if i == 0 else x
    text((tx, y + 4), kicker, 21, red if i == 0 else teal, True)
    for j, s in enumerate(headline):
        text((tx, y + 43 + j * 42), s, 32, ink, True)
    for j, s in enumerate(body):
        text((tx, y + 139 + j * 30), s, 20, ink)
    if row < 2:
        d.line((x, y + 238, x + 446, y + 238), fill=line, width=2)
d.line((512, 203, 512, 938), fill=line, width=2)
d.line((42, 971, 982, 971), fill=line, width=2)
text((42, 982), 'Six stories that defined Tuesday 24 November 2026', 16, muted)
im.save(ROOT / 'entry.png', format='PNG', optimize=True)
