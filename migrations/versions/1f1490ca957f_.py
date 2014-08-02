"""Added Admiral

Revision ID: 1f1490ca957f
Revises: 386de93b0678
Create Date: 2014-08-02 03:06:24.151074

"""

# revision identifiers, used by Alembic.
revision = '1f1490ca957f'
down_revision = '386de93b0678'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admiral_version',
        sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
        sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('nickname', sa.String(length=255), autoincrement=False, nullable=True),
        sa.Column('last_login', sa.DateTime(), autoincrement=False, nullable=True),
        sa.Column('level', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('rank', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('experience', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('tutorial_progress', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('furniture', sa.String(length=100), autoincrement=False, nullable=True),
        sa.Column('furniture_coins', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('max_ships', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('max_equips', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('max_furniture', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('available_fleets', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('available_cdocks', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('available_rdocks', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('sortie_successes', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('sortie_total', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('expedition_successes', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('expedition_total', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('pvp_successes', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('pvp_total', sa.Integer(), autoincrement=False, nullable=True),
        sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
        sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
        sa.Column('operation_type', sa.SmallInteger(), nullable=False),
        sa.PrimaryKeyConstraint('id', 'transaction_id')
    )
    op.create_index(op.f('ix_admiral_version_end_transaction_id'), 'admiral_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_admiral_version_operation_type'), 'admiral_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_admiral_version_transaction_id'), 'admiral_version', ['transaction_id'], unique=False)
    op.create_table('transaction',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('issued_at', sa.DateTime(), nullable=True),
        sa.Column('remote_addr', sa.String(length=50), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transaction_user_id'), 'transaction', ['user_id'], unique=False)
    op.create_table('admiral',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('nickname', sa.String(length=255), nullable=True),
        sa.Column('last_login', sa.DateTime(), nullable=True),
        sa.Column('level', sa.Integer(), nullable=True),
        sa.Column('rank', sa.Integer(), nullable=True),
        sa.Column('experience', sa.Integer(), nullable=True),
        sa.Column('tutorial_progress', sa.Integer(), nullable=True),
        sa.Column('furniture', sa.String(length=100), nullable=True),
        sa.Column('furniture_coins', sa.Integer(), nullable=True),
        sa.Column('max_ships', sa.Integer(), nullable=True),
        sa.Column('max_equips', sa.Integer(), nullable=True),
        sa.Column('max_furniture', sa.Integer(), nullable=True),
        sa.Column('available_fleets', sa.Integer(), nullable=True),
        sa.Column('available_cdocks', sa.Integer(), nullable=True),
        sa.Column('available_rdocks', sa.Integer(), nullable=True),
        sa.Column('sortie_successes', sa.Integer(), nullable=True),
        sa.Column('sortie_total', sa.Integer(), nullable=True),
        sa.Column('expedition_successes', sa.Integer(), nullable=True),
        sa.Column('expedition_total', sa.Integer(), nullable=True),
        sa.Column('pvp_successes', sa.Integer(), nullable=True),
        sa.Column('pvp_total', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admiral')
    op.drop_index(op.f('ix_transaction_user_id'), table_name='transaction')
    op.drop_table('transaction')
    op.drop_index(op.f('ix_admiral_version_transaction_id'), table_name='admiral_version')
    op.drop_index(op.f('ix_admiral_version_operation_type'), table_name='admiral_version')
    op.drop_index(op.f('ix_admiral_version_end_transaction_id'), table_name='admiral_version')
    op.drop_table('admiral_version')
    ### end Alembic commands ###
