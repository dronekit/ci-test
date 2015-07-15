def win_get_core():
    try:
        import winappdbg
        return int(winappdbg.win32.kernel32.GetCurrentProcessorNumber())
    except:
        return 0

print('what core am i?', win_get_core());

import sys
sys.exit(45)
