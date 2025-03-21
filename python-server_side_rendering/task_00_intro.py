import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list)\
       or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    if template == "" or None:
        print("Error: Template don't have to be empty")
        return
    if attendees == "" or None:
        print("Error: Attendees don't have to be empty")
        return

    generated_file = []
    for i, attendee in enumerate(attendees, start=1):
        try:
            template1 = template.replace(
                "{name}",
                str(attendee.get("name", "N/A")))
            template1 = template1.replace(
                "{event_title}",
                str(attendee.get("event_title", "N/A")))
            template1 = template1.replace(
                "{event_date}",
                str(attendee.get("event_date", "N/A")))
            template1 = template1.replace(
                "{event_location}",
                str(attendee.get("event_location", "N/A")))
            if not os.path.exists("output_{}.txt".format(i)):
                with open("output_{}.txt".format(i), "w") as f:
                    f.write(template1)
        except KeyError as e:
            print(f"Keyerror: {e}")
