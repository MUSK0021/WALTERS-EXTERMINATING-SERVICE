"""All words and data for the Walters Exterminating Service website.

Edit here, then run: python3 build.py

=============================================================================
HOUSE RULES. Read before changing a word.
=============================================================================
Short sentences, plain words, no em dashes. Warm and direct, never salesy.
The audience is homeowners and small business owners in Northeast Philadelphia,
eastern Montgomery County and lower Bucks County. Many are older. Big type,
strong contrast, no jargon.

FACTS ONLY. Every claim here was checked in September 2026. The rules below
came out of that check and they are not suggestions:

1. NEVER hard-code the company's age. The old site said "Our 63rd Year" and it
   went stale in April 2026. FOUNDED is the single source of truth and build.py
   computes any number from it.

2. The business has been in the family since 1963. The LLC has NOT existed
   since 1963: Pennsylvania's LLC statute dates from 1994, and the company
   originally traded as "Walters Exterminating Termite and Pest Control".
   Say "family owned since 1963", never "Walters Exterminating Service LLC,
   founded 1963".

3. The old site said "In 1967 the E.P.A required all Pest control companies to
   be Licensed by the State." This is false three times over. The EPA was not
   created until 2 December 1970, the EPA has never licensed pest control
   companies in Pennsylvania, and PA licensing comes from the Pennsylvania
   Pesticide Control Act of 1973 (enacted 1 March 1974). It is deleted. Do not
   reinstate it with a different year.

4. BU0014 is a Pennsylvania pesticide application BUSINESS licence number,
   issued by the PA Department of Agriculture and required by law to be
   displayed on both sides of service vehicles (it is, in their own photos).
   State the number plainly. Claim NOTHING about its rank. "BU" is a category
   prefix, so the digits do not prove it was the 14th licence issued.

5. The "my father was the 14th person tested in PA" story is the family's own
   account with no public record behind it. It appears ONLY as an attributed
   quote from Nolan, never as a stated fact.

6. NO ratings or review counts anywhere, and no AggregateRating in the schema.
   Marking up your own aggregate rating breaches Google's structured data
   policy. There is no BBB profile, so no BBB badge either.

7. NO street address. Neither their own site nor their Google listing publishes
   one, so the privacy is deliberate.

8. "Certified in I.P.M." and "Certified in Food Handling" appeared on the old
   site. Neither is a recognised PA certification category as worded, so they
   are described as how the team works, not claimed as credentials.

Anything marked ASK NOLAN below is unconfirmed and must not go live until he
confirms it. See the block at the bottom of this file.
=============================================================================
"""

FOUNDED = 1963
FOUNDED_MONTH = 'April'

SITE = {
    'name': 'Walters Exterminating Service',
    'legal': 'Walters Exterminating Service LLC',
    'tagline': "Don't Be Bugged - Bug Us!",
    'origin': 'https://bugwalters.com',
    'phone': '(215) 947-8818',
    'phone_href': 'tel:+12159478818',
    'email': 'info@bugwalters.com',
    'licence': 'BU0014',
    # No street address is published anywhere, on purpose. Do not add one.
    'region': 'PA',
    'areas': 'Northeast Philadelphia, eastern Montgomery County and lower Bucks County',
    'founder': 'Harvey Walters',
    'owner': 'Nolan Walters',
    'owner_nick': 'the Bug-Man',
}

NAV = [
    ('Services', '/services/'),
    ('What It Costs', '/what-it-costs/'),
    ('Bed Bugs', '/bed-bugs/'),
    ('Common Pests', '/pests/'),
    ('Our Story', '/about/'),
    ('Contact', '/contact/'),
]

# Short, checkable promises. Every one of these is either verified or is the
# business's own long-standing published claim.
PROMISES = [
    ('badge', 'Licensed in Pennsylvania',
     f'PA Department of Agriculture pesticide application business licence {SITE["licence"]}.'),
    ('clock', 'Weekdays and Saturdays',
     'We can give you a one hour window, so you are not waiting in all day.'),
    ('shield', 'No contracts, no sales calls',
     'Nothing to sign to get started, and nobody will ring you to sell you anything.'),
    ('home', 'Family owned since 1963',
     'Two generations, same family, same phone number.'),
]

HERO_SLIDES = [
    ('hero-van', 'Nolan Walters with the Walters Exterminating van in Northeast Philadelphia'),
    ('hero-porch', 'The covered front porch and door of a house on a residential street'),
    ('hero-street', 'A stone and clapboard house with shuttered windows on a quiet street'),
]

