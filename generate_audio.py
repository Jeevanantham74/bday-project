import wave
import math
import struct
import os

sample_rate = 44100
duration = 80 # seconds so 35s mark has plenty of music!
freqs = [261.63, 293.66, 329.63, 392.00, 440.0, 523.25, 493.88, 392.00]

output_path = os.path.join(os.path.dirname(__file__), 'song.wav')

with wave.open(output_path, 'w') as wav:
    wav.setnchannels(2)
    wav.setsampwidth(2)
    wav.setframerate(sample_rate)
    
    total_samples = sample_rate * duration
    for i in range(total_samples):
        t = i / sample_rate
        # Slow sweet romantic acoustic melody
        chord_idx = int(t / 3) % len(freqs)
        base_f = freqs[chord_idx]
        
        # gentle piano-like bell harmonics
        s = 0.35 * math.sin(2 * math.pi * base_f * t) * math.exp(-(t % 1.5) * 1.8)
        s += 0.20 * math.sin(2 * math.pi * base_f * 1.5 * t) * math.exp(-(t % 1.5) * 2.2)
        s += 0.15 * math.sin(2 * math.pi * base_f * 2.0 * t) * math.exp(-(t % 3.0) * 1.0)
        s += 0.10 * math.sin(2 * math.pi * (base_f * 0.5) * t)
        
        sample = int(s * 32767 * 0.5)
        sample = max(-32768, min(32767, sample))
        data = struct.pack('<hh', sample, sample)
        wav.writeframesraw(data)

print(f"Generated romantic audio at: {output_path}")
