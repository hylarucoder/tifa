import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model


class SysOrganization(Model):
    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String(255))


class SysDept(Model):
    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String(255))


class SysRole(Model):
    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String(50))
    #  users
    #  permissions


class SysUser(Model):
    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String(50), unique=True)
    password_hash = sa.Column(sa.String(255))

    # organization_roles = relationship('OrganizationRole', back_populates="user")


class SysUserRole(Model):
    name = sa.Column(sa.String(255))
    user_id = sa.Column(sa.BigInteger, sa.ForeignKey("sys_user.id"), primary_key=True)
    user = relationship(SysUser)
    role_id = sa.Column(sa.BigInteger, sa.ForeignKey("sys_role.id"), primary_key=True)
    role = relationship(SysRole)


class SysPermission(Model):
    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String(255))


class SysUserAudit(Model):
    id = sa.Column(sa.BigInteger, primary_key=True)
    content = sa.Column(sa.JSON(), default=dict)
