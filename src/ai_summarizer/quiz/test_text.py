test_text = [
	"""
		Key Establishment protocols. Définitions
		• Un protocole détablissement de clés (key establishment protocol ou KEP) est celui qui
		met à disposition des entités impliquées un secret partagé (une clé) qui servira comme
		base pour des échanges cryptographiques ultérieurs.
		• Les deux variantes des KEP sont les protocoles de transport de clé (key transport
		protocol ou KTP) et les protocoles de mise en accord (key agreement protocol ou KAP).
		• Un key transport protocol (KTP) est un mécanisme permettant à une entité de créer
		une clé secrète et de la transférer à son (ses) correspondant(s).
		• Un key agreement protocol (KAP) est un mécanisme permettant à deux (ou
		plusieurs) entités de dériver une clé à partir dinformations propres à chaque entité.
		• Key pré-distribution schemes sont ceux où les clés utilisées sont entièrement déterminées
		à priori (p.ex. à partir des calculs initiaux).
		• Dynamic key establishment schemes (DKE) sont ceux où les clés changent pour chaque
		exécution du protocole.
		• Implicit key authentication (ou key authentication): propriété par laquelle une entité est
		assurée que seul(s) son (ses) correspondant(s) peut (peuvent) accéder à une clé secrète.
		Cependant, ceci ne spécifie rien sur le fait de posséder effectivement la clé.
		• Key confirmation: propriété permettant à une entité dêtre sûre que ses correspondants
		sont en possession des clés de session générées
		• Explicit key authentication: = implicit key authentication + key confirmation.
		• Un authenticated KEP est un KEP capable de fournir key authentication.
		• Attaques:
		• Une attaque passive est celle qui essaye de démonter un système cryptographique
		en se limitant à lenregistrement et à lanalyse des échanges.
		• Une attaque active fait intervenir un adversaire qui modifie ou injecte des
		messages.
		• Un protocole est dit vulnérable à un known-key attack si lorsquune clé de session
		antérieure est compromise, il devient possible: (a) de compromettre par une attaque
		passive des clés futures et/ou (b) de monter des attaques actives visant lusurpation
		didentité
		La plupart des protocoles modernes garantissent les propriétés suivantes:
		• Perfect Forward Secrecy (PFS) est une caractéristique qui garantit la confidentialité des
		clés de sessions utilisées par le passé même si les clés long terme (par exemple la clé
		privé du destinataire) est compromise:
		• Future Secrecy: Le protocole garantit la sécurité des échanges ultérieurs (les clés des
		sessions futures sont protégées) même si les clés long terme sont compromises par un
		attaquant passif:
		• Deniability / Repudiability (répudiabilité): A limage des protocoles dauthentification
		Zéro-Knowledge, permet aux entités de garantir lauthentification des échanges sans
		apporter des informations qui permettraient de prouver à un tiers leur participation dans
		léchange cryptographique.
		""", 


	"""Harpy eagles dominate Neotropical rainforests with powerful talons adapted for grabbing monkeys and sloths. 
	Red-crowned cranes perform elaborate duet dances in East Asian wetlands, relying on synchronized calls to reinforce pair bonds. 
	Atlantic puffins nest in cliff burrows, carrying multiple sand eels crosswise in their beaks thanks to specialized tongue spines. 
	Great horned owls are nocturnal generalists in the Americas, using silent flight feathers to ambush rodents and other birds. 
	Scarlet macaws in the Amazon crack hard nuts with massive bills and maintain social cohesion through loud flock calls. 
	Emperor penguins breed on Antarctic sea ice, fasting for weeks while incubating a single egg on their feet. 
	Anna’s hummingbirds in western North America hover with rapid wingbeats and can dive at extreme speeds during courtship displays. 
	Common ravens show tool use and problem-solving, caching food and remembering hundreds of hiding spots. 
	Shoebills stalk lungfish in African swamps, using a broad shoe-shaped bill to deliver crushing bites. 
	Arctic terns migrate from pole to pole each year, logging the longest known migration of any bird. 
	House swifts spend most of their lives airborne, feeding, sleeping, and even mating in flight. 
	Kakapos, flightless parrots from New Zealand, are nocturnal herbivores that boom during lek displays. 
	Secretary birds stride across African savannas, stomping snakes with long legs. Sandhill cranes gather in vast flocks during migration, 
	trumpeting loudly as they feed in wetlands and prairies. Snowy owls irrupt southward in lemming crash years, 
	using keen eyesight to hunt across open tundra and fields.""", 


	"""Keyboard technology
	The technology of computer keyboards includes many
	elements. Many different keyboard technologies have been
	developed to meet consumer demands and optimized for
	industrial applications. The standard full-size (100%)
	computer alphanumeric keyboard typically uses 101 to 105
	keys; keyboards integrated in laptop computers are typically
	less comprehensive.
	Virtual keyboards, which are mostly accessed via a
	touchscreen interface, have no physical switches and provide
	artificial audio and haptic feedback instead. This variety of
	keyboard can prove useful, as it is not limited by the rigid
	nature of physical computer keyboards.
	The majority of modern keyboards include a control processor and indicator lights to provide feedback to
	the user (and to the central processor) about what state the keyboard is in. Plug-and-play technology
	means that its "out of the box" layout can be notified to the system, making the keyboard immediately
	ready to use without the need for further configuration, unless the user so desires. This also enables
	manufacture of generic keyboards for a variety of language markets, that differ only in the symbols
	engraved on the keytops.
	A common membrane design consists of three layers. The top
	and bottom layer have exposed electrical matrix traces, and
	the middle layer is a spacer to prevent current from passing
	through the top and bottom conductive traces passively. When
	pressure is applied to the top membrane, it bridges the top and
	bottom conductive contact pads, allowing current to transfer.
	Two of the most common types of membrane keyboards
	include full-travel rubber dome over membrane and flat-panel
	membrane keyboards. Flat-panel membrane keyboards are
	most often found on appliances like microwave ovens or
	photocopiers.
	Keystroke sensing
	Membrane
	Scissor switch mechanism
	Exploded view of a typical rubber dome
	over membrane design
	Full-travel rubber dome over membrane keyboards are the most common keyboard design manufactured
	today. In these keyboards, a rubber dome sheet is placed above the membranes, ensuring that the domes
	align with the contact pads. The rubber dome serves a dual purpose: it acts as a tactile return spring and
	provides a soft surface to transfer force onto the top membrane. To bridge the connection between the two
	contact pads, the rubber dome must be fully depressed.
	Rubber dome over membrane keyboards became very popular with computer manufacturers as they
	sought to reduce costs while PC prices declined.
	A common, compact variant of rubber dome over membrane
	is the scissor-switch, based on the scissors mechanism. Due to
	the requirement of many notebooks to be slim, they require
	the keyboards to be low-profile. Therefore, this technology is
	most commonly featured on notebooks. The keys are attached
	to the keyboard via two plastic pieces that interlock in a
	"scissor"-like fashion and snap to the keyboard and the
	keycap. These keyboards are generally quiet and the keys
	require little force to press.
	Scissor-switch keyboards are typically slightly more
	expensive. They are harder to clean (due to the limited
	movement of the keys and their multiple attachment points) but also less likely to get debris in them as
	the gaps between the keys are often smaller (as there is no need for extra room to allow for the 'wiggle' in
	the key, as typically found on a membrane keyboard).[1]
	Rubber dome over membrane
	Scissor-switch
	Atari 400 keyboard
	Most keyboards are rigid, but this
	keyboard is flexible.
	Flat-panel membrane keyboards are often used in harsh
	environments where water or leak-proofing is desirable. They
	can have non-tactile, polydome tactile and metal dome tactile
	keys. Polydome tactile membrane switches use polyester, or
	PET, and is formed to create a stiff plastic dome. When the
	stiff polydome is pressed, the conductive ink on the back of
	the polydome connects with the bottom layer of the circuit.
	Metal dome membrane switches are made of stainless steel
	and offer enhanced durability and reliability and can feature
	custom dome designs.[2] Non-tactile flat-panel membrane
	keyboards have little to no keypress feel and often issue a
	beep or flash of light on actuation.
	Although this keyboard design was commonly used in the early days of the personal computer (on the
	Sinclair ZX80, ZX81, and Atari 400), they have been supplanted by more responsive and modern
	designs.
	Computer keyboards made of flexible silicone or
	polyurethane materials can roll up in a bundle. This type of
	keyboard can take advantage of the thin flexible plastic
	membranes, but still pose the risk of damage. When they are
	completely sealed in rubber, they are water resistant. Roll-up
	keyboards provide relatively little tactile feedback. Because
	these keyboards are typically made of silicone, they
	unfavorably tend to attract dirt, dust, and hair.
	[3]
	Keyboards which have metal contact switches typically use discrete modules for each key. This type of
	switch are usually composed of a housing, a spring, and a slider, and sometimes other parts such as a
	separate tactile leaf or clickbar.
	Flat-panel membrane
	Roll-up keyboard
	Metal contact
	Cherry MX Blue (left) and disassembled
	Cherry MX Brown (right)
	Cherry MX switch contacts
	Reed switch with reed module removed
	At rest, the metal contacts inside of the switch are held apart.
	As the switch is pressed down, the contacts are held together
	to conduct current for actuation. Many switch designs use
	gold for contact material to prolong the lifetime of the switch
	by preventing switch failure from oxidization. Most designs
	use a metal leaf, where the movable contact is a leaf spring.
	A major producer of discrete metal contact switches is
	Cherry, who has manufactured the Cherry MX family of
	switches since the 1980s. Cherry's color-coding system of
	categorizing switches has been imitated by other switch
	manufacturers, such as Gateron and Kailh among many
	others.[4][5]
	Keyboards which utilize this technology are commonly
	referred to as "mechanical keyboards", but there is not a
	universally agreed-upon clear-cut definition for this term.[6]
	Since mid-2000s, mechanical keyboards are used by gamers
	and professionals again.[7]
	Hot-swappable keyboards are keyboards in which switches
	can be pulled out and replaced without requiring the typical
	solder connection.[8][9]
	Instead of the switch pins being
	directly soldered to the keyboard's PCB, hot-swap sockets are instead soldered on. Hot-swap sockets can
	allow users to change different switches out of the keyboard without having the tools or knowledge
	required to solder.
	The reed module in a reed switch consists of two metal
	contacts inside of a glass bubble usually sealed with some
	inert gas like nitrogen to help prevent particle build-up. The
	slider in the housing pushes a magnet down in front of the
	reed capsule and the magnetic field causes the reed contacts
	to become attracted to each other and make contact. The reed
	switch mechanism was originally invented in 1936 by W B
	Ellwood at Bell Telephone Laboratories.
	Although reed switches use metal leaf contacts, they are
	considered separate from all other forms of metal contact
	switch because the contacts are operated magnetically instead
	of using physical force from a slider to be pressed together.
	Hot-swappable keyboard
	Reed
	Topre electrostatic capacitive switch
	RAFI RS 76 C 010 hall effect switch fully
	disassembled
	In a capacitive mechanism, pressing a key changes the
	capacitance of a pattern of capacitor pads. The pattern
	consists of two D-shaped capacitor pads for each switch,
	printed on a printed circuit board (PCB) and covered by a
	thin, insulating film of soldermask which acts as a dielectric.
	For the most common, foam and foil implementation of this
	technology, the movable part ends with a flat foam element
	about the size of an aspirin tablet, finished with aluminum
	foil. Opposite the switch is a PCB with the capacitor pads.
	When the key is pressed, the foil tightly clings to the surface of the PCB, forming a daisy chain of two
	capacitors between contact pads and itself separated with a thin soldermask, and thus "shorting" the
	contact pads with an easily detectable drop of capacitive reactance between them. Usually, this permits a
	pulse or pulse train to be sensed.
	An advantage of the capacitive technology is that the switch is not dependent on the flow of current
	through metal contacts to actuate. There is no debouncing necessary.
	The sensor tells enough about the distance of the keypress to allow the user to adjust the actuation point
	(key sensitivity). This adjustment can be done with the help of the bundled software and individually for
	each key, if so implemented.[10] A keyboard which utilizes these abilities include the Real Force RGB.
	IBM's Model F keyboard is a design consisting of a buckling spring over a capacitive PCB, similar to the
	later Model M keyboard, but instead used membrane sensing in place of a PCB.
	The Topre Corporation design for switches uses a conical spring below a rubber dome. The dome
	provides resistance, while the spring does the capacitive action.[11]
	Hall effect keyboards use Hall effect sensors to detect the
	movement of a magnet by the potential difference in voltage.
	When a key is depressed, it moves a magnet that is detected
	by a solid-state sensor. Because they require no physical
	contact for actuation, Hall-effect keyboards are extremely
	reliable and can accept millions of keystrokes before failing.
	They are used for ultra-high reliability applications such as
	nuclear power plants, aircraft cockpits, and critical industrial
	environments. They can easily be made totally waterproof,
	and can resist large amounts of dust and contaminants.
	Because a magnet and sensor are required for each key, as
	well as custom control electronics, they are expensive to
	manufacture.
	Capacitive
	Hall effect
	A hall switch works through magnetic fields. Every switch has a small magnet fixed inside it. When the
	electricity passes through the main circuit, it creates a magnetic flux. Every time a key is pressed, the
	magnetic intensity changes. This change is noticed by the circuit and the sensors send the information to
	the motherboard.[12]
	Optical switch technology was introduced in 1962 by Harley E. Kelchner for use in a typewriter machine
	with the purpose of reducing the noise generated by typewriter keys.
	An optical keyboard technology utilizes light-emitting devices and photo sensors to optically detect
	actuated keys, offering faster response times and eliminating the need for physical contact between
	moving parts. Most commonly the emitters and sensors are located at the perimeter, mounted on a small
	PCB. The light is directed from side to side of the keyboard interior, and it can only be blocked by the
	actuated keys. Most optical keyboards require at least two beams (most commonly a vertical beam and a
	horizontal beam) to determine the actuated key. Some optical keyboards use a special key structure that
	blocks the light in a certain pattern, allowing only one beam per row of keys (most commonly a
	horizontal beam).
	The mechanism of the optical keyboard is very simple – a light beam is sent from the emitter to the
	receiving sensor, and the actuated key blocks, reflects, refracts or otherwise interacts with the beam,
	resulting in an identified key.
	A major advantage of optical switch technology is that it is very resistant to moisture, dust, and debris
	because there are no metal contacts that can corrode.
	The specialist DataHand keyboard uses optical technology to sense keypresses with a single light beam
	and sensor per key. The keys are held in their rest position by magnets; when the magnetic force is
	overcome to press a key, the optical path is unblocked and the keypress is registered.
	A laser projection device approximately the size of a computer mouse projects the outline of keyboard
	keys onto a flat surface, such as a table or desk. This type of keyboard is portable enough to be easily
	used with PDAs and cellphones, and many models have retractable cords and wireless capabilities.
	However, this design is prone to error, as accidental disruption of the laser will generate unwanted
	keystrokes. This type of keyboard's inherent lack of tactile feedback makes it often undesirable.
	The buckling spring mechanism (now expired U.S. patent 4,118,611 (https://patents.google.com/patent/U
	S4118611)) atop the switch is responsible for the characteristic clicky response of the keyboard. This
	mechanism controls a small hammer that strikes a capacitive or membrane switch.[13]
	Optical
	Laser projection
	Notable switch mechanisms
	Buckling spring
	Illustration from the original buckling
	spring U.S. patent 4,118,611 (https://pate
	nts.google.com/patent/US4118611),
	issued to IBM in 1978
	A classic full-size Model M keyboard with
	Spanish ISO key layout
	Snapshot of switch bounce on an
	oscilloscope. The switch bounces
	between on and off several times before
	settling.
	IBM's Model F keyboard series was the first to employ
	buckling spring key-switches, which used capacitive sensing
	to actuate. The original patent was never employed in an
	actual production keyboard but it establishes the basic
	premise of a buckling spring.
	The IBM Model M is a large family of computer keyboards
	created by IBM that began in late 1983 when IBM patented a
	membrane buckling spring key-switch design. The main
	intent of this design was to halve the production cost of the
	Model F.
	[14] The most well known full-size Model M is
	known officially as the IBM Enhanced Keyboard.
	In 1993, two years after spawning Lexmark, IBM transferred
	its keyboard operations to the daughter company. New Model
	M keyboards continued to be manufactured for IBM by
	Lexmark until 1996, when Unicomp was established and
	purchased the keyboard patents and tooling equipment to
	continue their production.
	IBM continued to make Model M's in their Scotland factory until 1999.[15]
	When a key is pressed, it oscillates (bounces) against its
	contacts several times before settling. When released, it
	oscillates again until it comes to rest. Although it happens on
	a scale too small to be visible to the naked eye, it can be
	enough to register multiple keystrokes.
	To resolve this, the processor in a keyboard debounces the
	keystrokes, by averaging the signal over time to produce one
	"confirmed" keystroke that (usually) corresponds to a single
	press or release. Early membrane keyboards had limited
	typing speed because they had to do significant debouncing.
	This was a noticeable problem on the ZX81.
	[16]
	Debouncing
	Keycaps are used on full-travel keyboards. While modern keycaps are typically surface-printed, they can
	also be double-shot molded, laser marked, dye sublimation printed, engraved, or made of transparent
	material with printed paper inserts. There are also keycaps which utilize thin shells that are placed over
	key bases, which were used on several IBM PC keyboards. A more modern but rare innovation is the
	OLED key which, on some specialty devices like stream controller keypads, feature a tiny OLED display
	under each keycap, which can be customized in software to display any icon or glyph the user wishes.
	Due to high cost most of these devices are not full keyboards for typing but are meant for shortcuts for
	launching applications or macro commands for other programs.
	Switches allow for the removal and replacement of keycaps with a common stem type.
	Almost all keyboards which utilize keys two or more units in length (such as the typical space bar or
	enter key) use stabilizers to ensure consistent movement and prevent key wobble during typing. Various
	lubricants and padding techniques can be used to reduce the rattle and ticking of components.
	A modern PC keyboard typically includes a control processor and indicator lights to provide feedback to
	the user about what state the keyboard is in. Depending on the sophistication of the controller's
	programming, the keyboard may also offer other special features. The processor is usually a single chip
	8048 microcontroller variant. The keyboard switch matrix is wired to its inputs and it processes the
	incoming keystrokes and sends the results down a serial cable (the keyboard cord) to a receiver in the
	main computer box. It also controls the illumination of the "caps lock", "num lock" and "scroll lock"
	lights.
	A common test for whether the computer has crashed is pressing the "caps lock" key. The keyboard sends
	the key code to the keyboard driver running in the main computer; if the main computer is operating, it
	commands the light to turn on. All the other indicator lights work in a similar way. The keyboard driver
	also tracks the shift, alt and control state of the keyboard.[17]
	The keyboard switch matrix is often drawn with horizontal wires and vertical wires in a grid which is
	called a matrix circuit. It has a switch at some or all intersections, much like a multiplexed display.
	Keycaps
	Stabilizers
	Other parts
	Keyboard switch matrix
	A close-up of a keyboard matrix circuit
	printed onto a flexible transparent PET
	sheet
	On-screen keyboard controlled with the
	mouse can be used by users with limited
	mobility.
	Almost all keyboards have only the switch (but no diode) at
	each intersection, which causes "ghost keys" and "key
	jamming" when multiple keys are pressed (rollover). Certain,
	often more expensive, keyboards have a diode between each
	intersection, allowing the keyboard microcontroller to
	accurately sense any number of simultaneous keys being
	pressed, without generating erroneous ghost keys.[18]
	Optical character recognition (OCR) is preferable to rekeying
	for converting existing text that is already written down but
	not in machine-readable format (for example, a Linotypecomposed book from the 1940s). In other words, to convert
	the text from an image to editable text (that is, a string of
	character codes), a person could re-type it, or a computer
	could look at the image and deduce what each character is.
	OCR technology has already reached an impressive state (for
	example, Google Book Search) and promises more for the
	future.
	Speech recognition converts speech into machine-readable text (that is, a string of character codes). This
	technology has also reached an advanced state and is implemented in various software products. For
	certain uses (e.g., transcription of medical or legal dictation; journalism; writing essays or novels) speech
	recognition is starting to replace the keyboard. However, the lack of privacy when issuing voice
	commands and dictation makes this kind of input unsuitable for many environments.
	Pointing devices can be used to enter text or characters in contexts where using a physical keyboard
	would be inappropriate or impossible. These accessories typically present characters on a display, in a
	layout that provides fast access to the more frequently used characters or character combinations. Popular
	examples of this kind of input are Graffiti, Dasher and on-screen virtual keyboards.
	Unencrypted Bluetooth keyboards are known to be vulnerable to signal theft for keylogging by other
	Bluetooth devices in range. Microsoft wireless keyboards 2011 and earlier are documented to have this
	vulnerability.
	[19]
	Keystroke logging (often called keylogging) is a method of capturing and recording user keystrokes.
	While it can be used legally to measure employee activity, or by law enforcement agencies to investigate
	suspicious activities, it is also used by hackers for illegal or malicious acts. Hackers use keyloggers to
	Ghost keys
	Alternative text-entering methods
	Other issues
	Keystroke logging
	obtain passwords or encryption keys.
	Keystroke logging can be achieved by both hardware and software means. Hardware key loggers are
	attached to the keyboard cable or installed inside standard keyboards. Software keyloggers work on the
	target computer's operating system and gain unauthorized access to the hardware, hook into the keyboard
	with functions provided by the OS, or use remote access software to transmit recorded data out of the
	target computer to a remote location. Some hackers also use wireless keylogger sniffers to collect packets
	of data being transferred from a wireless keyboard and its receiver, and then they crack the encryption
	key being used to secure wireless communications between the two devices.
	Anti-spyware applications are able to detect many keyloggers and remove them. Responsible vendors of
	monitoring software support detection by anti-spyware programs, thus preventing abuse of the software.
	Enabling a firewall does not stop keyloggers per se, but can possibly prevent transmission of the logged
	material over the net if properly configured. Network monitors (also known as reverse-firewalls) can be
	used to alert the user whenever an application attempts to make a network connection. This gives the user
	the chance to prevent the keylogger from "phoning home" with his or her typed information. Automatic
	form-filling programs can prevent keylogging entirely by not using the keyboard at all. Most keyloggers
	can be fooled by alternating between typing the login credentials and typing characters somewhere else in
	the focus window.
	[20]
	Keyboards are also known to emit electromagnetic signatures that can be detected using special spying
	equipment to reconstruct the keys pressed on the keyboard. Neal O'Farrell, executive director of the
	Identity Theft Council, revealed to InformationWeek that "More than 25 years ago, a couple of former
	spooks showed me how they could capture a user's ATM PIN, from a van parked across the street, simply
	by capturing and decoding the electromagnetic signals generated by every keystroke," O'Farrell said.
	"They could even capture keystrokes from computers in nearby offices, but the technology wasn't
	sophisticated enough to focus in on any specific computer."[21]
	The use of a keyboard may cause serious injury (such as carpal tunnel syndrome or other repetitive strain
	injuries) to the hands, wrists, arms, neck or back.[22] The risks of injuries can be reduced by taking
	frequent short breaks to get up and walk around a couple of times every hour. Users should also vary
	tasks throughout the day, to avoid overuse of the hands and wrists. When typing on a keyboard, a person
	should keep the shoulders relaxed with the elbows at the side, with the keyboard and mouse positioned so
	that reaching is not necessary. The chair height and keyboard tray should be adjusted so that the wrists are
	straight, and the wrists should not be rested on sharp table edges.[23] Wrist or palm rests should not be
	used while typing.[24]
	Some adaptive technology ranging from special keyboards, mouse replacements and pen tablet interfaces
	to speech recognition software can reduce the risk of injury. Pause software reminds the user to pause
	frequently. Switching to a much more ergonomic mouse, such as a vertical mouse or joystick mouse may
	provide relief.
	By using a touchpad or a stylus pen with a graphic tablet, in place of a mouse, one can lessen the
	repetitive strain on the arms and hands."""

]