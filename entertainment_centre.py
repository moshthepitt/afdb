# -*- coding: utf-8 -*-
import fresh_tomatoes
import media

house_of_lungula = media.Movie("House of Lungula",
    "​​HOUSE of Lungula is a Sexy Comedy touching on the sexual habits of Kenyans",
    "https://buni.tv/media/images/thumbnails/2014/4/house-of-lungula_1.png",
    "https://www.youtube.com/watch?v=coOhJL1EhEc",
    "https://buni.tv/video/house-of-lungula/",
    )

nairobi_half_life = media.Movie("Nairobi Half Life",
    "An aspiring actor tries to juggle a life of crime while trying to make his acting dreams a reality",
    "https://buni.tv/media/images/thumbnails/2014/4/nairobi-half-life_1.jpg",
    "https://www.youtube.com/watch?v=nRjBLAnx2jU",
    "https://buni.tv/video/nairobi-half-life/",
    )

skeem = media.Movie("Skeem",
    "​​Each of a host of characters are hell-bent on being the first to get their hands a box of cash!",
    "https://buni.tv/media/images/thumbnails/2014/9/skeem.jpg",
    "https://www.youtube.com/watch?v=EG2Lq03p7CI",
    "https://buni.tv/video/skeem/",
    )

confusion_na_wa = media.Movie("Confusion Na Wa",
    "A dark comedy that traces the criss-crossing paths of a hand full of strangers.",
    "https://buni.tv/media/images/thumbnails/2014/8/confusion-na-wa.png",
    "https://www.youtube.com/watch?v=o1SOzEe2fHU",
    "https://buni.tv/video/confusion-na-wa/")

me_wife_guru = media.Movie("Me, My Wife and her Guru",
    "Steve is happily married, but his wife soon starts to show unusual interest in her religious guru.",
    "https://buni.tv/media/images/thumbnails/2014/5/me-my-wife-and-her-guru.jpg",
    "https://www.youtube.com/watch?v=RlSe9_IDhd8",
    "https://buni.tv/video/me-my-wife-and-her-guru/")

flower_girl = media.Movie("Flower Girl",
    "A shy florist conspires with a movie star to persuade her long time boyfriend to propose.",
    "https://buni.tv/media/images/thumbnails/2014/8/flower-girl_1.png",
    "https://www.youtube.com/watch?v=4qY11ajv05Q",
    "https://buni.tv/video/flower-girl/")

goghelen = media.Movie("Gog'Helen",
    "​​Gog'Helen is a truly South African action comedy, telling a wacky tale of Gog’Helen, a seemingly typical township granny",
    "https://buni.tv/media/images/thumbnails/2014/4/goghelen.jpg",
    "https://www.youtube.com/watch?v=JMuzndQRQnQ",
    "https://buni.tv/video/goghelen/")

ni_sisi = media.Movie("Ni Sisi",
    "Ni Sisi portrays a typical Kenyan community: a harmonious muddle of tribes, intermarriages, and extended families that is suddenly poison",
    "https://buni.tv/media/images/thumbnails/2014/4/ni-sisi_1.jpg",
    "https://www.youtube.com/watch?v=j8_AJk4nSWM",
    "https://buni.tv/video/ni-sisi/")

something_necessary = media.Movie("Something Necessary",
    "​​Something Necessary is an intimate moment in the life of a woman struggling to rebuild her life after civil unrest",
    "https://buni.tv/media/images/thumbnails/2014/4/something-necessary_1.jpg",
    "https://www.youtube.com/watch?v=ckdS9PEkoQQ",
    "https://buni.tv/video/something-necessary/")

movies = [house_of_lungula, nairobi_half_life, skeem, confusion_na_wa, me_wife_guru, flower_girl, goghelen, ni_sisi, something_necessary]

fresh_tomatoes.open_movies_page(movies)
