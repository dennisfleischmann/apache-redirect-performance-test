FROM httpd:latest

ARG NUM_REDIRECTS=600000

COPY mywebsite_${NUM_REDIRECTS}.conf /usr/local/apache2/conf/mywebsite.conf

RUN echo "LoadModule rewrite_module modules/mod_rewrite.so" >> /usr/local/apache2/conf/httpd.conf
RUN echo "Include /usr/local/apache2/conf/mywebsite.conf" >> /usr/local/apache2/conf/httpd.conf
