FROM rabbitmq:3.8.9-management-alpine

RUN rabbitmq-plugins enable --offline \
    rabbitmq_prometheus \
    rabbitmq_shovel \
    rabbitmq_shovel_management
