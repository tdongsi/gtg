
from collections import deque, Counter


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
        # TODO: Use namedtuple for better code
        data.append((host_id, listing_id, score, city, idx))

    # Keeping track of unique host ID
    unique_host = Counter([e[0] for e in data])

    return data, unique_host


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
        while current and count < num and set_page:
            e = current.popleft()
            if e[0] in set_page:
                set_page.remove(e[0])

                # Update Counter hostid_set for more efficient set_page.
                sub = Counter()
                sub[e[0]] = 1
                hostid_set -= sub

                output.append(results[e[-1]])
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
            sub = Counter()
            sub[e[0]] = 1
            hostid_set -= sub

            output.append(results[e[-1]])
            count += 1

        output.append("")

        current = next
        next = deque()

    return output


