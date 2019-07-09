基于VUE + Flask (Python3.0)的在线图书馆，期末作业性质

实现功能：

    1. 标准登录注册

    2. 多条件查询图书

    3. 在线阅读

    4. 收藏夹功能
    
前端用到了Element组件库，用axios发请求；数据库用的MySQL

这个项目有个小问题，npm init生成的文件夹被移动到了static里面，因为我不会在不使用Nginx等搭服务器的情况下修改服务器目录，只会从static里读取，以后再说

Flask用到的扩展有：

    1. flask_login 用于登录登出管理 

    2. flask_sqlalchemy 用于连接数据库

    3. flask_wtf 用到里面的token

终端运行_init_.py即可
