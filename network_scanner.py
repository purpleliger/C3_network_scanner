import socket
import subprocess
import sys
from datetime import datetime

def scan_host(host, port):
    """
    Scan the host and port provided to check if it is open.
    """
    