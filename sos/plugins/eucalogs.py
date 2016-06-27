# Copyright (C) 2013 Eucalyptus Systems, Inc.

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from sos.plugins import Plugin, RedHatPlugin
import os

class eucalogs(Plugin, RedHatPlugin):
    """Eucalyptus Cloud - logfiles
    """

    def setup(self):

        # Collect eucaconsole logs
        if os.path.exists('/var/log/eucaconsole.log') or \
                os.path.exists('/var/log/eucaconsole_startup.log'):
            self.add_copy_spec('/var/log/eucaconsole*.log*')

        # Collect logs for most Eucalyptus components
        if os.path.exists('/var/log/eucalyptus'):
            self.add_copy_spec('/var/log/eucalyptus')

        return
