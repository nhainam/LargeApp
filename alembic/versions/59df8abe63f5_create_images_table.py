"""create images table

Revision ID: 59df8abe63f5
Revises: f1cc45a6cac
Create Date: 2015-11-10 16:12:12.370754

"""

# revision identifiers, used by Alembic.
revision = '59df8abe63f5'
down_revision = 'f1cc45a6cac'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'images',
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('product_id', sa.Integer, nullable=False),
        sa.Column('file_name', sa.String(100), nullable=True),
        sa.Column('default', sa.Boolean, nullable=False, default=0),
        sa.Column('date_created', sa.DateTime, nullable=False),
        sa.Column('date_modified', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('images')