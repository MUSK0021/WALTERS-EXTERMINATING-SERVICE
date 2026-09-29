
==============================================================================
OWN-SITE  (22 site-affecting)
==============================================================================

### Site structure: complete page inventory
  The live site is exactly 8 pages on an obsolete Trellix / Web.com Site Builder platform (meta
  generator="Trellix Site Builder"). Nav on every page: "Home | About Us | Services and Programs
  | Bed Bug Information | Specials/Coupons | Referrals | Contact Us | Pictures". Files:
  index.html (Home), id1.html (About Us), id2.html (Services and Programs), id72.html (Bed Bug
  Information), id21.html (Specials/Coupons), id17.html (Referrals), id4.html (Contact Us),
  id70.html (Pictures). I fetched all 8 and extracted every link; there are no other internal
  links and the Wayback CDX index for the whole domain lists no page files beyond these 8. No
  orphan pages.
  > NOTE: Nav order differs from content.py NAV. Their own order puts Bed Bug Information third,
  > and they have Specials/Coupons, Referrals and Pictures pages that content.py has no
  > equivalent for.
  src: http://www.bugwalters.com/

### Tagline exact punctuation
  CORRECTION. The site never uses a comma. Homepage: "Don't Be Bugged-Bug Us!" (hyphen, no
  spaces). About Us page: "Dont't Be Bugged - Bug Us!" (typo "Dont't", spaced hyphen). Alignable
  profile: "Don't be Bugged- Bug Us!!" (double exclamation). Wayback 2025-07-10 homepage
  capture: "Don't Be Bugged - Bug Us!".
  > NOTE: content.py has "Don't Be Bugged, Bug Us!" with a comma, which matches NO published
  > version. Four different punctuations exist in the wild. Pick one deliberately and tell Nolan
  > you normalised it.
  src: http://www.bugwalters.com/

### The founding YEAR claim has changed over time
  CONTRADICTION IN THEIR OWN HISTORY. The earliest Wayback capture (23 Feb 2009) of the homepage
  says: "Our business was established in 1967, and we pride ourselves on providing our customers
  with a personalized service." There is no mention of 1963 or of Harvey Walters anywhere in the
  2009 page. The 1963 / April / Harvey Walters story first appears later.
  > NOTE: IMPORTANT. This is almost certainly where the stray "1967" in the current EPA sentence
  > comes from: the site used to claim 1967 as the founding year, then the date was changed to
  > 1963 and the orphaned 1967 was rewritten into a bogus EPA regulation claim. Worth asking
  > Nolan which year is right before the new site hard-commits to 1963.
  src: https://web.archive.org/web/20090223090134id_/http://www.bugwalters.com/

