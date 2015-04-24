# vim: set sts=2 ts=8 sw=2 tw=99 et:
import os
import sys
from ambuild2 import run

script_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(script_dir)

builder = run.PrepareBuild(sourcePath=sys.path[0])
builder.options.add_option('--mms-dir', dest='mms_dir', default=os.path.join(parent_dir, 'metamod-source'), help='Path to metamod-source sourcecode.')
builder.options.add_option('--sm-dir', dest='sm_dir', default=os.path.join(parent_dir, 'sourcemod'), help='Path to sourcemod sourcecode.')
builder.options.add_option('--socket-dir', dest='socket_dir', default=script_dir, help='Path to socket sourcecode.') # Really only used because __file__ doesn't work in AMBuildScript.
builder.options.add_option('--enable-debug', action='store_true', dest='debug', default=False, help='Enable debugging symbols')
builder.Configure()
