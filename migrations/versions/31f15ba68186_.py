"""empty message

Revision ID: 31f15ba68186
Revises: 09d7bdb3c372
Create Date: 2023-12-19 20:08:35.553692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31f15ba68186'
down_revision = '09d7bdb3c372'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('case',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.Column('color', sa.String(length=20), nullable=True),
    sa.Column('side_panel', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('cpu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('clockSpeed', sa.Float(precision=1), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('cpu_cooler',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('rpm', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('drive',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('drive_type', sa.String(length=10), nullable=True),
    sa.Column('interface', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('fans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('rpm', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('gpu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('mem', sa.Integer(), nullable=False),
    sa.Column('core_clock', sa.Integer(), nullable=False),
    sa.Column('gpu_len', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('mobo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('mem_slot', sa.Integer(), nullable=False),
    sa.Column('mem_speed', sa.Integer(), nullable=False),
    sa.Column('socket_type', sa.String(length=20), nullable=False),
    sa.Column('form_factor', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('psu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('form_factor', sa.String(length=5), nullable=True),
    sa.Column('effi', sa.String(length=10), nullable=True),
    sa.Column('wattage', sa.Integer(), nullable=True),
    sa.Column('mod', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('ram',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('speed', sa.String(length=20), nullable=True),
    sa.Column('modules', sa.String(length=20), nullable=True),
    sa.Column('cas_latency', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.drop_table('ram_db')
    op.drop_table('cpu_db')
    op.drop_table('psu_db')
    op.drop_table('mobo_db')
    op.drop_table('fans_db')
    op.drop_table('gpu_db')
    op.drop_table('drive_db')
    op.drop_table('cpu_cooler_db')
    op.drop_table('case_db')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('case_db',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('model', sa.VARCHAR(length=50), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('type', sa.VARCHAR(length=20), nullable=True),
    sa.Column('color', sa.VARCHAR(length=20), nullable=True),
    sa.Column('side_panel', sa.VARCHAR(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('cpu_cooler_db',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('model', sa.VARCHAR(length=50), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('size', sa.INTEGER(), nullable=True),
    sa.Column('rpm', sa.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('drive_db',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('model', sa.VARCHAR(length=50), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('capacity', sa.INTEGER(), nullable=True),
    sa.Column('drive_type', sa.VARCHAR(length=10), nullable=True),
    sa.Column('interface', sa.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('gpu_db',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('model', sa.VARCHAR(length=50), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('mem', sa.INTEGER(), nullable=False),
    sa.Column('core_clock', sa.INTEGER(), nullable=False),
    sa.Column('gpu_len', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('fans_db',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('model', sa.VARCHAR(length=50), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('size', sa.INTEGER(), nullable=True),
    sa.Column('rpm', sa.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('mobo_db',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('model', sa.VARCHAR(length=50), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('mem_slot', sa.INTEGER(), nullable=False),
    sa.Column('mem_speed', sa.INTEGER(), nullable=False),
    sa.Column('socket_type', sa.VARCHAR(length=20), nullable=False),
    sa.Column('form_factor', sa.VARCHAR(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('psu_db',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('model', sa.VARCHAR(length=50), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('form_factor', sa.VARCHAR(length=5), nullable=True),
    sa.Column('effi', sa.VARCHAR(length=10), nullable=True),
    sa.Column('wattage', sa.INTEGER(), nullable=True),
    sa.Column('mod', sa.VARCHAR(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('cpu_db',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('model', sa.VARCHAR(length=50), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('clockSpeed', sa.FLOAT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('ram_db',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('model', sa.VARCHAR(length=50), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('speed', sa.VARCHAR(length=20), nullable=True),
    sa.Column('modules', sa.VARCHAR(length=20), nullable=True),
    sa.Column('cas_latency', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.drop_table('ram')
    op.drop_table('psu')
    op.drop_table('mobo')
    op.drop_table('gpu')
    op.drop_table('fans')
    op.drop_table('drive')
    op.drop_table('cpu_cooler')
    op.drop_table('cpu')
    op.drop_table('case')
    # ### end Alembic commands ###
