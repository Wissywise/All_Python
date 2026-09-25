"""def organize_hashtags(hashtags):
    organized = {}
    for hashtag in hashtags:
        first_letter = hashtag[0].lower()
        if first_letter not in organized:
            organized[first_letter] = []
        organized[first_letter].append(hashtag)

    # Sort the hashtags in each category
    for key in organized:
        organized[key].sort()

    return organized"""

def organize_hashtags(hashtags):
    unique_hashtags = set(hashtags)
    sorted_hashtags = sorted(unique_hashtags)
    return sorted_hashtags

hashtags = input("Enter hashtags seperated by spaces: ").split()
organized_hashtags = organize_hashtags(hashtags)
print("\nOrganized Hashtags:")
for tag in organized_hashtags:
    print("#" + tag)

