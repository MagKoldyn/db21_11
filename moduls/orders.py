import datetime
from sqlalchemy import Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from moduls.base import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from typing import List


class Orders(Base):
    __tablename__ = 'orders'
    code: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False), server_default=func.now())
    fk_user_code: Mapped[int]
    # use a list
    order_products: Mapped[List["Order_product"]] = relationship()

    def __repr__(self):
        return f"{self.code} {self.date} {self.fk_user_code} {self.order_products}"


class Order_product(Base):
    __tablename__ = 'order_product'
    fk_order_code: Mapped[int] = mapped_column(ForeignKey("orders.code"), primary_key=True)
    fk_product_code: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int]

    def __repr__(self):
        return f"{self.fk_order_code} {self.fk_product_code} {self.quantity}"
