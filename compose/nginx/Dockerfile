FROM nginx:latest

COPY ./compose/nginx/production.conf /etc/nginx/conf.d/production.conf
COPY ./fga_ontology/fga_ontology/staticfiles /usr/share/nginx/html

EXPOSE 8000

CMD ["nginx", "-g", "daemon off;"]
