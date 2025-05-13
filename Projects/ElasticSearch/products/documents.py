from django_elasticsearch_dsl import Document, fields

# Decorator helps to add data into elastic server
from django_elasticsearch_dsl.registries import registry
from .models import Product

 

# To use the following class as a elastic search class
# it register the class as a document -> following decorator
@registry.register_document
class ProductDocument(Document):    

    # Index => Table (table is available on elastic search server not into database)
    class Index:    
        # Name the table (elastic search server table)
        name = "products"
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}



    class Django:
        model = Product
        fields = [
            "title",
            "description",
            "category",
            "price",
            "brand",
            "sku",
            "thumbnail"
        ]