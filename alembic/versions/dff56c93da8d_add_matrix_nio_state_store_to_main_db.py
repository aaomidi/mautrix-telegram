"""Add matrix-nio state store to main db

Revision ID: dff56c93da8d
Revises: d3c922a6acd2
Create Date: 2020-03-31 22:04:04.014048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dff56c93da8d'
down_revision = 'd3c922a6acd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nio_account',
    sa.Column('user_id', sa.String(length=255), nullable=False),
    sa.Column('device_id', sa.String(length=255), nullable=False),
    sa.Column('shared', sa.Boolean(), nullable=False),
    sa.Column('sync_token', sa.Text(), nullable=False),
    sa.Column('account', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('user_id', 'device_id')
    )
    op.create_table('nio_device_key',
    sa.Column('user_id', sa.String(length=255), nullable=False),
    sa.Column('device_id', sa.String(length=255), nullable=False),
    sa.Column('display_name', sa.String(length=255), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=False),
    sa.Column('keys', sa.PickleType(), nullable=False),
    sa.PrimaryKeyConstraint('user_id', 'device_id')
    )
    op.create_table('nio_megolm_inbound_session',
    sa.Column('session_id', sa.String(length=255), nullable=False),
    sa.Column('sender_key', sa.String(length=255), nullable=False),
    sa.Column('fp_key', sa.String(length=255), nullable=False),
    sa.Column('room_id', sa.String(length=255), nullable=False),
    sa.Column('session', sa.LargeBinary(), nullable=False),
    sa.Column('forwarded_chains', sa.PickleType(), nullable=False),
    sa.PrimaryKeyConstraint('session_id')
    )
    op.create_table('nio_olm_session',
    sa.Column('session_id', sa.String(length=255), nullable=False),
    sa.Column('sender_key', sa.String(length=255), nullable=False),
    sa.Column('session', sa.LargeBinary(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('last_used', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('session_id')
    )
    op.create_table('nio_outgoing_key_request',
    sa.Column('request_id', sa.String(length=255), nullable=False),
    sa.Column('session_id', sa.String(length=255), nullable=False),
    sa.Column('room_id', sa.String(length=255), nullable=False),
    sa.Column('algorithm', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('request_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nio_outgoing_key_request')
    op.drop_table('nio_olm_session')
    op.drop_table('nio_megolm_inbound_session')
    op.drop_table('nio_device_key')
    op.drop_table('nio_account')
    # ### end Alembic commands ###
