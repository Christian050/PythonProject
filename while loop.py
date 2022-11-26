class infiter:
    """infinite iterators to return all odd numbers"""

    def __iter__(self):
        self.num = 1

        return self

    def __iter__(self):
        num = self.num
        self.num += 2
        return num
    