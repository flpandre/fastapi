"""First commit entity

Revision ID: db32ce7ebbaf
Revises: 
Create Date: 2023-07-27 17:52:05.930150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db32ce7ebbaf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entity',
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('entity_id')
    )
    op.create_index(op.f('ix_entity_entity_id'), 'entity', ['entity_id'], unique=False)
    op.create_index(op.f('ix_entity_type'), 'entity', ['type'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_entity_type'), table_name='entity')
    op.drop_index(op.f('ix_entity_entity_id'), table_name='entity')
    op.drop_table('entity')
    # ### end Alembic commands ###
