"""Users

Revision ID: 09afcba5268b
Revises: f6576113b12a
Create Date: 2022-05-26 20:02:33.008290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09afcba5268b'
down_revision = 'f6576113b12a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('addressCep', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('addressCity', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('addressDistrict', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('addressNumber', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('addressStreet', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('birth', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('cellphone', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('sex', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('surname', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('vinculo', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'vinculo')
    op.drop_column('user', 'surname')
    op.drop_column('user', 'sex')
    op.drop_column('user', 'cellphone')
    op.drop_column('user', 'birth')
    op.drop_column('user', 'addressStreet')
    op.drop_column('user', 'addressNumber')
    op.drop_column('user', 'addressDistrict')
    op.drop_column('user', 'addressCity')
    op.drop_column('user', 'addressCep')
    # ### end Alembic commands ###
