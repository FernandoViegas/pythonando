from gtts import gTTS
import os

def text_to_audio(texto, arquivo_mp3):
    try:
        # Converte o texto em áudio
        tts = gTTS(text=texto, lang='pt', slow=False)
        # Salva o áudio em um arquivo MP3
        tts.save(arquivo_mp3)
        print(f"Áudio salvo como: {arquivo_mp3}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    texto = """
        Transforme seu texto em áudio com Python!
    """
    arquivo_mp3 = "audio.mp3"  # Nome do arquivo MP3
    text_to_audio(texto, arquivo_mp3)