# --------------------------------------------------------------- services

SERVICES = [
    {
        'slug': 'home-pest-control',
        'name': 'Home Pest Control',
        'icon': 'home',
        'short': 'Inside and outside programs for houses, apartments, condos and rentals.',
        'meta': 'Inside and outside pest programs for houses, apartments, condos and rentals across Northeast Philadelphia and nearby Montgomery and Bucks. No contracts.',
        'title': 'Your home, looked after properly.',
        'banner': 'banner-home',
        'banner_alt': 'A Walters technician treating along the brick foundation of a house',
        'intro_title': 'Inside, outside, and the gaps in between.',
        'lead': ('Roaches in the kitchen, ants on the counter, mice in the basement. We treat inside and '
                 'outside, we explain what we are doing, and we do not ask you to sign anything to get started.'),
        'image': 'service-foundation',
        'image_alt': 'A Walters technician treating along the brick foundation of a house',
        'included_title': 'What a home visit covers',
        'included': [
            'A walk around the outside to find where pests are getting in',
            'Treatment inside where you are seeing them',
            'A perimeter treatment around the foundation',
            'Cracks, gaps and entry points pointed out to you',
            'Plain English on what we used and what to expect',
        ],
        'properties_title': 'Homes we look after',
        'properties': ['Houses', 'Apartments', 'Condos', 'Rentals', 'Twins and rowhomes'],
        'pests': ['roaches', 'ants', 'mice', 'spiders', 'silverfish', 'earwigs', 'crickets', 'pantry-pests'],
        'faqs': [
            ('Do I have to sign a contract?',
             'No. The old fashioned way still works here. We come out, we tell you what it will cost, and you '
             'decide.'),
            ('Will a sales person call me afterwards?',
             'No. Nobody will call you to sell you anything.'),
            ('Do you come on Saturdays?',
             'Weekdays and Saturdays, and we give you a one hour arrival window so you are not stuck waiting '
             'in all day.'),
            ('Is it safe around my kids and pets?',
             'Tell us about your household before we start and we will explain each product we use and how long '
             'to stay out of a treated area.'),
        ],
    },
    {
        'slug': 'bed-bugs',
        'name': 'Bed Bug Treatment',
        'icon': 'bed',
        'short': 'The work we are known for. Careful inspection, then a proper treatment.',
        'meta': 'Bed bug inspection and treatment in Northeast Philadelphia and nearby Montgomery and Bucks. The work we are known for, done properly. Call (215) 947-8818.',
        'title': 'Bed bugs are beatable. Store bought spray is not the way.',
        'banner': 'banner-bedbugs',
        'banner_alt': 'A mattress and bed frame being inspected for bed bugs',
        'intro_title': 'Find them first, then treat them.',
        'lead': ('Bed bugs are the problem people call us about most, and the one where doing it yourself usually '
                 'makes things worse. Over the counter sprays scatter them deeper into walls and furniture, and a '
                 'bigger, harder job is what is left behind.'),
        'image': 'service-bedbug',
        'image_alt': 'A Walters technician using a backpack vacuum on a bed frame during a bed bug treatment',
        'included_title': 'How we handle a bed bug job',
        'included': [
            'A full inspection of beds, frames, seams and the furniture around them',
            'We show you what we found and where',
            'Treatment worked through every place they are hiding, not just the mattress',
            'What to wash, bag and move, written down for you',
            'A follow up visit, because one treatment is rarely the end of it',
        ],
        'facts_title': 'What bed bugs actually do',
        'facts': [
            ('moon', 'They feed at night', 'They come out in the hours before dawn, feed for a few minutes, and '
                                          'are back in hiding before you are awake.'),
            ('search', 'They hide close to the bed', 'Mattress seams and box springs first, then frames, '
                                                    'headboards, nightstands, carpet edges and skirting.'),
            ('clock', 'They can wait you out', 'An adult can go months without a meal, so an empty room is not '
                                              'necessarily a clear one.'),
            ('alert', 'Spray drives them deeper', 'Store bought pesticide scatters them into wall voids, which '
                                                 'makes the job harder and longer.'),
        ],
        'signs_title': 'Signs worth a phone call',
        'signs': [
            'Small itchy bites in a line or cluster, often on arms, shoulders or legs',
            'Tiny dark spots on sheets, the mattress seam or the bed frame',
            'Shed skins or pale egg cases in the seams',
            'A sweet, musty smell in a room that will not shift',
            'Live insects about the size of an apple seed, flat and reddish brown',
        ],
        'pests': ['bed-bugs'],
        'faqs': [
            ('Can I treat bed bugs myself?',
             'We would rather you did not. Store bought pesticide usually scatters them deeper into the walls, '
             'which makes the job harder and more expensive than if you had called at the start.'),
            ('How do I know it is bed bugs and not fleas?',
             'Call us and we will come and look. Bed bugs hide within a few feet of where you sleep. Fleas are '
             'usually about a pet and you will often see them jumping. Guessing wrong wastes a treatment.'),
            ('Do I need to throw out my mattress?',
             'Usually no. Getting rid of furniture before an inspection often spreads the problem through the '
             'building rather than ending it. Let us look first.'),
            ('I am a landlord. Can you deal with a whole building?',
             'Yes. We work in apartments, condos and rental properties across the area, including buildings where '
             'more than one unit is affected.'),
        ],
    },
    {
        'slug': 'commercial-pest-control',
        'name': 'Commercial Pest Control',
        'icon': 'building',
        'short': 'Restaurants, bars, offices, warehouses and rental buildings.',
        'meta': 'Pest control for restaurants, bars, offices, warehouses and rental buildings. Northeast Philadelphia and nearby Montgomery and Bucks. We work around your hours.',
        'title': 'One sighting is all it takes.',
        'banner': 'banner-commercial',
        'banner_alt': 'A commercial kitchen with stainless steel counters',
        'intro_title': 'We work around your opening hours.',
        'lead': ('A customer who sees a roach does not come back, and they tell people. We work around your hours, '
                 'keep the paperwork straight for inspections, and treat the building rather than just the room '
                 'you called about.'),
        'image': 'service-commercial',
        'image_alt': 'A Walters technician treating a doorway from inside a building',
        'included_title': 'How commercial work runs',
        'included': [
            'A walk through of the whole building, not just the complaint',
            'Treatment scheduled around your opening hours',
            'Kitchens, storage, bins, cellars and delivery doors checked',
            'Records kept for your inspections',
            'One person who knows your building, visit after visit',
        ],
        'properties_title': 'Places we work',
        'properties': ['Restaurants', 'Bars', 'Offices', 'Warehouses', 'Stores', 'Apartment buildings'],
        # Deliberately worded as how they work, NOT as a held certification.
        'approach_title': 'How we approach a commercial building',
        'approach': ('We work the way integrated pest management describes: find out how pests are getting in and '
                     'what is feeding them, fix that first, and treat with that in mind rather than spraying on a '
                     'schedule and hoping.'),
        'pests': ['roaches', 'mice', 'rats', 'ants', 'flies', 'pantry-pests'],
        'faqs': [
            ('Can you come outside our opening hours?',
             'That is usually how commercial work gets done. Tell us your hours and we will fit around them.'),
            ('Do you keep records for health inspections?',
             'Yes. We keep a record of what was treated and when, so you have it when an inspector asks.'),
            ('Do you handle apartment buildings?',
             'Yes, including buildings where the problem has moved between units.'),
        ],
    },
    {
        'slug': 'rodents-and-wildlife',
        'name': 'Rodents & Wildlife',
        'icon': 'mouse',
        'short': 'Mice and rats, plus groundhogs, raccoons and squirrels.',
        'meta': 'Mice, rats, groundhogs, raccoons and squirrels in attics, sheds and crawl spaces. Northeast Philadelphia and nearby Montgomery and Bucks. Call (215) 947-8818.',
        'title': 'Something bigger than a bug.',
        'banner': 'banner-rodents',
        'banner_alt': 'A humane cage trap set outside a house',
        'intro_title': 'Get them out, then keep them out.',
        'lead': ('Scratching in the ceiling, droppings in a drawer, something living under the shed. We handle '
                 'mice and rats, and the small animals that get into attics, sheds and crawl spaces.'),
        'image': 'service-wildlife',
        'image_alt': 'Nolan Walters holding two young raccoons in gloved hands beside the company van',
        'included_title': 'What we deal with',
        'included': [
            'Mice and rats, inside and around the building',
            'Groundhogs under sheds, decks and concrete',
            'Raccoons and squirrels in attics, soffits and chimneys',
            'The gaps and entry points that let them in',
            'Droppings and nesting material pointed out so you know where they have been',
        ],
        'signs_title': 'What you might notice first',
        'signs': [
            'Scratching or scurrying in a wall or ceiling, usually at night',
            'Droppings in drawers, cupboards or along a wall',
            'Chewed packaging, wiring or insulation',
            'A burrow beside a shed, deck or foundation',
            'Noise in the chimney or above a bedroom ceiling',
        ],
        'pests': ['mice', 'rats', 'groundhogs', 'raccoons', 'squirrels'],
        'faqs': [
            ('There is something in my attic. Who do I call?',
             'Call us. Attic noise is usually squirrels, raccoons or mice, and which one it is changes how we '
             'handle it. We come and find out rather than guessing over the phone.'),
            ('Can you stop them coming back?',
             'Getting them out is half the job. The other half is finding the gap they used and telling you what '
             'needs closing up.'),
        ],
    },
    {
        'slug': 'bees-wasps-hornets',
        'name': 'Bees, Wasps & Hornets',
        'icon': 'wasp',
        'short': 'Nests under eaves, in walls, in the ground and in the shed.',
        'meta': 'Wasp, hornet and bee nests under eaves, in walls, in the ground and in the shed. Northeast Philadelphia and nearby Montgomery and Bucks. Call (215) 947-8818.',
        'title': 'Leave the nest alone and call someone.',
        'banner': 'banner-wasps',
        'banner_alt': 'A paper wasp nest built under a roof edge',
        'intro_title': 'We take the nest, not just the wasps.',
        'lead': ('A wasp or hornet nest near a door, a window or a walkway is worth dealing with quickly, '
                 'especially if anyone in the house reacts badly to stings. Knocking it down yourself tends to go '
                 'the way you would expect.'),
        'image': 'service-ladder',
        'image_alt': 'A Walters technician on a ladder treating under the eaves of a house',
        'included_title': 'Where nests turn up',
        'included': [
            'Under eaves, soffits and gutter lines',
            'Inside wall voids and behind siding',
            'In the ground, along banks and beside paths',
            'In sheds, garages and under decks',
            'In bushes and low branches near the house',
        ],
        'pests': ['wasps', 'hornets', 'bees'],
        'faqs': [
            ('There is a nest by my front door. How soon can you come?',
             'Call us and tell us where it is and how close it is to a doorway. A nest on a path or by a door, or '
             'anyone in the house with a sting allergy, moves it up the list.'),
            ('Can I just knock it down?',
             'Please do not. Hornets and yellow jackets defend a nest hard, and a nest in a wall void is bigger '
             'than the part you can see.'),
        ],
    },
]
SERVICE_BY_SLUG = {s['slug']: s for s in SERVICES}

