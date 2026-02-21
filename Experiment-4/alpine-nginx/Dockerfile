FROM alpine:latest

RUN apk add --no-cache nginx

RUN mkdir -p /var/www/localhost/htdocs

COPY alpine-html/index.html /var/www/localhost/htdocs/index.html

RUN printf "server {\n\
    listen 80;\n\
    root /var/www/localhost/htdocs;\n\
    index index.html;\n\
    location / {\n\
        try_files \$uri \$uri/ =404;\n\
    }\n\
}\n" > /etc/nginx/http.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]