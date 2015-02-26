# -*- coding: utf-8 -*-
 

{
    'name': 'auto_select_smtp ',
    'version': '1.0',
    'category': 'Base',
    'description': """

    根据 发件人 自动选择正确的 smtp 服务器. 主要用于 客户的smtp 服务器不允许代发邮件的情况
    patch: 首先查找 smtp_from 对应的 smtp 服务器
    要求 定义 Outgoing Mail Servers 时候, 确保 Description(name) 字段的值 为对应的 邮件发送账户(完整的eMail地址)
    本模块以此 为 邮件的发送者 查找 smtp 服务器
    需要为系统中 每个可能发送邮件的账户 按以上要求设置一个 服务器


    """,
    'author': 'CCDOS',
    'website': 'http://www.intoerp.com',
    'depends': ['base'],
    'data': [
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
