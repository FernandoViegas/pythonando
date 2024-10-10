from gtts import gTTS
import pyttsx3


def text_to_audio(texto, arquivo_mp3):
    try:
        # Converte o texto em áudio
        print("Convertendo texto em áudio...")
        tts = gTTS(text=texto, lang='pt', slow=False, tld='com.br')

        # Salva o áudio em um arquivo MP3
        print("Salvando áudio em MP3...")
        tts.save(arquivo_mp3)

        print(f"Áudio salvo como: {arquivo_mp3}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def text_to_audio_pyttsx3(texto, arquivo_mp3):
    engine = pyttsx3.init()

    # Configurar propriedades
    # engine.setProperty('rate', 150)  # Velocidade (palavras por minuto)
    # engine.setProperty('volume', 1.0)  # Volume (0.0 a 1.0)

    # Selecionar voz (dependendo das vozes instaladas no seu sistema)
    voices = engine.getProperty('voices')
    voz_pt = None

    for voice in voices:
        # Verifique se 'pt' está presente em qualquer uma das linguagens da voz
        if any('pt-br' in lang for lang in voice.languages):
            voz_pt = voice.id
            break

    if voz_pt:
        engine.setProperty('voice', voz_pt)
    else:
        print("Nenhuma voz em português encontrada. Usando a voz padrão.")

    # Salvar o áudio
    engine.save_to_file(texto, arquivo_mp3)
    engine.runAndWait()
    print(f"Áudio salvo como: {arquivo_mp3}")

if __name__ == "__main__":
    texto = input("Digite o texto para converter em áudio: ")
    # texto = """
    #     Transforme seu texto em áudio com Python!
    # """
    arquivo_mp3 = "audio.mp3"  # Nome do arquivo MP3
    text_to_audio(texto, arquivo_mp3) # Converte texto em áudio voz do Google
    # text_to_audio_pyttsx3(texto, arquivo_mp3) # Converte texto em áudio voz do sistema
