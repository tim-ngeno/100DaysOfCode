#!/usr/bin/env python3
# using cologram to extract colors from images

import colorgram

colors = colorgram.extract("image.jpg", 20)
rgb_colors = [color.rgb for color in colors]
print(rgb_colors)
print()
print(rgb_colors[0].r)

rgb = [(color.r, color.g, color.b) for color in rgb_colors]
print(rgb)
