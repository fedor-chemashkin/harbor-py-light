#!/usr/bin/env python

import sys
sys.path.append("../harborclient/")

import harborclient

host = "127.0.0.1"
user = "admin"
password = "Harbor12345"

client = harborclient.HarborClient(host, user, password)
print(client.check_project_exist("test-project"))