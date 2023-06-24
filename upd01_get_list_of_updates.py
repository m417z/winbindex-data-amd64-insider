import time
import requests
import json

import config


def get_builds(arch, min_time=None):
    url = 'https://uupdump.net/json-api/listid.php?sortByDate=1'
    r = requests.get(url)
    r.raise_for_status()

    builds_unfiltered = r.json()['response']['builds']

    def filter_build(build):
        if build['arch'] != arch:
            return False

        if min_time is None:
            return True

        if build['created'] is None or build['created'] < min_time:
            return False

        return True

    builds_filtered = list(filter(filter_build, builds_unfiltered))

    builds = {}
    for build in builds_filtered:
        uuid = build['uuid']
        del build['uuid']
        del build['arch']
        assert uuid not in builds
        builds[uuid] = build

    return {
        'builds': builds,
    }


def main():
    # Limit to builds created in the last x days.
    min_time = int(time.time()) - 60 * 60 * 24 * config.updates_days

    while True:
        try:
            result = get_builds(config.updates_architecture, min_time)
            break
        except requests.exceptions.RequestException as e:
            print(e)

            delay = 10
            print(f'Retrying in {delay} seconds...')
            time.sleep(delay)

    with open(config.out_path.joinpath('updates.json'), 'w') as f:
        json.dump(result, f, indent=4)


if __name__ == '__main__':
    main()
