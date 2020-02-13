def copy():
    with open("story.txt", "r+") as file:
        file.seek(0)
        text = file.read()
    with open("margot_story_copy2.txt", "w") as newfile:
            newfile.write(text)

copy()
