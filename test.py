import os
import select
import pyjournalctl

j = pyjournalctl.Journal()
# print j.next()
# print j.get_fd()

epoll = select.epoll()
epoll.register(j.get_fd(), select.EPOLLIN | select.EPOLLET)

j.seek(0, os.SEEK_END)
while True:
    events = epoll.poll(1)
    print events
    for fileno, event in events:
        print j.get_next()
        epoll.modify(j.get_fd(), select.EPOLLIN | select.EPOLLET)

epoll.unregister(j.get_fd())
