"""add department

Revision ID: e1cd633c8137
Revises: f398576be6ea
Create Date: 2024-06-26 12:15:35.997565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1cd633c8137'
down_revision = 'f398576be6ea'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('department')
