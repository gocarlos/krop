import sys

try:
    import sip
    try:
        import PyQt5
    except ImportError:
        print("Could not find Qt5...\n")
        pass

except ImportError:
    _msg = "Please install PyQt4 or PyQt5 first."
    raise RuntimeError(_msg)

sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
