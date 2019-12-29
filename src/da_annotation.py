#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
svakulenko
29 Dec 2019

Use pre-trained classifier to annotate utterance with dialog act labels, such as question, statement, etc.
'''
import argparse
import pickle
from bson.binary import Binary

from pymongo import MongoClient
from simpletransformers.classification import ClassificationModel

from settings import *
from collection_stats import get_das_distribution

# load pre-trained Transformer model with 14 DAs
model = ClassificationModel('roberta', './da_model/', num_labels=len(DA_LABELS))

# connect to Mongo DB
mongo = MongoClient()


def annotate_das(col_name):
    cmap = DATASETS[col_name]
    
    collection = mongo[DB_NAME][col_name]
    cursor = collection.find({'das': {"$exists": False}})
    for doc in cursor:
        # predict DA labels for all utterances in the dialog
        utterances = [m[cmap['text']] for m in doc[cmap['utterances']]]
        predictions, raw_outputs = model.predict(utterances)
        # annotate all utterances with DA labels
        doc['das'] = Binary(pickle.dumps(predictions, protocol=2))
        for j, m in enumerate(doc[cmap['utterances']]):
            m['da'] = DA_LABELS[predictions[j]]
        collection.update_one({'_id': doc['_id']}, {"$set": doc}, upsert=True, check_keys=False)

    # show a sampe dialogue
    sample_doc = collection.find_one()
    print (sample_doc[cmap['utterances']][2][cmap['text']])
    print (sample_doc[cmap['utterances']][2]['da'])
    print(pickle.loads(sample_doc['das']).tolist())

    get_das_distribution(col_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('collection', type=str, help='name of the MongoDB collection to annotate')
    args = parser.parse_args()
    annotate_das(args.collection)
