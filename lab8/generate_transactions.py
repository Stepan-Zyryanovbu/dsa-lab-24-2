import asyncio
import json
import random
import sys
from datetime import datetime

CATEGORIES = ["еда", "транспорт", "аренда", "образование"]


async def generate_transactions(count: int):
    buffer = []
    file_index = 1

    for i in range(count):
        transaction = {
            "timestamp": datetime.now().isoformat(),
            "category": random.choice(CATEGORIES),
            "amount": round(random.uniform(100, 5000), 2)
        }

        buffer.append(transaction)

        # имитация асинхронного потока
        await asyncio.sleep(0)

        if len(buffer) == 10:
            filename = f"transactions_{file_index}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(buffer, f, ensure_ascii=False, indent=2)

            print(f"Сохранено 10 транзакций в файл {filename}")

            buffer.clear()
            file_index += 1

    # если остались записи (< 10)
    if buffer:
        filename = f"transactions_{file_index}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(buffer, f, ensure_ascii=False, indent=2)

        print(f"Сохранено {len(buffer)} транзакций в файл {filename}")


if __name__ == "__main__":
    count = int(sys.argv[1])
    asyncio.run(generate_transactions(count))
