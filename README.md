# stepic_web_project
Шаг 12:
mkdir web
cd web
git clone https://github.com/stasberg/stepic_web_project.git  /home/box/web
sudo rm /etc/nginx/sites-enabled/default
sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
ps -o pid,euser,egroup,comm,args -C nginx
git status
git add --all
git config --global user.name %username%
git config --global user.email %useremail%
git config -l
git commit -a -m "nginx set"
git pull