### Alignable listing of "PO Box 42, Huntingdon Valley, PA 19006"
  CONFIRMED, with a casing correction. The profile exists at the URL below and its JSON-LD reads
  verbatim: "address":{"@type":"PostalAddress","streetAddress":"PO box
  42","addressLocality":"Huntingdon Valley","addressRegion":"PA","postalCode":"19006"},"sameAs":
  "www.bugwalters.com","telephone":"215 947-8818 ". Page heading: "Nolan Walters / Walters
  Exterminating Service LLC / Huntingdon Valley, PA".
  > NOTE: Their own words render it "PO box 42" with a lowercase b. The phone matches, and
  > sameAs points at bugwalters.com, so this is genuinely their listing and not a similar
  > business. Still: a PO Box on a third-party directory is not the same as consent to publish
  > it on their website. Keep it off the site unless Nolan says otherwise.
  src: https://www.alignable.com/huntingdon-valley-pa/walters-exterminating-service-llc

### FALSE EPA claim is STILL LIVE on the homepage
  Verbatim, currently live: "In 1967 the E.P.A required all Pest control companies to be
  Licensed by the State, and to this same day our State Company License number is #BU0014-".
  Also present in the Wayback capture of 10 Jul 2025 and in captures going back years.
  > NOTE: Confirms the previous pass was right to delete it. The EPA was created 2 December
  > 1970, so it cannot have acted in 1967; pesticide-applicator licensing in PA derives from the
  > Pennsylvania Pesticide Control Act of 1973. Keep it deleted. Flag to Nolan that it is still
  > live on the old site.
  src: http://www.bugwalters.com/

### FALSE "14th person tested" claim is live as a STATED FACT, not a quote
  Verbatim, currently live on the homepage: "My Father was the 14th person to be tested and
  granted a Pest Control License in the state of Pa." It is presented as plain fact in the body
  copy, not attributed or hedged. The 10 Jul 2025 capture has the same sentence with the typo
  "Licince", since corrected.
  > NOTE: Confirms the claim is genuinely theirs and long-standing. I found no public record
  > supporting it. content.py's rule 5 (attributed quote only) is the right call and is now
  > backed by the exact source wording.
  src: http://www.bugwalters.com/

### "Certified in I.P.M." and "Certified in Food Handling" are still live, and misspelled
  Services and Programs page, verbatim: "Bed Bug SpecialistCertified in Food Handleing and
  Restaurants Cerified in I.P.M (Intergrating Pest Management )". Their typos: "Handleing",
  "Cerified", "Intergrating", plus a missing line break running "Specialist" into "Certified".
  > NOTE: Confirms both claims were real and are still live. Note they also get the acronym
  > wrong: IPM is Integrated Pest Management, not "Intergrating". Neither is a recognised PA
  > certification category as worded, so content.py's rule 8 holds.
  src: http://www.bugwalters.com/id2.html

### "Our 63rd Year" is live and is off by one
  Homepage, currently live: "Our 63rd Year in the Pest Management Business". Their Alignable
  profile instead says "Celebrating our 64th year family Business" and "My father started
  Walters Exterminating Service / Over 64 years ago". Founded April 1963, so as of September
  2026 they have completed 63 years and are in their 64th.
  > NOTE: Their own two channels disagree by one. Alignable is arithmetically correct.
  > Vindicates content.py rule 1: never hard-code the number, compute it from FOUNDED.
  src: http://www.bugwalters.com/

### Evidence that the hard-coded year counter goes stale for years at a time
  The Wayback capture of 10 July 2025 still read: "2017 - is our 54th Year in the Pest
  Management Business My Father (Harvey Walters - Founder) In April 1963 (54 years ago)
  Founded...". So the counter sat frozen at 2017 for roughly eight years before being updated to
  "63rd Year".
  > NOTE: Concrete proof of the failure mode content.py rule 1 exists to prevent. Useful to show
  > Nolan.
  src: https://web.archive.org/web/20250710234601id_/http://www.bugwalters.com/

### Services offered, in their own words
  Services and Programs page, complete and verbatim: "Residential and Commericial" / "Inside and
  Outside Programs" / "Bed Bug Specialist" / "Certified in Food Handleing and Restaurants" /
  "Cerified in I.P.M (Intergrating Pest Management )" / "Homes,Apartments,Condos,Rentals" /
  "Offices,Warehouses,Restaurants,Bars" / "Insects, Rodents, and Small Animal Management
  Programs".
  > NOTE: That is the entire services list. There is no termite service named anywhere on the
  > current site, despite "Termite" being in the original 1963 trading name. Do not add termite
  > work without asking Nolan.
  src: http://www.bugwalters.com/id2.html

### Complete list of pests named on the site
  Services page list, verbatim and in their order: "Roaches / Ants / Bees / Wasps / Hornets /
  Silver Fish / Earwigs / Spiders / Fleas / Ticks / Bed Bugs / Crickets / Millipedes / Rats /
  Mice / Groundhogs / Raccoons / Squirrels / Pantry Pests". A photo on the same page is
  captioned "Bald Faced Hornet Nest".
  > NOTE: 19 pests. "Silver Fish" is their spelling (normally Silverfish). "Bald Faced Hornet
  > Nest" is an image caption, NOT a service line, so do not list it as a service. Notably
  > absent: termites, mosquitoes, stink bugs, carpenter ants, moths, flies, birds.
  src: http://www.bugwalters.com/id2.html

### Exact coupon / special offer and its terms
  Specials/Coupons page, complete and verbatim: heading "Here are our specials. Check back
  often, we're constantly updating this page." Coupon block: "WALTERS EXTERMINATING SERVICE LLC
  / INTERNET SPECIAL / $10.00 OFF INITIAL SERVICE* / Present this coupon at time of service."
  Terms: "* Applies to new customers only." and "Coupons and specials cannot be combined with
  other offers."
  > NOTE: That is the whole offer. There is NO expiry date and NO minimum spend. There is
  > exactly one coupon, not several, despite the plural heading. The page also carries a coupon-
  > print form posting to http://svcs.myregisteredsite.com/svcs/coupon_print.jsp.
  src: http://www.bugwalters.com/id21.html

### Referral programme terms
  Referrals page, complete and verbatim: "Many clients are referred to us by another satisfied
  client. Recommendations have allowed us to build a business family unique in terms of
  character, responsibility, and awareness. So if you have friends or relatives who would be
  interested in our services, just use the form below to let us know who they are. We're sure
  they would appreciate your recommendation and so would we."
  > NOTE: CRITICAL: there is NO reward, discount, credit or incentive of any kind. It is a
  > goodwill referral form only. Do not invent a "refer a friend and get X" offer for the new
  > site.
  src: http://www.bugwalters.com/id17.html

### Referral form fields
  POST form with fields: "Your information:" Full name, Email address, Telephone number, and a
  radio pair "Can we use your name? Yes / No". Then "Your friend's information:" Full name,
  Email address, Telephone number, Comments. Submits to
  http://svcs.myregisteredsite.com/svcs/formproc.jsp.
  > NOTE: The "Can we use your name?" consent toggle is a nice touch worth preserving. Note the
  > form collects a THIRD PARTY's name, email and phone without that person's consent, which is
  > a privacy problem worth raising with Nolan.
  src: http://www.bugwalters.com/id17.html

### Contact form fields
  Contact Us page, verbatim intro: "Here's how to get in touch with us:" ... "Or use the form
  below and we will get back to you as soon as we can. We look forward to hearing from you."
  Fields: Full name, Email address, "Comment or question:", radio pair "What is the best way to
  contact you? By email / By phone", and "If by phone, please provide number and best time of
  day to contact you?". Closing line: "Thank you for visiting our web site!"
  > NOTE: Bug in their form: the phone-and-best-time question and the main "Comment or question"
  > box are BOTH named "comments" in the HTML, so the two textareas collide on submit and one
  > answer is likely lost.
  src: http://www.bugwalters.com/id4.html

### Stated hours of operation
  There is NO hours block anywhere on the site. The only scheduling language is on About Us,
  verbatim: "We offer a personalized service at a value price, with scheduling for weekdays, and
  Saturdays for your convenience. We can offer a one hour window in our scheduling so as to
  minimize any interference with your schedule."
  > NOTE: So: weekdays and Saturdays, no opening or closing times, no Sunday mention. The one-
  > hour window in content.py's PROMISES is confirmed, but note their wording is the softer "We
  > CAN offer a one hour window", not a guarantee. Do not publish specific clock hours.
  src: http://www.bugwalters.com/id1.html

### Pictures page contents
  Page <title> and heading are both "Pictures 1963-2025". It contains 5 captioned photos:
  "Nolan- (Bossman) @1977 in company shirt", "Nolan Walters IN ACTION 2020", "The Bug-Man always
  learning 2024", "My Father Harvey and Me 2010", "Bed Bugs". Interleaved with them are SIX
  unedited Trellix template placeholders, live on the page: "Enter subhead content here", "Enter
  content here" (x4) and "Enter supporting content here".
  > NOTE: The placeholders appear on NO other page. The "1963-2025" in the title is a second
  > hard-coded date that is already stale. "My Father Harvey and Me 2010" is a usable, datable
  > photo of Harvey with Nolan.
  src: http://www.bugwalters.com/id70.html

### Bed Bug Information page content
  Opens with the species name "Cimex Lectularius", then three sections: "What are Bed Bugs?",
  "Where do they hide?", and "Treatment & Services". Closing call to action, verbatim: "If you
  suspect bed bugs in your home/facility, we strongly recommend contacting our office to
  schedule a professional inspection. Treating bed bugs with home remedies and store bought
  pesticides usually does little more than scatter the bed bugs deeper into the walls making
  them much more difficult to fully eradicate. For professional results / solutions, use our
  Contact Us page to obtain no obligation information."
  > NOTE: The first two sections read as generic purchased stock copy ("So what are bed bugs,
  > anyway? Everyone has heard of them.") and are not in the voice of the rest of the site. The
  > final paragraph IS in their voice and contains the only substantive promise: a professional
  > inspection and "no obligation information". Species should be styled Cimex lectularius,
  > lowercase epithet.
  src: http://www.bugwalters.com/id72.html

### HTTPS is completely broken on both hostnames
  https://www.bugwalters.com/ and https://bugwalters.com/ both fail TLS verification. The
  certificate presented covers only DNS:*.sites.myregisteredsite.com and
  DNS:sites.myregisteredsite.com. Plain HTTP returns 200 on both www and the apex
  (http://bugwalters.com/ returns 200 without redirecting to www).
  > NOTE: The site is HTTP-only and browsers will flag it as Not Secure. This also broke
  > WebFetch, which force-upgrades to HTTPS. There is no canonical host: www and apex both serve
  > 200 independently, which is a duplicate-content problem.
  src: https://www.bugwalters.com/

### Both web forms transmit personal data unencrypted
  The Contact and Referral forms both POST to http://svcs.myregisteredsite.com/svcs/formproc.jsp
  over plain HTTP, with no TLS. The endpoint still responds 200. Names, email addresses and
  phone numbers, including a referred third party's, travel in clear text.
  > NOTE: Worth raising with Nolan directly as the single most urgent problem with the existing
  > site. The new site must not replicate this.
  src: http://www.bugwalters.com/id4.html

### The site-search box on every page is dead
  Every page carries a search widget with radio options "This site" and "The Web", posting to
  http://search.web.com/searchresults.aspx. That host does not respond: curl times out with no
  bytes received after 20 seconds.
  > NOTE: A visibly broken control on all 8 pages. Web.com retired the legacy search service.
  > Drop it from the new site rather than porting it.
  src: http://www.bugwalters.com/

### Complete list of typos and errors still live on the site
  Homepage: "we maintain strict confidentially" (confidentiality); "We hope you\"ll find" (a
  straight double-quote used as an apostrophe); "Pest Control . In 1967" (space before the
  period); "#BU0014- My Father" (hyphen used as a dash). About Us: "PA Department of Agiculture"
  (Agriculture); "Dont't Be Bugged - Bug Us!" (Don't); "Montgomery County,and Lower Bucks"
  (missing space); "our customer's needs" (should be customers'). Services: "Commericial"
  (Commercial); "Bed Bug SpecialistCertified" (missing break); "Food Handleing" (Handling);
  "Cerified" (Certified); "Intergrating Pest Management" (Integrated); "Silver Fish"
  (Silverfish). Bed Bug page: "Cimex Lectularius" (lowercase epithet). Pictures: six unedited
  template placeholders.
  > NOTE: 16 distinct defects. The "you\"ll" and "confidentially" errors have survived unchanged
  > since at least the February 2009 capture.
  src: http://www.bugwalters.com/id1.html

==============================================================================
GOOGLE-LISTING  (11 site-affecting)
==============================================================================

### Exact business name as listed on Google
  "Walters Exterminating Services" — plural "Services", and NO "LLC".
  > NOTE: CORRECTION to working facts. The legal/site name is "WALTERS EXTERMINATING SERVICE
  > LLC" (singular, with LLC) per bugwalters.com. Bing and Birdeye also use the plural
  > "Services"; Yelp uses singular "Walters Exterminating Service". Three different name forms
  > are live across listings. Use the legal name on the site, but be aware searchers see the
  > plural.
  src: https://www.google.com/maps?cid=15215549394653833153&hl=en

### Google address / service-area status
  City-level only: "Abington, PA 19001, United States", plus the plus-code "4VJ7+H5 Abington,
  Abington Township, PA, USA". No street address, no suite, no PO Box.
  > NOTE: CONFIRMS the "no published street address" working fact for Google. Note the locality
  > is Abington, PA 19001 — NOT Huntingdon Valley 19006. Yelp, Birdeye, Bing and Chamber of
  > Commerce all also say Abington 19001. Nothing in any map listing corroborates the Alignable
  > "PO Box 42, Huntingdon Valley, PA 19006".
  src: https://www.google.com/maps?cid=15215549394653833153&hl=en

### Phone number on Google
  +1 215-947-8818
  > NOTE: CONFIRMS the working fact (215) 947-8818. Same number independently on Bing Maps,
  > Yelp, Chamber of Commerce, AllPages and his LinkedIn profile, and on bugwalters.com itself
  > as "Phone: 215 947-8818".
  src: https://www.google.com/maps?cid=15215549394653833153&hl=en

### Owner's own description of the business (Yelp, owner-written)
  "We are a Family Company started in 1963. We offer Pest Management for Residential and
  commercial license and insured No contacts Don't Be Bugged - Bug Us !! 215 947-8818"
  > NOTE: Useful owner-voice corroboration of: founded 1963, family company, residential AND
  > commercial, licensed and insured, no contracts. "No contacts" is plainly a typo for "No
  > contracts" — corroborated by the Google review that praises not having to "sign a forever
  > contract". Do not reproduce the typo.
  src: https://www.yelp.com/biz/walters-exterminating-service-abington

### Tagline exact punctuation
  bugwalters.com renders it "Remember Don't Be Bugged-Bug Us!" (hyphen). Yelp owner text renders
  it "Don't Be Bugged - Bug Us !!" (spaced hyphen, two exclamation marks).
  > NOTE: MINOR CORRECTION to working facts. The working fact records it with a comma — "Don't
  > Be Bugged, Bug Us!" — but no source I found uses a comma. Both owner-controlled sources use
  > a hyphen. Either adopt the hyphen or ask Nolan which form he wants; do not silently keep the
  > comma.
  src: http://bugwalters.com/

### Owner name, generation and "Bug-Man" nickname
  bugwalters.com: "Nolan Walters 2nd generation Owner - Walters Exterminating Service LLC". His
  LinkedIn profile title is "Nolan (The Bug-Man) Walters - Walters Exterminating Service LLC",
  Job Title: Owner, listing 215-947-8818 and www.bugwalters.com.
  > NOTE: CONFIRMS the working facts (Nolan Walters, 2nd generation, "the Bug-Man"). The
  > nickname is self-applied on his own LinkedIn profile, so it is safe to use. LinkedIn profile
  > URL verified via search result only (LinkedIn blocks unauthenticated fetch):
  > https://www.bing.com/search?q=%22Nolan%22+Walters+linkedin+%22Walters+Exterminating%22
  src: http://bugwalters.com/

### Founding facts still live on bugwalters.com
  "Our 63rd Year in the Pest Management Business My Father (Harvey Walters - Founder) In April
  1963 Founded Walters Exterminating Termite and Pest Control ."
  > NOTE: CONFIRMS founded April 1963, by Harvey Walters, original trading name "Walters
  > Exterminating Termite and Pest Control". Also note the live site says "63rd Year" — 1963 +
  > 63 = 2026, which is internally consistent for the current year.
  src: http://bugwalters.com/

### The false EPA/1967 claim is still live on the client's current site
  Verbatim from bugwalters.com: "In 1967 the E.P.A required all Pest control companies to be
  Licensed by the State, and to this same day our State Company License number is #BU0014- My
  Father was the 14th person to be tested and granted a Pest Control License in the state of
  Pa."
  > NOTE: CONFIRMS the previous pass was right to delete the 1967 EPA sentence — the EPA was not
  > created until Dec 1970 and PA licensing derives from the Pennsylvania Pesticide Control Act
  > of 1973. Two things worth separating: (1) licence number BU0014 is asserted by the owner on
  > his own site and is consistent with the working fact; (2) the "14th person tested in PA"
  > story is in the same sentence and remains unverified — keep it as an attributed quote only,
  > exactly as the working facts say.
  src: http://bugwalters.com/

### Review theme 1 — speed of response on urgent stinging-insect jobs
  The strongest and most repeated theme. Google's own auto-generated topic chip is "wasp nest
  removal (2)". Danielle Kay (Google, 6 years ago) describes finding a large hornet nest at
  night and being fitted in the same day. Shannon Dunn (Google, 5 years ago) describes a
  wasp/yellow-jacket nest in a retaining wall after a vacation and says they came out the next
  day.
  > NOTE: Both of these review texts are truncated by Google at "… More" signed-out, so I am
  > summarising the visible portion rather than quoting them in full. Strong argument for giving
  > stinging insects / same-day urgency real prominence on the site.
  src: https://www.google.com/maps/place/Walters+Exterminating+Services/@40.1314063,-75.1370551,17z/data=!4m8!3m7!1s0x89c6b06eaaaaaaab:0xd3287d8f1ac067c1!8m2!3d40.1314063!4d-75.1370551!9m1!1b1!16s%2Fg%2F1tfpw6rc?hl=en

### Review theme 2 — honesty, fair pricing, and no long-term contract
  Repeated across both platforms. Representative: Big Harve (Google, 4 years ago) — "Honest and
  reliable. On time and educated me about bugs." Robert Spinrad (Google, 4 years ago) — "Great
  service, honest, and very reasonable." Jerry D. (Yelp, May 6 2025) — "a little old school but
  super effective and reliable. Fair pricing".
  > NOTE: The "no forever contract" point is one of the two quotes Google itself surfaces in its
  > review summary, and it matches the owner's own Yelp copy ("No contacts" = no contracts).
  > This is the single most defensible differentiator to lead with.
  src: https://www.yelp.com/biz/walters-exterminating-service-abington

### Review theme 3 — knowledgeable, educates the customer, punctual and clean
  Google's second auto-topic chip is "knowledgeable staff (2)". Allison K. (Yelp, Sep 26 2023) —
  "Wonderfully helpful in scheduling, sweetest receptionist. Walters is so kind, clean, and
  thorough." Kimiya R. (Yelp, Feb 7 2017) praises punctuality and depth of bug knowledge at
  length.
  > NOTE: "On time" and "clean" recur independently across reviewers years apart. The Allison K.
  > mention of a receptionist suggests there is someone answering the phone besides Nolan —
  > worth checking with him, as it bears on the 'we answer the phone' angle.
  src: https://www.yelp.com/biz/walters-exterminating-service-abington

==============================================================================
DIRECTORIES  (9 site-affecting)
==============================================================================

### No published street address exists anywhere
  REFUTED. MapQuest publishes "Walters Exterminating Service, 1833 Carwithan St, Philadelphia,
  PA 19152-1105, US" with a map pin, click-to-call and breadcrumb "Philadelphia County >
  Philadelphia > 19152". Superpages publishes the same address in its page title: "Walters
  Exterminating Service 1833 Carwithan St ... - Superpages". A third directory snippet repeats
  "Walters Exterminating Service. 1833 Carwithan St. Philadelphia, PA."
  > NOTE: This is the single biggest correction. The working note says the absence of a street
  > address is deliberate; that intent may well be real, but the factual claim that it is
  > published nowhere is wrong. The site must not assert "we publish no address". Separately,
  > flag to Nolan that this address is already public on at least three aggregators — 19152 is a
  > residential part of Northeast Philadelphia, so this is plausibly his home or base, and he
  > may want to know it is exposed. Do NOT put it on the new site.
  src: https://www.mapquest.com/us/pennsylvania/walters-exterminating-service-544565150

### Alignable lists "PO Box 42, Huntingdon Valley, PA 19006"
  CONFIRMED. Exact text on the Alignable listing card: "PO box 42 Huntingdon Valley, PA 19006"
  (lowercase "box", no comma after 42). It appears on the Products & Services sub-page, not the
  main profile — the main profile shows only "Huntingdon Valley, PA".
  > NOTE: Verbatim capitalisation differs from the working note. If the site ever shows a
  > mailing address, this is the only PO box found and it is self-published by Nolan, so it is
  > the safest one to use — but still ask him.
  src: https://www.alignable.com/huntingdon-valley-pa/walters-exterminating-service-llc/walters-exterminating-service-llc

### A BBB profile exists
  DENIED. BBB search returns "No results for \"Walters Exterminating\" in \"Huntingdon Valley,
  PA\"". A second search scoped to Philadelphia, PA returns the page title "Search Again, No
  Results Found | Better Business Bureau" and "Sorry we didn't find any businesses or charities
  that match your search."
  > NOTE: Two independent metro searches. No BBB profile, therefore no accreditation, no BBB
  > letter grade and no BBB badge. The previous pass was right to delete it. Philadelphia
  > search: https://www.bbb.org/search?find_country=USA&find_text=Walters+Exterminating&find_loc
  > =Philadelphia%2C+PA
  src: https://www.bbb.org/search?find_country=USA&find_text=Walters+Exterminating&find_loc=Huntingdon+Valley%2C+PA

### Tagline is "Don't Be Bugged, Bug Us!"
  CORRECTED. No source uses a comma. The homepage uses "Don't Be Bugged-Bug Us!"; the About page
  uses "Dont't Be Bugged - Bug Us!" (sic, typo in original); Alignable uses "Don't be Bugged-
  Bug Us!!"; Nextdoor uses "Don't Be Bugged - Bug US!!"; the Facebook group uses "Don't be
  Bugged –Bug us".
  > NOTE: Every variant uses a dash, never a comma. The most common and cleanest rendering is
  > "Don't Be Bugged - Bug Us!". Worth matching his own punctuation rather than inventing a
  > comma.
  src: https://www.bugwalters.com/index.html

### "Certified in I.P.M." and "Certified in Food Handling" are not claims the client makes
  REFUTED — both are live on the client's own Services page right now, verbatim: "Certified in
  Food Handleing and Restaurants" and "Cerified in I.P.M (Intergrating Pest Management )" (typos
  in original).
  > NOTE: The previous pass deleted these as false. They are unverifiable from any independent
  > source and the wording does not match any real PA credential — PA certification categories
  > are numbered, and there is no PA "IPM certification". But they are Nolan's own standing
  > claims, so deleting them silently changes his marketing. Raise it with him rather than just
  > dropping it: ask which numbered categories he actually holds.
  src: https://www.bugwalters.com/id2.html

### The 1967 EPA licensing claim was invented and is not the client's
  REFUTED as to origin — it is the client's own homepage text, verbatim: "In 1967 the E.P.A
  required all Pest control companies to be Licensed by the State, and to this same day our
  State Company License number is #BU0014- My Father was the 14th person to be tested and
  granted a Pest Control License in the state of Pa."
  > NOTE: The statement is still factually false — the EPA was created in December 1970, and PA
  > licensing flows from the PA Pesticide Control Act of 1973. Correct to delete it from the new
  > site. But it is Nolan's own long-standing copy, so he should be told it is being removed and
  > why, not have it vanish. Note the site's actual wording is "the 14th person to be tested and
  > granted a Pest Control License", which is slightly stronger than the working note's "14th
  > person tested".
  src: https://www.bugwalters.com/index.html

### Which town the business is associated with
  FOUR-WAY DISAGREEMENT. Alignable: "Huntingdon Valley, PA" (PO box 42, 19006). Yelp / MapQuest
  / Manta: "Abington, PA 19001", MapQuest breadcrumb "Montgomery County > Abington > 19001".
  MapQuest second listing / Superpages / Yellow Pages: "Philadelphia, PA 19152", breadcrumb
  "Philadelphia County > Philadelphia > 19152". Nextdoor: "Rockledge, PA".
  > NOTE: Worse than the two-way Abington-vs-Huntingdon Valley split the working notes
  > anticipated. All four are within a few miles of each other in the Northeast Philadelphia /
  > eastern Montgomery fringe, which is consistent with a van-based business with no storefront.
  > Strong argument for naming no home town at all and describing the service area instead.
  src: https://nextdoor.com/pages/walters-exterminating-service-llc-rockledge-pa/

### No-contract / no-salesmen / free-quote policy
  CONFIRMED verbatim on the company's own About page: "No sales people will call. No contracts
  are required." Also: "We can offer a one hour window in our scheduling so as to minimize any
  interference with your schedule." and "our goal is 100% customer satisfaction". Alignable adds
  "Licensed and insured".
  > NOTE: The one-hour scheduling window is a concrete, verifiable differentiator already
  > published by the client and currently missing from content.py. Good candidate for the new
  > site. Note content.py's FAQ answer about free quotes is still marked ASK NOLAN — the About
  > page confirms no contracts and no salespeople but does not actually confirm that quotes are
  > free.
  src: https://www.bugwalters.com/id1.html

### Licensing authority
  CONFIRMED. Company About page: "We are licensed by the PA Department of Agiculture." (sic).
  The PA Department of Agriculture confirms the framework: "All businesses ... which are
  required to have commercial or public applicators to apply pesticides need to have a pesticide
  application business license", requiring "at least one certified applicator, meet financial
  responsibility (insurance) required, and pay $35 application fee initially (and annually)."
  > NOTE: Confirms BU0014 is a business licence requiring a named certified applicator and
  > current insurance, which supports the "licensed and insured" line. It also means the licence
  > is renewed annually — so "we still carry that number" implies continuous renewal since the
  > 1970s, which only the state registry can prove. The registry lookup is at http://cedatarepor
  > ting.pa.gov/reports/powerbi/Public/AG/PI/PBI/Pesticide%20Application%20Businesses but needs
  > a real browser.
  src: https://www.pa.gov/agencies/pda/plants-land-water/plant-industry/pesticide-programs/pesticide-application-businesses

==============================================================================
ENTITY  (11 site-affecting)
==============================================================================

### Founded April 1963 by Harvey Walters, originally trading as "Walters Exterminating Termite and Pest Control"
  Homepage, verbatim: "My Father (Harvey Walters - Founder) In April 1963 Founded Walters
  Exterminating Termite and Pest Control ."
  > NOTE: Confirmed as the business's own first-person claim — which is the right standard for a
  > company history page. Founder name, month, year and original trading name all match
  > content.py exactly. Independently echoed on Alignable: "We are a family Pest Management
  > Company started in 1963".
  src: http://bugwalters.com/

### Service area: Northeast Philadelphia, eastern Montgomery County, lower Bucks County
  About Us page, verbatim: "Our company is family owned and operated and was established in 1963
  to provide efficient low cost solutions to businesses and individuals in Northeast
  Philadelphia, Eastern Montgomery County,and Lower Bucks County."
  > NOTE: Exact match to content.py. Safe to publish as-is.
  src: http://bugwalters.com/id1.html

### Phone (215) 947-8818 and email info@bugwalters.com
  Homepage: "e-mail: info@bugwalters.com" and "Phone: 215 947-8818". Contact page repeats:
  "Telephone: 215 947-8818 / Email: info@bugwalters.com".
  > NOTE: Both appear on two separate pages of their own site and match content.py.
  src: http://bugwalters.com/id4.html

### No published street address (deliberate)
  CONFIRMED on their own site. The Contact Us page lists ONLY phone, email and a contact form —
  "Here's how to get in touch with us: Telephone... Email... Or use the form below". No address
  anywhere on it.
  > NOTE: The no-address policy is real and should be preserved on the new site — despite the
  > registry address above and the junk directory addresses below.
  src: http://bugwalters.com/id4.html

### Tagline exact wording
  The site does NOT use the comma form in content.py. Homepage reads "Don't Be Bugged-Bug Us!"
  (hyphen). Alignable reads "Don't be Bugged- Bug Us!!". Nextdoor reads "Don't Be Bugged - Bug
  US!!".
  > NOTE: content.py has "Don't Be Bugged, Bug Us!" with a comma — that exact punctuation
  > appears on none of the three sources. Not a falsehood, but if the tagline is set in type as
  > a brand mark it is worth matching what he actually writes, or asking him which he prefers.
  src: http://bugwalters.com/

### Licensed by the PA Department of Agriculture as a pesticide application business
  About Us, verbatim: "We are licensed by the PA Department of Agiculture." (misspelling in
  original). Homepage: "our State Company License number is #BU0014".
  > NOTE: Confirmed as their own claim, and the licensing AGENCY is right — PA Dept of
  > Agriculture, not EPA. BU0014 itself I could NOT independently verify against the state
  > register (see dead_ends).
  src: http://bugwalters.com/id1.html

### The false EPA/1967 claim is still live on the current site
  Homepage, verbatim: "In 1967 the E.P.A required all Pest control companies to be Licensed by
  the State, and to this same day our State Company License number is #BU0014".
  > NOTE: The previous pass was RIGHT to delete this and should hold the line. The EPA was
  > created Dec 1970, three years after 1967, and has never licensed pest-control firms in PA.
  > Expect pushback from Nolan since it is his own long-standing copy — worth framing to him as
  > 'this is the one thing on the old site a competitor could call out'.
  src: http://bugwalters.com/

### Nolan Walters, 2nd generation owner, nicknamed "the Bug-Man"
  Homepage: "Nolan Walters 2nd generation Owner". Nickname confirmed repeatedly in his own
  Alignable posts: "The Bug-Man", "From the Bug-Man", "From Nolan Walters (The Bug-Man)". His
  LinkedIn headline is indexed as "Nolan (The Bug-Man) Walters".
  > NOTE: Self-applied nickname, used publicly and often. Safe.
  src: https://www.alignable.com/huntingdon-valley-pa/walters-exterminating-service-llc

### "Certified in I.P.M." and "Certified in Food Handling" (deleted by previous pass)
  DELETION WAS CORRECT. The underlying sources describe SERVICE CATEGORIES, never
  certifications. Alignable, his own words: "service Residential ,Commercial,Food Handing
  ,Restaurants and are Bed Bug Specialist". His LinkedIn is indexed as "Residential / Commercial
  / Food Handling / Restaurants / IPM Specialist".
  > NOTE: "IPM Specialist" and "services food handling premises" are marketing descriptors;
  > "Certified in" asserts a credential that no source supports. Keep them deleted. He could
  > truthfully say the company treats restaurants and food-handling premises and works to IPM
  > principles.
  src: https://www.alignable.com/huntingdon-valley-pa/walters-exterminating-service-llc

### Operational details usable as site copy
  About Us, verbatim: "We offer a personalized service at a value price, with scheduling for
  weekdays, and Saturdays for your convenience. We can offer a one hour window in our scheduling
  so as to minimize any interference with your schedule. No sales people will call. No contracts
  are required."
  > NOTE: Directly relevant to the FAQ at content.py line 454 (the ASK NOLAN about whether no-
  > contract holds). His own current site already states "No contracts are required" and "No
  > sales people will call" unconditionally, plus Saturday availability and a one-hour arrival
  > window — all sourceable to him.
  src: http://bugwalters.com/id1.html

### bugwalters.com has no working HTTPS
  Fetching https://bugwalters.com fails with a certificate mismatch: the certificate presented
  covers only "DNS:*.sites.myregisteredsite.com, DNS:sites.myregisteredsite.com". The site loads
  over plain http:// only.
  > NOTE: Observed directly and repeatedly. The current site is on a Network Solutions / web.com
  > sitebuilder with no valid cert for the domain, so browsers flag it as insecure — and the
  > Contact Us page collects names, emails and phone numbers over unencrypted HTTP. Worth
  > raising: the new site must serve valid HTTPS on the apex domain before that form goes live.
  src: http://bugwalters.com/

==============================================================================
OWNER  (4 site-affecting)
==============================================================================

### Years Nolan has been in the business / when he took over
  Nolan's own Alignable profile, "How We Got Started": "My father started Walters Exterminating
  Service / Over 64 years ago / I'm a second-generation owner / With over 40 full time years in
  the business -"
  > NOTE: (e) PARTLY ANSWERED. "Over 40 full time years" is Nolan's own wording and is safe to
  > publish. The handover DATE from Harvey is NOT stated in any source I found — no source
  > anywhere gives a year Nolan took over. content.py line 464 says "more than forty years"
  > which is safe; do not add a handover year.
  src: https://www.alignable.com/huntingdon-valley-pa/walters-exterminating-service-llc

### "NO published street address anywhere (deliberate)"
  REFUTED. Three different addresses are published by third parties: (1) PA corporate registry —
  "1680 Huntingdon Pike Unit 231, Huntingdon Valley, 19006, PA"; (2) Alignable structured data —
  "PO box 42", Huntingdon Valley, PA, 19006; (3) Bing/Yelp/Chamber/MapQuest/Manta — "19001
  Woodland Rd, Abington, PA 19001-3013"
  > NOTE: The half that HOLDS: bugwalters.com itself publishes no address on any of its 8 pages,
  > including Contact Us (http://bugwalters.com/id4.html shows only phone and email). Keep the
  > new site address-free. But the premise "nowhere" is wrong, and the three disagree — the
  > "19001 Woodland Rd" one is plainly a data-entry artifact (the 19001 ZIP reused as a house
  > number). PROVENANCE WARNING on the OpenCorporates URL: my browser tab landed on that page
  > without my navigating to it, so I treat it as untrusted; I tried to confirm it at the
  > primary source and could not (see dead_ends).
  src: https://opencorporates.com/companies/us_pa/3981492

### Saturday hours, one-hour appointment window, no contracts, no sales calls
  About Us, verbatim: "We offer a personalized service at a value price, with scheduling for
  weekdays, and Saturdays for your convenience. We can offer a one hour window in our scheduling
  so as to minimize any interference with your schedule." and "No sales people will call. No
  contracts are required."
  > NOTE: NEW / USEFUL. This directly backs content.py line 454's no-contract claim and line
  > 95's "Nobody will call you to sell you something" — that ASK NOLAN flag can be downgraded,
  > it is his own published copy. The Saturday availability and the one-hour window are strong
  > selling points not currently surfaced. Note: an aggregator lists "Mon - 8:00 am - 5:00 pm,
  > Tue - 8:00 am -..." and Bing's panel says "Open · Closes 23:59" — both third-party and
  > unreliable; do not publish specific hours without asking Nolan.
  src: http://bugwalters.com/id1.html

### Interviews, podcasts, speaking, awards, local press
  None found. The only third-party write-up in existence is the mysmallbusinesspodcast.com blog
  post, which despite the domain name has no audio or video — og:type is "blog" and the page
  contains no <audio>, <video> or <iframe> element.
  > NOTE: ANGLE RESULT: there is no press coverage, no awards, no speaking, no real podcast
  > appearance. Do not imply media presence. The richest source of Nolan in his own voice is
  > Alignable, where he has answered 9 questions — e.g. May 26, 2020: "We never closed / We very
  > busy it's ant 🐜 season !! / The Bug-Man"; Feb 22, 2020: "From the Bug-Man / Business is
  > great - the Warmer weather this winter is keeping us very busy!!"; Oct 8, 2021: "Nothing but
  > I will always think of ways to better teach the team and new ways to approach issues that's
  > fresh and positive solutions". These are genuinely his and are better raw material than the
  > marketing blog.
  src: https://mysmallbusinesspodcast.com/post/walters-exterminating-service-over-40-years-of-trusted-pest-management

==============================================================================
MARKET  (21 site-affecting)
==============================================================================

### Tagline exact punctuation
  Homepage: "Don't Be Bugged-Bug Us!" About page: "Dont't Be Bugged - Bug Us!" (their typo). The
  site never uses a comma.
  > NOTE: content.py uses "Don't Be Bugged, Bug Us!" with a comma. Not a factual error, but it
  > is not what the business writes. Either adopt the hyphen form or get Nolan to bless the
  > comma. Worth one line in ASK NOLAN since a tagline is the one string a customer might
  > recognise letter for letter.
  src: https://bugwalters.com/index.html

### Company age currently published on the live site
  "Our 63rd Year in the Pest Management Business"
  > NOTE: Now stale. Founded April 1963, so April 2025 began the 63rd year and April 2026 began
  > the 64th. As of today the live site understates their age by one year. This is exactly the
  > failure house rule 1 exists to prevent, and it confirms the rule was right. The Pictures
  > page is dated "Pictures 1963-2025", stale in the same way.
  src: https://bugwalters.com/index.html

### $10 coupon terms
  "INTERNET SPECIAL $10.00 OFF INITIAL SERVICE* Present this coupon at time of service." / "*
  Applies to new customers only." / "Coupons and specials cannot be combined with other offers."
  > NOTE: COUPON in content.py says "Mention it when you call". Their own terms say "Present
  > this coupon at time of service". Minor but it is a term of an offer, so either match their
  > wording or confirm the change with Nolan.
  src: https://bugwalters.com/id21.html

### PA applicator Category 11 expressly covers food handling establishments
  "(11) Household and health related - The use of a pesticide in, on or around a food handling
  establishment, a human or nonagricultural animal dwelling, an institution such as a school or
  hospital, an industrial establishment, a warehouse, a grain elevator and other types of
  structures whether public or private... The use of a rodenticide or avicide is permitted in
  this category. The use of a pesticide in outdoor perimeter treatments to control pests, which
  may infest the structure, is included."
  > NOTE: This CORRECTS the previous pass's framing. "Certified in Food Handling" is not an
  > invention; it is a garbled reference to Category 11, which really is the category covering
  > food handling establishments and restaurants. Category 11 also explicitly covers
  > rodenticides and exterior perimeter treatments, which is precisely the work Walters
  > describes. Once Nolan confirms he holds Category 11, the site can say so accurately and it
  > is a genuinely strong credential. There is still NO category called "I.P.M." and none called
  > "Food Handling" - the correct name is the one above.
  src: https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/007/chapter128/s128.42.html&d=reduce

### PA applicator Category 12 is the termite category
  "(12) Wood destroying pests - The use of a pesticide to control or prevent termites, powder
  post beetles or other wood destroying pests infesting a residence, school, hospital, store,
  warehouse or other structures..."
  > NOTE: Relevant because the business originally traded as "Walters Exterminating Termite and
  > Pest Control" yet the new site's SERVICES list has no termite service. Add to ASK NOLAN:
  > does he hold Category 12, and does he still do termite work? Other categories a pest firm
  > may hold: 13 Structural fumigation, 15 Public health vertebrate pest control, 16 Public
  > health invertebrate pest control.
  src: https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/007/chapter128/s128.42.html&d=reduce

### bugwalters.com has a broken TLS certificate
  Fetching https://bugwalters.com returns: "Hostname/IP does not match certificate's altnames:
  Host: bugwalters.com. is not in the cert's altnames: DNS:*.sites.myregisteredsite.com,
  DNS:sites.myregisteredsite.com". The site is a Trellix Site Builder page hosted on web.com
  infrastructure.
  > NOTE: Not a content fact, but it matters more than most content facts. Every visitor on
  > https today gets a full-page browser security warning before they see anything. Whoever cuts
  > over to the new site must make sure the certificate matches bugwalters.com. Add to ASK
  > NOLAN: who controls the domain and hosting.
  src: https://bugwalters.com/index.html

### Additional real Northeast Philadelphia neighbourhoods available if the list needs to look denser
  Lower Northeast also includes Castor Gardens, Crescentville, Frankford, Juniata, Lawncrest,
  Lawndale, Lexington Park, Northwood, Ryers, Wissinoming and Bridesburg. Far Northeast also
  includes Ashton-Woodenbridge, Byberry, Crestmont Farms, Holme Circle, Krewstown, Millbrook,
  Modena Park, Morrell Park, Normandy, Pennypack, Pine Valley and Upper Holmesburg.
  > NOTE: Lawncrest, Holme Circle, Krewstown, Pennypack, Upper Holmesburg and Byberry are names
  > a local would immediately recognise and are natural additions. Only add what Nolan actually
  > covers.
  src: https://en.wikipedia.org/wiki/Northeast_Philadelphia

### Northeast Philadelphia's boundaries, for the service-area page prose
  "Northeast Philadelphia is bounded by the Delaware River on the east, Bucks County on the
  north, and Montgomery County on the west. The southern limit is given as Frankford/Tacony
  Creek or Adams Avenue." The city planning commission splits it into Lower Northeast and Far
  Northeast and "The demarcation line between the two sections is typically given as Pennypack
  Creek."
  > NOTE: Useful and locally credible: the Northeast literally borders both of the other two
  > counties Walters serves, which is a one-sentence explanation of why the service area is
  > shaped the way it is. Also note "Far Northeast" is in everyday local use while "Near
  > Northeast" is not - locals say Lower Northeast.
  src: https://en.wikipedia.org/wiki/Northeast_Philadelphia

### "Newtown" is ambiguous in Pennsylvania and needs its county shown
  A ZIP lookup for the city name "Newtown, PA" returns two ZIPs: 18940 and 19073. 18940 is
  Newtown, Bucks County. 19073 is Newtown Square, Delaware County, on the far side of
  Philadelphia.
  > NOTE: Keep "Newtown" inside the visibly labelled Lower Bucks County group so it can never
  > read as Newtown Square. Separately, a local would more often file Newtown and Yardley under
  > Central or Upper-Lower Bucks than plain "lower Bucks" - not wrong, but if authenticity is
  > the goal, consider whether Nolan really drives that far north.
  src: https://api.zippopotam.us/us/pa/newtown

### Competitor: Grove Pest Control publishes full hours and a street address, and already claims Walters' two differentiators
  "Happily serving Willow Grove, Abington, Huntingdon Valley, Warminster, Warrington, Ivyland,
  Richboro, Rydal, Meadowbrook, Wyndmoor, and Northeast Philadelphia." / "No strict contracts,
  just customer satisfaction." / "Don't expect a hard sales pitch from us." / "128 Gilpin Road,
  Willow Grove, PA 19090, 1-215-237-6831" / "Monday 8:00AM-5:00PM" through "Saturday
  8:00AM-5:00PM"
  > NOTE: The single most important competitive finding. This is a direct neighbour covering
  > Walters' exact eastern-Montgomery core plus Northeast Philadelphia, running an almost
  > identical pitch, but publishing Monday-to-Saturday 8-5 hours and a real address. Walters'
  > "no contracts, no sales people" is therefore not a differentiator in this market - the
  > differentiator is 63 years and two generations. And Walters is losing on the basics: no
  > hours published anywhere. They also publish seasonal local blog posts ("Mice in Abington",
  > "Ants Are Here", "Keep Ticks Away On The Trails In Willow Grove").
  src: https://grovepestcontrol.com/

### Competitor: Terminators Pest Control, Bensalem, publishes an address, a dated founder timeline and service promises but no hours or prices
  "Since 1975, Terminators Pest Control has been more than a pest control company, we're your
  neighbors." / "Trusted by your neighbors for over 50 years." / "LICENSED AND INSURED", "SAME
  DAY SERVICE OPTIONS", "FAMILY AND PET FRIENDLY", "Three generations of dedication." / timeline
  entries 1975, 1991, 1998, TODAY / "4201 Neshaminy, Blvd #273 Bensalem, PA 19020" / phone
  215-781-3115
  > NOTE: Their dated timeline is the same device content.py's TIMELINE uses, which validates
  > the approach. Two things they publish that Walters does not: "Licensed AND INSURED" (Walters
  > only ever says licensed - ASK NOLAN whether he carries liability insurance, because it is
  > cheap to say and customers look for it) and same-day service. They also run a DIY product
  > store as a certified Nature-Cide botanical partner. No hours and no prices anywhere on the
  > homepage.
  src: https://www.terminatorspestcontrol.com/

### Competitor: WebLock Pest Control publishes a full price list, full hours and a written guarantee
  Prices: one-time general pest control "$125 - $200"; quarterly plan "$90 - $140 / visit";
  every-other-month "$80 - $110 / visit"; bed bug single room "$400 - $700"; bed bug whole home
  "$1,200 - $2,500"; mouse exclusion "$450 - $900"; rat "$550 - $1,200"; German cockroach "$250
  - $650"; wasp/hornet nest "$125 - $250"; in-ground yellow jacket "$150 - $300"; mosquito
  monthly Apr-Oct "$75 - $95 / visit"; tick yard "$85 - $140 / visit". Hours: "Mon-Fri 7:00 AM -
  8:00 PM, Sat 8:00 AM - 6:00 PM, Sun: Emergency calls only". Guarantee: "If they come back, we
  come back... Bed bug treatments are guaranteed for 30 days after the 3rd visit. Mouse
  exclusion jobs come with a 60-day guarantee. Wasp/hornet single-nest removal carries a 30-day
  re-treat guarantee." Also "free 15-minute inspection", price "in writing before any work
  starts", and "No contract lock-in".
  > NOTE: IMPORTANT CAVEAT: I could not establish WebLock as an established operator. No street
  > address, a gmail contact address, and a very new-looking marketing site. Treat it as
  > evidence of what a modern competitor publishes, NOT as a benchmark of a long-standing local
  > firm. Its value is the shape of the disclosure: a price band per service rather than a
  > single number, named plan tiers, and guarantees with explicit day counts. If Nolan will give
  > even three or four bands, that is the biggest content win available after hours.
  src: https://weblockpestcontrol.com/pricing

### Competitor: Patriot Pest Solutions publishes free inspections, protection plans and free emergency response between visits
  "We stand behind our work which is why we offer free initial inspections and estimates so you
  know exactly how severe your pest problem is. Patriot Pest Solutions also will provide you
  with customized home protection plans that can help prevent future pest incidents, inspect for
  termites on a yearly basis and even give you emergency responses for free between regular
  visits." / "We're a local, veteran owned and family operated business with over 50 years of
  pest control experience." / "Proud to be Women Owned!" / "156 W Ridge Pike  Limerick, PA
  19468"
  > NOTE: NOT a direct competitor in Walters' towns despite the page title. Their published
  > Bucks County list is UPPER Bucks (Perkasie, Quakertown, Sellersville, Souderton, Telford)
  > and their Montgomery list overlaps Walters only at Hatboro. Use them for what they publish,
  > not as a local rival. Two ideas worth stealing honestly: "Termite Certifications - WDI's for
  > Real Estate Transfers" is a high-intent local search Walters says nothing about, and an
  > organic/low-toxicity option is offered by two of the six competitors.
  src: https://www.patriotpestsolutions.net/bucks-county-pennsylvania-pest-control/

### What competitors publish that Walters currently does not, across the six examined
  Business hours (Grove: Mon-Sat 8-5; WebLock: Mon-Fri 7-8, Sat 8-6, Sun emergency only). A
  street address (Grove, Terminators, Patriot). Published prices or bands (WebLock only). Named
  service plans or tiers (WebLock quarterly and every-other-month; Patriot "home protection
  plans"). A written guarantee with stated durations (WebLock; Patriot's free emergency response
  between visits). "Licensed AND insured" (Terminators, WebLock, Patriot - Walters says licensed
  only). Free inspection or estimate as an explicit offer (WebLock, Patriot). Same-day or same-
  week response (Terminators, WebLock). Termite WDI certification for real estate transfers
  (Patriot). An organic or botanical option (Terminators, Patriot). Seasonal local blog content
  (Grove, WebLock).
  > NOTE: Ranked by effort-to-value for Walters: 1) hours, the single biggest gap and free to
  > fix; 2) "and insured", if true, one word; 3) a free inspection or free estimate line, if
  > true; 4) price bands, hardest but highest differentiation; 5) a termite/WDI page if he still
  > does Category 12 work. NO competitor in this set publishes financing, so not offering it
  > costs Walters nothing.
  src: https://grovepestcontrol.com/

