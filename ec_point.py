class ECPoint:
    def __init__(self, xi: int, yi: int):
        self.x = xi
        self.y = yi

    def __repr__(self):
        return f"({hex(self.x)},{hex(self.y)})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
