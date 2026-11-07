import math

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
        self.recompute()

    def recompute(self):
        hw, hh, hd = self.width / 2, self.height / 2, self.depth / 2

        local_corners = [
            (-hw, -hh, -hd),
            (hw, -hh, -hd),
            (hw, hh, -hd),
            (-hw, hh, -hd),
            (-hw, -hh, hd),
            (hw, -hh, hd),
            (hw, hh, hd),
            (-hw, hh, hd)
        ]

        roll = math.radians(self.roll)
        pitch = math.radians(self.pitch)
        yaw = math.radians(self.yaw)

        croll, sroll = math.cos(roll), math.sin(roll)
        cpitch, spitch = math.cos(pitch), math.sin(pitch)
        cyaw, syaw = math.cos(yaw), math.sin(yaw)

        for i, (lx, ly, lz) in enumerate(local_corners):
            x1 = lx * croll - ly * sroll
            y1 = lx * sroll + ly * croll
            z1 = lz

            x2 = x1
            y2 = y1 * cpitch - z1 * spitch
            z2 = y1 * spitch + z1 * cpitch

            x3 = x2 * cyaw + z2 * syaw
            y3 = y2
            z3 = -x2 * syaw + z2 * cyaw

            self.corners[i] = (self.x + x3, self.y + y3, self.z + z3)