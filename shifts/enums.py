from enum import Enum


class ShiftDuration(Enum):
    FIRST_SHIFT = "00-08"
    SECOND_SHIFT = "08-16"
    THIRD_SHIFT = "16-24"

    @classmethod
    def get_shift_duration_values(cls):
        return list(map(lambda shift_duration: shift_duration.value, cls))