import asyncio
import json

LIMIT = 8000  # лимит расходов по категории


async def process_file(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        transactions = json.load(f)

    totals = {}

    for tx in transactions:
        category = tx["category"]
        amount = tx["amount"]

        totals.setdefault(category, 0)
        totals[category] += amount

        await asyncio.sleep(0)

    for category, total in totals.items():
        print(f"Категория: {category}, сумма: {total:.2f}")

        if total > LIMIT:
            print(f"Превышение расходов в категории '{category}'")


if __name__ == "__main__":
    asyncio.run(process_file("transactions_1.json"))
