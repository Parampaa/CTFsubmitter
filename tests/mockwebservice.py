from __future__ import absolute_import, print_function, unicode_literals

from bottle import post, run, request, abort
from config import config
import re
import logging
import time

logging.basicConfig(
    format='[%(asctime)s] %(message)s',
    level=logging.DEBUG)

log = logging.getLogger(__name__)


# define a regex for flags
flag_regex = config.get("flag_regex", "^\w{31}=$")
service_regex = "^\w{32}$"

#  web interface here
@post('/submit')
def submit_flag():
    team = request.forms.get('team')
    service = request.forms.get('service')
    flags = request.forms.getall('flags')

    if not flags or not team or not service:
        # bad request
        abort(400)

    try:
        team = int(team)
    except:
        abort(400, "team should be a number!")

    if not re.match(service_regex, service):
        abort(400, "wrong format for service \w{32}")

    time.sleep(0.3)



if __name__ == "__main__":
        run(
            host='localhost',
            port=8080,
            reloader=True,
            debug=config.get("debug", False))
