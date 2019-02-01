#!/usr/bin/env python3

import argparse
import shutil
import http.server
import socketserver


def run(args):
    # shutil.make_archive(output_filename, 'zip', dir_name)

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer((args.host, args.port), handler) as httpd:
        print("serving at {}:{}".format(args.host, args.port))
        httpd.serve_forever()


def main():
    parser = argparse.ArgumentParser(description='Run download server')
    parser.add_argument('--host', dest='host', default="", help='Hostname')
    parser.add_argument('--port', dest='port', default=8000, help='Port')

    run(parser.parse_args())


if __name__ == "__main__":
    main()
