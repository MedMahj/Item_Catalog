#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robot",
             email="robot@gmail.com",
             picture="/static/blank_user.gif")
session.add(User1)
session.commit()


# Items for Soccer
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()


item1 = Item(user_id=1,
             title="Soccer Cleats",
             description="Protrusions on the sole of a shoe, or on an \
             external attachment to a shoe, that provide additional traction \
             on a soft or slippery surface. They can be conical or blade-like \
             in shape, and made of plastic, rubber or metal. The type worn \
             depends on the environment of play, whether it be grass, ice, \
             artificial turf, or other grounds.",
             category=category1)

session.add(item1)
session.commit()


item2 = Item(user_id=1,
             title="Jersey",
             description="an item of knitted clothing, traditionally in wool \
             or cotton, with sleeves, worn as a pullover, as it does not open \
             at the front, unlike a cardigan. It is acommonly worn by sports \
             teams as part of the team uniform, in team colors, often with a \
             required number and optionally the player's name on the back.",
             category=category1)

session.add(item2)
session.commit()


item3 = Item(user_id=1,
             title="Singuards",
             description="a thick piece of material that you wear inside your \
             socks to protect the lower part of your leg when you are playing \
             a game such as soccer",
             category=category1)

session.add(item3)
session.commit()


# Items for Snowboarding
category2 = Category(user_id=1, name="Snowboarding")

session.add(category2)
session.commit()


item1 = Item(user_id=1,
             title="Snowboard",
             description="Snowboards are boards where both feet are secured \
             to the same board, which are wider than skis, with the ability \
             to glide on snow.[1] Snowboards widths are between 6 and 12 \
             inches or 15 to 30 centimeters.[2] Snowboards are differentiated \
             from monoskis by the stance of the user. In monoskiing, the user \
             stands with feet inline with direction of travel (facing tip of \
             monoski/downhill) (parallel to long axis of board), whereas in \
             snowboarding, users stand with feet transverse (more or less) to \
             the longitude of the board.",
             category=category2)

session.add(item1)
session.commit()


item2 = Item(user_id=1,
             title="Goggles",
             description="Goggles are one of the most important pieces of \
             equipment you can purchase; they are just as important as your \
             jacket and pants. Any skier or snowboarder can tell you that not \
             being able to see ruins a day as fast as poor fitting boots or \
             a bad chili dog. All ski and snowboard goggles will offer some \
             basic protection from wind and cold, but beyond the basics there \
             are some key features to consider: lens type, lens color/tint, \
             interchangeable lenses, frame size and fi",
             category=category2)

session.add(item2)
session.commit()


# Items for Baseball
category3 = Category(user_id=1, name="Baseball")

session.add(category3)
session.commit()


item1 = Item(user_id=1,
             title="Bat",
             description="is a smooth wooden or metal club used in the sport \
             of baseball to hit the ball after it is thrown by the pitcher. \
             By regulation it may be no more than 2.75 inches (7.0 cm) in \
             diameter at the thickest part and no more than 42 inches \
             (1.067 m) in length.",
             category=category3)

session.add(item1)
session.commit()


# Items for Basketball
category4 = Category(user_id=1, name="Basketball")

session.add(category4)
session.commit()


item1 = Item(user_id=1,
             title="Basketball",
             description="is a spherical ball used in basketball games. \
             Basketballs typically range in size from very small promotional \
             # items only a few inches in diameter to extra large balls \
             nearly a foot in diameter used in training exercises. ",
             category=category4)

session.add(item1)
session.commit()


# Items for Hockey
category5 = Category(user_id=1, name="Hockey")

session.add(category5)
session.commit()


item1 = Item(user_id=1,
             title="Stick",
             description="It is a piece of equipment used in ice hockey to \
             shoot, pass, and carry the puck across the ice. Ice hockey \
             sticks are approximately 150-200 cm long, composed of a long, \
             slender shaft with a flat extension at one end called the blade.",
             category=category5)

session.add(item1)
session.commit()


# Items for Frisbee
category6 = Category(user_id=1, name="Frisbee")

session.add(category6)
session.commit()


item1 = Item(user_id=1,
             title="Frisbee",
             description="a gliding toy or sporting item that is generally \
             plastic and roughly 8 to 10 inches (20 to 25 cm) in diameter \
             with a pronounced lip. It is used recreationally and \
             competitively for throwing and catching, \
             as in flying disc games",
             category=category6)

session.add(item1)
session.commit()


print "added menu items!"
