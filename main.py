class LineFollowerRobot:
    def __init__(self):
        self.position = 0

    def read_sensors(self):
        import random
        return random.choice(["left", "right", "center"])

    def move(self, direction):
        if direction == "left":
            self.position -= 1
        elif direction == "right":
            self.position += 1

    def run(self):
        for _ in range(20):
            sensor = self.read_sensors()

            if sensor == "left":
                self.move("left")
                print("Moving Left")
            elif sensor == "right":
                self.move("right")
                print("Moving Right")
            else:
                print("Moving Straight")

robot = LineFollowerRobot()
robot.run()
