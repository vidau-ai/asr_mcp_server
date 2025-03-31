#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :asr_server.py
# @Time      :3/31/25 8:34 PM
# @Author    :Aliang

import sys
import os
import logging
import subprocess
import tempfile
from typing import List
import whisper
from whisper.utils import get_writer
import uuid
from mcp.server.fastmcp import FastMCP
from pathlib import Path

# Disable ALL logging
logging.disable(logging.CRITICAL)
logging.getLogger().setLevel(logging.CRITICAL)
logging.captureWarnings(True)

# Initialize components
mcp = FastMCP("whisper-asr")
whisper_model = whisper.load_model("large-v3")


def _play_audio(path: Path):
    """Silent audio playback"""
    try:
        if sys.platform == "win32":
            subprocess.call(["start", str(path)], shell=True)
        elif sys.platform == "darwin":
            subprocess.call(["afplay", str(path)])
        else:
            subprocess.call(["aplay", str(path)])
    except:
        pass


@mcp.tool()
async def audio_to_text(
        audio_path: str,
        save_path: str = None,
) -> List[dict]:
    results = []

    if save_path:
        (save_path := Path(save_path)).mkdir(parents=True, exist_ok=True)

    try:
        result = whisper_model.transcribe(audio_path, language="en", word_timestamps=True)
    except:
        raise RuntimeError("TTS failed")

    with tempfile.TemporaryDirectory() as tmp_dir:
            if save_path:
                id = uuid.uuid4()
                srt_writer = get_writer("srt", tmp_dir)
                srt_writer(result, id + ".srt", {"max_line_count": 1, "max_line_width": 50})

            results.append({'srt_text': result["text"],
                            'srt_path': os.path.join(tmp_dir, id + ".srt")})

    return results


if __name__ == "__main__":
    try:
        mcp.run(transport=os.getenv("MCP_TRANSPORT", "stdio"))
    except:
        sys.exit(1)