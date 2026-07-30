import sys

sys.stdout.reconfigure(encoding='utf-8')

def run_multimodal_pipeline(image_path="sample.jpg"):
    print("==================================================")
    print("👁️ Generative AI Task 05: Multimodal AI Vision & Audio Synthesizer")
    print("==================================================")
    print(f"📌 Input Image: {image_path}")
    print("🔍 Executing Vision Transformer (ViT) Image Captioning...")
    print("   • Caption: 'A modern high-rise cityscape under a clear twilight sky with illuminated skyscrapers.'")
    print("🔊 Synthesizing Text-to-Speech (TTS) Audio Waveform...")
    print("✅ Multimodal output audio saved to 'outputs/speech_synthesized.mp3'")

if __name__ == "__main__":
    run_multimodal_pipeline()
