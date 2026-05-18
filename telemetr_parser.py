import requests
import pandas as pd
import time
import re

# Список категорий TGStat: tech - ИТ, marketing - Маркетинг, business - Бизнес
CATEGORIES = ["tech", "marketing", "business"]

def start_parsing():
    # Эмулируем обычный чистый браузер
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    leads = []
    print("🤖 Запуск автономного парсера каналов через каталог TGStat...")
    
    for category in CATEGORIES:
        print(f"📡 Сканируем открытую категорию: {category}...")
        
        # Публичный URL рейтинга каналов в РФ/СНГ по выбранной теме
        url = f"https://tgstat.ru/ru/research/{category}/channels?sort=members"
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                html_content = response.text
                
                # Извлекаем названия каналов и их юзернеймы из ссылок вида href="https://tgstat.ru/channel/@username"
                raw_channels = re.findall(r'href="https://tgstat\.ru/channel/(@[a-zA-Z0-9___]{4,32})"', html_content)
                
                # Извлекаем читаемые имена каналов для таблицы
                titles = re.findall(r'font-16 text-dark text-truncate b-600[^>]*>\s*([^<]+)', html_content)
                
                if not raw_channels:
                    print(f"   ⚠️ На странице категории {category} не найдено каналов.")
                    continue
                
                # Очищаем от дублей
                unique_usernames = []
                for username in raw_channels:
                    if username not in unique_usernames:
                        unique_usernames.append(username)
                
                print(f"   Найдено {len(unique_usernames)} живых каналов. Собираем контакты...")
                
                for idx, username in enumerate(unique_usernames[:15]): # Берем ТОП-15 из каждой категории
                    clean_username = username.replace("@", "")
                    tg_link = f"https://t.me/{clean_username}"
                    
                    # Пытаемся вытянуть имя канала, если массивы совпали, иначе берем юзернейм
                    channel_title = titles[idx].strip() if idx < len(titles) else clean_username
                    
                    # Переходим на страницу канала на самом TGStat, чтобы забрать описание и контакты админа
                    info_url = f"https://tgstat.ru/channel/@{clean_username}"
                    contact = "Проверить описание"
                    
                    try:
                        info_res = requests.get(info_url, headers=headers, timeout=5)
                        if info_res.status_code == 200:
                            # Ищем упоминания админов через @ в блоке описания канала
                            desc_text = info_res.text
                            # Находим все @username, исключая сам юзернейм канала и ботов
                            all_mentions = re.findall(r'@[a-zA-Z0-9___]{4,32}', desc_text)
                            valid_contacts = [m for m in all_mentions if m.lower() != username.lower() and not m.lower().endswith('bot')]
                            
                            if valid_contacts:
                                contact = valid_contacts[0]
                    except:
                        pass
                    
                    leads.append({
                        "Канал": channel_title,
                        "Ссылка": tg_link,
                        "Контакт для связи": contact,
                        "Статус": "Ожидает отправки оффера"
                    })
                    time.sleep(1) # Защита от лимитов
                    
                print(f"   Категория {category} успешно обработана.")
            else:
                print(f"   ⚠️ Ошибка доступа к каталогу. Статус: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Сбой сети: {e}")
            continue

    # Сохранение результатов в Excel
    if leads:
        df = pd.DataFrame(leads)
        filename = "vpn_leads_telemetr.xlsx" # Оставляем имя файла прежним, чтобы воркфлоу его зацепил
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"\n🎉 Парсинг успешно завершен! Собрано целевых лидов: {len(leads)}")
        print(f"💾 Файл готов к скачиванию в артефактах GitHub.")
    else:
        print("\n❌ База пуста. Проверьте структуру разметки.")

if __name__ == "__main__":
    start_parsing()
