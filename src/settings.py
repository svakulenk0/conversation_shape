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
            'ccpe': {'utterances': 'utterances', 'speaker': 'speaker', 'id': 1},
            'msdialog': {'utterances': 'utterances', 'speaker': 'actor_type', 'id': 2},
            'multiwoz': {'utterances': 'log', 'speaker': 'speaker', 'id': 3},
            'redial': {'utterances': 'messages', 'speaker': 'senderWorkerId', 'id': 4},
            'wow': {'utterances': 'dialog', 'speaker': 'speaker', 'id': 5}
            }

DA_LABELS = ['Statement', 'Emotion', 'Greet', 'Accept', 'Reject', 'whQuestion', 'Continuer',
             'ynQuestion', 'yAnswer', 'Bye', 'Clarify', 'Emphasis', 'nAnswer', 'Other']
