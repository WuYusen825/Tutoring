"""Content for the Part 2 (听后记录和转述) practice sets.

Single source of truth: build.py turns this into the Markdown sheets, the MP3 audio
and the practice page.

Markup used in the text fields:
  script : " / " marks a sense-group pause (only where there is no punctuation),
           {word} marks the answer to a blank.
  rows   : [n] in a table detail marks blank number n.
  model  : [[...]] marks linking words and reporting verbs worth imitating.
"""

SETS = [
    {
        "id": 1,
        "slug": "set1-sleep",
        "topic_cn": "睡眠建议",
        "theme": "人与自我 · 健康生活",
        "genre": "建议类（Tips）",
        "speaker": "校医 Dr. Lin（女声，美音）",
        "pronoun": "she",
        "voice": "en-US-EmmaNeural",
        "rate": "-24%",
        "title": "Tips on Getting Better Sleep",
        "opening": "The speaker shares some tips on getting better sleep.",
        "script": """
Good afternoon, everyone. I'm Dr. Lin / from the school health center. Many of you are working hard / for the college entrance exam, and some of you tell me / that you often stay up late. But sleep is not a waste of time. While we sleep, our brain sorts out / what we learned during the day / and turns it into long-term {memory}. So today, I'd like to share three tips / on getting better sleep.

First, keep a regular schedule. Try to go to bed and get up / at the same time every day, even on {weekends}. Your body has an inner clock, and a regular schedule / helps it work properly. If you stay in bed until noon on Sunday, you may find it hard / to fall asleep that night.

Second, put away your phone / at least half an hour before bed. The blue light from screens / tells your brain / that it's still daytime, so you feel less {sleepy}. Besides, chatting online / or watching short videos / keeps your mind active. Instead, you can read a paper book / or listen to some soft music.

Third, make your bedroom / a good place for sleep. It should be dark, {quiet} and a little cool. If there's noise outside, earplugs may help. Also, avoid drinks like coffee or strong tea / in the afternoon, because their effect / can last for several hours.

Remember, a good night's sleep / will help you think more clearly / and stay in a better mood. Try these tips tonight, and I believe / you'll feel the difference in class tomorrow. Thank you.
""",
        "rows": [
            {
                "main": "Why sleep matters",
                "table": ["Our brain turns what we learned during the day into long-term [1]."],
                "extras": ["Many students stay up late, but sleep is not a waste of time."],
            },
            {
                "main": "Tip 1: Keep a regular schedule",
                "table": [
                    "Go to bed and get up at the same time every day, even on [2].",
                    "This helps the body's inner clock work properly.",
                ],
                "extras": ["Staying in bed until noon on Sunday makes it hard to fall asleep that night."],
            },
            {
                "main": "Tip 2: Put away your phone",
                "table": [
                    "Do it at least half an hour before bed.",
                    "Blue light from screens makes you feel less [3].",
                ],
                "extras": [
                    "Chatting online or watching short videos keeps your mind active.",
                    "Read a paper book or listen to soft music instead.",
                ],
            },
            {
                "main": "Tip 3: Make your bedroom a good place for sleep",
                "table": [
                    "It should be dark, [4] and a little cool.",
                    "Avoid coffee or strong tea in the afternoon.",
                ],
                "extras": [
                    "Earplugs may help if there's noise outside.",
                    "The effect of coffee or tea can last for several hours.",
                ],
            },
            {
                "main": "Ending",
                "in_table": False,
                "table": [],
                "extras": ["Good sleep helps you think more clearly and stay in a better mood."],
            },
        ],
        "answers": [
            {"word": "memory", "accept": ["memory"], "note": "名词单数：long-term memory"},
            {"word": "weekends", "accept": ["weekends"], "note": "名词复数，别漏 s"},
            {"word": "sleepy", "accept": ["sleepy"], "note": "形容词 less sleepy，不要写成 sleep"},
            {"word": "quiet", "accept": ["quiet"], "note": "安静的；别和 quite（相当）混淆"},
        ],
        "model": """
She [[points out]] that sleep is not a waste of time, [[because]] while we sleep, our brain turns what we learned into long-term memory.

Her [[first]] tip is to keep a regular schedule. We should go to bed and get up at the same time every day, even on weekends, which helps our inner clock work properly. [[For example]], staying in bed until noon on Sunday may make it hard to fall asleep that night.

[[Second]], she [[advises us to]] put away our phones at least half an hour before bed, [[because]] blue light from screens makes us feel less sleepy. We can read a paper book [[instead]].

[[Third]], our bedroom should be dark, quiet and a little cool, and earplugs may help if it's noisy outside. We'd [[also]] better avoid coffee or strong tea in the afternoon.

[[Finally]], she [[says]] good sleep helps us think more clearly and stay in a better mood.
""",
        "pitfalls": [
            "说话人是女校医，全程用 she / her，不要 he、she 混用。",
            "原文是对“你”说的祈使句，转述时要换成转述结构：Keep a regular schedule. → Her first tip is to keep a regular schedule. / She advises us to …",
            "you 转述成 we / us（说话人和学生是一方），不要照搬 “you should …”。",
            "填空拼写：weekends 要加 s；quiet（安静）≠ quite（相当）。",
        ],
        "vocab": [
            ("inner clock", "生物钟"),
            ("stay up late", "熬夜"),
            ("earplugs", "耳塞"),
            ("in a better mood", "心情更好"),
        ],
    },
    {
        "id": 2,
        "slug": "set2-central-axis",
        "topic_cn": "北京中轴线",
        "theme": "人与社会 · 历史与文化",
        "genre": "介绍类（事物介绍）",
        "speaker": "讲座主讲人（男声，英音）",
        "pronoun": "he",
        "voice": "en-GB-RyanNeural",
        "rate": "-12%",
        "title": "The Beijing Central Axis",
        "opening": "The speaker gives an introduction to the Beijing Central Axis.",
        "script": """
Hello, everyone, and welcome to today's lecture. In July 2024, the Beijing Central Axis / was added to the World Heritage List. Today I'll tell you what it is, why it's special, and how it's being protected.

So, what is the Central Axis? It's an imaginary line / that runs from north to south / through the center of old Beijing. It's 7.8 kilometers long, starting from Yongdingmen in the south / and ending at the Bell and Drum Towers in the north. Along this line / you can find some of the most famous buildings in the city, such as the Forbidden City, Tiananmen and Jingshan Park.

Why is it so special? First, it has a long history. The planning of the axis / began in the Yuan Dynasty, more than 700 years ago, and it kept growing / in the centuries that followed. Second, it shows the traditional Chinese idea of {balance}. Buildings on the east and west sides of the line / are arranged like mirror images, and the most important buildings / sit right in the middle. For example, the Temple of Heaven stands on the east, while the Temple of Agriculture stands on the west. Third, it's still full of life. People live, work and go {shopping} along it / every day.

Protecting such a heritage site / is not easy. In recent years, some buildings that blocked the view / were {removed}, and old courtyards along the axis / were repaired. Digital technology / is also playing a part. Visitors can now take a {virtual} tour online / and see how the axis looked / hundreds of years ago.

So next time you walk along the axis, remember that you are walking through / seven centuries of history. Thank you.
""",
        "rows": [
            {
                "main": "What it is",
                "table": [
                    "An imaginary line running from north to south through old Beijing",
                    "7.8 kilometers long; famous buildings like the Forbidden City stand along it",
                ],
                "extras": [
                    "It was added to the World Heritage List in July 2024.",
                    "It runs from Yongdingmen in the south to the Bell and Drum Towers in the north.",
                ],
            },
            {
                "main": "Why it is special",
                "table": [
                    "History: its planning began more than 700 years ago.",
                    "Design: it shows the Chinese idea of [1].",
                    "Daily life: people live, work and go [2] along it.",
                ],
                "extras": [
                    "Its planning began in the Yuan Dynasty and kept growing in later centuries.",
                    "Buildings on the two sides are like mirror images; the most important ones sit in the middle.",
                    "Example: the Temple of Heaven on the east, the Temple of Agriculture on the west.",
                ],
            },
            {
                "main": "How it is protected",
                "table": [
                    "Some buildings that blocked the view were [3].",
                    "Visitors can take a [4] tour online.",
                ],
                "extras": [
                    "Old courtyards along the axis were repaired.",
                    "Online, visitors can see how the axis looked hundreds of years ago.",
                ],
            },
            {
                "main": "Ending",
                "in_table": False,
                "table": [],
                "extras": ["Walking along the axis means walking through seven centuries of history."],
            },
        ],
        "answers": [
            {"word": "balance", "accept": ["balance"], "note": "名词：the idea of balance（平衡、对称）"},
            {"word": "shopping", "accept": ["shopping"], "note": "go shopping，双写 p"},
            {"word": "removed", "accept": ["removed"], "note": "被动语态 were removed，填过去分词"},
            {"word": "virtual", "accept": ["virtual"], "note": "形容词 a virtual tour（虚拟游览）"},
        ],
        "model": """
He [[mentions]] that it was added to the World Heritage List in July 2024.

[[First]], he explains what it is. It's an imaginary line running from north to south through old Beijing. It's 7.8 kilometers long, from Yongdingmen in the south to the Bell and Drum Towers in the north, and famous buildings like the Forbidden City stand along it.

[[Then]] he tells us why it is special. [[To begin with]], it has a long history, [[because]] its planning began in the Yuan Dynasty more than 700 years ago. [[Besides]], it shows the Chinese idea of balance. [[For example]], the Temple of Heaven on the east side matches the Temple of Agriculture on the west. [[What's more]], it's still full of life, [[since]] people live, work and go shopping along it.

[[Finally]], he talks about how it is protected. Some buildings that blocked the view were removed, and old courtyards were repaired. Visitors can [[also]] take a virtual tour online.
""",
        "pitfalls": [
            "说话人是男主讲人，用 he / his。",
            "被动语态要说对：was added to the World Heritage List / were removed / were repaired。",
            "专有名词（Yongdingmen、the Temple of Agriculture）一时说不出，就用 a famous gate / another temple 带过，千万别停下来卡住。",
            "7.8 kilometers 读作 seven point eight kilometers；700 读作 seven hundred。",
        ],
        "vocab": [
            ("axis", "轴线"),
            ("imaginary", "想象中的；假想的"),
            ("World Heritage List", "《世界遗产名录》"),
            ("courtyard", "院落"),
            ("virtual tour", "虚拟游览"),
            ("the Temple of Agriculture", "先农坛"),
            ("the Bell and Drum Towers", "钟鼓楼"),
        ],
    },
    {
        "id": 3,
        "slug": "set3-swifts",
        "topic_cn": "北京雨燕",
        "theme": "人与自然 · 动物保护",
        "genre": "说明类（问题—措施）",
        "speaker": "观鸟志愿者（女声，英音）",
        "pronoun": "she",
        "voice": "en-GB-SoniaNeural",
        "rate": "-14%",
        "title": "Beijing Swifts",
        "opening": "The speaker is talking about Beijing swifts.",
        "script": """
Hi, everyone. Every April, a special group of guests / returns to Beijing. They are Beijing swifts, the only wild bird / named after our city. Today I'd like to tell you about these amazing birds, the trouble they're facing, and what we can do to help.

Beijing swifts are small dark birds / with long, narrow wings. They are excellent fliers. In fact, they spend most of their lives / in the air. They can eat, drink and even {sleep} while flying, and they seldom land / except to build nests and raise their young. After spending the summer in Beijing, they leave in late July / and fly all the way to southern {Africa} / for the winter. That's a round trip of more than 30,000 kilometers / every year!

However, the number of Beijing swifts / has dropped sharply / over the past few decades. The main reason is / that they are losing their homes. Swifts like to nest in holes / under the roofs of tall old buildings, such as city gates and temples. As many old buildings were pulled down or {repaired}, those holes disappeared.

The good news is / that people are taking action. Scientists have put tiny tracking devices on some swifts / to learn more about their journey. Volunteers have hung up nest {boxes} / under the roofs of buildings. And now, when old buildings are repaired, workers try to keep the holes / for the birds.

You can help, too. Join a bird-watching activity, or simply share what you know / with your friends and family. With our care, the swifts will keep coming back to Beijing / every spring. Thank you.
""",
        "rows": [
            {
                "main": "Amazing birds",
                "table": [
                    "The only wild bird named after Beijing",
                    "They can eat, drink and even [1] while flying.",
                    "In late July, they fly to southern [2] for the winter.",
                ],
                "extras": [
                    "They return to Beijing every April.",
                    "They spend most of their lives in the air and seldom land except to nest.",
                    "The round trip is more than 30,000 kilometers every year.",
                ],
            },
            {
                "main": "The problem",
                "table": [
                    "Their number has dropped sharply.",
                    "They are losing their homes as old buildings were pulled down or [3].",
                ],
                "extras": ["They nest in holes under the roofs of tall old buildings, such as city gates and temples."],
            },
            {
                "main": "Actions taken",
                "table": [
                    "Scientists study their journey with tracking devices.",
                    "Volunteers hang up nest [4].",
                ],
                "extras": ["When old buildings are repaired, workers try to keep the holes for the birds."],
            },
            {
                "main": "What we can do",
                "in_table": False,
                "table": [],
                "extras": [
                    "Join a bird-watching activity or share what we know with friends and family.",
                    "With our care, the swifts will keep coming back every spring.",
                ],
            },
        ],
        "answers": [
            {"word": "sleep", "accept": ["sleep"], "note": "动词原形：can eat, drink and even sleep"},
            {"word": "Africa", "accept": ["Africa"], "note": "专有名词，首字母大写"},
            {"word": "repaired", "accept": ["repaired"], "note": "与 pulled down 并列，被动语态，填过去分词"},
            {"word": "boxes", "accept": ["boxes"], "note": "复数加 -es：nest boxes"},
        ],
        "model": """
[[First]], she tells us that they are amazing birds. They are the only wild bird named after Beijing, and they return to the city every April. They spend most of their lives in the air and can eat, drink and even sleep while flying. In late July, they fly to southern Africa for the winter, which is a round trip of more than 30,000 kilometers.

[[However]], their number has dropped sharply, [[because]] they are losing their homes. They like to nest in holes under the roofs of old buildings, [[but]] as many old buildings were pulled down or repaired, the holes disappeared.

[[Luckily]], people are taking action. Scientists study their journey with tracking devices, volunteers hang up nest boxes, [[and]] workers try to keep the holes when repairing old buildings.

[[Finally]], the speaker [[encourages us to]] join bird-watching activities or share what we know with others.
""",
        "pitfalls": [
            "说话人是女志愿者，用 she；雨燕用 they / their，别把 it 和 they 混着用。",
            "主谓一致：the number of swifts has dropped（the number of 作主语，谓语用单数）。",
            "填空：Africa 首字母大写；boxes 是 box 的复数，加 -es。",
            "30,000 读作 thirty thousand；over the past few decades 用现在完成时 has dropped。",
        ],
        "vocab": [
            ("swift", "雨燕"),
            ("round trip", "往返行程"),
            ("nest", "筑巢；巢"),
            ("tracking device", "追踪装置"),
            ("decade", "十年"),
        ],
    },
    {
        "id": 4,
        "slug": "set4-note-taking",
        "topic_cn": "手写 vs 电脑记笔记",
        "theme": "人与自我 · 学习方法",
        "genre": "研究报告类（研究—结果—原因—建议）",
        "speaker": "教师讲座（男声，美音）",
        "pronoun": "he",
        "voice": "en-US-AndrewNeural",
        "rate": "-18%",
        "title": "A Study on Note-taking",
        "opening": "The speaker is talking about a study on note-taking.",
        "script": """
Good morning, everyone. Do you take notes by {hand} / or on a laptop? Many students believe / that typing is better / because it's faster. But a study by two American psychologists / suggests something different. Let me tell you about it.

In the study, a group of university students / watched some short talks / and took notes as they usually did. Half of them used laptops, while the other half / wrote with pen and paper. About half an hour later, they answered two kinds of questions. Some questions tested facts, such as dates and names. Others tested / whether they really understood / the ideas in the talks.

The results were surprising. On the fact questions, the two groups did {equally} well. But on the understanding questions, the students who wrote by hand / did much better.

Why? The researchers found / that the laptop users typed so fast / that they copied down the speaker's words / almost {exactly}. They were just recording, not thinking. The handwriting group, on the other hand, couldn't write down every word. So they had to listen carefully, pick out the main points / and put them into their own words. This extra thinking / helped them understand and remember better.

So what can we learn from this? It doesn't mean / that laptops are useless. But whether you write or type, don't try to copy everything. Listen for the key ideas / and use your own words. After class, spend a few minutes {reviewing} your notes. That's how notes become knowledge. Thank you.
""",
        "rows": [
            {
                "main": "The study",
                "table": [
                    "Students took notes on laptops or by [1].",
                    "Later, they answered questions about facts and about understanding.",
                ],
                "extras": [
                    "Many students think typing is better because it's faster.",
                    "The study was done by two American psychologists.",
                    "University students watched short talks; the test came about half an hour later.",
                ],
            },
            {
                "main": "The results",
                "table": [
                    "Fact questions: the two groups did [2] well.",
                    "Understanding questions: the handwriting group did much better.",
                ],
                "extras": ["The fact questions tested things like dates and names."],
            },
            {
                "main": "The reasons",
                "table": [
                    "Laptop users copied the speaker's words almost [3].",
                    "Handwriting users had to pick out the main points and use their own words.",
                ],
                "extras": [
                    "Laptop users were just recording, not thinking.",
                    "Handwriting users couldn't write down every word, so they had to listen carefully.",
                    "This extra thinking helped them understand and remember better.",
                ],
            },
            {
                "main": "The advice",
                "table": [
                    "Don't try to copy everything; listen for the key ideas.",
                    "Spend a few minutes [4] your notes after class.",
                ],
                "extras": [
                    "This doesn't mean laptops are useless.",
                    "That's how notes become knowledge.",
                ],
            },
        ],
        "answers": [
            {"word": "hand", "accept": ["hand"], "note": "固定搭配 by hand（手写）"},
            {"word": "equally", "accept": ["equally"], "note": "副词修饰 well，注意双写 l"},
            {"word": "exactly", "accept": ["exactly"], "note": "副词：almost exactly（几乎一字不差）"},
            {"word": "reviewing", "accept": ["reviewing"], "note": "spend time doing，用 -ing 形式"},
        ],
        "model": """
Many students think typing is better because it's faster, [[but]] a study by two American psychologists suggests something different.

In the study, some university students watched short talks. Half of them took notes on laptops, [[while]] the other half took notes by hand. About half an hour later, they answered questions about facts and about understanding.

[[The results showed that]] the two groups did equally well on the fact questions, [[but]] the handwriting group did much better on the understanding questions.

[[The reason is that]] the laptop users copied the speaker's words almost exactly. They were just recording, not thinking. [[In contrast]], the handwriting group couldn't write down every word, [[so]] they had to pick out the main points and use their own words.

[[Therefore]], the speaker [[advises us]] not to copy everything but to listen for the key ideas. We should [[also]] spend a few minutes reviewing our notes after class.
""",
        "pitfalls": [
            "时态分两层：研究过程用一般过去时（watched / took / answered / did better），结论和建议用一般现在时。",
            "对比关系要说出来：while / but / in contrast / on the other hand，否则“两组学生”会讲乱。",
            "填空：equally 双写 l；spend a few minutes reviewing（spend time doing）。",
            "建议部分别照搬 “don't copy everything”，换成 He advises us not to copy everything …",
        ],
        "vocab": [
            ("psychologist", "心理学家"),
            ("take notes", "记笔记"),
            ("pick out", "挑出"),
            ("in one's own words", "用自己的话"),
        ],
    },
    {
        "id": 5,
        "slug": "set5-volunteer",
        "topic_cn": "教老人用手机",
        "theme": "人与社会 · 志愿服务",
        "genre": "经历类（第一人称叙事）",
        "speaker": "学生 Li Na（女声，美音）",
        "pronoun": "she",
        "voice": "en-US-AvaNeural",
        "rate": "-21%",
        "title": "A Volunteer Experience",
        "opening": "The speaker, Li Na, shares her experience as a volunteer last summer.",
        "script": """
Hello, everyone. I'm Li Na from Class 3. Last summer, I joined a volunteer program / in my neighborhood. Our job was to help {elderly} people / use smartphones. At first, I thought it would be easy. After all, I use my phone every day. But I soon found / that I was wrong.

On the first day, I met Mrs. Wang, who was seventy-eight. She wanted to make video calls / with her grandson, who is studying abroad. I showed her the steps quickly, and she nodded. But the next day, she had forgotten everything. I was a little disappointed. Then I realized / that the problem was not with her, but with me. I had gone too fast. Besides, the words on the screen / were too small for her to read, and she was afraid of pressing the wrong {button}.

So I changed my way. First, I made the words on her phone {bigger}. Then I wrote each step on a card / in large letters, so that she could check them at home. And instead of doing things for her, I let her practice / again and again. I also told her how to avoid phone scams, which worried her a lot.

Two weeks later, Mrs. Wang called her grandson / all by herself. She was so excited / that she held my hands / and said thank you many times.

This experience taught me / that {patience} matters more than skills. It also showed me / that the elderly are not slow learners. They just need someone / to walk at their pace. I hope more young people will join us / and help our grandparents / keep up with the digital world. Thank you.
""",
        "rows": [
            {
                "main": "Background",
                "table": [
                    "Last summer, Li Na joined a volunteer program.",
                    "Her job was to help [1] people use smartphones.",
                ],
                "extras": ["At first, she thought it would be easy because she uses her phone every day, but she was wrong."],
            },
            {
                "main": "Difficulties",
                "table": [
                    "Mrs. Wang forgot all the steps the next day.",
                    "The words on the screen were too small, and she was afraid of pressing the wrong [2].",
                ],
                "extras": [
                    "Mrs. Wang, aged 78, wanted to make video calls with her grandson studying abroad.",
                    "Li Na realized the problem was with herself: she had gone too fast.",
                ],
            },
            {
                "main": "Solutions",
                "table": [
                    "She made the words on the phone [3].",
                    "She wrote each step on a card and let Mrs. Wang practice again and again.",
                ],
                "extras": [
                    "The steps were in large letters, so Mrs. Wang could check them at home.",
                    "She told Mrs. Wang how to avoid phone scams.",
                ],
            },
            {
                "main": "Result",
                "table": ["Two weeks later, Mrs. Wang called her grandson by herself."],
                "extras": ["Mrs. Wang was so excited that she held Li Na's hands and said thank you many times."],
            },
            {
                "main": "Lessons",
                "table": [
                    "She learned that [4] matters more than skills.",
                    "The elderly are not slow learners.",
                ],
                "extras": [
                    "They just need someone to walk at their pace.",
                    "She hopes more young people will help grandparents keep up with the digital world.",
                ],
            },
        ],
        "answers": [
            {"word": "elderly", "accept": ["elderly"], "note": "形容词：elderly people（老年人）"},
            {"word": "button", "accept": ["button"], "note": "名词单数：the wrong button"},
            {"word": "bigger", "accept": ["bigger"], "note": "比较级，双写 g"},
            {"word": "patience", "accept": ["patience"], "note": "耐心；别写成 patients（病人）"},
        ],
        "model": """
She joined a program to help elderly people use smartphones. [[At first]], she thought it would be easy, [[but]] she soon found she was wrong.

She met Mrs. Wang, a 78-year-old woman who wanted to make video calls with her grandson abroad. Li Na showed her the steps, [[but]] the next day Mrs. Wang had forgotten everything. Li Na realized she had gone too fast. [[Besides]], the words on the screen were too small, and Mrs. Wang was afraid of pressing the wrong button.

[[So]] Li Na changed her way. She made the words on the phone bigger, wrote each step on a card so that Mrs. Wang could check them at home, and let her practice again and again. [[Two weeks later]], Mrs. Wang called her grandson all by herself.

[[From this experience]], Li Na learned that patience matters more than skills, and that the elderly just need someone to walk at their pace.
""",
        "pitfalls": [
            "第一人称要全部转成第三人称：I → Li Na / she，my → her，me → her。",
            "故事里有两位女性（Li Na 和 Mrs. Wang），多用名字，少用 she，免得指代不清。",
            "叙事用一般过去时；“已经忘了 / 教得太快”用过去完成时 had forgotten / had gone。",
            "填空：bigger 双写 g；patience（耐心）≠ patients（病人）。",
        ],
        "vocab": [
            ("elderly", "年长的；the elderly 老年人"),
            ("phone scam", "电话 / 网络诈骗"),
            ("at one's pace", "按某人的节奏"),
            ("keep up with", "跟上"),
        ],
    },
]


