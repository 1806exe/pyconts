import matplotlib.pyplot as plt

def plot_words(word_counts, n=10):
    """plot a bar charts for word counts"""
    top_n_words = word_counts.most_common(n)
    word, count = zip(*word_counts)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), label=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    return fig