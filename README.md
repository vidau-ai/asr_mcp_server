### ASR MCP Server
A Model Context Protocol (MCP) server that provides ASR(Automatic Speech Recognition) capabilities using the whisper engine. This server exposes TTS functionality through MCP tools, making it easy to integrate speech synthesis into your applications.

### Prerequisites
- Python 3.10 or higher
- uv package manager

### MCP Configuration
```json
{
  "mcpServers": {
    "kokoro-tts": {
      "command": "/YOUR_CONDA_PATH/bin/uv",
      "args": [
        "--directory",
        "/YOUR_PATH/asr_mcp_server",
        "run",
        "asr_server.py"
      ]
    }
  }
}
```

### Related Links
🚀 VidAU.ai – Revolutionize Video Marketing with AI: Create Global Hit Content in 3 Minutes! 🚀
Tired of time-consuming, costly video production?
VidAU.ai redefines creativity with AI, generating multilingual marketing videos instantly – break language barriers and amplify your brand globally!

🔥 Core Features
- Batch AI Video Generation

  - Input product links/descriptions → AI auto-generates scripts + voiceovers, optimized for TikTok/YouTube formats. 10x production efficiency.

  - Virtual Digital Spokesperson: Realistic AI avatars with multi-language accents (EN/JP/ES/etc.) for hyper-localized marketing.

- All-in-One AI Editing Suite

  - Face-swap, translation, subtitling, watermark removal – zero technical barriers for editing.

  - Smart clipping recommendations auto-extract highlights for social media trends.

- Cross-Border E-Commerce Powerhouse

  - Multi-language localization engine boosts ROI by 20%+ for global campaigns.

👉 Visit vidau.ai now – Let AI supercharge your traffic!
https://www.vidau.ai/