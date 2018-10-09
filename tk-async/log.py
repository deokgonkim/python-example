# -*- coding: utf-8 -*-
#
# $Id: log.py,v 1.0 2018/10/09 dgkim Exp $
#
# $Log: log.py,v $
# Revision 1.0
# 최초 구현
#

import logging

class Loggable(object):

    def __init__(self):
        super(Loggable, self).__init__()

        self.logger = logging.getLogger(self.__class__.__name__)