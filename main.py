#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from apriori import EjecutarCorrida

argumentos = sys.argv

EjecutarCorrida(str(argumentos[1]), float(argumentos[2]), float(argumentos[3]))



