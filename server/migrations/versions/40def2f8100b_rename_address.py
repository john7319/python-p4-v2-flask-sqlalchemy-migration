"""rename address

Revision ID: 40def2f8100b
Revises: a56db2e65a29
Create Date: 2024-06-26 12:59:17.848641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40def2f8100b'
down_revision = 'a56db2e65a29'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('departments', 'address',  new_column_name='location')


def downgrade():
    op.alter_column('departments', 'location',  new_column_name='address')
