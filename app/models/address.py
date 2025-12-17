from typing import TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship

if TYPE_CHECKING:
    from app.models.user import User
    


class Address(SQLModel, table=True):
    __tablename__ = "address"
    id: int | None = Field(default=None, primary_key=True)
    email_address: str
    user_id: int | None = Field(default=None, foreign_key="user_account.id")
    
    user: "User" = Relationship(
        # Address has a many-to-one relationship to aka many Addresses can belong to 1 User
        back_populates="addresses"
    )
    
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"