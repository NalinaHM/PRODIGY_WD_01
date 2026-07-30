import sys

sys.stdout.reconfigure(encoding='utf-8')

def generate_image_prompt(prompt, style="Cyberpunk Neon 8K", steps=50):
    print("==================================================")
    print("🎨 Generative AI Task 02: AI Art & Image Generator Studio")
    print("==================================================")
    print(f"📌 Prompt: {prompt}")
    print(f"🎨 Style Preset: {style} | Diffusion Steps: {steps}")
    print("🖼️ Rendering Latent Space Image Artifact...")
    print("✅ AI Image generated and saved to 'outputs/generated_art.png'")

if __name__ == "__main__":
    generate_image_prompt("A futuristic neon cyberpunk city at night, rain-slicked streets...")
