from enum import Enum

class ChoiceEnum(Enum):
    @classmethod
    def enum_choices(cls):
        return tuple((i.name, i.value) for i in cls)

class orderStatus(ChoiceEnum):
    PENDING = 'PENDING'
    DELIVERED = 'DELIVERED'

    def __str__(self):
        return self.name

ORDER_STATUS_CHOICES = [(x.name, x.value) for x in list(orderStatus)]