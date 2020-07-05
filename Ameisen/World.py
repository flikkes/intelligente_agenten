class World:
    fields = []
    sizeX = 10
    sizeY = 10

    def _init__(self, sizeX, sizeY = None):
        if not sizeX is None:
            if sizeY is None:
                self.sizeY = sizeX
            else:
                self.sizeY = sizeY
            self.sizeX = sizeX

