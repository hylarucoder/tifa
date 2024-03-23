from tortoise import fields

from tifa.db import Model


class SysUser(Model):
    class Meta:
        table = "sys_user"
        table_description = "系统管理员表"

    def __str__(self):
        return self.username

    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=20, default='', description='用户名')
    password_hash = fields.CharField(max_length=300, default='', description='密码')
    avatar = fields.CharField(max_length=300, default='', description='头像')
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
