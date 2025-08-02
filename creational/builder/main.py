from abc import ABC, abstractmethod


class Robot:
    def __init__(self):
        self.material = None
        self.type = None
        self.power = None
        
    def set_material(self, material):
        self.material = material
    
    def set_type(self, type):
        self.type = type
    
    def set_power(self, power):
        self.power = power
    
    def show_robot(self):
        print(f"Material: {self.material}. Power: {self.power}, Type: {self.type}")
        
    
class RobotBuilder(ABC):
    @abstractmethod
    def build_material(self):
        pass

    @abstractmethod
    def build_type(self):
        pass

    @abstractmethod
    def build_power_source(self):
        pass

    @abstractmethod
    def get_robot(self):
        pass


class SteelRobotBuilder(RobotBuilder):
    def __init__(self):
        self.robot = Robot()
    
    def build_material(self):
        self.robot.set_material("Steel")

    def build_type(self):
        self.robot.set_type("Warrior")

    def build_power_source(self):
        self.robot.set_power("Nuclear")

    def get_robot(self):
        return self.robot


class RobotDirector:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct_robot(self):
        self.builder.build_material()
        self.builder.build_type()
        self.builder.build_power_source()
        return self.builder.get_robot()


if __name__ == "__main__":
    director = RobotDirector()
    builder = SteelRobotBuilder()
    director.set_builder(builder)

    robot = director.construct_robot()
    robot.show_robot()