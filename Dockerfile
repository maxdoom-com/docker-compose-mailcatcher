FROM alpine:3.17

RUN apk add                     \
    bash                        \
    mc                          \
    mini_httpd                  \
    python3                     #

ADD ["sbin/boot.sh", "/sbin/"]
ADD ["sbin/mailcatcher.py", "/sbin/"]
ENTRYPOINT ["/bin/sh", "/sbin/boot.sh"]
