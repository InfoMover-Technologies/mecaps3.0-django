from mongoengine import Document, IntField , StringField


class Customer(Document):
    _id = IntField(blank=False)
    name = StringField(blank=True)


    meta = {
        'collection': 'customer',  # This should match your MongoDB collection name
        'strict': False
    }

    @property
    def id(self):
        print(f'The value of id is {self._id}')
        return str(self._id)

    def __str__(self):
        return f"{self._id} {self.name}"
