import elasticsearch
import os
import json
import query



def build_index(article, search_engine, index_name, article_id):
    search_engine.index(index = index_name, doc_type = "article",id = article_id, body = article)

def retrieve_file_index(file_name):
    return int(file_name.split('-')[0])

def read_articles(root_path, n, search_engine):
     for root, dirs, files in os.walk(root_path):
         for file in files[:n]:
            if file.endswith('.json'):
                with open(os.path.join(root, file), 'r') as f:
                     article = json.load(f)
                     build_index(article, search_engine, "test", retrieve_file_index(file))



es = elasticsearch.Elasticsearch()
read_articles("articles", 500, es)
print(es.search(index='test', body=query.search("body", "surbrize", "fuzzy")))
