from flask import Flask, json, send_file, request, render_template, abort
from os.path import join
import os
import requests
import socket

api = Flask('flask')
actuator_location = '/actuator/health'
default_prefix = 'http://'
host_name = None
server_name = None
ip_address = None
platform = None
servers = []


@api.route(actuator_location, methods=['GET'])
def actuator():
    print("'actuator': 'ok'")
    return "ok"


@api.route('/', methods=['GET'])
def root():
    json_reply = {'server_info': {'hostname': host_name, 'servername': server_name,
                                  'uname': platform, 'ip_address': ip_address}, 'neighbours': live_list()}
    return json.dumps(json_reply, indent=4, sort_keys=True)


def live_list():
    json_reply = {}
    for server in servers:
        json_reply[server] = is_live(server)
    return json_reply


def is_live(server):
    json_reply = {'actuator': actuator_location}
    try:
        if not server.startswith(default_prefix):
            server = default_prefix+server
        reply = requests.head(server+actuator_location)
        json_reply['status'] = str(reply.status_code)
    except Exception as e:
        json_reply['Exception'] = str(e)
    return json_reply


def get_platform():
    import platform
    return {'system': platform.system(),
            'architecture': platform.architecture(),
            'machine': platform.machine(),
            'node': platform.node(),
            'processor': platform.processor()}


if __name__ == '__main__':
    host_name = socket.gethostname()
    server_name = os.getenv('SERVERNAME')
    if not server_name:
        server_name = host_name
    platform = get_platform()
    servers_string = os.getenv('SERVERS')
    ip_address = socket.gethostbyname(socket.gethostname())
    if servers_string:
        servers_strings = servers_string.split(';')
        for string in servers_strings:
            stripped_string = string.strip()
            if len(stripped_string) > 0:
                servers.append(string.strip())
    api.run(host="0.0.0.0", port=int("8080"))
