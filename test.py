#!/usr/bin/env python3

import json
import os
import unittest

import arrow

REQUIRED_KEYS = ['name', 'username', 'fun_fact', 'date_joined']

class TestJsonData (unittest.TestCase):
  def test_json (self):
    dirpath = os.path.dirname(__file__)
    
    for root, dirs, files in os.walk(dirpath):
      for file in files:
        if file.endswith('.json') and file != 'template.json':
          full_path = os.path.join(root, file)
          with open(full_path, 'r') as fh:
            data = fh.read()
            data = json.loads(data)
            self.data_check(data)
            
  def data_check (self, data):
    for key in REQUIRED_KEYS:
      self.assertIn(key, data, msg="Required data")
      
    now = arrow.utcnow()
    joined = arrow.get(data['date_joined'])
    self.assertFalse(joined.datetime > now.datetime, msg="Can't join in the future")
    
if __name__ == '__main__':
  unittest.main()
  