HOW_IT_WORKS = [
    ('phone', 'Call and tell us what you are seeing',
     'You get a person, not a call centre. Describe it in your own words. There is no wrong way to say it.'),
    ('clipboard', 'We come out and look',
     'We find where they are getting in and what is keeping them there, then tell you what it will cost before '
     'we start.'),
    ('shield', 'We treat it, and we tell you what we did',
     'What we used, what to expect over the next few days, and what to call us about.'),
]

# --------------------------------------------------------------- pests

PESTS = [
    {'slug': 'bed-bugs', 'name': 'Bed Bugs', 'icon': 'bed', 'when': 'All year', 'service': 'bed-bugs',
     'summary': 'Flat, reddish brown, about the size of an apple seed. They hide within a few feet of the bed.',
     'signs': ['Dark spots on the mattress seam or frame', 'Bites in a line or cluster', 'Shed skins in the seams']},
    {'slug': 'roaches', 'name': 'Cockroaches', 'icon': 'roach', 'when': 'All year', 'service': 'home-pest-control',
     'summary': 'They spoil food, they spread through a building, and they can set off asthma and allergies.',
     'signs': ['Roaches scattering when a light goes on', 'Dark specks in cupboards', 'A musty smell in the kitchen']},
    {'slug': 'ants', 'name': 'Ants', 'icon': 'ant', 'when': 'Spring, Summer', 'service': 'home-pest-control',
     'summary': 'The classic spring phone call. Carpenter ants are the ones that damage wood while they nest.',
     'signs': ['A trail across a counter or floor', 'Fine sawdust under woodwork', 'Winged ants indoors in spring']},
    {'slug': 'mice', 'name': 'Mice', 'icon': 'mouse', 'when': 'Autumn, Winter', 'service': 'rodents-and-wildlife',
     'summary': 'A mouse fits through a gap the width of a pencil. They chew wiring and nest in insulation.',
     'signs': ['Droppings in drawers or cupboards', 'Chewed food packets', 'Scratching in a wall at night']},
    {'slug': 'rats', 'name': 'Rats', 'icon': 'rat', 'when': 'All year', 'service': 'rodents-and-wildlife',
     'summary': 'Common around older blocks, alleys and outbuildings. They burrow and they gnaw.',
     'signs': ['Burrows by a shed or foundation', 'Large droppings along a wall', 'Gnawed pipes, wire or sacks']},
    {'slug': 'wasps', 'name': 'Wasps', 'icon': 'wasp', 'when': 'Spring to Autumn', 'service': 'bees-wasps-hornets',
     'summary': 'Paper nests under eaves and decks, and ground nests along paths and banks.',
     'signs': ['A papery nest under an eave', 'Wasps going in and out of one spot', 'Wasps around bins and food']},
    {'slug': 'hornets', 'name': 'Hornets', 'icon': 'hornet', 'when': 'Summer, Autumn', 'service': 'bees-wasps-hornets',
     'summary': 'Bald faced hornets build the big grey football shaped nests. They defend them hard.',
     'signs': ['A large grey nest in a tree or on a wall', 'Hornets patrolling one area', 'Nests high under a gable']},
    {'slug': 'bees', 'name': 'Bees', 'icon': 'bee', 'when': 'Spring to Autumn', 'service': 'bees-wasps-hornets',
     'summary': 'Carpenter bees bore round holes in untreated wood. Others nest in wall voids and soffits.',
     'signs': ['Round holes in a deck rail or eave', 'Sawdust below the holes', 'Bees going into a wall gap']},
    {'slug': 'spiders', 'name': 'Spiders', 'icon': 'spider', 'when': 'Summer, Autumn', 'service': 'home-pest-control',
     'summary': 'Mostly harmless. A lot of spiders usually means a lot of other insects to eat.',
     'signs': ['Webs in corners and basements', 'Egg sacs in quiet spots', 'More of them indoors in autumn']},
    {'slug': 'fleas', 'name': 'Fleas', 'icon': 'flea', 'when': 'Summer, Autumn', 'service': 'home-pest-control',
     'summary': 'Usually arrive on a pet, then live in carpet, bedding and the cracks between floorboards.',
     'signs': ['A pet scratching more than usual', 'Bites around ankles', 'Dark grit in pet bedding']},
    {'slug': 'ticks', 'name': 'Ticks', 'icon': 'tick', 'when': 'Spring to Autumn', 'service': 'home-pest-control',
     'summary': 'Picked up in long grass and leaf litter, at the edge of a yard where it meets cover.',
     'signs': ['Ticks on a pet after time outside', 'Long grass along a fence or wood line', 'Leaf piles and brush']},
    {'slug': 'silverfish', 'name': 'Silverfish', 'icon': 'silverfish', 'when': 'All year', 'service': 'home-pest-control',
     'summary': 'Damp loving and fast. They feed on paper, starch and stored fabric.',
     'signs': ['Silver insects in a bath or sink', 'Damage to books or wallpaper', 'Activity in damp basements']},
    {'slug': 'earwigs', 'name': 'Earwigs', 'icon': 'earwig', 'when': 'Spring, Summer', 'service': 'home-pest-control',
     'summary': 'Outdoor insects that come inside when it turns dry, usually through a low door or window.',
     'signs': ['Earwigs in a bath or basement', 'Under pots, mulch and paving', 'Activity after heavy rain']},
    {'slug': 'crickets', 'name': 'Crickets', 'icon': 'cricket', 'when': 'Summer, Autumn', 'service': 'home-pest-control',
     'summary': 'Noisy in a basement or garage, and they will chew paper and fabric while they are there.',
     'signs': ['Chirping in a basement at night', 'Crickets by a garage door', 'Small holes in stored fabric']},
    {'slug': 'millipedes', 'name': 'Millipedes', 'icon': 'millipede', 'when': 'Spring, Autumn', 'service': 'home-pest-control',
     'summary': 'They live in damp ground and wander in through basement doors after rain.',
     'signs': ['Curled up on a basement floor', 'Under mulch and leaf litter', 'More of them after heavy rain']},
    {'slug': 'pantry-pests', 'name': 'Pantry Pests', 'icon': 'pantry', 'when': 'All year', 'service': 'home-pest-control',
     'summary': 'Moths and beetles that breed inside flour, cereal, rice and dry pet food.',
     'signs': ['Small moths flying in the kitchen', 'Webbing inside a packet', 'Beetles in the back of a cupboard']},
    {'slug': 'groundhogs', 'name': 'Groundhogs', 'icon': 'groundhog', 'when': 'Spring to Autumn', 'service': 'rodents-and-wildlife',
     'summary': 'They dig large burrows under sheds, decks, steps and concrete slabs.',
     'signs': ['A burrow mouth beside a shed or deck', 'Fresh soil piled at the entrance', 'Damage to a vegetable patch']},
    {'slug': 'raccoons', 'name': 'Raccoons', 'icon': 'raccoon', 'when': 'All year', 'service': 'rodents-and-wildlife',
     'summary': 'Strong, clever and heavy. They get into attics, soffits and chimneys, especially in spring.',
     'signs': ['Heavy movement overhead at night', 'A torn soffit or vent', 'Bins turned over repeatedly']},
    {'slug': 'squirrels', 'name': 'Squirrels', 'icon': 'squirrel', 'when': 'All year', 'service': 'rodents-and-wildlife',
     'summary': 'They chew their way into attics and nest there, and they gnaw wiring once inside.',
     'signs': ['Running noises in the ceiling by day', 'A gnawed hole at a roof edge', 'Nesting material in the attic']},
    {'slug': 'flies', 'name': 'Flies', 'icon': 'fly', 'when': 'Summer', 'service': 'commercial-pest-control',
     'summary': 'A kitchen and bin problem. Where they breed matters more than the ones you can see.',
     'signs': ['Flies around bins or drains', 'Clusters at a window', 'More of them in warm weather']},
]
PEST_BY_SLUG = {p['slug']: p for p in PESTS}
HOME_PESTS = ['bed-bugs', 'roaches', 'mice', 'ants', 'wasps', 'rats']

