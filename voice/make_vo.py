"""Make one voiceover line in an approved Auxilium voice.
Usage: python3 voice/make_vo.py --voice 13 --text "Line to say." --out line.wav [--work /home/claude/voicework]
Voice numbers are the ones Rob picked (see voices.md). Output is a WAV file."""
import argparse, os
VOICES = {
 1:("k","bm_george"), 2:("k","bm_lewis"), 3:("k","bm_daniel"), 4:("k","bm_fable"),
 5:("k","bf_emma"), 6:("k","bf_isabella"), 7:("k","bf_alice"), 8:("k","bf_lily"),
 9:("k","bm_george+bm_lewis"), 10:("k","bm_daniel+bm_fable"), 11:("k","bm_george+bm_daniel"), 12:("k","bf_emma+bf_isabella"),
 13:("v","p292"), 14:("v","p304"), 15:("v","p293"), 16:("v","p351"),
}
a=argparse.ArgumentParser(); a.add_argument("--voice",type=int,required=True); a.add_argument("--text",required=True)
a.add_argument("--out",required=True); a.add_argument("--work",default="/home/claude/voicework"); a.add_argument("--speed",type=float,default=1.05)
x=a.parse_args(); kind,name=VOICES[x.voice]; W=x.work
if kind=="k":
    import soundfile as sf
    from kokoro_onnx import Kokoro
    k=Kokoro(f"{W}/kokoro-v1.0.onnx",f"{W}/voices-v1.0.bin")
    parts=name.split("+")
    v=parts[0] if len(parts)==1 else sum(k.get_voice_style(p) for p in parts)/len(parts)
    s,sr=k.create(x.text,voice=v,speed=x.speed,lang="en-gb"); sf.write(x.out,s,sr)
else:
    from TTS.api import TTS
    d=f"{W}/vctk/tts_models--en--vctk--vits"
    TTS(model_path=f"{d}/model_file.pth",config_path=f"{d}/config.json").tts_to_file(text=x.text,speaker=name,file_path=x.out)
print("ok",x.voice,x.out)
