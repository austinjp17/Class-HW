
import random
from random import choice
import time

material = ['SAND', 'DUST', 'LEAVES', 'PAPER', 'TIN', 'ROOTS', 'BRICK', 'STONE', 'DISCARDED CLOTHING', 'GLASS', 'STEEL', 'PLASTIC', 'MUD', 'BROKEN DISHES', 'WOOD', 'STRAW', 'WEEDS']

location = ['IN A GREEN, MOSSY TERRAIN', 'IN AN OVERPOPULATED AREA', 'BY THE SEA', 'BY AN ABANDONED LAKE', 'IN A DESERTED FACTORY', 'IN DENSE WOODS', 'IN JAPAN', 'AMONG SMALL HILLS', 'IN SOUTHERN FRANCE', 'AMONG HIGH MOUNTAINS', 'ON AN ISLAND', 'IN A COLD, WINDY CLIMATE', 'IN A PLACE WITH BOTH HEAVY RAIN AND BRIGHT SUN', 'IN A DESERTED AIRPORT', 'IN A HOT CLIMATE', 'INSIDE A MOUNTAIN', 'ON THE SEA', 'IN MICHIGAN', 'IN HEAVY JUNGLE UNDERGROWTH', 'BY A RIVER', 'AMONG OTHER HOUSES', 'IN A DESERTED CHURCH', 'IN A METROPOLIS', 'UNDERWATER']

light_source = ['CANDLES', 'ALL AVAILABLE LIGHTING', 'ELECTRICITY', 'NATURAL LIGHT']

inhabitants = ['PEOPLE WHO SLEEP VERY LITTLE', 'VEGETARIANS', 'HORSES AND BIRDS', 'PEOPLE SPEAKING MANY LANGUAGES WEARING LITTLE OR NO CLOTHING', 'ALL RACES OF MEN REPRESENTED WEARING PREDOMINANTLY RED CLOTHING', 'CHILDREN AND OLD PEOPLE', 'VARIOUS BIRDS AND FISH', 'LOVERS', 'PEOPLE WHO ENJOY EATING TOGETHER', 'PEOPLE WHO EAT A GREAT DEAL', 'COLLECTORS OF ALL TYPES', 'FRIENDS AND ENEMIES', 'PEOPLE WHO SLEEP ALMOST ALL THE TIME', 'VERY TALL PEOPLE', 'AMERICAN INDIANS', 'LITTLE BOYS', 'PEOPLE FROM MANY WALKS OF LIFE', 'NEGROS WEARING ALL COLORS', 'FRIENDS', 'FRENCH AND GERMAN SPEAKING PEOPLE', 'FISHERMEN AND FAMILIES', 'PEOPLE WHO LOVE TO READ']

