class Cube:
    def __init__(self, x: int, y: int, z: int, width: int, height: int, depth: int, roll=0, pitch=0, yaw=0):
        self.x=x
        self.y=y
        self.z=z
        self.width=width
        self.height=height
        self.depth=depth
        self.roll=roll
        self.pitch=pitch
        self.yaw=yaw
        self.corners = [(0, 0, 0),]*8
        self.recompute()

    def recompute(self):
        self.corners[0] = (self.x, self.y, self.z)
        self.corners[1] = (self.x + self.width, self.y, self.z)
        self.corners[2] = (self.x + self.width, self.y + self.height, self.z)
        self.corners[3] = (self.x, self.y + self.height, self.z)
        self.corners[4] = (self.x, self.y, self.z + self.depth)
        self.corners[5] = (self.x + self.width, self.y, self.z + self.depth)
        self.corners[6] = (self.x + self.width, self.y + self.height, self.z + self.depth)
        self.corners[7] = (self.x, self.y + self.height, self.z + self.depth)