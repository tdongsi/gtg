
from collections import deque, Counter, namedtuple

Row = namedtuple('Row', ['host_id', 'listing_id', 'score', 'city', 'index'])


def parse_results(results):
    """ Parse list of strings into list of structured data.

    :param results: List of results as CSV.
    :return:
    data: List of results as tokenized strings
    unique_host: Map of unique IDs to their ocurrences
    """

    data = []

    for idx, e in enumerate(results):
        host_id, listing_id, score, city = e.split(",")
        data.append(Row(host_id, listing_id, score, city, idx))

    # Keeping track of unique host ID
    unique_host = Counter([e.host_id for e in data])

    return data, unique_host


def print_data(current):
    print("############")
    for e in current:
        print(e)
    print("############")
    pass


def paginate(num, results):

    # corner cases
    if not results or num <= 0:
        return []

    data, hostid_set = parse_results(results)

    current = deque(data)
    next = deque()
    output = []

    while current:
        count = 0
        set_page = set(hostid_set.keys())  # Current valid host IDs

        print_data(current)
        print(set_page)

        while current and count < num and set_page:
            e = current.popleft()
            if e.host_id in set_page:
                set_page.remove(e[0])

                # Update Counter hostid_set for more efficient set_page.
                sub = Counter({e.host_id: 1})
                hostid_set -= sub

                output.append(results[e.index])
                count += 1
            else:
                # Put to the next deque
                next.append(e)

        # Move the rest in current to next
        next.extend(current)
        # If unique hosts is exhausted before
        while next and count < num:
            e = next.popleft()

            # Update Counter hostid_set for more efficient set_page
            sub = Counter({e.host_id: 1})
            hostid_set -= sub

            output.append(results[e.index])
            count += 1

        if count == num:
            output.append("")

        current = next
        next = deque()

    return output


