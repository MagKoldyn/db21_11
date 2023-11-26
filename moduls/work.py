from sqlalchemy.orm import Mapped, mapped_column
from moduls.base import Base


class Work(Base):
    __tablename__ = 'work'
    job_id: Mapped[int] = mapped_column(primary_key=True)
    job_name: Mapped[str]
    salary: Mapped[int]
