"""drop topic_id from votes

Revision ID: b4b77f80e1bd
Revises: 
Create Date: 2025-06-21 21:52:02.531823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4b77f80e1bd'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Para Postgres:
    op.drop_constraint('votes_topic_id_fkey', 'votes', type_='foreignkey')
    op.drop_column('votes', 'topic_id')


def downgrade() -> None:
    # Recria a coluna e a FK em caso de rollback:
    op.add_column('votes',
        sa.Column('topic_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key(
        'votes_topic_id_fkey', 'votes', 'topics',
        ['topic_id'], ['id'], ondelete='CASCADE'
    )