# --------------------------------------------------------------- story

STORY = {
    'lead': ('Harvey Walters started this company in April 1963. His son Nolan grew up in it, and runs it now. '
             'Same family, same phone number, same way of doing things.'),
    'paragraphs': [
        'Harvey Walters began Walters Exterminating Termite and Pest Control in April 1963, more than a decade '
        'before Pennsylvania began licensing pest control businesses under the Pennsylvania Pesticide Control Act '
        'of 1973.',
        'Nolan was in a company shirt as a boy in the 1970s, out on jobs with his father. He has worked in the '
        'business full time for more than forty years, and took it over as the second generation owner. Most '
        'people around here just call him the Bug-Man.',
        'The company is licensed by the Pennsylvania Department of Agriculture as a pesticide application '
        'business, licence number BU0014. By law that number is painted on both sides of the van, so you can '
        'check it on the truck sitting outside your house.',
        'What has not changed in sixty years: no sales people, no pressure, and the owner still turns up at jobs '
        'himself.',
    ],
    # Attributed family history, NOT asserted as documented fact. Do not restate as a claim.
    'quote': ('My father was the 14th person in Pennsylvania to be tested and granted a pest control licence. '
              'We still carry that number. BU0014.'),
    'quote_by': 'Nolan Walters',
    'quote_note': 'The family’s own account.',
    # ASK NOLAN before publishing: confirm he said this and is happy for it to be on his site.
    'motto': 'Always work from the heart, not the wallet. Treat every customer like it is your home.',
    'motto_by': 'Nolan Walters',
}

