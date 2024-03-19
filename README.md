Installasi Odoo 17 Comunnity Edition Menggunakan Docker

1. Install Docker dan Docker Compose
2. Install Git

Clone repository config odoo 17
_**git clone https://github.com/giangianna/odoo-17.git**_

Mulai Installasi: buka terminal atau command prompt arahkan ke direktori tempat menyimpan file docker-compose.yml lalu jalankan perintah 
_**docker-compose up -d**_

Jika proses setup odoo sudah selesai, jalankan perintah 
_**docker ps**_

Untuk Akses Odoo buka web
http://localhost:8079/


#Odoo Scaffold
1. Odoo Windows Command
Odoo scaffold command
----
<python path> <odoo bin path> scaffold <module_name> <target_dir>
contoh :
"E:\_Installed Apps\python\python.exe" "E:\_Installed Apps\server\odoo-bin" scaffold learn_customization "E:\_Installed Apps\server\addons"

2. Odoo Docker Command
docker exec odoo-17 /usr/bin/odoo scaffold learn_customization /mnt/extra-addons

Serve endpoints in odoo using controller
Reference
https://www.odoo.com/documentation/17.0/developer/reference/backend/http.html