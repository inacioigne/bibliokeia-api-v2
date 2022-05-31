"""Loan

Revision ID: 4d11c1898b59
Revises: 2ce511743545
Create Date: 2022-05-31 17:41:37.605217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d11c1898b59'
down_revision = '2ce511743545'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('loan', sa.Column('due', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('loan', 'due')
    # ### end Alembic commands ###
