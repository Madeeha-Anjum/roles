from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.address import Address
 
class User(SQLModel, table=True):
    __tablename__ = "user_account"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=30)
    fullname: Optional[str] = None

    addresses: List["Address"] = Relationship(
        # Address has a many-to-one relationship to User aka 1 User can have multiple Addresses
        back_populates="user",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
