#!/usr/bin/env python3

import json
import os
import sys

import arrow

def run (directory):
  stats = {
    'count': 0,
    'class': [],
  }
  
  for file in os.listdir(directory):
    if file.endswith('.json') and file != 'template.json':
      path = os.path.join(directory, file)
      with open(path, 'r') as fh:
        data = json.loads(fh.read())
        stats['count'] += 1
        stats['class'].append(data)
        print('{name}\t\t{username}\t\t{date_joined}'.format(**data))
        
  print('Total:', stats['count'])
  
if __name__ == '__main__':
  run(sys.argv[1])
  