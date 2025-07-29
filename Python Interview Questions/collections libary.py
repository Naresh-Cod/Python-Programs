from collections import deque

def word_ladder(start, end, word_list):
    word_set = set(word_list)
    if end not in word_set:
        return 0  # No possible transformation

    queue = deque()
    queue.append((start, 1))  # (current_word, steps_taken)
    visited = set()

    while queue:
        current_word, steps = queue.popleft()

        if current_word == end:
            return steps

        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = current_word[:i] + c + current_word[i+1:]

                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))

    return 0  # If no transformation is possible
