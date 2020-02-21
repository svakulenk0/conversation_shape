#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
svakulenko
13 Jan 2019

Collections metadata mapping
'''
import numpy as np


DB_NAME = 'cm'

# metadata mappings of the conversational datasets
DATASETS = {'scs': {'utterances': 'turns', 'speaker': 'role', 'text': 'text', 'id': 0,
                    'A_User': 'Seeker', 'B_Receiver': 'Assistant'},
            'ccpe': {'utterances': 'utterances', 'speaker': 'speaker', 'text': 'text', 'id': 1,
                     'USER': 'Seeker', 'ASSISTANT': 'Assistant'},
            'msdialog': {'utterances': 'utterances', 'speaker': 'actor_type', 'text': 'utterance', 'id': 2,
                         'User': 'Seeker', 'Agent': 'Assistant',
                         'Seeker': 'User', 'Assistant': 'Agent'},
            'multiwoz': {'utterances': 'log', 'speaker': 'speaker', 'text': 'text', 'id': 3,
                         'Seeker': 'Seeker', 'Assistant': 'Assistant'},
            'redial': {'utterances': 'messages', 'speaker': 'speaker', 'text': 'text', 'id': 4,
                       'Seeker': 'Seeker', 'Assistant': 'Assistant'},
            'wow': {'utterances': 'dialog', 'speaker': 'speaker', 'text': 'text', 'id': 5,
                    'Seeker': ['0_Apprentice', '1_Apprentice'], 'Assistant': ['0_Wizard', '1_Wizard'],
                    '1_Apprentice': 'Seeker', '0_Apprentice': 'Seeker',
                    '0_Wizard': 'Assistant', '1_Wizard': "Assistant"},
            'daily': {'utterances': 'dialogue', 'speaker': 'speaker', 'text': 'text', 'id': 6,
                      'Seeker': 'Seeker', 'Assistant': 'Assistant'},
            'convai2': {'utterances': 'dialog', 'speaker': 'sender_class', 'text': 'text', 'id': 7,
                        'Seeker': 'Human', 'Assistant': 'Bot',
                        'Human': 'Seeker', 'Bot': 'Assistant'},
            'control': {'utterances': 'dialog', 'speaker': 'speaker', 'text': 'text', 'id': 8,
                        'Seeker': 'human_evaluator', 'Assistant': 'model',
                        'human_evaluator': 'Seeker', 'model': 'Assistant'},
            'meena': {'utterances': 'utterances', 'speaker': 'role', 'text': 'text', 'id': 9,
                      'Seeker': 'Seeker', 'Assistant': 'Assistant'}            
            }

DA_LABELS = ['Statement', 'Emotion', 'Greet', 'Accept', 'Reject', 'whQuestion', 'Continuer',
                     'ynQuestion', 'yAnswer', 'Bye', 'Clarify', 'Emphasis', 'nAnswer', 'Other']

def get_cmap(col_name):
        return DATASETS[col_name.split('_')[0]]

def calculate_stats(int_list):
        print(min(int_list), int(np.mean(int_list)), int(np.var(int_list)), max(int_list))
