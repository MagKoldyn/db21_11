from sqlalchemy.orm import Mapped, mapped_column
from moduls.base import Base


class Order_product(Base):
    __tablename__ = 'order_product'
    fk_order_code: Mapped[int]
    fk_product_code: Mapped[int]
    quantity: Mapped[int]
