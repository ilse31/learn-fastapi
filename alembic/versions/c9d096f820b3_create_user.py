"""create user

Revision ID: c9d096f820b3
Revises: 
Create Date: 2024-05-06 15:54:14.669697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9d096f820b3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String),
        sa.Column("email", sa.String),
        sa.Column("password", sa.String),
        sa.Column("fullname", sa.String),
        sa.Column("avatar", sa.String),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_index(op.f("ix_user_username"), "user", ["username"], unique=True)


def downgrade() -> None:
    op.drop_index(op.f("ix_user_username"), table_name="user")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
