from enum import Enum


class RobotMonitoring(str, Enum):
    BLOCKING_PAGE_1_TO_2 = "BLOCKING_PAGE_1_TO_2"
    BLOCKING_PAGE_1_TO_2_FIX = "BLOCKING_PAGE_1_TO_2_FIX"
    BLOCKING_PAGE_1_TO_2_NOT_FIX = "BLOCKING_PAGE_1_TO_2_NOT_FIX"
    BLOCKING_DURING_OPERATION = "BLOCKING_DURING_OPERATION"
    BLOCKING_DURING_OPERATION_FIX = "BLOCKING_DURING_OPERATION_FIX"
    BLOCKING_DURING_OPERATION_NOT_FIX = "BLOCKING_DURING_OPERATION_NOT_FIX"

