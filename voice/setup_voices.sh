#!/usr/bin/env bash
# Sets up the approved Auxilium voiceover voices in a fresh sandbox.
# Usage: bash voice/setup_voices.sh /home/claude/voicework
set -e
W="${1:-/home/claude/voicework}"; mkdir -p "$W"; cd "$W"
command -v espeak-ng >/dev/null || (sudo apt-get update -qq && sudo apt-get install -y -qq espeak-ng) || (apt-get update -qq && apt-get install -y -qq espeak-ng)
pip install -q --break-system-packages kokoro-onnx soundfile coqui-tts torchcodec
B=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
[ -f kokoro-v1.0.onnx ] || curl -sSL -o kokoro-v1.0.onnx $B/kokoro-v1.0.onnx
[ -f voices-v1.0.bin ] || curl -sSL -o voices-v1.0.bin $B/voices-v1.0.bin
if [ ! -f vctk/tts_models--en--vctk--vits/model_file.pth ]; then
  curl -sSL -o vctk.zip https://github.com/coqui-ai/TTS/releases/download/v0.6.1_models/tts_models--en--vctk--vits.zip
  mkdir -p vctk && (cd vctk && unzip -oq ../vctk.zip)
fi
python3 - "$W" <<'PY'
import json,sys,os
d=os.path.join(sys.argv[1],"vctk/tts_models--en--vctk--vits")
c=json.load(open(f"{d}/config.json")); p=f"{d}/speaker_ids.json"
c["speakers_file"]=p; c["model_args"]["speakers_file"]=p
json.dump(c,open(f"{d}/config.json","w"))
PY
echo "voices ready in $W"
