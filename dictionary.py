voters = {}  # dictionary to track who has voted

def cast_vote(person):
    if voters.get(person, False):
        print(f"{person} has already voted.")
    else:
        voters[person] = True
        print(f"{person} voted successfully!")

# Example usage
cast_vote("Alice")
cast_vote("Bob")
cast_vote("Alice")
