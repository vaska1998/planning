"""init

Revision ID: 0
Revises:
Create Date: 2024-04-25 22:43:11.756882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('id', sa.INT, nullable=False),
    sa.Column('created_at', sa.Float(), nullable=False),
    sa.Column('updated_at', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    # ### end Alembic commands ###