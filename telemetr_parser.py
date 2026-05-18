import os
import requests
import pandas as pd
import time

TELEMETR_API_KEY = os.getenv("TELEMETR_API_KEY")

CATEGORIES = [12, 17, 23] 
MIN_MEMBERS = 3000        
MAX_MEMBERS = 30000       
MIN_ERR = 15              
MAX_PAGES = 2             

# Список возможных вариантов URL эндпоинтов API Telemetr
URL_VARIANTS = [
    "https://api.telemetr.me/v1/channels",
    "https://api.telemetr.me/v1/channels/search",
    "https://api.telemetr.me/v1/public/channels",
    "https://api.telemetr.me/channels"
]

def start_parsing():
    if not TELEMETR_API_KEY:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: API-ключ Telemetr не найден в секретах GitHub!")
        return

    headers = {
        "Authorization": f"Bearer {TELEMETR_API_KEY}",
        "Accept": "application/json"
    }
    
    # 1. Сначала подбираем рабочий эндпоинт
    working_url = None
    print("🔍 Тестируем эндпоинты API Telemetr на доступность...")
    
    test_params = {"category_id": 12, "page": 1, "limit": 1}
    for url in URL_VARIANTS:
        try:
            res = requests.get(url, headers=headers, params=test_params)
            print(f"   Проверка {url} -> Статус: {res.status_code}")
            if res.status_code == 200:
                working_url = url
                print(f"✅ Найдена рабочая точка доступа: {working_url}")
                break
        except Exception as e:
            print(f"   Сбой сети для {url}: {e}")
            
    if not working_url:
        print("❌ ОШИБКА: Ни один из известных адресов API не вернул статус 200.")
        print("Проверьте, не заблокирован ли ваш токен на тарифе 'Старт' для работы с внешним API.")
        return

    # 2. Основной цикл парсинга по рабочему URL
    leads = []
    print("\n🤖 Начинаем сбор данных...")
    
    for cat_id in CATEGORIES:
        print(f"📡 Сканируем категорию ID: {cat_id}...")
        
        for page in range(1, MAX_PAGES + 1):
            params = {
                "category_id": cat_id,
                "participants_from": MIN_MEMBERS,
                "participants_to": MAX_MEMBERS,
                "err_from": MIN_ERR,
                "page": page
            }
            
            try:
                response = requests.get(working_url, headers=headers, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    channels = data.get("results", []) or data.get("data", [])
                    
                    if not channels:
                        break
                        
                    for ch in channels:
                        about = ch.get("about", "") or ch.get("description", "")
                        username = ch.get("username", "N/A")
                        
                        contact = "Проверить вручную"
                        for word in about.split():
                            if "@" in word and not word.lower().endswith("bot") and len(word) > 4:
                                contact = word.strip(".,()![]{} ")
                                break
                        
                        leads.append({
                            "Канал": ch.get("title", ch.get("name", "Без имени")),
                            "Ссылка": f"https://t.me/{username}" if username != "N/A" else "N/A",
                            "Подписчики": ch.get("participants_count", ch.get("subscribers", 0)),
                            "ERR": f"{ch.get('err', 0)}%",
                            "Контакт для связи": contact,
                            "Статус": "Ожидает отправки оффера"
                        })
                    
                    print(f"   Успешно обработана страница {page}")
                    time.sleep(1)
                else:
                    print(f"   ⚠️ Ошибка на странице {page}: Статус {response.status_code}")
                    break
            except Exception as e:
                print(f"   ❌ Сбой: {e}")
                break

    # 3. Сохранение результатов
    if leads:
        df = pd.DataFrame(leads)
        filename = "vpn_leads_telemetr.xlsx"
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"\n🎉 Парсинг успешно завершен! Собрано лидов: {len(leads)}")
        print(f"💾 Файл сохранен как: {filename}")
    else:
        print("\n❌ База пуста.")

if __name__ == "__main__":
    start_parsing()
