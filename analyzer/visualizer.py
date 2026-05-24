import matplotlib.pyplot as plt


def plot_top_endpoints(endpoint_count):
    endpoints = list(endpoint_count.keys())
    counts = list(endpoint_count.values())

    plt.figure()
    plt.bar(endpoints[:10], counts[:10])
    plt.title("Top Endpoints")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_status_codes(status_count):
    labels = list(status_count.keys())
    values = list(status_count.values())

    plt.figure()
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Status Code Distribution")
    plt.show()