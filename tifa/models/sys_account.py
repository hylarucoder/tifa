import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import db
from tifa.models.base import ModelMixin, ContentTypeMixin


class SysOrganization(ModelMixin, db.Model):
    __tablename__ = "sys_organizations"

    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String(255))


class SysDept(ModelMixin, db.Model):
    __tablename__ = "sys_dept"

    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String(255))


class SysRole(ModelMixin, db.Model):
    __tablename__ = "sys_role"

    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String(50))
    #  users
    #  permissions


class SysUser(ModelMixin, db.Model):
    __tablename__ = "sys_user"

    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String(50), unique=True)
    password_hash = sa.Column(sa.String(255))

    # organization_roles = relationship('OrganizationRole', back_populates="user")


class SysUserRole(ModelMixin, db.Model):
    __tablename__ = "sys_user_role"

    name = sa.Column(sa.String(255))
    user_id = sa.Column(sa.BigInteger, sa.ForeignKey('sys_user.id'), primary_key=True)
    user = relationship(SysUser)
    role_id = sa.Column(sa.BigInteger, sa.ForeignKey('sys_role.id'), primary_key=True)
    role = relationship(SysRole)


class SysPermission(ModelMixin, db.Model):
    __tablename__ = "sys_permission"
    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String(255))


class SysUserAudit(ModelMixin, ContentTypeMixin, db.Model):
    __tablename__ = "sys_user_audit"

    id = sa.Column(sa.BigInteger, primary_key=True)
    content = sa.Column(sa.JSON(), default=dict)


