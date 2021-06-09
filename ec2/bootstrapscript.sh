#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
cd /var/www/html
echo "<html><h1>Hello Lbistech, Welcome To My Webpage - Region Ireland - Web Server 02</h1></html>" > index.html


aws s3 sync s3://lbistech-wesite-url/ .
aws s3 mb s3://YOURBUCKETNAMEHERE
aws s3 cp index.html s3://YOURBUCKETNAMEHERE


s3-website-ap-southeast-1.amazonaws.com.