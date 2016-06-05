"""empty message

Revision ID: 3eb9ac3b8fd2
Revises: 1fe77f1378e9
Create Date: 2016-05-29 18:11:32.384043

"""

# revision identifiers, used by Alembic.
revision = '3eb9ac3b8fd2'
down_revision = '1fe77f1378e9'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cabinet', sa.Column('pwer', sa.String(length=10), nullable=True))
    op.drop_column('cabinet', 'power')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cabinet', sa.Column('power', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('cabinet', 'pwer')
    ### end Alembic commands ###