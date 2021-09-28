from threading import Event

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_event, self.bar_event = Event(), Event()
        self.foo_event.set()
        self.bar_event.clear()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.foo_event.wait()

            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()

            self.foo_event.clear()
            self.bar_event.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.bar_event.wait()

            # printBar() outputs "bar". Do not change or remove this line.
            printBar()

            self.bar_event.clear()
            self.foo_event.set()