#!/opt/python3/bin/python3

import sys
import os
import time
import atexit
from signal import SIGTERM
from pet.utils import Logger
from pet.src.thread import PETThread

logger = Logger.getLogger()


class PETDaemon:
    """
    Subclass Daemon class and override the run() method.
    """
    def __init__(
        self,
        pidfile,
        stdin='/dev/null',
        stdout='/dev/null',
        stderr='/dev/null'
    ):

        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile
        self.thread = PETThread()

    def daemonize(self):
        """
        Deamonize, do double-fork magic.
        """
        try:
            pid = os.fork()
            if pid > 0:
                # Exit first parent.
                sys.exit(0)
        except OSError as e:
            message = "Fork #1 failed: {}\n".format(e)
            sys.stderr.write(message)
            sys.exit(1)

        # Decouple from parent environment.
        os.chdir("/")
        os.setsid()
        os.umask(0)

        # Do second fork.
        try:
            pid = os.fork()
            if pid > 0:
                # Exit from second parent.
                sys.exit(0)
        except OSError as e:
            message = "Fork #2 failed: {}\n".format(e)
            sys.stderr.write(message)
            sys.exit(1)

        logger.info('deamon going to background, PID: {}'.format(os.getpid()))

        # Redirect standard file descriptors.
        sys.stdout.flush()
        sys.stderr.flush()
        si = open(self.stdin, 'r')
        so = open(self.stdout, 'a+')
        se = open(self.stderr, 'a+')
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # Write pidfile.
        pid = str(os.getpid())
        open(self.pidfile, 'w+').write("{}\n".format(pid))

        # Register a function to clean up.
        atexit.register(self.delpid)

    def delpid(self):
        os.remove(self.pidfile)

    def start(self, config):
        """
        Start daemon.
        """
        # Check pidfile to see if the daemon already runs.
        try:
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            message = "Pidfile {} already exist. Daemon already running?\n"\
                .format(self.pidfile)
            sys.stderr.write(message)
            sys.exit(1)

        # Start daemon.
        self.daemonize()
        self.run()

    def status(self, config):
        """
        Get status of daemon.
        """
        try:
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            message = "There is not PID file. Daemon already running?\n"
            sys.stderr.write(message)
            sys.exit(1)

        try:
            procfile = open("/proc/{}/status".format(pid), 'r')
            procfile.close()
            message = "There is a process with the PID {}\n".format(pid)
            sys.stdout.write(message)
        except IOError:
            message = "There is not a process with the PID {}\n"\
                .format(self.pidfile)
            sys.stdout.write(message)

    def stop(self, config):
        """
        Stop the daemon.
        """
        # Get the pid from pidfile.
        try:
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError as e:
            message = str(e) + "\nDaemon not running?\n"
            sys.stderr.write(message)
            sys.exit(1)

        # Try killing daemon process.
        try:
            os.kill(pid, SIGTERM)
            time.sleep(1)
        except OSError as e:
            print(str(e))
            sys.exit(1)

        try:
            if os.path.exists(self.pidfile):
                os.remove(self.pidfile)
        except IOError as e:
            message = str(e) + "\nCan not remove pid file {}"\
                .format(self.pidfile)
            sys.stderr.write(message)
            sys.exit(1)

    def restart(self, config):
        """
        Restart daemon.
        """
        self.stop()
        time.sleep(1)
        self.start()

    def test(self, config):
        pass

    def run(self):
        self.thread.start()