TIMELINE = [
    ('1963', 'Harvey Walters starts the company',
     'Walters Exterminating Termite and Pest Control opens in April, serving Northeast Philadelphia and the '
     'townships just outside it.'),
    ('1970s', 'A boy in a company shirt',
     'Nolan is out on jobs with his father before he is old enough to drive the van.'),
    ('1973', 'Pennsylvania starts licensing',
     'The Pennsylvania Pesticide Control Act brings in licensing for pest control businesses. Walters carries '
     'business licence BU0014.'),
    ('Today', 'Second generation, still local',
     f'Nolan Walters runs the company his father started, across {SITE["areas"]}.'),
]

# The old site had a Pictures page. These are the photographs from it, plus the
# ones off their vans. All of them are the family's own, which is the point:
# everything else on this site is stock, and this page is not.
PHOTO_CAPTIONS = [
    ('archive-1977', 'Nolan in a company shirt, 1977',
     'Out on jobs with his father before he was old enough to drive the van.'),
    ('archive-shirt', 'The company shirt, 1970s',
     'The oval has barely changed in fifty years. It is still on the vans.'),
    ('archive-harvey', 'Harvey and Nolan, 2010',
     'Harvey founded the company in April 1963. Nolan runs it now.'),
    ('nolan-van', 'Nolan Walters, 2020',
     'Two generations, same family, same phone number.'),
    ('team-group', 'The crew',
     'Small team, all of them known to the customers they visit.'),
    ('nolan-glove', 'On a job',
     'Gloves on, looking where the pests actually are rather than where they were seen.'),
    ('team-inspect', 'An inspection',
     'Most jobs start with a walk around the outside to find the way in.'),
    ('nolan-training', 'Still learning',
     'Pennsylvania licences have to be kept current, so the training never really stops.'),
    ('cage-trap', 'A humane cage trap',
     'For the things that are bigger than a bug and need to leave in one piece.'),
]

