# tx_site
---
1. 环境搭建
安装python、安装pip、安装vscode、pycharm、django……略
虚拟环境：

		pip install vi
		PowerShell(cmd减掉此部分)  Set-ExecutionPolicy Unrestricted 
		virtualenv .  (建立虚拟环境)
		.\scripts\activate(激活虚拟环境、去激活deactivate)
		django-admin startproject XXXX
		cd XXX
		code .(启动vscode)
		python manage.py runserver
		python manage.py migrate

2. 配置路由
建立app 

		python manage.py startapp YYYYY(在XXXX项目下建立起YYYYY子项目)
urls.py需要配置路由可以在访问主页面时跳转到YYYYY子项目下

		path('',include('YYYYY.urls')),
在YYYYY目录下也有路由文件urls.py，此时就需要指向视图文件中的处理函数

		path('', views.tx_home,name="tx_home"),
视图文件views.py调用框架文件，index.html开始完成页面代码

3. 调用CSS、images、js等资源
html文件中调用相关框架、图片等资源，必须放在django固定的目录下面
在主程序的settings.py文件中有

		# Static files (CSS, JavaScript, Images)
		# https://docs.djangoproject.com/en/3.0/howto/static-files/

		STATIC_URL = '/static/'
在html文件中就可以加载该路径

		{% load static %}
然后再需要调用该路径位置，调用{%  %}来补充路径

		<link rel="stylesheet" type="text/css" href="{% static '/css/main.css' %}" />


