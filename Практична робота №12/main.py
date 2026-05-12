import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def load_audio():
    # Завантажує аудіофайл та обробляє виключення
    filepath = input("Введіть шлях до аудіофайлу (наприклад, test.wav): ").strip()
    
    try:
        print("Завантаження та підготовка даних...")
        y, sr = librosa.load(filepath, sr=None)
        duration = librosa.get_duration(y=y, sr=sr)
        print(f"Успішно! Завантажено файл. Тривалість: {duration:.2f} сек. Частота: {sr} Гц.")
        return y, sr, filepath
    except FileNotFoundError:
        print("Помилка: Файл за вказаним шляхом не знайдено!")
    except Exception as e:
        print(f"Помилка обробки файлу. Деталі: {e}")
    
    return None, None, None

def plot_spectrogram(y, sr):
    # Будує спектрограму та зберігає її у PNG
    print("Обчислення спектрограми...")
    plt.figure(figsize=(10, 4))
    
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
    
    plt.colorbar(format='%+2.0f dB')
    plt.title('Спектрограма аудіосигналу')
    plt.tight_layout()
    
    filename = "spectrogram_output.png"
    plt.savefig(filename)
    plt.close()
    print(f"Графік успішно збережено у файл: {filename}")

def analyze_rhythm(y, sr):
    # Аналізує ритм (темп у BPM) та зберігає звіт у текстовий файл
    print("Аналіз ритму та бітів...")
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    
    tempo_val = tempo[0] if isinstance(tempo, np.ndarray) else tempo
    
    report = (
        "=== Звіт аналізу ритму ===\n"
        f"Оціночний темп: {tempo_val:.2f} BPM (ударів на хвилину)\n"
        f"Загальна кількість знайдених ударів: {len(beats)}\n"
        "==========================\n"
    )
    
    print("\n" + report)
    
    filename = "rhythm_report.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report)
        print(f"Текстовий звіт збережено у файл: {filename}")
    except IOError:
        print("Помилка запису у файл.")

def analyze_tonality(y, sr):
    # Будує хромаграму для аналізу тональності і зберігає у PNG
    print("Обчислення хромаграми...")
    plt.figure(figsize=(10, 4))
    
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
    
    plt.colorbar()
    plt.title('Хромаграма (розподіл енергії по нотах)')
    plt.tight_layout()
    
    filename = "chromagram_output.png"
    plt.savefig(filename)
    plt.close()
    print(f"Графік успішно збережено у файл: {filename}")

def main():
    # Головна функція програми (меню)
    print("="*40)
    print(" Аудіо-аналізатор на базі Python (Librosa)")
    print("="*40)
    
    y, sr, filepath = None, None, None
    
    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1. Завантажити аудіофайл (WAV)")
        print("2. Побудувати спектрограму (PNG)")
        print("3. Проаналізувати ритм/темп (TXT)")
        print("4. Проаналізувати тональність (PNG)")
        print("0. Вийти з програми")
        
        choice = input("Оберіть дію (0-4): ").strip()
        
        if choice == '1':
            y, sr, filepath = load_audio()
        elif choice in ['2', '3', '4']:
            if y is None:
                print("Увага: Спочатку завантажте аудіофайл!")
                continue
            
            if choice == '2':
                plot_spectrogram(y, sr)
            elif choice == '3':
                analyze_rhythm(y, sr)
            elif choice == '4':
                analyze_tonality(y, sr)
        elif choice == '0':
            print("Дякую за використання! Програму завершено.")
            break
        else:
            print("Некоректний ввід. Будь ласка, введіть число від 0 до 4.")

if __name__ == "__main__":
    main()