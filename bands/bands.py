#!/usr/bin/env python3

from math import fabs
import re
import sys
import yaml

def get_color(v):
  out = [
    fabs(v * 6.0 - 3.0) - 1.0,
    2.0 - fabs(v * 6.0 - 2.0),
    2.0 - fabs(v * 6.0 - 4.0),
  ]

  out = [max(0.0, min(1.0, x)) for x in out]
  return [format(int(x*255), "02x") for x in out]

earliest = 1960
latest = 2020

with open(sys.argv[1]) as stream:
   try:
      data = yaml.safe_load(stream)
   except:
      sys.exit()

print('''
digraph D {
	overlap=false
	node [style="filled"]
''')

bands = data['bands']
for band_name in bands:
   band = bands[band_name]
   founded = int(band['founded'])
   v = (founded-earliest)/(latest-earliest)
   rgb = get_color(v)
   color = ''.join(rgb)
   if rgb[2] == 'ff':
      fontcolor = '#ffffff'
   else:
      fontcolor = '#000000'
    
   print(f'"{band_name}" [URL="{band["url"]}" founded="{band["founded"]}" fillcolor="#{color}" fontcolor="{fontcolor}"]')
   for influence in band['influences']:
      print(f'"{band_name}" -> "{influence}"')

print('}')
