#! /usr/bin/python3

import opuslib
import wave
import numpy as np
import struct

if __name__ == '__main__':
	pcm = wave.open("piano2.wav")

	print('channels', pcm.getnchannels())
	print('sample width', pcm.getsampwidth())
	print('framerate', pcm.getframerate())
	print('frame count', pcm.getnframes())
	print('compression type', pcm.getcomptype())
	print('compression name', pcm.getcompname())

	pcm = pcm.readframes(2880)
	print(len(pcm))

	wave_out = wave.open('wav_out1.wav', 'w')
	wave_out.setnchannels(2)
	wave_out.setsampwidth(2)
	wave_out.setframerate(48000)
	wave_out.writeframes(pcm)
	wave_out.close()

#framesize is per channel samples, but max is 60ms frame, ie 2880
# not particularly good for storage, since we need to break it up into
# many frames

	encoder = opuslib.Encoder(48000, 2, opuslib.APPLICATION_AUDIO)
	opus_encode = encoder.encode(pcm_data = pcm,
	                             frame_size = 2880)
	print(len(opus_encode))

	decoder = opuslib.Decoder(48000, 2)	
	opus_decode = decoder.decode(opus_data = opus_encode, 
	                             frame_size = 2880)
	print(len(opus_decode))

	#raw = struct.unpack('h' * (len(opus_decode)//2), opus_decode)
	#raw = raw[0::2]
	#print(len(raw))

	out = wave.open('wav_out2.wav', 'w')
	out.setnchannels(2)
	out.setsampwidth(2)
	out.setframerate(48000)
	out.writeframes(opus_decode)
	out.close()

