"""Initial Migration

Revision ID: 67dfad97eb56
Revises: 
Create Date: 2020-07-13 15:56:41.641809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67dfad97eb56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('pitch_id', sa.Integer(), nullable=False),
    sa.Column('pitch', sa.String(length=100000), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('upvotes', sa.Integer(), nullable=True),
    sa.Column('downvote', sa.Integer(), nullable=True),
    sa.Column('submitted_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['submitted_by'], ['users.u_id'], ),
    sa.PrimaryKeyConstraint('pitch_id')
    )
    op.add_column('comments', sa.Column('for_pitch', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'pitches', ['for_pitch'], ['pitch_id'])
    op.drop_column('comments', 'category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('category', sa.VARCHAR(length=150), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'for_pitch')
    op.drop_table('pitches')
    # ### end Alembic commands ###