import os
import requests
import pandas as pd
import time

# Получаем защищенный токен из секретов GitHub Actions
TELEMETR_API_KEY = os.getenv("TELEMETR_API_KEY")

# Настройки фильтрации каналов
CATEGORIES = [12, 17, 23] # 12 - ИТ, 17 - Маркетинг, 23 - Бизнес
MIN_MEMBERS = 3000        # От 3к подписчиков
MAX_MEMBERS = 30000       # До 30к подписчиков
MIN_ERR = 15              # ERR от 15% (защита от накруток)
MAX_PAGES = 3             # Сколько страниц парсить в каждой категории

def start_parsing():
    if not TELEMETR_API_KEY:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: API-ключ Telemetr не найден в секретах GitHub!")
        return

    headers = {
        "Authorization": f"Bearer {TELEMETR_API_KEY}",
        "Accept": "application/json"
    }
    
    leads = []
    print("🤖 Запуск поиска партнеров для VPN сервиса на GitHub...")
    
    for cat_id in CATEGORIES:
        print(f"📡 Сканируем категорию ID: {cat_id}...")
        
        for page in range(1, MAX_PAGES + 1):
            # ИСПРАВЛЕНО: Изменен URL эндпоинта в соответствии с актуальным API (убран конечный слэш)
            url = "https://api.telemetr.me/v1/channels"
            params = {
                "category_id": cat_id,
                "participants_from": MIN_MEMBERS,
                "participants_to": MAX_MEMBERS,
                "err_from": MIN_ERR,
                "page": page
            }
            
            try:
                response = requests.get(url, headers=headers, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    channels = data.get("results", [])
                    
                    if not channels:
                        print(f"   На странице {page} нет результатов.")
                        break
                        
                    for ch in channels:
                        about = ch.get("about", "")
                        username = ch.get("username", "N/A")
                        
                        contact = "Проверить вручную"
                        for word in about.split():
                            if "@" in word and not word.lower().endswith("bot") and len(word) > 4:
                                contact = word.strip(".,()![]{} ")
                                break
                        
                        leads.append({
                            "Канал": ch.get("title", "Без имени"),
                            "Ссылка": f"https://t.me/{username}" if username != "N/A" else "N/A",
                            "Подписчики": ch.get("participants_count", 0),
                            "ERR": f"{ch.get('err', 0)}%",
                            "Контакт для связи": contact,
                            "Статус": "Ожидает отправки оффера"
                        })
                    
                    print(f"   Успешно обработана страница {page}")
                    time.sleep(1)
                else:
                    print(f"   ⚠️ Ошибка API Telemetr (Статус {response.status_code})")
                    # Выводим подсказку от сервера, если она есть в теле ответа
                    try:
                        print(f"   📝 Ответ сервера: {response.text}")
                    except:
                        pass
                    break
            except Exception as e:
                print(f"   ❌ Сбой сети: {e}")
                break

    # Формируем итоговую таблицу
    if leads:
        df = pd.DataFrame(leads)
        filename = "vpn_leads_telemetr.xlsx"
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"\n🎉 Парсинг успешно завершен! Собрано лидов: {len(leads)}")
        print(f"💾 Файл сохранен как: {filename}")
    else:
        print("\n❌ База пуста. Если статус был 404/403, проверьте эндпоинт или ограничения тарифа.")

if __name__ == "__main__":
    start_parsing()
