import speedtest
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

def format_speed(bps):
    if bps >= 1_000_000_000:
        return f"{bps / 1_000_000_000:.2f} Gbps"
    elif bps >= 1_000_000:
        return f"{bps / 1_000_000:.2f} Mbps"
    elif bps >= 1_000:
        return f"{bps / 1_000:.2f} Kbps"
    else:
        return f"{bps:.2f} bps"

def process_request():
    try:
        # Cria nova instância para evitar sessão travada
        s = speedtest.Speedtest()

        # Busca servidores e escolhe o melhor
        s.get_servers([])
        s.get_best_server()

        # Executa testes
        s.download()
        s.upload()

        # Coleta resultados
        results = s.results.dict()
        upload_speed = format_speed(results["upload"])
        download_speed = format_speed(results["download"])

        print("Upload:", upload_speed)
        print("Download:", download_speed)

        return upload_speed, download_speed

    except Exception as e:
        print(f"Erro ao processar o speedtest: {e}")
        return None, None

@app.route('/')
def home():
    upload, download = process_request()
    if upload and download:
        return render_template('index.html', upload=upload, download=download)
    else:
        return "Erro ao executar o speed test. Tente novamente."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
