from sqlalchemy.orm import Mapped, mapped_column
from moduls.base import Base


class Users(Base):
    __tablename__ = 'users'
    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    user_age: Mapped[int]
    fk_job_id: Mapped[int]

    def __repr__(self):
        return f"{self.user_id} {self.user_name} {self.user_age} {self.fk_job_id}"
