import json

def searchBody(word):
    body= {}
    body['body'] = word
    return body

def searchTitle(word):
    title= {}
    title['title'] = word
    return title

def searchAuthors(word):
    author= {}
    author['authors'] = word
    return author

def search(field, word, type):
    query = {}
    query_type  = {}
    if (field == "title"):
        field = searchTitle(word)
    if (field == "body"):
        field = searchBody(word)
    if (field == "author"):
        field = searchAuthors(word)
    query_type[type] = field
    query['query'] = query_type
    json_query = json.dumps(query)
    return json_query
