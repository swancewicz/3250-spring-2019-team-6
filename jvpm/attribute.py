from jvpm.utils import parse_bytes_value

ATTRIBUTE_LENGTH_BYTE_START = 2
ATTRIBUTE_LENGTH_BYTE_LENGTH = 4
ATTRIBUTE_NAME_LENGTH = 2


class Attribute():
    def __init__(self, data, start):
        self.data = data
        self.start = start
        self.attribute_name_index = parse_bytes_value(self.data, start, ATTRIBUTE_NAME_LENGTH)
        self.attribute_length = parse_bytes_value(self.data, start+ATTRIBUTE_LENGTH_BYTE_START,
                                                  ATTRIBUTE_LENGTH_BYTE_LENGTH)
        self.total_length = self.attribute_length + ATTRIBUTE_LENGTH_BYTE_START +\
            ATTRIBUTE_LENGTH_BYTE_LENGTH

    def get_attribute_bytes(self):
        length_start = self.start + ATTRIBUTE_LENGTH_BYTE_LENGTH + ATTRIBUTE_NAME_LENGTH
        return self.data[length_start:length_start + self.attribute_length]

    def __str__(self):
        return "Atrribute:\n{}: {}\n{}: {}"\
            .format("Attribute Name Index", self.attribute_name_index,
                    "Attribute Byte Code", self.get_attribute_bytes()
                    )
