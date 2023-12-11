"""review table

Revision ID: 961d81be71b5
Revises: a2e2fffcdc4f
Create Date: 2023-12-11 09:44:41.867644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '961d81be71b5'
down_revision: Union[str, None] = 'a2e2fffcdc4f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('star_rating', sa.Integer(), nullable=False),
        sa.Column('restaurant_id', sa.Integer(), sa.ForeignKey('restaurant.id'), nullable=False),
        sa.Column('customer_id', sa.Integer(), sa.ForeignKey('customer.id'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('reviews')