absallergies = ['celery', 'cherry', 'avocado', 'carrot', 'green bean', 'edamame', 'bell pepper', 'pea', 'snap pea', 'apple', 'blackberry']
possallergies = ['peach', 'plum', 'nectarine', 'tomato', 'apricot', 'almond', 'walnut', 'hazelnut', 'pistachio']
allergy = input("Input food (singular):\n").lower()
if allergy in absallergies:
    print('You are allergic to ' + allergy)
elif allergy in possallergies:
    print(allergy + ' is labeled as a possible allergy.')
    posstoabs = input('Would you like to move ' + allergy + " to an absolute allergy? [y/n}")
    if posstoabs == 'y':
        possallergies.remove(allergy)
        absallergies.append(allergy)
    elif posstoabs == 'n':
        print(allergy + ' will remain as a possible allergy.')
    else:
        print('Error: User Misspelling')
else:
    print(allergy + ' is not found in any list.')
    newallergy = input('Would you like to put ' + allergy + ' in the possible allergy list, the absolute allergy list, or in neither? [p/a/n')
    if newallergy == 'p':
        possallergies.append(allergy)
    elif newallergy == 'a':
        absallergies.append(allergy)
    elif newallergy == 'n':
        print('')
    else:
        print('Error: User Misspelling')
print('New Absolute Allergy List: ' + str(absallergies))
print('New Possible Allergy List: ' + str(possallergies))
f = open('allergies.rtf', 'w')
f.write(absallergies)
f.write(possallergies)