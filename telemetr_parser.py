import os
import requests
import pandas as pd
import time
import re

# Нам больше не нужны токены и куки! Скрипт парсит открытый веб-каталог.
# Список популярных категорий Telemetr (можно менять ID)
CATEGORIES = [12, 17, 23] # 12 - ИТ, 17 - Маркетинг, 23 - Бизнес

def start_parsing():
    # Имитируем обычный браузер, чтобы сайт отдавал нам контент
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    leads = []
    print("🤖 Запуск автономного веб-скрейпера каналов Telemetr...")
    
    for cat_id in CATEGORIES:
        print(f"📡 Сканируем открытую категорию ID: {cat_id}...")
        
        # Запрашиваем публичную веб-страницу категории
        url = f"https://telemetr.me/channels/cat/{cat_id}/"
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                html_content = response.text
                
                # Ищем блоки каналов с помощью регулярных выражений (чтобы не ставить дополнительные тяжелые библиотеки)
                # Находим ссылки на каналы вида /channels/12345-username/
                channel_blocks = re.findall(r'href="/channels/(\d+)-([^/"]+)/"', html_content)
                
                if not channel_blocks:
                    print(f"   ⚠️ На открытой странице категории {cat_id} не найдено каналов. Возможно, изменилась верстка.")
                    continue
                
                # Убираем дубликаты каналов на странице
                unique_channels = list(set(channel_blocks))
                print(f"   Найдено {len(unique_channels)} потенциальных каналов...")
                
                for ch_id, ch_username in unique_channels[:15]: # Берем первые 15 каналов для теста лимитов
                    # Формируем прямую ссылку на Телеграм-канал
                    tg_link = f"https://t.me/{ch_username}"
                    
                    # Для поиска контактов админа заглядываем на открытую страницу описания канала
                    ch_url = f"https://telemetr.me/channels/{ch_id}-{ch_username}/"
                    contact = "Проверить в описании"
                    
                    try:
                        ch_res = requests.get(ch_url, headers=headers, timeout=5)
                        if ch_res.status_code == 200:
                            # Ищем юзернеймы админов через @ в блоке описания
                            description = ch_res.text
                            found_contacts = re.findall(r'@[a-zA-Z0-9___]{4,32}', description)
                            # Отсекаем ботов, если они нашлись
                            valid_contacts = [c for c in found_contacts if not c.lower().endswith('bot')]
                            if valid_contacts:
                                contact = valid_contacts[0]
                    except:
                        pass
                        
                    leads.append({
                        "Канал": ch_username,
                        "Ссылка": tg_link,
                        "Контакт для связи": contact,
                        "Статус": "Ожидает отправки оффера"
                    })
                    time.sleep(1) # Небольшая пауза, чтобы сайт не забанил по IP
                    
                print(f"   Категория {cat_id} успешно обработана.")
            else:
                print(f"   ⚠️ Не удалось открыть страницу категории. Статус: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Ошибка запроса: {e}")
            continue

    # Сохраняем в файл
    if leads:
        df = pd.DataFrame(leads)
        filename = "vpn_leads_telemetr.xlsx"
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"\n🎉 Сбор успешно окончен! Создано лидов: {len(leads)}")
        print(f"💾 Файл сохранен на GitHub как: {filename}")
    else:
        print("\n❌ Не удалось собрать данные. Сайт заблокировал запрос или изменил структуру страниц.")

if __name__ == "__main__":
    start_parsing()
