import os
import threading

import app_PM
import app_SNM
import app_TTM

doc = {
    'help': """Meta-Database 帮助

有关某个命令的详细信息，请键入 “help 命令名”"""
}


class MDB(object):
    """docstring for MDB."""

    isRunning = {}

    def __init__(self, debug=False):
        super(MDB, self).__init__()
        self.debug = debug
        os.system('title MDB')
        self.isRunning['MDB'] = True
        print('Welcome to MDB!')
        self.pm = app_PM.PM()
        self.snm = app_SNM.SNM()
        self.ttm = app_TTM.TTM()
        self.current_app = None
        self.startInputStar()

    def startInputStar(self):
        def inputStar():
            print('You can type "help" to get help.')
            while self.isRunning['MDB']:
                cmd = input('>')
                if cmd == '':
                    continue
                else:
                    cmd = cmd.split(' ')
                    if cmd[0] == 'exit' or cmd[0] == 'quit':
                        self.isRunning['MDB'] = False
                    elif cmd[0] == 'help':
                        self.help(cmd)
                    else:
                        self.doCMD(cmd)
        self.t_inputStar = threading.Thread(target=inputStar)
        self.t_inputStar.start()

    def help(self, cmd):
        if len(cmd) == 1:
            print(doc['help'])

    def doCMD(self, cmd):
        if self.current_app == None:
            if cmd[1] == 'pm':
                self.current_app = self.pm
                self.current_app.start(api)
            elif cmd[1] == 'snm':
                self.current_app = self.snm
                self.current_app.start(api)
            elif cmd[1] == 'ttm':
                self.current_app = self.ttm
                self.current_app.start(api)
        else:
            self.current_app.doCMD(cmd)

    def api(self, cmd):
        if cmd == 'exit' or cmd == 'quit':
            self.current_app = None

if __name__ == '__main__':
    MDB()
