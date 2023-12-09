init python:
    import json
    import os

    # Mapping of achievement title to (index, description)
    # The index is so achievements stay in order on the achivements page.
    ACHIEVEMENTS = {
        "First Death": (0, "Die for the first time."),
        "Fake Protagonist": (1, "Discover the truth behind the agent's fate."),
        "Corruption": (2, "Watch Sonny or Fulgur succumb to corruption."),
        "Kleptomaniac": (3, "Placeholder text for Alban's achievement."),
        "Psychic": (4, "Placeholder text for Uki's achievement."),
        "Do You Read Me?": (5, "Placeholder text for Fulgur's achievement."),
        "Lightning Fast": (6, "Placeholder text for achievement."),
        "True Ending": (7, "Reach the true ending of Noctyx's story."),
    }

    class Achievement:
        """In-game achievements."""
        def __init__(self, title, completed=False) -> None:
            self.title = title
            self.completed = completed

    class AchievementTracker:
        """Tracker for in-game achievements."""

        SAVE_FILENAME = "saved_achievements.txt"

        def __init__(self) -> None:
            self.num_completed = 0
            self.num_achievements = len(ACHIEVEMENTS)
            self.load_achievements()

        def initialize_achievements(self):
            """Initialize achievements from scratch."""
            self.achievements = {}
            for title, _ in ACHIEVEMENTS.items():
                self.achievements[title] = Achievement(title)

        def load_achievements(self):
            """Load achievements from save directory."""
            save_filename = os.path.join(config.savedir, self.SAVE_FILENAME)
            if not os.path.exists(save_filename):
                self.initialize_achievements()
            else:
                num_completed = 0
                self.achievements = {}
                with open(save_filename, "r") as f:
                    achievement_str = f.read()
                for achievement in json.loads(achievement_str):
                    if achievement["completed"]:
                        num_completed += 1
                    title = achievement["title"]
                    self.achievements[title] = Achievement(**achievement)
                self.num_completed = num_completed

        def save_achievements(self):
            """Save achievements to the save directory."""
            save_filename = os.path.join(config.savedir, self.SAVE_FILENAME)
            achievement_lst = []
            for achievement in self.achievements.values():
                achievement_lst.append(achievement.__dict__)
            with open(save_filename, "w") as f:
                f.write(json.dumps(achievement_lst))

        def clear_saved_achievements(self):
            """
            Clear saved achievements, including the savefile.
            For testing purposes only.
            """
            save_filename = os.path.join(config.savedir, self.SAVE_FILENAME)
            if os.path.exists(save_filename):
                os.remove(save_filename)
            self.num_completed = 0
            self.initialize_achievements()

        def complete_achievement(self, name) -> None:
            """Mark achievement as completed."""
            self.achievements[name].completed = True
            self.num_completed += 1
            self.save_achievements()

        def get_sorted_achievements(self):
            """Get Achievements sorted by index."""
            return sorted(
                self.achievements.values(),
                key=lambda a: ACHIEVEMENTS[a.title][0]
            )

    achievement_tracker = AchievementTracker()

## Achievements screen 

screen achievements():

    tag menu

    use game_menu(_("Achievements"), scroll="viewport"):

        style_prefix "achievements"

        vbox:
            style "achievements_vbox"
            label "[achievement_tracker.num_completed]/[achievement_tracker.num_achievements] Completed"
            xalign 0.5

            for achievement in achievement_tracker.get_sorted_achievements():
                if achievement.completed:
                    $ description = ACHIEVEMENTS[achievement.title][1]
                    $ styling = "completed"
                else:
                    $ description = "Locked"
                    $ styling = "locked"

                hbox:
                    style_prefix "achievement_" + styling
                    hbox:
                        style "achievement_title"
                        text "[achievement.title]"

                    hbox:
                        style "achievement_description"
                        text "[description]"


style achievements_label is gui_label
style achievements_label_text is gui_label_text

style achievements_label:
    xfill True
    bottom_margin 30

style achievements_label_text:
    xalign 0.5

style achievements_vbox is default
style achievement_title is default
style achievement_description is default
style achievement_completed_text is gui_text
style achievement_locked_text is gui_text

style achievements_vbox:
    spacing 30

style achievement_title:
    xsize 350
    bottom_margin 30

style achievement_description:
    box_wrap True
    xfill True
    left_margin 30
    bottom_margin 30

style achievement_completed_text:
    color "#ffffff"

style achievement_locked_text:
    color "#888888"
