#!/usr/bin/env python3
'''
This file initializes your application and brings together all of the various components.
'''
from flask import Flask
from btcxplr.api import RPC, RPC_USER, RPC_PASS, RPC_HOST, RPC_PORT

app = Flask(__name__)
rpc = RPC(RPC_USER, RPC_PASS, RPC_HOST, RPC_PORT)
app.secret_key = "HH{gv_g;J1p:x^+q*,O/c;}~)Ib~L[%E"

import btcxplr.views