1.验证django是否安装成功
（1）检查版本
import django
django.get_version()
或者
python -c 'import django; print(django.get_version())'
或者
django-admin --version

（2）查看帮助
django -h


2.Models

python manage.py makemigrations to create migrations for those changes
python manage.py migrate to apply those changes to the database.

（1）models的一些方法
例如：Question，Choice类

Question.objects.get(pub_date__year=current_year)   # pub_date__year 取时间类型中的year
Question.objects.get(pk=1)

q = Question.objects.get(pk=1)
c = q.choice_set.create()
c.question.pub_date
c.question
q.choice_set.count()

3.admin site


4.views and template


5.forms and generic views


6.testing


7.static files


