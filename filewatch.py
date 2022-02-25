import pyinotify
import asyncio

def handle_read_callback(notifier):
    """
    Just stop receiving IO read events after the first
    iteration (unrealistic example).
    """
    print('handle_read callback')
    notifier.loop.stop()


wm = pyinotify.WatchManager()
loop = asyncio.get_event_loop()
notifier = pyinotify.AsyncioNotifier(wm, loop,
                                     callback=handle_read_callback)
watch = wm.add_watch('/tmp', pyinotify.ALL_EVENTS, rec=True, auto_add=True)
print(watch) # Prints something like this: {'/tmp': 1, '/tmp/python-languageserver-cancellation': 2, '/tmp/python-languageserver-cancellation/21e87816d29701a6a5028632578e631360d1d1be8b': 3}
loop.run_forever()
"""Output:
<Event dir=True mask=0x40000020 maskname=IN_OPEN|IN_ISDIR name=python-languageserver-cancellation path=/tmp pathname=/tmp/python-languageserver-cancellation wd=1 >
<Event dir=True mask=0x40000001 maskname=IN_ACCESS|IN_ISDIR name=python-languageserver-cancellation path=/tmp pathname=/tmp/python-languageserver-cancellation wd=1 >
<Event dir=True mask=0x40000010 maskname=IN_CLOSE_NOWRITE|IN_ISDIR name=python-languageserver-cancellation path=/tmp pathname=/tmp/python-languageserver-cancellation wd=1 >
<Event dir=True mask=0x40000020 maskname=IN_OPEN|IN_ISDIR name=21e87816d29701a6a5028632578e631360d1d1be8b path=/tmp/python-languageserver-cancellation pathname=/tmp/python-languageserver-cancellation/21e87816d29701a6a5028632578e631360d1d1be8b wd=2 >
<Event dir=True mask=0x40000001 maskname=IN_ACCESS|IN_ISDIR name=21e87816d29701a6a5028632578e631360d1d1be8b path=/tmp/python-languageserver-cancellation pathname=/tmp/python-languageserver-cancellation/21e87816d29701a6a5028632578e631360d1d1be8b wd=2 >
<Event dir=True mask=0x40000010 maskname=IN_CLOSE_NOWRITE|IN_ISDIR name=21e87816d29701a6a5028632578e631360d1d1be8b path=/tmp/python-languageserver-cancellation pathname=/tmp/python-languageserver-cancellation/21e87816d29701a6a5028632578e631360d1d1be8b wd=2 >
"""
notifier.stop()