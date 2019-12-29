#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
svakulenko
29 Dec 2019

Database identifiers and annotation labels
'''

DB_NAME = 'cm'

# metadata mappings of the conversational datasets
DATASETS = {'scs': {'utterances': 'turns', 'speaker': 'role', 'id': 0},
            'ccpe': {'utterances': 'utterances', 'speaker': 'speaker', 'id': 1}
            }

DA_LABELS = ['Statement', 'Emotion', 'Greet', 'Accept', 'Reject', 'whQuestion', 'Continuer',
             'ynQuestion', 'yAnswer', 'Bye', 'Clarify', 'Emphasis', 'nAnswer', 'Other']
