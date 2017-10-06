class State:
    def __init__(self):
        self.K = []
        self.Q = []
        self.map = []

    def __init__(self, q, k, _map=[]):
        self.Q = q[:]
        self.K = k[:]
        self.map = _map[:]

    def copy(self):
        return State(self.Q, self.K)
