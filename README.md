Usage:

    version: "3"
    services:
        mailcatcher:
            build: mailcatcher/
            env_file: .env
            ports:
                - "8080:8080"
                - "25:25"
            volumes:
                - ./mails/:/srv/mails/
        # ...

Send mails to smtp://mailcatcher:25 .

And then surf to http://localhost.direct:8080/ .
