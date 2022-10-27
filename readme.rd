Write in any language you prefer (our preferred language is python using flask) a web
service that have two end points ( two api) one to post a message in a Rabbit- MQ and
another one to consume what was produced in the previous API the delivery of this web
application should a docker image.


To start the project:
- docker-compose up -d

- send request using postman : localhost:5000/create-message/<msg>
and the message will be appear at the console the consumed from rabbitmq
