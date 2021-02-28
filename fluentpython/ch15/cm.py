import contextlib

@contextlib.contextmanager
def lookingglass() :
    import sys
    original_write = sys.stdout.write

    def revwrite(text) :
        original_write(text[::-1])

    sys.stdout.write = revwrite
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write
