


def value_histogram(data, column, title):
    plt.hist(data[column], bins=10, edgecolor='black')

    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Count")

    plt.show()


file = "students_mental_health_survey.csv"
df = pd.read_csv(file)
print(df)
