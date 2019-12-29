# conversation_mining

Python library for advanced conversation analysis.


## Requirements

* torch
* simpletransformers
* pymongo
* sklearn
* seaborn


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

2. Dialog classification


## Results

Get collection statistics:

```
python src/collection_stats.py *mongo_collection_name*
```
