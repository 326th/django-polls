### Server Customization

Create your environment file to customize this application to your liking

To do so, create .env file in Myweb folder,here's the list  of what setting you can change

- DEBUG - You can make this be False if you want to your server to display
error in detailed way in case of an unexpected error or if you edited this
application and want to test this

**DO NOT SET DEBUG TO False DURING REAL USE**

 - SECRET_KEY - by defualt this value is set to2+xwj9ktuue@s659ahw7zowjyrlou/cl#opw4ffm    
              you should change this value to something else

should anyone know SECRET_KEY, change it or your web's security is compermised

 - TIME_ZONE - your preferred time zone (you can check your possible timezone [here](TIMZONE.txt)
 
 - DATABASES_ENGINE - default is 'django.db.backends.sqlite3'    
use your preferred like 'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', or 'django.db.backends.oracle'    
**You may have to edit setting.py - DATABASES dictionary (line #75)**    
**section to add USER, PASSWORD, PORT, HOST or change NAME to their appropriate database if you use engine other than sqlite3**
 
 - DATABASES_NAME - for sqlite3 engine use ( \<database name\>.sqlite3 )
  **If you change the name after you have already run migrate command and change database name you have to run it again**

.env file example

> DEBUG=True    
> SECRET_KEY=4u2y%iukg#g5zvx-8n%+/-b7pdyeq#l+1*pri$5+    
> TIME_ZONE=Asia/Tokyo    
> DATABASES_ENGINE=django.db.backends.sqlite3    
> DATABASES_NAME=mydatabase.sqlite3    

You don't have to include setting you don't want to change, it will be set to default
