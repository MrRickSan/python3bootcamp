'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''


def copy_and_reverse(file_name, new_file_name):
    with open(file_name, encoding='UTF8') as file:
        text = file.read()

    with open(new_file_name, "w", encoding='UTF8') as new_file:
        new_file.write(text[::-1])


copy_and_reverse('story.txt', 'alice_reversed.txt')
