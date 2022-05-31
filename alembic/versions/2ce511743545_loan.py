"""Loan

Revision ID: 2ce511743545
Revises: d9e7063d4181
Create Date: 2022-05-31 17:20:28.598193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ce511743545'
down_revision = 'd9e7063d4181'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('exemplar', sa.Column('loan_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'exemplar', 'loan', ['loan_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'exemplar', type_='foreignkey')
    op.drop_column('exemplar', 'loan_id')
    # ### end Alembic commands ###