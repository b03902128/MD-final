# MD-final

# usage 
python run.py "the new word" > log/"log file"

ex:
python run.py council > log/council.log

The default corpus name would be "corpus_"+ "the new word" ex:"corpus_council"

# output

including:

1. word2id mapping

2. word embedding vectors

3. coocurrence matrix

download : https://drive.google.com/open?id=0B5IxAjH6-LZ9QkgzOFdMSEY0bVk

# dataset
large(600MB) Europarl v7: http://www.statmt.org/wmt15/translation-task.html

split by some selective 'new' words by voc.txt to:
* corpus_council
* corpus_commission
* corpus_parliament
* corpus_president
...

and exclusive all the new words:
* corpus_exclusive

Original large embedding(Europarl v7) is also provided. 
