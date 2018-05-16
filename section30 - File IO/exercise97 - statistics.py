'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''


def statistics(file_name):
    with open(file_name, encoding='UTF8') as file:
        lines = file.readlines()

    return {
            'lines': len(lines),
            'words': sum(len(line.split(" ")) for line in lines),
            'characters': sum(len(line) for line in lines)
    }


print(statistics('story.txt'))