### Termite swarm season in Pennsylvania
  "In Pennsylvania, swarms of winged termites usually emerge between February and June." and
  "During late winter or early spring, swarms of the reproductive caste may be noticed in
  infested buildings."
  > NOTE: Penn State Extension, page updated 24 June 2026. Note the window is February to June,
  > wider and earlier than the common "spring" shorthand. A February termite page is publishable
  > and locally useful.
  src: https://extension.psu.edu/eastern-subterranean-termites

### Carpenter ant season in Pennsylvania
  "Winged males and females emerge from established colonies on warm days in the spring and
  early summer." "Approximately 200 to 400 winged ants develop in the summer, remain in the nest
  through the winter, and leave the nest the following spring or early summer." "Check basement,
  attic, garage, and building exterior from May through July..."
  > NOTE: Penn State Extension, updated 24 June 2026. The "May through July" inspection window
  > is a concrete, citable hook for a spring ants page. Careful: this is carpenter ants
  > specifically, not the pavement and odorous house ants people usually mean by "ants in
  > spring".
  src: https://extension.psu.edu/carpenter-ants

### Wasp and hornet season peaks in late summer in Pennsylvania
  Eastern yellowjacket: "In Pennsylvania, overwintered queens begin nest development in May or
  early June, depending on the spring temperatures. The first brood of workers appears in
  June... Males are produced in August/September, closely followed by a brood of new queens."
  Baldfaced hornet: "In the spring, fertilized queens that have overwintered... become active
  and begin to build a nest. As the summer progresses, the colony grows until there may be 100
  to 400 workers."
  > NOTE: Both from Penn State Extension. Supports a late-summer stinging-insect push: the
  > colony is largest in August and September, which is exactly when homeowners notice it.
  > Directly relevant because Walters' own Services page already features a "Bald Faced Hornet
  > Nest" photo - see https://extension.psu.edu/baldfaced-hornet for the hornet quote.
  src: https://extension.psu.edu/eastern-yellowjacket

