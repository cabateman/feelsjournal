"""feelsjournal RESTFUL API Server

Usage:
  server.py [--port=<port>] [--debug=<debug>] [--network=<network>]

Options:
  --port=<port>     HTTP PORT [default: 5000]
  --debug=<debug>   Debug mode, true or false. [default: false]
  --network=<network>    Network accessible mode, true or false. [default: false]
"""

from docopt import docopt
from feels import app
from feels.lib import logger

logger.init_web_logging()
if __name__ == '__main__':
    arguments = docopt(__doc__)
    app.debug = (arguments['--debug'].lower() == 'true')
    host = '0.0.0.0' if(arguments['--network'].lower() == 'true') else '127.0.0.1'
    app.run(host=host, port=int(arguments['--port']))