chance = [
    """There were a lot of things we couldn’t do in an SR-71, but we were the fastest guys on the block and loved reminding our fellow 
    aviators of this fact. People often asked us if, because of this fact, it was fun to fly the jet. Fun would not be the first word 
    I would use to describe flying this plane. Intense, maybe. Even cerebral. But there was one day in our Sled experience when we would 
    have to say that it was pure fun to be the fastest guys out there, at least for a moment. It occurred when Walt and I were flying our 
    final training sortie. We needed 100 hours in the jet to complete our training and attain Mission Ready status. Somewhere over Colorado 
    we had passed the century mark. We had made the turn in Arizona and the jet was performing flawlessly. My gauges were wired in the 
    front seat and we were starting to feel pretty good about ourselves, not only because we would soon be flying real missions but because 
    we had gained a great deal of confidence in the plane in the past ten months. Ripping across the barren deserts 80,000 feet below us, 
    I could already see the coast of California from the Arizona border. I was, finally, after many humbling months of simulators and study
    , ahead of the jet. I was beginning to feel a bit sorry for Walter in the back seat. There he was, with no really good view of the 
    incredible sights before us, tasked with monitoring four different radios. This was good practice for him for when we began flying 
    real missions, when a priority transmission from headquarters could be vital. It had been difficult, too, for me to relinquish control 
    of the radios, as during my entire flying career I had controlled my own transmissions. But it was part of the division of duties in 
    this plane and I had adjusted to it. I still insisted on talking on the radio while we were on the ground, however. Walt was so good 
    at many things, but he couldn’t match my expertise at sounding smooth on the radios, a skill that had been honed sharply with years in 
    fighter squadrons where the slightest radio miscue was grounds for beheading. He understood that and allowed me that luxury. Just to 
    get a sense of what Walt had to contend with, I pulled the radio toggle switches and monitored the frequencies along with him. 
    The predominant radio chatter was from Los Angeles Center, far below us, controlling daily traffic in their sector. While they had us 
    on their scope (albeit briefly), we were in uncontrolled airspace and normally would not talk to them unless we needed to descend into 
    their airspace. We listened as the shaky voice of a lone Cessna pilot asked Center for a readout of his ground speed. Center replied:
    November Charlie 175, I’m showing you at ninety knots on the ground. Now the thing to understand about Center controllers, was that 
    whether they were talking to a rookie pilot in a Cessna, or to Air Force One, they always spoke in the exact same, calm, deep, 
    professional, tone that made one feel important. I referred to it as the “ HoustonCentervoice.” I have always felt that after years of 
    seeing documentaries on this country’s space program and listening to the calm and distinct voice of the Houstoncontrollers, that all
    other controllers since then wanted to sound like that… and that they basically did. And it didn’t matter what sector of the country
    we would be flying in, it always seemed like the same guy was talking. Over the years that tone of voice had become somewhat of a 
    comforting sound to pilots everywhere. Conversely, over the years, pilots always wanted to ensure that, when transmitting, 
    they sounded like Chuck Yeager, or at least like John Wayne. Better to die than sound bad on the radios. Just moments after 
    the Cessna’s inquiry, a Twin Beech piped up on frequency, in a rather superior tone, asking for his groundspeed. Twin Beach, 
    I have you at one hundred and twenty-five knots of ground speed. Boy, I thought, the Beechcraft really must think he is 
    dazzling his Cessna brethren. Then out of the blue, a navy F-18 pilot out of NAS Lemoore came up on frequency. You knew right away 
    it was a Navy jock because he sounded very cool on the radios. Center, Dusty 52 ground speed check Before Center could reply, 
    I’m thinking to myself, hey, Dusty 52 has a ground speed indicator in that million-dollar cockpit, so why is he asking Center 
    for a readout? Then I got it, ol’ Dusty here is making sure that every bug smasher from Mount Whitney to the Mojave knows what
    true speed is. He’s the fastest dude in the valley today, and he just wants everyone to know how much fun he is having in his 
    new Hornet. And the reply, always with that same, calm, voice, with more distinct alliteration than emotion: Dusty 52, Center, 
    we have you at 620 on the ground. And I thought to myself, is this a ripe situation, or what? As my hand instinctively reached 
    for the mic button, I had to remind myself that Walt was in control of the radios. Still, I thought, it must be done – in mere 
    seconds we’ll be out of the sector and the opportunity will be lost. That Hornet must die, and die now. I thought about all of 
    our Sim training and how important it was that we developed well as a crew and knew that to jump in on the radios now would 
    destroy the integrity of all that we had worked toward becoming. I was torn. Somewhere, 13 miles above Arizona, there was a 
    pilot screaming inside his space helmet. Then, I heard it. The click of the mic button from the back seat. That was the very 
    moment that I knew Walter and I had become a crew. Very professionally, and with no emotion, Walter spoke: Los Angeles Center,
    Aspen 20, can you give us a ground speed check? There was no hesitation, and the replay came as if was an everyday request. 
    Aspen 20, I show you at one thousand eight hundred and forty-two knots, across the ground. I think it was the forty-two knots 
    that I liked the best, so accurate and proud was Center to deliver that information without hesitation, and you just knew he was
    smiling. But the precise point at which I knew that Walt and I were going to be really good friends for a long time was when he 
    keyed the mic once again to say, in his most fighter-pilot-like voice: Ah, Center, much thanks, We’re showing closer to nineteen 
    hundred on the money. For a moment Walter was a god. And we finally heard a little crack in the armor of the HoustonCentervoice,
    when L.A.came back with: Roger that Aspen, Your equipment is probably more accurate than ours. You boys have a good one. It all
    had lasted for just moments, but in that short, memorable sprint across the southwest, the Navy had been flamed, all mortal 
    airplanes on freq were forced to bow before the King of Speed, and more importantly, Walter and I had crossed the threshold 
    of being a crew. A fine day’s work. We never heard another transmission on that frequency all the way to the coast. For just one day, it truly was fun being the fastest guys out there.""" ,

    """What the fuck did you just fucking say about me, you little bitch? Ill have you know I graduated top of my class in the Navy Seals, and Ive been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and Im the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. Youre fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and thats just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little clever comment was about to bring down upon you, maybe you would have held your fucking tongue. 
    But you couldnt, you did not, and now youre paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You are fucking dead, kiddo.""" ,

    """I sexually Identify as an Attack Helicopter. Ever since I was a boy I dreamed of soaring over the oilfields dropping hot sticky loads on disgusting foreigners. People say to me that a person being a helicopter is Impossible and I’m fucking retarded but I don’t care, I’m beautiful. I’m having a plastic surgeon install rotary blades, 30 mm cannons and AMG-114 Hellfire missiles on my body. From now on I want you guys to call me “Apache” and respect my right to kill from above and kill needlessly. If you can’t accept me you’re a heliphobe and need to check your vehicle privilege. Thank you for being so understanding.""",
    """The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.""",
    'I\'m not answering the question, but I need help. I\'ve looked this up on several occasions and I still can\'t quite figure out what copypasta is. As near as I can tell, story-length memes? Is it just some elite-level inside joke that TL;DR people will never get? I just don\'t get it. I mean, do people laugh about these?'

]

Number = random.randint(0,100)
print('>>  ' + str(Number))
if Number > 0 and Number < 89:
    print('')
    print('A HOUSE OF ' + random.choice(material))
    print('      ' + random.choice(location))
    print('            USING ' + random.choice(light_source))
    print('                  INHABITED BY ' + random.choice(inhabitants))
    print('')
elif Number > 89:
    string = random.choice(chance)
    for char in string:
        print(char, end='')
        time.sleep(.03)

