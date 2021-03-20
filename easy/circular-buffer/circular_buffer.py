class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self.buffs = []
        self.cap = capacity
        self.Wplace = 0
        self.Rplace = 0

    def read(self):
        if len(self.buffs) < 1 or self.Rplace+1 > self.cap:
            raise BaseException("buffer is empty")
        else:
            read = self.buffs[self.Rplace]
            self.Rplace += 1
            return read

    def write(self, data):
        if len(self.buffs) < self.cap:
            self.buffs.append(data)
        else:
            raise BaseException("buffer is full")

    def overwrite(self, data):
        if len(self.buffs) < self.cap:
            self.write(data)
        else:
            self.buffs[0] = data

    def clear(self):
        self.buffs = [None]*self.cap
