from typing import List
import requests

import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
import PIL.Image as Image

def cut_lines(text: str) -> List[str]:
    words: List[str] = text.split()
    lines: List[str] = []
    line: str = ""
    for word in words:
        line += word + " "
        if len(line) >= 18:
            lines.append(line)
            line = ""
        
    lines.append(line)
    
    return lines

def draw_text(text: str):
    font_name = 'VenrynSans-Regular.ttf'
    font = ImageFont.truetype(font_name, 24)

    img = Image.open("zhirinovsky.png")
    draw = ImageDraw.Draw(img)

    x = 80
    y = 400
    for line in cut_lines(text):
        draw.text((x, y), line, (0, 0, 0), font=font)
        y += 30

    return img

def draw_image(path: str):
    img = Image.open("zhirinovsky.png")
    photo = Image.open(path)

    img.paste(photo.resize((243, 196), Image.LANCZOS), (80, 400))

    return img