# conversation_mining

Python library for conversation analysis.


## Requirements

Python 3.6

* torch
* simpletransformers
* pymongo
* sklearn
* seaborn

## Setup

1. Index the conversation dataset into a MongoDB collection, where each conversation transcript is represented as a JSON dictionary object.

2. Add field mappings for your collection in settings.py specifying the structure of the dictionary object.

Each conversation transcript is a dictionary that contains the list of *utterances*. Each utterance in turn consists of a 
*text* field that stores a String value of the utterance content and a *speaker* label which is used to identify to whom of the conversation participants the utterance belongs. Finally add bi-directional mappings for speaker labels to identify *Seeker* and *Assistant* roles among the conversation participants.

## Approach

1. Dialog annotation  

1.1. Utterance classification labels  

```
python src/da_annotation.py *mongo_collection_name*
e.g. python src/da_annotation.py scs
```

1.2. Vocabulary reuse patterns

```
x
x
```

2. Metrics


## Results

Get collection statistics:

```
python src/collection_stats.py *mongo_collection_name*
```
