"""add content column

Revision ID: 1ca1ccae1f3c
Revises: 321687d84d52
Create Date: 2024-03-23 14:23:26.345690

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ca1ccae1f3c'
down_revision: Union[str, None] = '321687d84d52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
