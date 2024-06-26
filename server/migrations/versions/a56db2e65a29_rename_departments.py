"""rename departments

Revision ID: a56db2e65a29
Revises: e1cd633c8137
Create Date: 2024-06-26 12:28:26.706231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a56db2e65a29'
down_revision = 'e1cd633c8137'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('department', 'departments')


def downgrade():
    op.rename_table('departments', 'department')
