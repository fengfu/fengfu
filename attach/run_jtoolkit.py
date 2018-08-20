# $language = "python"
# $interface = "1.0"

# This automatically generated script may need to be
# edited in order to work correctly.

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.Send("mkdir jtoolkit && cd jtoolkit && wget --no-check-certificate --no-cache https://raw.githubusercontent.com/fengfu/jtoolkit/master/jtoolkit.sh && source jtoolkit.sh" + chr(13))

Main()
