"""create account table

Revision ID: 333feb26e32b
Revises: 
Create Date: 2016-04-27 21:11:30.690293

"""

# revision identifiers, used by Alembic.
revision = '333feb26e32b'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
 op.create_table(
  'account',
  sa.Column('id', sa.Integer, primary_key=True),
  sa.Column('name', sa.String(50), nullable=False),
  sa.Column('password', sa.String(50), nullable=False),
  sa.Column('description', sa.Unicode(200)),
 )


def downgrade():
 op.drop_table('account')
