import pandas as pd

print("Задание 1")
data = {
    "name": list(("Анна", "Борис", "Виктор", "Анна", "Дмитрий", "Елена", "Борис", "Жанна", "Захар", "Ирина")),
    "age": list((25, 34, None, 25, 45, 29, 34, None, 150, 31)),
    "city": list(("Москва", None, "Казань", "Москва", "Сочи", "Москва", "Казань", "Тверь", "Омск", "Уфа")),
    "salary": list((50000, 60000, 55000, 50000, 70000, None, 60000, 52000, 90000, 58000)),
    "experience": list(("3", "5", "2", "3", "10", "7", "5", None, "20", "4"))
}
df = pd.DataFrame(data)
print(df)

print("Задание 2")
print(df.isnull().sum())

print("Задание 3")
df = df.dropna(subset=list(("name", "age")))
print("Осталось строк:", len(df))
print(df)

print("Задание 4")
mean_salary = df["salary"].mean()
print("Средняя зарплата:", mean_salary)
df["salary"] = df["salary"].fillna(mean_salary)
print(df)

print("Задание 5")
print("Дубликатов найдено:", df.duplicated().sum())
df = df.drop_duplicates()
print("Осталось строк:", len(df))
print(df)

print("Задание 6")
mask = df["age"] > 100
print("Выбросы:")
print(df[mask])
median_age = df.loc[~mask, "age"].median()
print("Медиана без выбросов:", median_age)
df.loc[mask, "age"] = median_age
print(df)

print("Задание 7")
df["experience"] = pd.to_numeric(df["experience"], errors="coerce")
df["experience"] = df["experience"].fillna(df["experience"].mean())
df["experience"] = df["experience"].astype(int)
print(df.dtypes)
print(df)

print("Задание 8")
df.to_csv("clean_data.csv", index=False, encoding="utf-8")
print("Файл clean_data.csv сохранён.")
print(df.info())
