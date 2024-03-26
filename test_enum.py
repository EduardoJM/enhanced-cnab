from enum import Enum
from cnab.core.registro import RegistroBase
from cnab.core.field import CNABFieldEnum

class EnumA(Enum):
    A = "A"
    B = "B"

class EnumB(Enum):
    AAAA = 1
    BBBB = 2

class C(RegistroBase):
    field = CNABFieldEnum(EnumB, "", length=6, default=EnumB.AAAA, is_integer=True, required=True)

reg = C()
#reg.field = EnumB.BBBB

reg.field

print(reg._meta['field'].get_value())