### Spotted lanternfly calendar in Pennsylvania
  "The eggs are laid in the fall (September to December) and hatch in the spring (late April to
  June)." "In Pennsylvania, SLF adults begin to emerge in July and remain active as adults until
  they are killed by hard freezes later in the fall." Also "Spotted lanternflies, SLF, hatch
  from their egg masses in May" and "These nymphs undergo four instars (growth stages) before
  becoming adults in August or September."
  > NOTE: Penn State Extension Management Guide, recommendations current as of June 2024. Gives
  > a clean two-season content calendar: egg-mass scraping September to December, hatch and
  > nymph treatment late April to June, adults July until hard frost. The nymph-stage quotes are
  > from https://extension.psu.edu/spotted-lanternfly-nymph-lookalikes
  src: https://extension.psu.edu/spotted-lanternfly-management-guide

### Spotted lanternfly quarantine covers the whole service area, and businesses may need a permit
  "SLF is currently found in 56 counties in Pennsylvania, all of which are under a state-imposed
  quarantine." "The quarantine is in place to stop the movement of SLF to new areas within or
  out of the current quarantine zone." Penn State also links "Does Your Business Need a Spotted
  Lanternfly Permit? Find out if your business or organization is required to have a spotted
  lanternfly permit in Pennsylvania."
  > NOTE: Philadelphia, Bucks and Montgomery are all inside the quarantine. Add to ASK NOLAN:
  > does Walters hold a PA spotted lanternfly permit? If he does, that is a real, verifiable,
  > locally meaningful credential - and unlike "Certified in I.P.M." it actually exists. Do not
  > state the county names as quarantined without checking the current PDA county list; I
  > confirmed only the 56-county statewide figure.
  src: https://extension.psu.edu/spotted-lanternfly

