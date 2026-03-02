import re
import json

def parse_receipt(file_content):
    data = {
        "items": [],
        "total_amount": 0.0,
        "date_time": "",
        "payment_method": ""
    }

    item_pattern = re.compile(r"\d+\.\n(.*?)\n[\d, ]+ x [\d, ]+\n([\d, ]+)", re.DOTALL)
    items = item_pattern.findall(file_content)
    
    for item_name, price_str in items:
        clean_name = item_name.strip().replace('\n', ' ')
        clean_price = float(price_str.replace(' ', '').replace(',', '.'))
        data["items"].append({
            "product": clean_name,
            "price": clean_price
        })

    # Общая сумма
    total_match = re.search(r"Total:\n([\d, ]+)", file_content)
    if total_match:
        data["total_amount"] = float(total_match.group(1).replace(' ', '').replace(',', '.'))

    # Дата и время
    dt_match = re.search(r"Time: ([\d.]+ [\d:]+)", file_content)
    if dt_match:
        data["date_time"] = dt_match.group(1)

    # Метод оплаты
    if "bank card" in file_content:
        data["payment_method"] = "Bank Card"
    else:
        data["payment_method"] = "Cash"

    return data

# Чтение файла и запуск
try:
    with open('raw.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    result = parse_receipt(content)
    
    # Структурированный вывод (JSON)
    print(json.dumps(result, indent=4, ensure_ascii=False))

except FileNotFoundError:
    print("Error: raw.txt is not found.")