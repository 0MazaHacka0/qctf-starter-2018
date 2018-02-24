"""empty message

Revision ID: e156032bc0ef
Revises: 
Create Date: 2018-02-23 21:02:52.607874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e156032bc0ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('balance', sa.Integer(), server_default='10', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('bet', sa.Integer(), nullable=False),
    sa.Column('secret_number', sa.String(length=4), nullable=False),
    sa.Column('has_ended', sa.Boolean(), server_default='false', nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('moves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('guess', sa.String(length=4), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moves')
    op.drop_table('games')
    op.drop_table('users')
    # ### end Alembic commands ###
