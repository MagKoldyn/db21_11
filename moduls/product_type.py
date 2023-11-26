from sqlalchemy.orm import Mapped, mapped_column
from moduls.base import Base


class Product_type(Base):
    __tablename__ = 'product_type'
    code: Mapped[int] = mapped_column(primary_key=True)
    pname: Mapped[str]
