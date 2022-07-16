arg1 = /home/baadalvm/NSS/Lab1/assignment-1/INPUT/ciphertext-1.txt
arg2 =/home/baadalvm/NSS/Lab1/assignment-1/INPUT/ciphertext-2.txt
arg3 =
arg4 =

all: extract decrypt
all1: extract1 decrypt1
all2: extract2 decrypt2

decrypt:
	python decryptText.py

extract:
	python extractKey.py

decrypt1:
	python decryptText.py $(arg1)

extract1:
	python extractKey.py $(arg1)

decrypt2:
	python decryptText.py $(arg2)

extract2:
	python extractKey.py $(arg2)

clear:
	rm -f ./OUTPUT/*.txt

