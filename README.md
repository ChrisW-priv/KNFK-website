# KNFK website repo
This entire repo is used to host code for our main website advertising our
club.

## Hosting and setup
Our website is hosted on our private server in faculty of physics in Warsaw
University of Technology.

Code running is located in VM called kubit01 to which only the admin has
access.

To replicate exact state of current server following steps need to be taken:
- Create new VM
    - Bridge needs to be set to vmbr1 and VLAN to 85
    - Rest is optional but preferably a good amount of storage and memory +
      cores should be allocated.
    - Setup OS
    - Connect to internet
- Clone the repo to VM:
```bash
git clone https://github.com/ChrisW-priv/KNFK-website.git
```
- Replicate virtual environment:
```bash
python3 -m venv ~/env/glob/
source ~/env/glob/bin/activate
pip install flask gunicorn
```
- Bind wsgi to host:
```bash
gunicorn --bind 0.0.0.0:5000 wsgi:app
```
- Create a systemd service to automaticaly start website on VM boot
```bash
sudo vim /etc/systemd/system/website.service
```
And paste text from below:
```
[Unit]
Description=Gunicorn instance to serve Flask website app
After=network.target

[Service]
User=ubuntu-server
Group=www.data
WorkingDirectory=/home/ubuntu-server/knfk_site
Environment=/home/ubuntu-server/env/glob/bin
ExecStart=/home/ubuntu-server/env/glob/bin/gunicorn --workers 3 --bind unix:main.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```
And start the service:
```bash
sudo systemctl start website
sudo systemctl enable website
```
- Setup nginx deploy:
```bash
sudo vim /etc/nginx/sites-available/website.conf
```
And paste text from below:
```
server {
    listen 80;
    server_name www-knfk.fizyka.pw.edu.pl

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu-server/knfk_site/main.sock;
    }
}
```
Create symlink and restart nginx:
```bash
sudo ln -s /etc/nginx/sites-available/website.conf /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```
Finally to prevent 502 error we need to change permitions:
```bash
sudo chmod 775 /home/ubuntu-server/
```
