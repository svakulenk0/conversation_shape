#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
svakulenko
29 Dec 2019

Use pre-trained classifier to annotate utterance with dialog act labels, such as question, statement, etc.
'''
import argparse

from pymongo import MongoClient
from simpletransformers.classification import ClassificationModel

from settings import *

# load pre-trained Transformer model with 14 DAs
model = ClassificationModel('roberta', './da_model/', num_labels=len(DA_LABELS))

# connect to Mongo DB
mongo = MongoClient()


def annotate_das(col_name):
    cmap = DATASETS[col_name]
    
    collection = mongo[DB_NAME][col_name]
    cursor = collection.find()
    for doc in cursor:
        doc_updated = False
        for m in doc[cmap['utterances']]:
            if 'da' not in m:
                predictions, raw_outputs = model.predict([m['text']])
                m['da'] = DA_LABELS[predictions[0]]
                doc_updated = True
        if doc_updated:
            collection.update_one({'_id': doc['_id']}, {"$set": doc}, upsert=True)

    # show a sampe dialogue
    sample_doc = collection.find_one()
    print (sample_doc[cmap['utterances']][2]['text'])
    print (sample_doc[cmap['utterances']][2]['da'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('collection', type=str, help='name of the MongoDB collection to annotate')
    args = parser.parse_args()
    annotate_das(args.collection)
