"""seed

Revision ID: 1
Revises: 0
Create Date: 2024-04-24 14:21:04.349530

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session
from migrations.to_seed import project_to_seed
from src.domain.model.project import Project

# revision identifiers, used by Alembic.
revision = '1'
down_revision = '0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    with Session(bind=bind) as session:
        for project in project_to_seed:
            new_project = Project(**project)
            session.add(new_project)

        session.commit()


def downgrade() -> None:
    op.execute('DELETE FROM projects')
