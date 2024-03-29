"""empty message

Revision ID: 6e3196c3a983
Revises: 6065428b7f94
Create Date: 2024-03-22 15:31:55.223301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e3196c3a983'
down_revision = '6065428b7f94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pc_build',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('cpu_id', sa.Integer(), nullable=True),
    sa.Column('cpucooler_id', sa.Integer(), nullable=True),
    sa.Column('mobo_id', sa.Integer(), nullable=True),
    sa.Column('gpu_id', sa.Integer(), nullable=True),
    sa.Column('ram_id', sa.Integer(), nullable=True),
    sa.Column('drive_id', sa.Integer(), nullable=True),
    sa.Column('psu_id', sa.Integer(), nullable=True),
    sa.Column('case_id', sa.Integer(), nullable=True),
    sa.Column('fans_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['case_id'], ['case.id'], ),
    sa.ForeignKeyConstraint(['cpu_id'], ['cpu.id'], ),
    sa.ForeignKeyConstraint(['cpucooler_id'], ['cpucooler.id'], ),
    sa.ForeignKeyConstraint(['drive_id'], ['drive.id'], ),
    sa.ForeignKeyConstraint(['fans_id'], ['fans.id'], ),
    sa.ForeignKeyConstraint(['gpu_id'], ['gpu.id'], ),
    sa.ForeignKeyConstraint(['mobo_id'], ['mobo.id'], ),
    sa.ForeignKeyConstraint(['psu_id'], ['psu.id'], ),
    sa.ForeignKeyConstraint(['ram_id'], ['ram.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pc_build')
    # ### end Alembic commands ###
