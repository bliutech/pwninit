#!/usr/bin/env python3

from pwn import *

context.terminal = ["tmux", "splitw", "-h"]

{bindings}

context.binary = {bin_name}

nc = "".split()
HOST = nc[1]
PORT = int(nc[2])

gdbscript = """
"""

if args.REMOTE:
    r = remote(HOST, PORT)
else:
    r = process({proc_args})
    if args.GDB:
        gdb.attach(r, gdbscript)

hlog = lambda x: log.info(f"{hex(x)=}")



r.interactive()
