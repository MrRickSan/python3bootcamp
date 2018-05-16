'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''


def find_and_replace(file_name, old_word, new_word):
    with open(file_name, 'r+', encoding='UTF8') as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()


print(find_and_replace('story.txt', 'Alice', 'Richard'))
