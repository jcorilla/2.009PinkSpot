import pysimpledmx
COMport = "/dev/cu.usbserial-ENYXTLPV"
mydmx = pysimpledmx.DMXConnection(COMport)

mydmx.setChannel(2, 0)
mydmx.setChannel(6, 0) # pan coarse
mydmx.setChannel(7, 0) # pan fine
mydmx.render()

bin(6)
'0b110'
>>> bin(65535)
'0b1111111111111111'
>>> num = bin(65535)
>>> numstr = str(num)
>>> numstr
'0b1111111111111111'
>>> numstr[2:15]
'1111111111111'
>>> numstr = "0b123456789abcdefg"
>>> numstr[1:15]
'b123456789abcd'
>>> numbstr[2:18]

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    numbstr[2:18]
NameError: name 'numbstr' is not defined
>>> numstr[2:18]
'123456789abcdefg'
>>> num = bin(6)
>>> num
'0b110'
>>> "{0:16b}".format(num)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    "{0:16b}".format(num)
ValueError: Unknown format code 'b' for object of type 'str'
>>> "{0:16b}".format(0x1234)
'   1001000110100'
>>> num = 10
>>> format(num,'#018b')
'0b0000000000001010'
>>> format(num,'018')
'000000000000000010'
>>> format(num,'016)
       
SyntaxError: EOL while scanning string literal
>>> format(num, '016')
'0000000000000010'
>>> format(num, '016b')
'0000000000001010'
