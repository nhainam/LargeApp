"""delete image_id in product table

Revision ID: 4501463f1047
Revises: 59df8abe63f5
Create Date: 2015-11-10 16:16:23.272474

"""

# revision identifiers, used by Alembic.
revision = '4501463f1047'
down_revision = '59df8abe63f5'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_column('products', 'image_id')


def downgrade():
    op.add_column('products', 'image_id', sa.Integer)
