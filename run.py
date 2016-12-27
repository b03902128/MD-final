import tf_glove
from data_utils import reddit_comment_corpus
from sys import argv

data_dir="../../data/corpus_"

model = tf_glove.GloVeModel(embedding_size=50, context_size=10, min_occurrences=25,
                            learning_rate=0.05, batch_size=512)

cntn_corpus = open(data_dir+argv[1],'r').readlines()
corpus=[line.split() for line in cntn_corpus]
print(len(corpus))

model.fit_to_corpus(corpus)
print("fit_to_corpus done.")

print("Start training.")
model.train(num_epochs=50, log_dir="log/example", summary_batch_interval=300, tsne_epoch_interval=300)

#new_word=["european","commission","president", "parliament", "council"]
new_word=[argv[1]]
for word in new_word:
    print(word, model.embedding_for(word))

tf_glove.get_mapping(model)

model.generate_tsne("log/"+argv[1])
