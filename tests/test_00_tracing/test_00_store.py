from tracing import Store


def test_store() -> None:
    store = Store[int](1)
    assert store.get() == 1

    store.set(2)
    assert store.get() == 2

    assert store == Store[int](2)
    assert store != Store[int](1)

    assert Store().set(1.0).get() == 1.0
    assert Store().set(None).get() is None
    assert Store().set("Hello").get() == "Hello"
    assert Store().set(1 + 2j).get() == 1 + 2j
    assert Store().set(object).get() == object
