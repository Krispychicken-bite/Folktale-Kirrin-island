import textwrap


def say(text=""):
    for paragraph in text.split("\n"):
        print(textwrap.fill(paragraph, width=78) if paragraph else "")
    print()


def play():
    inventory = set()
    flags = set()
    room = "beach"
    running = True

    def choose(options):
        for number, label in enumerate(options, 1):
            print(f"  {number}. {label}")

        while True:
            answer = input("\nYour choice: ").strip().lower()

            if answer in ("quit", "q"):
                return "quit"

            if answer in ("inventory", "i"):
                say(
                    "You are carrying: "
                    + (", ".join(sorted(inventory)) if inventory else "nothing yet.")
                )
                continue

            if answer in ("help", "h"):
                say(
                    "Enter a choice number. Explore carefully and revisit places "
                    "after finding new items. Type 'inventory' to check your "
                    "belongings, or 'quit' to leave."
                )
                continue

            if answer.isdigit() and 1 <= int(answer) <= len(options):
                print()
                return int(answer)

            print("Please enter one of the listed numbers.")

    def puzzle(prompt):
        answer = input(prompt).strip().lower()
        print()
        return answer

    say("THE FAMOUS FIVE: THE BELL BENEATH KIRRIN")
    say(
        "An original, unofficial fan-made text adventure.\n"
        "You play as George. Your companions are Julian, Dick, Anne, "
        "and Timmy the dog."
    )
    say(
        "The bell rings just as your boat scrapes onto Kirrin Island.\n"
        "One deep note. Then another.\n"
        "'There isn't a working bell on this island,' you say.\n"
        "Timmy jumps onto the shingle and begins barking at the cliffs. "
        "Far above him, a thin thread of smoke rises through the ruined castle.\n"
        "Julian ties the boat securely. 'Let's find out who's here.'"
    )

    while running:
        if room == "beach":
            say("LANDING BEACH")
            say(
                "Your boat rests above the waterline. Footprints lead towards "
                "the castle, but another set disappears behind a heap of driftwood."
            )
            action = choose([
                "Search the driftwood",
                "Walk to the castle courtyard",
                "Leave the island",
            ])

            if action == 1:
                if "rope" in inventory:
                    say("You have already taken the useful rope.")
                else:
                    inventory.add("rope")
                    say(
                        "Behind the driftwood is a coil of strong rope. "
                        "You sling it over your shoulder."
                    )

            elif action == 2:
                room = "courtyard"

            elif action == 3:
                say(
                    "You push the boat out and leave the island behind. "
                    "The bell rings once more, but its secret remains unsolved.\n"
                    "ENDING: THE UNANSWERED BELL"
                )
                running = False

            elif action == "quit":
                running = False

        elif room == "courtyard":
            say("CASTLE COURTYARD")
            say(
                "Grass grows between the broken stones. A ruined tower stands "
                "to the north, an old storehouse to the east, and a narrow path "
                "winds down towards the cliffs."
            )
            action = choose([
                "Enter the ruined tower",
                "Inspect the old storehouse",
                "Follow the cliff path",
                "Return to the landing beach",
            ])

            if action == 1:
                room = "tower"
            elif action == 2:
                room = "storehouse"
            elif action == 3:
                room = "cliff"
            elif action == 4:
                room = "beach"
            elif action == "quit":
                running = False

        elif room == "tower":
            say("RUINED TOWER")
            say(
                "Anne spots a metal box beneath a fallen stone. Its lid has "
                "a three-digit combination lock and a scratched message:\n"
                "'Six crates. Four bottles in each. Three bottles broken. "
                "Enter the number left, using three digits.'"
            )
            action = choose([
                "Try the combination",
                "Examine the tower window",
                "Return to the courtyard",
            ])

            if action == 1:
                if "tower_box_open" in flags:
                    say("The box is open. There is nothing else inside.")
                elif puzzle("Combination: ") == "021":
                    flags.add("tower_box_open")
                    inventory.add("brass key")
                    inventory.add("signal note")
                    say(
                        "The lock clicks open. Inside are a brass key and a note:\n"
                        "'Transfer after dusk. Two bell strikes mean the "
                        "tunnel is clear. Keep the red ledger dry.'\n"
                        "Dick frowns. 'That sounds rather organised.'"
                    )
                else:
                    say("The lock refuses to move. Dick suggests counting carefully.")

            elif action == 2:
                say(
                    "Through the window you see a concealed cove. A motorboat "
                    "is tied beneath the cliffs. Nobody is aboard."
                )
                flags.add("boat_spotted")

            elif action == 3:
                room = "courtyard"
            elif action == "quit":
                running = False

        elif room == "storehouse":
            say("OLD STOREHOUSE")

            if "storehouse_open" not in flags:
                say(
                    "A heavy padlock secures the door. There are fresh scratches "
                    "around its brass keyhole."
                )
            else:
                say(
                    "Inside are empty crates, muddy boots, and a shelf "
                    "covered with fishing equipment."
                )

            action = choose([
                "Unlock the door",
                "Search inside",
                "Return to the courtyard",
            ])

            if action == 1:
                if "storehouse_open" in flags:
                    say("The door is already unlocked.")
                elif "brass key" in inventory:
                    flags.add("storehouse_open")
                    say("The brass key turns. You ease the door open.")
                else:
                    say("You need a key. Forcing the door would make too much noise.")

            elif action == 2:
                if "storehouse_open" not in flags:
                    say("You cannot search the room while the door is locked.")
                elif "torch" in inventory:
                    say("You have already collected the useful equipment.")
                else:
                    inventory.update({"torch", "tide chart"})
                    say(
                        "You find a working torch and a tide chart. Someone "
                        "has circled today's evening tide.\n"
                        "A pencilled warning reads: 'Lower passage floods first. "
                        "Use the upper ledge.'"
                    )

            elif action == 3:
                room = "courtyard"
            elif action == "quit":
                running = False

        elif room == "cliff":
            say("CLIFF PATH")
            say(
                "The path ends above a sheltered cove. The old wooden steps "
                "have collapsed, leaving a steep drop. A sturdy stone post "
                "stands beside the edge."
            )
            action = choose([
                "Climb down to the cove",
                "Listen towards the cliffs",
                "Return to the courtyard",
            ])

            if action == 1:
                if "rope" not in inventory:
                    say(
                        "'Not without a rope,' Julian says. "
                        "'We need a safe way back up, too.'"
                    )
                else:
                    flags.add("rope_secured")
                    say(
                        "You secure the rope around the post. Everyone climbs "
                        "down carefully, with Timmy supported between you."
                    )
                    room = "cove"

            elif action == 2:
                say(
                    "You hear water slapping against rock—and a faint metallic "
                    "clink from somewhere inside the island."
                )

            elif action == 3:
                room = "courtyard"
            elif action == "quit":
                running = False

        elif room == "cove":
            say("HIDDEN COVE")
            say(
                "The motorboat rocks beside a narrow landing. Behind a curtain "
                "of seaweed, Timmy has found an opening in the cliff."
            )
            action = choose([
                "Inspect the motorboat",
                "Enter the sea tunnel",
                "Climb back to the cliff path",
            ])

            if action == 1:
                if "boat_searched" in flags:
                    say("There is nothing more to find without disturbing the boat.")
                else:
                    flags.add("boat_searched")
                    inventory.add("shipping label")
                    say(
                        "You leave the boat untouched, but pick up a loose "
                        "shipping label from the landing.\n"
                        "'Museum collection: coastal navigation instruments.'\n"
                        "Anne looks towards the tunnel. 'Why bring museum "
                        "instruments here?'"
                    )

            elif action == 2:
                if "torch" not in inventory:
                    say(
                        "Beyond the entrance is complete darkness. "
                        "You decide to find a light before entering."
                    )
                else:
                    room = "tunnel"

            elif action == 3:
                room = "cliff"
            elif action == "quit":
                running = False

        elif room == "tunnel":
            say("SEA TUNNEL")
            say(
                "Your torch reveals a passage splitting around a black pool. "
                "A low walkway runs beside the water. Above it, a narrow stone "
                "ledge leads towards a metal door.\n"
                "A bell hangs from an iron bracket. Its rope runs through "
                "a hole towards the cove."
            )
            action = choose([
                "Take the low walkway",
                "Take the upper ledge",
                "Inspect the bell",
                "Return to the cove",
            ])

            if action == 1:
                if "tide chart" in inventory:
                    say(
                        "You remember the warning on the tide chart. Water is "
                        "already spilling across the lower walkway. You turn back."
                    )
                else:
                    say(
                        "A wave washes over the stones ahead. Julian catches "
                        "your arm before you step into the flooded section. "
                        "You retreat to the junction."
                    )

            elif action == 2:
                if "tide chart" not in inventory:
                    say(
                        "You cannot see where the ledge ends. A better "
                        "understanding of the tides would help you choose safely."
                    )
                else:
                    say(
                        "Following the route marked on the chart, you cross "
                        "the upper ledge and reach the metal door."
                    )
                    room = "vault"

            elif action == 3:
                if "signal note" in inventory:
                    say(
                        "The note explains it: the bell signals whether the "
                        "tunnel is clear. You leave the rope alone."
                    )
                    flags.add("signal_understood")
                else:
                    say(
                        "The bell appears to be a signalling device. "
                        "You leave it alone rather than alert whoever uses it."
                    )

            elif action == 4:
                room = "cove"
            elif action == "quit":
                running = False

        elif room == "vault":
            say("SMUGGLERS' VAULT")

            if "vault_open" not in flags:
                say(
                    "The door has a letter-wheel lock. Someone has scratched "
                    "a reminder beside it:\n"
                    "'Where the boat waits: V O C E'"
                )
            else:
                say(
                    "The open vault contains wrapped instruments and a desk. "
                    "Farther along the passage, voices echo through the rock."
                )

            action = choose([
                "Try the letter lock",
                "Search the vault",
                "Confront the people in the passage",
                "Return to the tunnel",
                "Leave quietly and report what you found",
            ])

            if action == 1:
                if "vault_open" in flags:
                    say("The vault door is already open.")
                elif puzzle("Unscramble the word: ") == "cove":
                    flags.add("vault_open")
                    say("The wheels settle into place. The door swings inward.")
                else:
                    say("The lock stays shut.")

            elif action == 2:
                if "vault_open" not in flags:
                    say("First you need to open the door.")
                elif "red ledger" in inventory:
                    say("You already have the ledger and have recorded the crate marks.")
                else:
                    inventory.update({"red ledger", "crate details"})
                    say(
                        "The red ledger lists stolen navigation instruments, "
                        "boat registrations, and delivery dates. You copy the "
                        "crate markings before taking the ledger.\n"
                        "From the passage comes a man's voice: "
                        "'Bring the boat round. We load tonight.'"
                    )

            elif action == 3:
                say(
                    "You step towards the voices, but Timmy growls. Two shadows "
                    "move across the wall.\n"
                    "'There are better ways to catch them,' Julian whispers, "
                    "drawing everyone back behind the door.\n"
                    "You retreat without being seen."
                )

            elif action == 4:
                room = "tunnel"

            elif action == 5:
                if "red ledger" not in inventory:
                    say(
                        "You retrace your steps, climb out of the cove, and "
                        "return to the mainland.\n"
                        "The police take your report seriously, but by the time "
                        "they reach the island, the vault has been emptied.\n"
                        "ENDING: A NARROW ESCAPE\n"
                        "You kept everyone safe, but left without the strongest "
                        "evidence."
                    )
                elif "shipping label" not in inventory:
                    say(
                        "You return to the mainland with the ledger. "
                        "The police identify the stolen collection and arrange "
                        "a search of the coast.\n"
                        "The instruments are eventually recovered, although "
                        "the boat has already left Kirrin.\n"
                        "ENDING: THE RECOVERED COLLECTION"
                    )
                else:
                    say(
                        "You slip back through the tunnel without touching "
                        "the signal bell. Soon your boat is heading home.\n"
                        "The ledger supplies the names and delivery times. "
                        "The shipping label identifies the stolen collection, "
                        "and your description pinpoints the hidden landing.\n"
                        "That evening, officers wait above the cove. When the "
                        "smugglers arrive to load their boat, the police are "
                        "ready for them.\n"
                        "The next morning, you return to Kirrin Island.\n"
                        "'One mystery solved,' Dick says, opening the picnic basket.\n"
                        "Timmy noses beneath the sandwiches and produces "
                        "an extremely ordinary tennis ball.\n"
                        "'And that,' you tell him, 'is quite enough discoveries "
                        "for one holiday.'\n"
                        "ENDING: THE SECRET OF THE BELL"
                    )
                running = False

            elif action == "quit":
                running = False

    say("Thanks for playing.")


if __name__ == "__main__":
    play()