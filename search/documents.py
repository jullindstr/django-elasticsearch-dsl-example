from django_elasticsearch_dsl import DocType, Index, fields

from blog.models import Post, Author

posts = Index('posts')


@posts.doc_type
class PostDocument(DocType):
    author = fields.NestedField(properties={
        'name':fields.TextField(),
        })
    class Meta:
        model = Post

        fields = [
            'title',
            'id',
            'slug',
            'description',
            
        ]


@posts.doc_type
class AuthorDocument(DocType):
    class Meta:
        model = Author

        fields = [
                'name',
                ]
