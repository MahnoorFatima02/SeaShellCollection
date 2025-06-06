"""Initial migration

Revision ID: 8ac8ae8a5643
Revises: 
Create Date: 2025-05-19 13:22:45.430378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ac8ae8a5643'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shells',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('species', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('size', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shells_id'), 'shells', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shells_id'), table_name='shells')
    op.drop_table('shells')
    # ### end Alembic commands ###