### Brown marmorated stink bug is the autumn home-invader with a citable date range
  "It also becomes a nuisance pest of homes as it is attracted to the outside of houses on warm
  fall days in search of protected, overwintering sites and can enter houses in large numbers."
  "Adults begin to search for overwintering sites starting in September through October."
  "...first collected in September of 1998 in Allentown, but probably arrived several years
  earlier."
  > NOTE: A strong autumn page, and better sourced than mice-in-autumn which I could not verify
  > at all. The Allentown 1998 detail is a genuine eastern-Pennsylvania hook. Note stink bugs
  > are not currently in the SERVICES pest lists on the new site - ASK NOLAN whether he treats
  > them.
  src: https://extension.psu.edu/brown-marmorated-stink-bug

### Full pest list currently published by Walters, for checking the new site's coverage
  "Roaches  Ants  Bees Wasps Hornets Silver Fish Earwigs Spiders Fleas Ticks Bed Bugs Crickets
  Millipedes Rats Mice Groundhogs Raccoons Squirrels Pantry Pests" plus "Insects, Rodents, and
  Small Animal Management Programs" and property types "Homes,Apartments,Condos,Rentals" and
  "Offices,Warehouses,Restaurants,Bars".
  > NOTE: Compare against the new site's lists. Notable: their own site claims bees, wasps,
  > hornets, fleas, ticks, millipedes, rats, groundhogs, raccoons and squirrels, and the
  > commercial property types "Offices, Warehouses, Restaurants, Bars". Also notable for what is
  > absent: no termites and no mosquitoes, despite the original company name containing
  > "Termite". Worth confirming with Nolan before the new site either drops or adds anything
  > here.
  src: https://bugwalters.com/id2.html