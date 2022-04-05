"""empty message

Revision ID: 97354897e2ff
Revises: 8294cfc79c3d
Create Date: 2022-01-12 15:54:25.303974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97354897e2ff'
down_revision = '8294cfc79c3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email_address', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(length=60), nullable=False),
    sa.Column('budget', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_address'),
    sa.UniqueConstraint('username')
    )
    op.add_column('item', sa.Column('owner', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'item', 'user', ['owner'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.drop_column('item', 'owner')
    op.drop_table('user')
    # ### end Alembic commands ###
