import mongomock

from mongo_thingy import Model


def test_collection_alias():
    col = mongomock.MongoClient().db.collection

    class Foo(Model):
        _collection = col

    assert Foo.collection == col


def test_get_database_from_table():
    col = mongomock.MongoClient().db.collection

    class Foo(Model):
        _collection = col

    assert isinstance(Foo.database, mongomock.Database)


def test_get_table_from_database():
    db = mongomock.MongoClient().db

    class Foo(Model):
        _database = db

    assert Foo.collection_name == "foo"
