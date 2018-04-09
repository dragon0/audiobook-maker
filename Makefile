ESARGS = -s 210 -v en+f2
SOURCES=$(shell ls *.html)
WAVS=$(SOURCES:%.html=%.wav)
URL=

all: $(WAVS)

download: get-files clean-files

get-files:
	-wget -r -p -np -nd $(URL)

clean-files:
	python3 clean.py *.html

clean:
	$(RM) *.wav *.html *.png *.css

%.wav: %.html
	espeak $(ESARGS) -m -f $< -w $@

%.ogg: %.wav
	avconv -i $< -codec libvorbis $@

%.flac: %.wav
	avconv -i $< $@

