"""create product table

Revision ID: f1cc45a6cac
Revises: 
Create Date: 2015-11-09 16:09:28.577763

"""

# revision identifiers, used by Alembic.
revision = 'f1cc45a6cac'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('summary', sa.String(100), nullable=True),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('image_id', sa.Integer, nullable=False),
        sa.Column('price', sa.Integer, nullable=True),
        sa.Column('status', sa.Integer, nullable=False, default=0),
        sa.Column('date_created', sa.DateTime, nullable=False),
        sa.Column('date_modified', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('products')
