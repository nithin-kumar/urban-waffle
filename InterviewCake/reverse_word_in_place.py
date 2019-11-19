def reverse_words(message):
    print message
    message_list = list(message)
    # Decode the message by reversing the words
    reverse_chars(message_list, 0, len(message_list) - 1)
    start = 0
    i = 0
    while i <= len(message_list):
        if i == len(message_list) or message_list[i] == ' ' or message_list[i] == '!':
            reverse_chars(message_list, start, i - 1)
            start = i + 1
        i += 1
    print ''.join(message_list)
    return ''.join(message_list)

def reverse_chars(word, start, end):
    while start < end:
        if word[end] == '!':

            end -= 1
        word[start], word[end] = word[end], word[start]
        start += 1
        end -= 1

if __name__ == '__main__':
    reverse_words('yummy is cake bundt chocolate!')