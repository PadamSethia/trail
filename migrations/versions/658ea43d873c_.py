"""empty message

Revision ID: 658ea43d873c
Revises: 
Create Date: 2019-06-18 15:34:10.670388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '658ea43d873c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    # ### end Alembic commands ###
