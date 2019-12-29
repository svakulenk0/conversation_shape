#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
svakulenko
29 Dec 2019

Calculate conversation statistics
'''
from collections import defaultdict
import argparse

from pymongo import MongoClient

from settings import *


# connect to Mongo DB
mongo = MongoClient()

# collect distribution of DAs per speaker: ynQuestion, whQuestion, Statement, Accept
def get_das_distribution(col_name):
    cmap = DATASETS[col_name]

    das = {'Seeker': defaultdict(int), 'Assistant': defaultdict(int)}
    collection = mongo[DB_NAME][col_name]
    cursor = collection.find({})

    for doc in cursor:
        for m in doc[cmap['utterances']]:
            das[m[cmap['speaker']]][m['da']] += 1
    print(das)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('collection', type=str, help='name of the MongoDB collection to annotate')
    args = parser.parse_args()
    get_das_distribution(args.collection)
