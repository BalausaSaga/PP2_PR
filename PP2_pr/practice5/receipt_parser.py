import re
import json

def parse_receipt(text):
    data = {
        "items": [],
        "total_amount": 0.0,
        "date_time": None,
        "payment_method": None
    }

    datetime_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2})', text)
    if datetime_match:
        data["date_time"] = datetime_match.group(1)

    if "Банковская карта" in text:
        data["payment_method"] = "Card"
    elif "Наличные" in text:
        data["payment_method"] = "Cash"

    item_pattern = re.compile(
        r'(\d+)\.\n(.*?)\n(\d+,\d+)\s*x\s*([\d\s]+,\d+)\n([\d\s]+,\d+)', 
        re.DOTALL
    )

    matches = item_pattern.finditer(text)
    for match in matches:
        def clean_num(s):
            return float(s.replace(' ', '').replace(',', '.'))

        product_name = match.group(2).replace('\n', ' ').strip()
        quantity = clean_num(match.group(3))
        unit_price = clean_num(match.group(4))
        subtotal = clean_num(match.group(5))

        data["items"].append({
            "index": int(match.group(1)),
            "name": product_name,
            "quantity": quantity,
            "unit_price": unit_price,
            "subtotal": subtotal
        })

    total_match = re.search(r'ИТОГО:\s*([\d\s]+,\d+)', text)
    if total_match:
        data["total_amount"] = float(total_match.group(1).replace(' ', '').replace(',', '.'))

    return data

if __name__ == "__main__":
    with open('raw.txt', 'r', encoding='utf-8') as f:
        raw_text = f.read()
    
    parsed_data = parse_receipt(raw_text)
    print(json.dumps(parsed_data, indent=4, ensure_ascii=False))