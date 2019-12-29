#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
svakulenko
29 Dec 2019

Database identifiers and annotation labels
'''

DB_NAME = 'cm'

# metadata mappings of the conversational datasets
DATASETS = {'scs': {'utterances': 'turns', 'speaker': 'role', 'text': 'text', 'id': 0,
                    'A_User': 'Seeker', 'B_Receiver': 'Assistant'},
            'ccpe': {'utterances': 'utterances', 'speaker': 'speaker', 'text': 'text', 'id': 1},
            'msdialog': {'utterances': 'utterances', 'speaker': 'actor_type', 'text': 'utterance', 'id': 2},
            'multiwoz': {'utterances': 'log', 'speaker': 'speaker', 'text': 'text', 'id': 3,
                         'Seeker': 'Seeker', 'Assistant': 'Assistant'},
            'redial': {'utterances': 'messages', 'speaker': 'speaker', 'text': 'text', 'id': 4,
                       'Seeker': 'Seeker', 'Assistant': 'Assistant'},
            'wow': {'utterances': 'dialog', 'speaker': 'speaker', 'text': 'text', 'id': 5}
            }

DA_LABELS = ['Statement', 'Emotion', 'Greet', 'Accept', 'Reject', 'whQuestion', 'Continuer',
             'ynQuestion', 'yAnswer', 'Bye', 'Clarify', 'Emphasis', 'nAnswer', 'Other']