# --------------------------------------------------------------- service area
# ASK NOLAN to confirm this list before launch. Every place below was checked
# for the right county, because putting a town in the wrong county on a local
# business site is the fastest way to look like you are not from around here.

AREAS = [
    ('Northeast Philadelphia',
     ['Somerton', 'Bustleton', 'Fox Chase', 'Rhawnhurst', 'Holmesburg', 'Mayfair', 'Torresdale',
      'Parkwood', 'Academy Gardens', 'Burholme', 'Oxford Circle', 'Tacony', 'Winchester Park']),
    ('Eastern Montgomery County',
     ['Abington', 'Huntingdon Valley', 'Jenkintown', 'Willow Grove', 'Hatboro', 'Horsham',
      'Cheltenham', 'Elkins Park', 'Glenside', 'Rockledge', 'Lower Moreland', 'Upper Moreland', 'Bryn Athyn']),
    ('Lower Bucks County',
     ['Bensalem', 'Feasterville', 'Trevose', 'Langhorne', 'Levittown', 'Bristol', 'Croydon',
      'Newtown', 'Richboro', 'Churchville', 'Holland', 'Yardley', 'Morrisville']),
]

# --------------------------------------------------------------- offer

COUPON = {
    'headline': '$10 off your first service',
    'terms': 'New customers only. Mention it when you call. Cannot be combined with other offers.',
}

