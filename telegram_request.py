from enum import Enum

from shared_class.robot_monitoring import RobotMonitoring


class Receiver(Enum):
    SUBSCRIBER = 0
    DISTRIBUTOR = 1
    NATUITION = 2

class TelegramRequest:
    
    def __init__(self, 
                 message : str,
                 send_to : Receiver,
                 robot_serial_number: str, 
                 subscriber_username: str = None,
                 robot_monitoring: RobotMonitoring = None):
        self.robot_serial_number = robot_serial_number
        self.subscriber_username = subscriber_username
        self.message = message
        self.send_to = send_to
        self.robot_monitoring = robot_monitoring
        self.buttons = None
        
    def add_button(self, name: str, link : str):
        if self.buttons is None:
            self.buttons = list()
        self.buttons.append({"name":name, "link":link})