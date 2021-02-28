class LookingGlass :
    def __enter__(self) :
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.revwrite
        return "JABERWOCKY"

    def revwrite(self, text) :
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, trc) :
        import sys
        sys.stdout.write = self.original_write
        if (exc_type) : sys.stdout.write(str(exc_type))
        if (exc_value) : sys.stdout.write(str(exc_value))
        if (trc) : sys.stdout.write(trc)
        sys.stdout.write("Done")