# --------------------------------------------------------------- pricing

# There are no prices on this site, because he does not publish any and his
# model is to quote on the doorstep. What CAN be published is how the price is
# arrived at, which is the question the page has to answer. Every line below is
# either his own published copy or a plain description of the process.
PRICING = {
    'lead': 'We do not publish a price list, because the job is never the same twice. '
            'What we can tell you is exactly how the number is arrived at, and that you '
            'will hear it before anyone starts work.',
    'steps': [
        ('phone', 'You call and describe it',
         'You get a person, not a call centre. Most of the time we can tell you what it '
         'probably is from the description.'),
        ('search', 'We come out and look',
         'We find where they are getting in and what is keeping them there. Looking costs '
         'you nothing and does not commit you to anything.'),
        ('clipboard', 'You get the price before we start',
         'One number, for the work we have just described to you. If it needs a follow up '
         'visit we say so then, not afterwards.'),
        ('check-circle', 'You decide',
         'There is nothing to sign to get started, and nobody will ring you afterwards to '
         'sell you something else.'),
    ],
    'factors_title': 'What moves the number',
    'factors': [
        'How big the property is, and whether we are treating inside, outside or both',
        'Which pest it is. A wasp nest is one visit; bed bugs and roaches are a course of work',
        'How far it has got before you called',
        'Whether it needs a follow up, which for bed bugs it usually does',
        'Whether it is a home or a business with paperwork to keep straight',
    ],
    'faq': [
        ('Do you charge to come out and look?',
         'No. We look, we tell you what it is, and we tell you what it would cost. What you '
         'do with that is up to you.'),
        ('Do I have to sign a contract?',
         'No. You call, we come out, we tell you the price, and you decide. Nothing to sign '
         'to get started.'),
        ('Is there a monthly plan?',
         'Not as a package you sign up to. Plenty of our customers have us back on a regular '
         'basis, but that is a standing arrangement between us, not a contract.'),
        ('Can I use the coupon with something else?',
         'The coupon is for new customers and cannot be combined with other offers. Mention it '
         'when you call and we will take it off.'),
    ],
}

