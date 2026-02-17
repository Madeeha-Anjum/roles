from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.address import Address
 
class User(SQLModel, table=True):
    __tablename__ = "user_account"

    id: int | None = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=30)

    addresses: List["Address"] = Relationship(
        # 1 User can have multiple Addresses
        back_populates="user",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, first_name={self.first_name!r})"
