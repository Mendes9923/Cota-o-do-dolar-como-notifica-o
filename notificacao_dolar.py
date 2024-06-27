import schedule
import time
import requests
from plyer import notification

def get_dollar_rate():
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        brl_rate = data['rates']['BRL']
        return brl_rate
    except Exception as e:
        print(f"Erro ao obter a cotação do dólar: {e}")
        return None

def notify_dollar_rate():
    rate = get_dollar_rate()
    if rate:
        notification.notify(
            title='Cotação do Dólar',
            message=f'A cotação do dólar é R$ {rate:.2f}',
            timeout=10
        )

# Agende a tarefa para ser executada a cada 10 minutos
schedule.every(10).minutes.do(notify_dollar_rate)

print("Iniciando a notificação do dólar a cada 10 minutos...")

# Loop principal para executar a tarefa agendada
while True:
    schedule.run_pending()
    time.sleep(1)
