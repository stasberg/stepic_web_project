sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
gunicorn -w 2 -c /home/box/web/etc/hello.py hello:app
