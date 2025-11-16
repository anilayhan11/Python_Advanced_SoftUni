n: int = int(input())
invitations: set = set()
attendees: set = set()

for _ in range(n):
    invitations.add(input())

while True:
    attendee = input()
    if attendee == 'END':
        break
    attendees.add(attendee)

not_attended = sorted(invitations.difference(attendees))
print(len(not_attended))
print(*not_attended, sep='\n')
