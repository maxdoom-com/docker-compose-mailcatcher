#!/usr/bin/env python3

from smtpd import DebuggingServer
import asyncore
import time
from datetime import datetime
 


class MyDebuggingServer(DebuggingServer):

    def _print_message_content(self, peer, data):
        with open(datetime.today().strftime('%Y-%m-%d_%H:%M:%S.txt'), "w") as output:
            inheaders = 1
            lines = data.splitlines()
            for line in lines:
                # headers first
                if inheaders and not line:
                    peerheader = 'X-Peer: ' + peer[0]
                    if not isinstance(data, str):
                        # decoded_data=false; make header match other binary output
                        peerheader = repr(peerheader.encode('utf-8'))
                    output.write(peerheader + "\n")
                    inheaders = 0
                if not isinstance(data, str):
                    # Avoid spurious 'str on bytes instance' warning.
                    line = repr(line)
                output.write(line + "\n")

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        # print('---------- MESSAGE FOLLOWS ----------')
        # if kwargs:
        #     if kwargs.get('mail_options'):
        #         print('mail options: %s' % kwargs['mail_options'])
        #     if kwargs.get('rcpt_options'):
        #         print('rcpt options: %s\n' % kwargs['rcpt_options'])
        self._print_message_content(peer, data)
        # print('------------ END MESSAGE ------------')


if __name__ == '__main__':
    smtpd = MyDebuggingServer( ("0.0.0.0", 25), None, 33554432, None, False, True)
    asyncore.loop()

