import os
import sys
import logging
import web
#enforce import of web.http, o/w py2exe don't understand it need to package it.
import web.http
import json
import time
import mimerender
import jsonpickle
import fnmatch

import socket
import control

mimerender = mimerender.WebPyMimeRender()
# JSON wrapper for @mimerender
render_txt = lambda message: message


logger = logging.getLogger('server')



class GetInfo:
    
    def GET(self, arg):
        print arg
        ret = control.main(arg)
        print ret
        return ret
        #return control.main(arg)
        



### Server Methods ###
"""
For each url class, we should add here a pair of 'url','class_name'
"""

urls = (
    '/search=(.+)', GetInfo.__name__,
)

if __name__ == "__main__":
    try:
        app = web.application(urls, globals())
        app.run()
    except socket.error as e:
        print "error: no socket could be created"
        print "port might be bind already"
        logger.error("Exception raised: " + e.message, exc_info=True)
        os._exit(0)
    
        
