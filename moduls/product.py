from sqlalchemy.orm import Mapped, mapped_column
from moduls.base import Base


class Product(Base):
    __tablename__ = 'product'
    code: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str]
    price: Mapped[int]
    fk_type_code: Mapped[int]
