init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_tripleS",
            category=["tripleS", "triplescosmos"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_tripleS:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Isn't twenty-four too many?",
            "~Oooh, rising~",
            "Do you have a bias in tripleS, [player]? My bias is ChaeYeon!"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_tripleS')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ARTMS",
            category=["ARTMS", "artms", "official_artms"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ARTMS:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "~To you, I'm a virtual angel~ <3",
            "'We rise togther, back to the moon, and beyond' I hope to rise together just like ARTMS did with you, [player]~",
            "Who's your favorite member, [player]? Mine is Haseul!"

        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_ARTMS')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_Chuu",
            category=["Chuu", "chuu", "chuuo3o", "chuucandoit", "chuu_atrp", "chuuhi_official"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_Chuu:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "You attack my heart~ ! <3",
            "You're my little hero, [player]~",
            "Chuu's dedication to a clean environment is admirable!"

        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_Chuu')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_Yves",
            category=["Yves", "yves", "yvesntual", "Yves___official"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_Yves:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "~Yeah, I'm lost, but I like it~",
            "I really admire Yves' songwriting talents, I could read her lyrics for hours..",
            "~I don't wanna free you, no, I just wanna feel you, babe~ <3"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_Yves')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_Loossemble",
            category=["LOOSSEMBLE", "Loossemble", "Looble", "loossemble.official", "Loossemble_twt"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_Loossemble:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "~My intuition perfect!~",
            "~He said, I said, 'I like you, [player]'~ ehehe~",
            "Looking for their friends, huh? Have they tried looking in the characters folder? ahahaha~"

        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_Loossemble')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_BLACKPINK",
            category=["BLACKPINK", "blackpinkofficial", "ygofficialblink", "roses_are_rosie", "jennierubyjane","oddatelier", "officialBLISSOO", "blissoo", "sooyaaa__", "lalalalisa_m"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_BLACKPINK:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "~BLACKPINK in your area!~"

        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_BLACKPINK')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_KCON",
            category=["KCON", "Let's KCON!", "KCON official", "kcon_official", "kcon.official", "kconhongkong", "kconjapan", "kconusa", "kcon_germany", "kconsaudiarabia"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_KCON:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Have you ever been to KCON, [player]?",
            "Let's KCON! ehehe~",
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_KCON')
    return