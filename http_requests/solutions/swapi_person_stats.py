import requests

# Task
# Napis skript, ktory zisti, aka je priemerna vyska postavy zo starwars
# a vypise statistiku pohlavia.
# url = 'https://swapi.dev/api/people/'

import requests


class NotFoundException(Exception):
    pass


def get_person_stats(people_url):
    heights = []
    genders = {}
    next_page = people_url
    page_count = 1
    while next_page is not None:
        print(f'On page {page_count}, url={next_page}')
        response = requests.get(next_page)
        if response.status_code == 404:
            raise NotFoundException("Planet not found")

        data = response.json()
        for person in data['results']:
            heights.append(person['height'])
            genders[person['gender']] = genders.get(person['gender'], 0) + 1
        next_page = data['next']
        page_count += 1

    return sum(int(height) for height in heights if height != 'unknown') / len(heights), genders


url = 'https://swapi.dev/api/people/'
print(get_person_stats(url))
