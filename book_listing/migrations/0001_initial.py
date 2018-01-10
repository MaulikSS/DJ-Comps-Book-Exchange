# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-10 18:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sem', models.CharField(choices=[('1', 'Semester 1'), ('2', 'Semester 2'), ('3', 'Semester 3'), ('4', 'Semester 4'), ('5', 'Semester 5'), ('6', 'Semester 6'), ('7', 'Semester 7'), ('8', 'Semester 8')], default='Semester 1', max_length=200)),
                ('subject', models.CharField(choices=[('Maths 1 ', ' Applied Mathematics-I'), ('Physics 1 ', ' Applied Physics-I'), ('Chemistry 1 ', ' Applied Chemistry-I'), ('Mechanics ', ' Engineering Mechanics'), ('BEE ', ' Basic Electrical & Electronics Engineering'), ('EVS ', ' EVS'), ('Maths 2 ', ' Applied Mathematics-II'), ('Physics 2 ', ' Applied Physics-II'), ('Chemistry 2 ', ' Applied Chemistry-II'), ('ED ', ' Engineering Drawing'), ('Communication Skills ', ' Communication Skills'), ('SPA ', ' Structured Programming Approach'), ('Maths 3 ', ' Applied Mathematics-III'), ('DLDA ', ' Digital Logic Design and Analysis'), ('ECCF ', ' Electronic Circuits and Communication Fundamentals'), ('DS ', ' Data Structures'), ('Discrete Maths ', ' Discrete Mathematics'), ('Maths 4 ', ' Applied Mathematics-IV'), ('Analysis of Algorithms ', ' Analysis of Algorithms'), ('Computer Organization and Architecture ', ' Computer Organization and Architecture'), ('Computer Graphics ', ' Computer Graphics'), ('Operating System ', ' Operating System'), ('Microprocessor ', ' Microprocessor'), ('DBMS ', ' Database Management System'), ('Computer Network ', ' Computer Network'), ('Theory of Computer Science ', ' Theory of Computer Science'), ('Multimedia System ', ' Multimedia System'), ('Advance Operating System ', ' Advance Operating System'), ('Advance Algorithm ', ' Advance Algorithm'), ('Software Engineering ', ' Software Engineering'), ('System Programming & Compiler Construction ', ' System Programming & Compiler Construction'), ('Data Warehousing and Mining ', ' Data Warehousing and Mining'), ('Cryptography and System Security ', ' Cryptography and System Security'), ('Machine Learning ', ' Machine Learning'), ('Advance Database System ', ' Advance Database System'), ('Advance Computer Network ', ' Advance Computer Network'), ('Enterprise Resource Planning ', ' Enterprise Resource Planning'), ('Digital Signal & Image Processing ', ' Digital Signal & Image Processing'), ('Mobile Communication & Computing ', ' Mobile Communication & Computing'), ('Artificial Intelligence & Soft Computing ', ' Artificial Intelligence & Soft Computing'), ('Advance System Security & Digital Forensics ', ' Advance System Security & Digital Forensics'), ('Big Data & Analytics ', ' Big Data & Analytics'), ('Robotics ', ' Robotics'), ('Product Lifecycle Management ', ' Product Lifecycle Management'), ('Reliability Engineering ', ' Reliability Engineering'), ('Management Information System ', ' Management Information System'), ('Design of Experiments ', ' Design of Experiments'), ('Operation Research ', ' Operation Research'), ('Cyber Security and Laws ', ' Cyber Security and Laws'), ('Disaster Management & Mitigation Measures ', ' Disaster Management & Mitigation Measures'), ('Energy Audit and Management ', ' Energy Audit and Management'), ('Development Engineering ', ' Development Engineering'), ('Human Machine Interaction ', ' Human Machine Interaction'), ('Distributed Computing ', ' Distributed Computing'), ('High Performance Computing ', ' High Performance Computing'), ('Natural Language Processing ', ' Natural Language Processing'), ('Adhoc Wireless Network ', ' Adhoc Wireless Network'), ('Project Management ', ' Project Management'), ('Finance Management ', ' Finance Management'), ('Entrepreneurship Development and Management ', ' Entrepreneurship Development and Management'), ('Human Resource Management ', ' Human Resource Management'), ('Professional Ethics and CSR ', ' Professional Ethics and CSR'), ('Research Methodology ', ' Research Methodology'), ('IPR and Patenting ', ' IPR and Patenting'), ('Digital Business Management ', ' Digital Business Management'), ('Environmental Management ', ' Environmental Management')], default='Maths 1', max_length=1000)),
                ('description', models.TextField(max_length=500)),
                ('book_image', models.FileField(blank=True, null=True, upload_to='')),
                ('author', models.CharField(max_length=50)),
                ('publication', models.CharField(choices=[('Techmax', 'Techmax'), ('Technical', 'Technical'), ('Reference Book', 'Reference Book'), ('Easy Solution', 'Easy Solution')], default='Tech-Max', max_length=20)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
