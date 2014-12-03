#Auto generate certificate openssl
#!/bin/bash
openssl req -new -newkey rsa:4096 -days 2 -nodes -x509 -subj "/C=SP/ST=Madrid/L=Madrid/O=EndikaIG/OU=Internet Services/CN=endikaiglesias.com" -keyout server.key  -out server.cert
mv /root/server.key /etc/ssl/private/server.key
mv /root/server.cert /etc/ssl/certs/server.crt
/etc/init.d/apache2 reload
