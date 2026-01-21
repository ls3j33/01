def find_anomalous_words(text: str) -> list[str]:
    """
    Находит слова, длина которых отличается от средней длины слов в тексте более чем на 2 символа.
 
    :param text: Входная строка.
    :return: Список аномальных слов.
    """
    words = text.strip().split(' ')
    avg_len = sum(len(w) for w in words) / len(words)
    result = []
    for w in words:
        if abs(len(w) - avg_len) > 2:
            result.append(w) 
    return result

#print(find_anomalous_words("Python is great for data science"))