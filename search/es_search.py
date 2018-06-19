from documents import PostDocument, AuthorDocument
'''
title="python" or "django"
'''


def search_title(title):
    s =  PostDocument.search().query("match", title=title)
    return s.to_queryset()
'''
author='lenny' or 'john'
'''

def search_author(author):
    s = PostDocument.search().query("match", author__name=author)
    return s.to_queryset()

