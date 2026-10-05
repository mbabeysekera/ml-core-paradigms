from pydantic import BaseModel, Field
from datetime import datetime, timezone


class User(BaseModel):
    id: int = Field(..., ge=1,
                    description="The unique identifier for the user")
    name: str = Field(..., min_length=1, max_length=64,
                      description="The name of the user")
    email: str = Field(..., min_length=1, max_length=64,
                       description="The email address of the user")
    age: int = Field(15, ge=0, description="The age of the user")
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc),
                                 description="The timestamp when the user was created")


def validate_user_data(user_data: dict) -> User:
    """
    Validate user data using Pydantic.

    Args:
        user_data (dict): A dictionary containing user data.

    Returns:
        User: A validated User object.

    Raises:
        ValidationError: If the user data is invalid.
    """
    return User(**user_data)