# --------------------------------------------------------------- FAQ (home)

HOME_FAQ = [
    ('Do you make me sign a contract?',
     'No. You call, we come out, we tell you the price, and you decide. Nothing to sign to get started.'),
    ('Will someone ring me trying to sell me something?',
     'No. No sales people will call you.'),
    ('Which areas do you cover?',
     f'{SITE["areas"][0].upper() + SITE["areas"][1:]}. If you are near the edge of that, call and ask.'),
    ('Are you licensed?',
     f'Yes. We are licensed by the Pennsylvania Department of Agriculture as a pesticide application business, '
     f'licence number {SITE["licence"]}. By law that number is on both sides of our vans.'),
    ('How long have you been doing this?',
     f'The family has run this business since {FOUNDED}. Nolan has worked in it full time for more than forty years.'),
    ('Do you handle bed bugs?',
     'Yes, and it is the work we are best known for. Please do not treat them with store bought spray first, '
     'because it usually scatters them deeper and makes the job harder.'),
]

# =============================================================================
# ASK NOLAN. Nothing in this list is confirmed. Resolve before launch.
# =============================================================================
OPEN_QUESTIONS = [
    # Resolved by the September 2026 research pass, kept here as a record:
    #   Hours       his About page says "weekdays, and Saturdays", with no clock times anywhere.
    #   Contracts   his About page says "No contracts are required" and "No sales people will call",
    #               unconditionally and site wide, so both are safe to publish.
    #   LLC         PA entity 3981492, Certificate of Organization filed 23 September 2010, forty seven
    #               years after the family business began. Never write "LLC since 1963".
    #   Google      the profile is UNCLAIMED, so there is nothing to log in to yet.
    #   Tagline     no published source uses a comma, so the site now sets the hyphen he uses himself.
    'His Google Business Profile is unclaimed. Claiming it at google.com/business and adding hours, '
    'the service area and photos is the single biggest local visibility win available, and it is free. '
    'He has already done this on Yelp, so he has the drill.',
    'Exact opening and closing times for weekdays and Saturday. "Weekdays and Saturdays" is his own '
    'published wording, but every nearby competitor publishes clock times and he does not.',
    'Is he insured? His Yelp and Nextdoor profiles both say "licensed and insured", but his own website '
    'only ever says licensed, so the site says licensed only. One word to add if he confirms it.',
    'The founding year needs one confirmation. The site says April 1963, but the earliest archived '
    'capture of his own site (Feb 2009) said "established in 1967". The stray 1967 in the old EPA '
    'sentence probably came from there. 1963 is what he publishes everywhere now, so 1963 is what we use.',
    'Which town, if any, should the site name? Four listings disagree: Huntingdon Valley (Alignable), '
    'Abington (Google, Yelp), Philadelphia 19152 (Superpages), Rockledge (Nextdoor). The site currently '
    'names none and describes the service area instead, which is the safest answer for a van based business.',
    'Should the site show a mailing address at all? His own eight page site shows none, deliberately, '
    'but third parties publish three different ones.',
    'Which PA pesticide applicator certification categories does Nolan hold? They are numbered. The old '
    'site said "Certified in I.P.M" and "Certified in Food Handling", neither of which is a recognised '
    'PA category as worded.',
    'His LinkedIn lists "Penn State Department of Agriculture", which is not a real organisation. Does he '
    'mean Penn State Extension training, or the PA Department of Agriculture?',
    'A marketing blog says he "pursued his education in entomology at Penn State". True? In what form?',
    'May we use the family photos on the site, including the 1977 photo and the 2010 photo of Harvey and Nolan?',
    'Is he happy with the quote "Always work from the heart, not the wallet" on the site? A blog attributes '
    'it to him but we have not confirmed it with him.',
    'Is there a cell or after hours number for emergencies? No listing anywhere shows one.',
    'The coupon. His page says "Present this coupon at time of service"; the new site has no coupon to '
    'print, so it says "Mention it when you call". Confirm that is fine.',
    'Does he have anything physical from the early years, an old advert, an invoice, letterhead, the '
    'original licence certificate? A photo of any of it would prove 1963 rather than just asserting it.',
    'His current contact and referral forms POST over plain HTTP, so names, emails and phone numbers '
    'travel in clear text. The new site fixes this, but the old one should come down once it does.',
]
