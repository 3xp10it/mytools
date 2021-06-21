#本程序用于获取内存模块基址,需要安装frida
#eg.python3 get_base_address.py qq.exe
from __future__ import print_function
import frida
import sys

def on_message(message, data):
    print("[%s] => %s" % (message, data))

def main(target_module):
    session = frida.attach(target_module)

    script = session.create_script("""

    // Find base address of current imported jvm.dll by main process fledge.exe
    var baseAddr = Module.findBaseAddress('%s');
    console.log('%s baseAddr: ' + baseAddr);
""" % (target_module,target_module))
    script.on('message', on_message)
    script.load()
    print("[!] Ctrl+D on UNIX, Ctrl+Z on Windows/cmd.exe to detach from instrumented program.\n\n")
    sys.stdin.read()
    session.detach()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <module name>" % __file__)
        sys.exit(1)


    target_module = sys.argv[1]
    main(target_module)