# Memory passages (短文 1–5), printed before the student sheets. Short ones first:
# 3 × 80 words, then 2 × 150 words. Each mirrors the structure of the listening set
# with the same number: tips, introduction, problem–action, study report, experience.
PASSAGES = [
    """
Good morning, everyone. Many students spend hours looking at books and screens, so today I'd like to share three tips on protecting your eyes. First, follow the 20-20-20 rule: every 20 minutes, look at something 20 feet away for 20 seconds. Second, keep your book about 30 centimeters from your eyes, and study in good light. Third, spend two hours outdoors every day, because natural light is good for your eyes. Try these tips, and your eyes will thank you.
""",
    """
Hello, everyone. Today I'd like to introduce Chinese paper cutting, a traditional folk art with a history of more than 1,500 years. With just scissors and red paper, artists can create flowers, animals and lucky characters. During the Spring Festival, people stick paper cuttings on windows and doors to welcome good luck. In 2009, this art was added to UNESCO's list of intangible cultural heritage. Today, many schools offer paper-cutting classes, so the old art is still full of life.
""",
    """
Hi, everyone. Bees are small, but they do a big job. They carry pollen from flower to flower, which helps plants grow fruit and seeds. However, bee numbers have been falling in many places. The main reasons are the loss of wild flowers and the use of chemicals on farms. The good news is that people are taking action. Farmers are using fewer chemicals, and cities are planting more flowers. You can help too: grow some flowers on your balcony.
""",
    """
Good afternoon, everyone. When you want to remember a text, do you read it again and again? A study by researchers at an American university suggests a better way.

In the study, students read a short science passage. One group read it four times. The other group read it only once. Then, without looking at the passage, they wrote down everything they could remember, and they did this three times.

Five minutes later, the reading group remembered more. But one week later, the result was the opposite. The recall group remembered about 60 percent of the passage, while the reading group remembered only 40 percent.

Why? Reading again feels easy, so we think we have learned the text. But pulling information out of our memory is hard work, and this hard work makes the memory stronger.

So next time, close your book and try to retell what you have read.
""",
    """
Hi, I'm Zhang Wei. A year ago, speaking English was my biggest problem. In my first speaking test, I stopped in the middle of my retelling because I forgot what came next. I got only four points out of nine, and I felt terrible.

My teacher, Ms. Chen, gave me three pieces of advice. First, read aloud for ten minutes every morning. Second, after reading a short passage, close the book and retell it in my own words. Third, record my voice and listen for my mistakes.

At first, it felt strange to hear my own voice, but I kept going. Three months later, I could retell a whole passage without stopping, and in the next test, I got eight points.

Now I know that speaking is a skill, just like swimming. You can't learn it by watching others. You have to practice every day, even when it feels hard.
""",
]
