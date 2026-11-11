import pandas as pd
data = {
    "student": ["Alice", "Bob", "Charlie", "Diana", "Eve",
                 "Frank", "Grace", "Henry", "Iris", "Jack"],
    "course": ["Python", "Python", "SQL", "SQL", "Python",
               "SQL", "Python", "SQL", "Python", "SQL"],
    "score": [92, 78, 85, 91, 88, 72, 95, 68, 84, 90],
    "hours_studied": [20, 12, 18, 22, 15, 8, 25, 10, 16, 19],
    "passed": [True, True, True, True, True, False, True, False, True, True],
}

df = pd.DataFrame(data)

print(df["course"].value_counts())

print(df.groupby("course")["score"].mean())

print(df.nlargest(3, "score")[["student", "score"]])

print(df.groupby("passed")["hours_studied"].mean())

df["grade"]= pd.cut(
  df["score"],
  bins=[0, 69, 79, 89, 100],            labels=["F", "C", "B", "A"]
)

print(pd.crosstab(df["course"], df["grade"]))